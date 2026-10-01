# Transaction Concept & ACID Properties

**Q. Define a database transaction. Explain the ACID properties in detail with real-world examples and state which DBMS components enforce each property. Draw and explain the transaction state transition diagram.**

---

> 📌 **Definition to Remember**
> A **Transaction** is a single logical unit of database processing that includes one or more database access operations (Read and Write). To maintain database integrity in the presence of concurrent execution and hardware failures, every transaction must strictly satisfy the four **ACID Properties**.

---

### 1. The ACID Properties Explained

```
A - ATOMICITY     : "All-or-Nothing" execution.
C - CONSISTENCY   : Preserves database invariants and integrity constraints.
I - ISOLATION     : Concurrent transactions execute without mutual interference.
D - DURABILITY    : Committed updates persist permanently on non-volatile storage.
```

#### 1. Atomicity (All-or-Nothing)
* A transaction cannot partially execute; either all its operations complete successfully and are committed, or none take effect and the database is rolled back.
* **Enforcing Component:** **Recovery Manager** using Write-Ahead Logging (WAL) and undo mechanisms.

#### 2. Consistency (Correctness Preservation)
* Execution of a transaction in isolation transforms the database from one valid consistent state to another valid consistent state, maintaining all integrity constraints.
* **Enforcing Component:** **Integrity Subsystem** (Primary Key, Foreign Key, `CHECK` constraints) and application logic.

#### 3. Isolation (Concurrency Independence)
* Multiple transactions executing concurrently must not witness each other's intermediate uncommitted states. Each transaction executes as if it is the only one in the system.
* **Enforcing Component:** **Concurrency Control Manager** using Locking protocols (2PL) or Timestamping.

#### 4. Durability (Persistence)
* Once a transaction successfully commits, its modifications are permanently recorded in non-volatile storage (disk/SSD) and will never be lost, even in the event of a system crash.
* **Enforcing Component:** **Recovery Manager** using redo logs and Checkpointing.

---

### 2. Real-World Banking Example

Consider transferring \$500 from Account $A$ (Balance = \$1000) to Account $B$ (Balance = \$2000):

```
Transaction T:
  1. Read(A)
  2. A = A - 500
  3. Write(A)
     [---> CRASH OCCURS HERE! <---]
  4. Read(B)
  5. B = B + 500
  6. Write(B)
  7. Commit
```

* **If Atomicity fails:** \$500 is deducted from $A$, but never added to $B$. System loses \$500!
* **If Consistency fails:** Total money before transfer = \$3000. Total money after crash = \$2500 (violates sum invariant).
* **If Isolation fails:** Another transaction $T_2$ reads $A$ after step 3, seeing a dirty intermediate value before $T$ commits.
* **If Durability fails:** Power is cut immediately after step 7; upon reboot, the database reverts to old balances.

---

### 3. Transaction State Transition Diagram

```
                 +----------------------+
                 |        ACTIVE        |  <-- Initial state: Executing Read/Write
                 +----------------------+
                  /                    \
   Last statement/                      \ Operation fails /
   executed     /                        \ Aborted by system
               v                          v
     +--------------------+     +--------------------+
     | PARTIALLY COMMITTED|     |       FAILED       |
     +--------------------+     +--------------------+
               |                          |
   Log flushed |                          | System rolls back
   to disk     |                          | dirty modifications
               v                          v
     +--------------------+     +--------------------+
     |     COMMITTED      |     |      ABORTED       |
     +--------------------+     +--------------------+
     (Permanent success)        (Database restored to
                                 pre-transaction state)
```

1. **Active:** The initial state where transaction operations are executing.
2. **Partially Committed:** All operations have finished, but updates are still held in RAM buffers.
3. **Committed:** The transaction has successfully written its commit log record to persistent disk storage.
4. **Failed:** Normal execution cannot proceed due to hardware error or concurrency conflict.
5. **Aborted:** The transaction has been rolled back and the database is restored to its prior state.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A transaction is a single logical unit of database work executing Read and Write operations.
> 2. **Atomicity:** All-or-nothing principle enforced by the **Recovery Manager** via WAL rollback.
> 3. **Consistency:** Transforms database between valid states, enforced by database constraints.
> 4. **Isolation:** Concurrent transactions execute without seeing intermediate states, enforced by **Concurrency Control (2PL)**.
> 5. **Durability:** Committed updates survive crashes, enforced by **Recovery Manager** log flushing.
> 6. State transitions: **Active $\rightarrow$ Partially Committed $\rightarrow$ Committed** (or **Failed $\rightarrow$ Aborted**).
> 7. The commit point occurs when the `<T, commit>` log record is safely flushed to non-volatile disk.

---

> ⚡ **Quick Recall**
> `Transaction → ACID (Atomicity, Consistency, Isolation, Durability) → Enforcing Managers → Active → Partially Committed → Committed / Aborted`
