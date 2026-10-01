# Insertion-Deletion & Predicate Reads (The Phantom Phenomenon)

**Q. What is the Phantom Phenomenon in database concurrency control? Explain why traditional record-level locking fails to prevent phantom tuples. Describe solutions including Predicate Locking and Next-Key Index Locking, and summarize ANSI SQL isolation levels.**

---

> 📌 **Definition to Remember**
> The **Phantom Phenomenon** occurs when a concurrent transaction inserts, deletes, or modifies tuples that satisfy a search predicate while another transaction is executing repeated range queries over that same predicate, causing a newly inserted "phantom" record to unexpectedly appear in subsequent reads.

---

### 1. Concrete Phantom Phenomenon Scenario

Suppose Transaction $T_1$ calculates the total bonus for all employees in `Dept_ID = 10`:

```
Time   Transaction T1                             Transaction T2
 1   SELECT * FROM Emp WHERE Dept_ID = 10;
     (Returns 3 rows: Alice, Bob, Charlie)
 2                                              INSERT INTO Emp VALUES (104, 'David', 10);
 3                                              COMMIT;
 4   SELECT * FROM Emp WHERE Dept_ID = 10;
     (Returns 4 rows! David is a PHANTOM TUPLE!)
```

* **The Problem:** $T_1$ sees a different set of rows within the same transaction even though it held locks on Alice, Bob, and Charlie!

---

### 2. Why Traditional Record-Level Locking Fails

Traditional two-phase locking locks **individual physical records**.
* In step 1, $T_1$ successfully locked records for `Alice`, `Bob`, and `Charlie`.
* However, `David` **did not physically exist in the database** at time step 1!
* Therefore, $T_1$ could not place a lock on David, allowing $T_2$ to insert David without triggering any lock conflict.

---

### 3. Solutions to the Phantom Problem

#### 1. Predicate Locking (Logical Locking)
* Instead of locking individual records, $T_1$ acquires a lock on the **predicate condition** itself:
  $$\text{Lock Predicate: } \text{Dept\_ID} = 10$$
* Any other transaction attempting an `INSERT`, `UPDATE`, or `DELETE` on a tuple satisfying that predicate will conflict with the predicate lock and be blocked.
* *Drawback:* Exponential computational overhead to evaluate arbitrary arbitrary SQL predicate intersections; rarely used in practice.

#### 2. Index-Range Locking & Next-Key Locking
Used by modern commercial engines (such as MySQL InnoDB):
* **Index-Range Lock:** If an index exists on `Dept_ID`, $T_1$ locks the index page containing `Dept_ID = 10`.
* **Next-Key Locking:** Locks both the index record AND the "gap" immediately preceding it in the B+ Tree index.
* When $T_2$ attempts to insert `David` (`Dept_ID = 10`), it must update the B+ Tree index page, but finds the gap locked by $T_1$, blocking the phantom insert!

```
B+ Tree Index Leaf Nodes:
... [ Dept 05 ] -------- [ Gap Locked ] -------- [ Dept 10 ] -------- [ Dept 20 ] ...
                            ^
                            |-- T2 attempts to insert Dept 10 here -> BLOCKED!
```

---

### 4. ANSI SQL Transaction Isolation Levels

| Isolation Level | Dirty Read ($G_1$) | Non-Repeatable Read ($G_2$) | Phantom Read ($A_3$) |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | **Allowed** | **Allowed** | **Allowed** |
| **Read Committed** | Prevented | **Allowed** | **Allowed** |
| **Repeatable Read** | Prevented | Prevented | **Allowed** *(Prevented in InnoDB via Next-Key Locks)* |
| **Serializable** | **Prevented** | **Prevented** | **Prevented** |

* **Dirty Read:** Reading uncommitted data that may later be rolled back.
* **Non-Repeatable Read:** Re-reading the same record returns modified values.
* **Phantom Read:** Re-reading a range predicate returns newly inserted rows.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. The Phantom Phenomenon occurs when concurrent insertions/deletions alter the result of a repeated range query.
> 2. Traditional row-level locks fail because phantom rows do not exist at lock request time.
> 3. **Predicate Locking** places locks on logical search conditions, but suffers from high computational overhead.
> 4. **Next-Key Locking** combines index record locks with **gap locks** in the B+ Tree index structure.
> 5. Next-Key locks prevent phantoms efficiently by blocking insertions into index gaps.
> 6. ANSI SQL defines 4 isolation levels: **Read Uncommitted, Read Committed, Repeatable Read, and Serializable**.
> 7. The **Serializable** isolation level is the only ANSI level that strictly guarantees complete freedom from phantom reads.

---

> ⚡ **Quick Recall**
> `Range Query → Concurrent INSERT → Phantom Tuple Appears → Row Locks Fail → Predicate Locks (Logical) vs Next-Key Index Locks (Gap Locks) → Serializable Level`
