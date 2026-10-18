# Insertion-Deletion & Predicate Reads (The Phantom Phenomenon)

**Q. What is the Phantom Phenomenon in database concurrency control? Explain why traditional record-level locking fails to prevent phantom tuples. Describe solutions including Predicate Locking and Next-Key Index Locking. Compare ANSI SQL isolation levels with their underlying locking mechanisms and prevented anomalies.**

---

> 📌 **Definition to Remember**
> The **Phantom Phenomenon** occurs when a concurrent transaction inserts, deletes, or modifies tuples that satisfy a search predicate while another transaction is executing repeated range queries over that same predicate, causing newly inserted "phantom" records to unexpectedly appear in subsequent reads within the same transaction.

---

### 1. Concrete Phantom Phenomenon Scenario

Suppose Transaction `T1` calculates the total bonus for all employees in `Dept_ID = 10`:

```
Time   Transaction T1                                     Transaction T2
 1     SELECT * FROM Employee 
       WHERE Dept_ID = 10;
       (Returns 3 rows: Alice, Bob, Charlie)
 2                                                        INSERT INTO Employee 
                                                          VALUES (104, 'David', 10, 50000);
 3                                                        COMMIT;
 4     SELECT SUM(Salary) FROM Employee 
       WHERE Dept_ID = 10;
       (Calculates sum across 4 rows! 
        David is a PHANTOM TUPLE that appeared mid-way!)
 5     COMMIT;
```

#### The Problem:
`T1` sees an inconsistent, changing set of rows during its execution lifetime despite holding shared locks on `Alice`, `Bob`, and `Charlie`!

---

### 2. Why Traditional Record-Level Locking Fails

Traditional Two-Phase Locking (2PL) protocols place locks exclusively on **existing, physical data records**:
1. At Time 1, `T1` requested and received Shared (`S`) locks on every existing employee record with `Dept_ID = 10` (`Alice`, `Bob`, and `Charlie`).
2. However, record `David` **did not physically exist in the database table** at Time 1!
3. Because `David` did not exist, the DBMS Lock Manager could not attach a lock to `David`.
4. Transaction `T2` was therefore free to insert `David` without triggering any lock conflict with `T1`.
5. When `T1` re-read `Dept_ID = 10` at Time 4, `David` was visible, breaking serializability!

---

### 3. Solutions to the Phantom Problem

#### 1. Predicate Locking (Logical Locking)
* Instead of placing locks on physical records, `T1` acquires a lock on the **logical predicate condition** itself:
  ```
  Lock Predicate: "Dept_ID = 10"
  ```
* Any concurrent transaction attempting an `INSERT`, `UPDATE`, or `DELETE` on a tuple that satisfies that predicate will detect a conflict with the active predicate lock and be forced to wait.
* *Major Limitation:* Evaluating the mathematical intersection and satisfiability of arbitrary complex SQL predicates (involving multiple joins, subqueries, and mathematical expressions) is **NP-Hard** in the general case. Consequently, pure predicate locking is rarely implemented in commercial database engines.

#### 2. Index-Range Locking & Next-Key Index Locking
Modern relational database engines (such as MySQL InnoDB) solve the phantom problem efficiently by locking ranges within **B+ Tree indexes**:

* **Record Lock:** Locks the specific index entry itself.
* **Gap Lock:** Locks the empty "gap" between two adjacent index key values (or the gap before the first key or after the last key).
* **Next-Key Lock:** A combined lock that locks **both the index record AND the gap immediately preceding it** in the B+ Tree index.

```
B+ Tree Index Leaf Node on Dept_ID:

... [ Dept 05 ] ------- [ Gap Locked by T1 ] ------- [ Dept 10 ] ------- [ Dept 20 ] ...
                               ^
                               |
                   T2 attempts to INSERT Dept 10 here:
                   DBMS detects Gap Lock held by T1 ---> T2 is BLOCKED!
```

When `T1` executes `SELECT * WHERE Dept_ID = 10` using Next-Key Locking:
* It locks all existing index records for `Dept_ID = 10`.
* It simultaneously places a **Gap Lock** on the index gaps surrounding `Dept_ID = 10`.
* When `T2` attempts to insert `David` with `Dept_ID = 10`, it must insert an entry into the B+ Tree leaf page, finds the gap locked, and is blocked until `T1` commits!

---

### 4. ANSI SQL Transaction Isolation Levels

ANSI SQL defines four standard transaction isolation levels offering distinct trade-offs between concurrency throughput and anomaly prevention:

| Isolation Level | Dirty Read (`G1`) | Non-Repeatable Read (`G2`) | Phantom Read (`A3`) | Lost Update (`G0`) |
| :--- | :---: | :---: | :---: | :---: |
| **Read Uncommitted** | **Allowed** | **Allowed** | **Allowed** | Prevented *(via short-term X locks)* |
| **Read Committed** | **Prevented** | **Allowed** | **Allowed** | Prevented |
| **Repeatable Read** | **Prevented** | **Prevented** | **Allowed** *(Prevented in InnoDB via Next-Key)* | Prevented |
| **Serializable** | **Prevented** | **Prevented** | **Prevented** | Prevented |

#### Underlying Locking Mechanisms for Isolation Levels:
1. **Read Uncommitted (Browsing Level):**
   - Reads without acquiring Shared locks.
   - Updates acquire Exclusive locks until commit.
   - Fastest throughput, but allows dirty reads.
2. **Read Committed (Industry Default — PostgreSQL, Oracle, SQL Server):**
   - Transactions acquire **short-term Shared locks** released immediately after each SQL statement completes.
   - Long-term Exclusive locks held until transaction commit.
   - Eliminates dirty reads; allows non-repeatable reads and phantoms.
3. **Repeatable Read (MySQL InnoDB Default):**
   - Transactions acquire **long-term Shared locks** held until transaction commit.
   - Long-term Exclusive locks held until transaction commit.
   - Eliminates dirty and non-repeatable reads.
4. **Serializable (Full Strict Isolation):**
   - Requires rigorous 2PL combined with **Next-Key Locking** or Predicate Locking.
   - Eliminates all concurrency anomalies including phantoms.

#### Snapshot Isolation (MVCC Alternative):
Modern relational DBMSs use **Multi-Version Concurrency Control (MVCC)** to implement Repeatable Read and Serializable levels without read locks:
* Readers never block writers, and writers never block readers!
* Every query reads a consistent transactional "snapshot" based on its starting timestamp.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. The Phantom Phenomenon occurs when concurrent insertions/deletions alter the row count of repeated range queries.
> 2. Traditional row-level 2PL fails because phantom records do not exist at lock acquisition time.
> 3. **Predicate Locking** places locks on logical search conditions, but suffers from high computational overhead.
> 4. **Next-Key Locking** in B+ Trees combines index record locks with **gap locks** to efficiently block insertions.
> 5. ANSI SQL defines four isolation levels: **Read Uncommitted, Read Committed, Repeatable Read, and Serializable**.
> 6. **Read Committed** uses short-term read locks; **Repeatable Read** holds read locks until transaction commit.
> 7. The **Serializable** isolation level is the only ANSI level that strictly guarantees complete immunity from phantom reads.

---

> ⚡ **Quick Recall**
> `Range Query → Concurrent INSERT → Phantom Tuple Appears → Row Locks Fail → Predicate Locks (Logical) vs Next-Key Index Locks (Record + Gap) → ANSI Isolation Levels (Uncommitted → Committed → Repeatable Read → Serializable)`
