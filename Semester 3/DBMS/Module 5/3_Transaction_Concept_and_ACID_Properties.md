# Transaction Concept, ACID Properties & Concurrency Anomalies

**Q. Define a database transaction. Explain the ACID properties in detail with real-world examples and state which DBMS components enforce each property. Draw and explain the transaction state transition diagram. Explain the 4 classic concurrency anomalies (Lost Update, Dirty Read, Unrepeatable Read, and Phantom Read) with schedule traces.**

---

> 📌 **Definition to Remember**
> A **Transaction** is a single logical unit of database work comprising one or more database access operations (such as `Read` and `Write`). To guarantee database consistency and reliability under concurrent access and unexpected system failures, every transaction must strictly adhere to the four **ACID Properties** (Atomicity, Consistency, Isolation, and Durability).

---

### 1. The ACID Properties Explained

```
A - ATOMICITY     : "All-or-Nothing" execution guarantee.
C - CONSISTENCY   : Transforms database from one valid consistent state to another.
I - ISOLATION     : Concurrent transactions execute without mutual interference.
D - DURABILITY    : Committed modifications persist permanently on non-volatile storage.
```

#### 1. Atomicity ("All-or-Nothing")
* A transaction is an indivisible unit of work: either **all** its operations execute successfully and are permanently committed, or **none** take effect and the database is completely rolled back to its pre-transaction state.
* **Enforcing Component:** **Recovery Manager** using Write-Ahead Logging (WAL) and Undo mechanisms.

#### 2. Consistency ("Preserving Invariants")
* Execution of a transaction in isolation preserves database validity by upholding all explicit integrity constraints (Primary Keys, Foreign Keys, `NOT NULL`, `CHECK` constraints) as well as implicit business rules (e.g. account balances cannot drop below zero).
* **Enforcing Component:** **Integrity Subsystem** (via database schema constraints) and the application programmer.

#### 3. Isolation ("Concurrency Independence")
* The execution of a transaction must not be interfered with by any other concurrent transaction. Even when multiple transactions execute interleaved in time, the net outcome must appear as if each transaction executed sequentially in complete isolation.
* **Enforcing Component:** **Concurrency Control Manager** using Locking protocols (2PL), Timestamp Ordering, or Multi-Version Concurrency Control (MVCC).

#### 4. Durability ("Crash Survival")
* Once a transaction successfully commits, its updates are permanently recorded in non-volatile storage (disk/SSD) and will never be lost, even if an operating system crash or power outage occurs immediately afterward.
* **Enforcing Component:** **Recovery Manager** using Redo log records and periodic Checkpointing.

---

### 2. Real-World Banking Example

Consider transferring 500 Rupees from Account `A` (Balance = 1,000) to Account `B` (Balance = 2,000):

```
Transaction T:
  Step 1: Read(A)
  Step 2: A = A - 500
  Step 3: Write(A)
          [ ---> SYSTEM CRASH OR POWER CUT OCCURS HERE! <--- ]
  Step 4: Read(B)
  Step 5: B = B + 500
  Step 6: Write(B)
  Step 7: Commit
```

* **If Atomicity fails:** 500 is deducted from `A`, but never credited to `B`. 500 Rupees simply vanishes from the bank!
* **If Consistency fails:** Total money before transfer = `1000 + 2000 = 3000`. Total money after the partial crash = `500 + 2000 = 2500` (violating the conservation of money invariant).
* **If Isolation fails:** Another transaction `T2` reads `A` immediately after Step 3, viewing an uncommitted intermediate balance of 500 before `T` decides whether to commit or abort.
* **If Durability fails:** Power is cut immediately after Step 7; upon reboot, the system forgets the transfer and reverts balances back to 1,000 and 2,000.

---

### 3. Transaction State Transition Diagram

During its execution lifecycle, a transaction transitions through distinct internal states:

```
                 +----------------------+
                 |        ACTIVE        |  <-- Transaction is executing Read/Write operations
                 +----------------------+
                  /                    \
   Last statement/                      \ Hardware error / Aborted by system /
   executed     /                        \ Integrity constraint violation
               v                          v
     +--------------------+     +--------------------+
     | PARTIALLY COMMITTED|     |       FAILED       |
     +--------------------+     +--------------------+
               |                          |
   Commit log  |                          | Recovery manager rolls back
   flushed to  |                          | all uncommitted modifications
   stable disk |                          |
               v                          v
     +--------------------+     +--------------------+
     |     COMMITTED      |     |      ABORTED       |
     +--------------------+     +--------------------+
     (Permanent success)        (Database restored to prior valid state;
                                 Transaction may be restarted or killed)
```

#### Detailed Transaction States:
1. **Active:** The initial state when the transaction enters the system and executes its `Read` and `Write` operations.
2. **Partially Committed:** The state entered after the final statement has been executed, but updates are still held temporarily in main memory volatile buffers.
3. **Committed:** The transaction has successfully written its `<T, commit>` record to non-volatile log storage. Its modifications are now guaranteed to survive crashes.
4. **Failed:** Normal execution can no longer proceed due to hardware failure, software exception, deadlock detection, or logical constraint violation.
5. **Aborted:** The transaction has completed its rollback; all dirty modifications have been undone and the database is restored to its exact pre-transaction state.

---

### 4. Concurrency Anomalies (Failures of Isolation)

When concurrent transactions execute interleaved without adequate concurrency control, four classic concurrency anomalies occur:

#### 1. Lost Update Problem (Write-Write / WW Conflict)
Occurs when two transactions concurrently read the same data item and subsequently write updated values, with the second write blindly overwriting the first write without incorporating its changes.

```
Time   Transaction T1             Transaction T2             Balance X (Initial: 100)
 1     Read(X)  [reads 100]                                  100
 2                                Read(X)  [reads 100]       100
 3     X = X + 50                                            100
 4     Write(X) [writes 150]                                 150
 5                                X = X - 20                 150
 6                                Write(X) [writes 80]       80  <-- T1's +50 update is LOST!
 7     Commit                     Commit                     80  (Correct final balance should be 130!)
```

#### 2. Dirty Read Problem / Reading Uncommitted Data (Write-Read / WR Conflict)
Occurs when transaction `T2` reads data that has been modified by an active transaction `T1`, but `T1` subsequently fails and is aborted (rolled back).

```
Time   Transaction T1             Transaction T2             Balance X (Initial: 100)
 1     Read(X)                                               100
 2     X = X + 500
 3     Write(X) [writes 600]                                 600
 4                                Read(X) [reads 600 (DIRTY!)]600
 5                                X = X - 100
 6                                Write(X) [writes 500]      500
 7     ABORT / ROLLBACK!                                     ??? <-- T1 rolls back to 100, but
                                                                    T2 already acted on invalid 600!
```

#### 3. Unrepeatable Read / Inconsistent Analysis (Read-Write / RW Conflict)
Occurs when transaction `T1` reads a data item twice, but another transaction `T2` modifies or deletes that item in between the two reads, causing `T1` to observe inconsistent values.

```
Time   Transaction T1             Transaction T2             Balance X (Initial: 100)
 1     Read(X) [reads 100]                                   100
 2                                Read(X)                    100
 3                                X = X + 200
 4                                Write(X) [writes 300]      300
 5                                Commit                     300
 6     Read(X) [reads 300!]                                  300 <-- Same transaction T1 sees two
                                                                     different values for item X!
```

#### 4. Phantom Read Problem
Occurs when transaction `T1` executes a range query (e.g. `SELECT COUNT(*) WHERE Dept = 'IT'`), and transaction `T2` inserts a new row satisfying that predicate before `T1` repeats the query, causing a "phantom" row to appear.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A transaction is a single logical unit of database work executing `Read` and `Write` primitives.
> 2. **Atomicity:** All-or-nothing principle enforced by the **Recovery Manager** via WAL rollback.
> 3. **Consistency:** Transforms database between valid states, enforced by database constraints and DDL rules.
> 4. **Isolation:** Concurrent transactions execute without mutual interference, enforced by the **Concurrency Control Manager** (2PL/Timestamping).
> 5. **Durability:** Committed updates survive crashes, enforced by the **Recovery Manager** log flushing.
> 6. State transitions: **Active → Partially Committed → Committed** (or **Failed → Aborted**).
> 7. The four classic concurrency anomalies are **Lost Update (WW)**, **Dirty Read (WR)**, **Unrepeatable Read (RW)**, and **Phantom Read**.

---

> ⚡ **Quick Recall**
> `Transaction → ACID (Atomicity, Consistency, Isolation, Durability) → Enforcing Managers → Active → Partially Committed → Committed / Aborted → 4 Concurrency Anomalies (Lost Update, Dirty Read, Unrepeatable Read, Phantom)`
