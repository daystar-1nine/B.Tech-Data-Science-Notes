# Distributed Transactions, TCL & Performance Tuning

**Q. Explain the Two-Phase Commit (2PC) protocol for distributed transactions. Describe Transaction Control Language (TCL) commands with SQL examples and explain key database performance tuning strategies.**

---

> 📌 **Definition to Remember**
> **Distributed Transactions** execute across multiple autonomous database nodes interconnected via a network, coordinated atomically using the **Two-Phase Commit (2PC)** protocol. Application workflows control transactions via **TCL commands** and optimize efficiency through systematic **Performance Tuning**.

---

### 1. Two-Phase Commit (2PC) Protocol

In a distributed database, a transaction may update data at multiple physical sites. The 2PC protocol ensures all sites either commit together or abort together (Atomicity across nodes):

```
COORDINATOR NODE                                  PARTICIPANT NODES (Sites 1, 2, 3)
      |                                                        |
      | ================ PHASE 1: PREPARE ===================> |
      |                                                        | (Write updates to log)
      | <--------------- VOTE_COMMIT / VOTE_ABORT ------------ |
      |                                                        |
      | (If ALL vote COMMIT):                                  |
      | ================ PHASE 2: GLOBAL COMMIT =============> |
      |                                                        | (Make changes permanent)
      | <--------------- ACKNOWLEDGEMENT --------------------- |
```

#### Phase 1: Prepare (Voting Phase)
1. Coordinator writes `<prepare T>` to its log and sends `PREPARE` message to all participant sites.
2. Each participant checks local resources:
   * If ready: Writes log records to disk and replies `VOTE_COMMIT`.
   * If failure: Writes abort log and replies `VOTE_ABORT`.

#### Phase 2: Commit / Decision Phase
1. **If ALL participants vote COMMIT:**
   * Coordinator writes `<commit T>` and broadcasts `GLOBAL_COMMIT`.
   * Participants commit locally and send `ACK`.
2. **If ANY participant votes ABORT (or times out):**
   * Coordinator writes `<abort T>` and broadcasts `GLOBAL_ABORT`.
   * Participants roll back local updates and send `ACK`.

---

### 2. Transaction Control Language (TCL) Commands in SQL

TCL commands manage transactional boundaries in SQL:

```sql
-- 1. Begin transactional block
START TRANSACTION;

-- 2. Deduct $1000 from Sender
UPDATE Accounts SET Balance = Balance - 1000 WHERE Account_ID = 101;

-- 3. Create an intermediate Savepoint
SAVEPOINT after_deduction;

-- 4. Attempt transfer to Receiver
UPDATE Accounts SET Balance = Balance + 1000 WHERE Account_ID = 202;

-- 5. If receiver account is invalid, rollback to Savepoint only
-- ROLLBACK TO SAVEPOINT after_deduction;

-- 6. Make all modifications permanent
COMMIT;
```

* `COMMIT`: Permanently saves all modifications made in current transaction.
* `ROLLBACK`: Undoes all modifications made since transaction start.
* `SAVEPOINT`: Establishes intermediate checkpoints within a long transaction allowing partial rollbacks.

---

### 3. Database Performance Tuning Strategies

1. **Index Optimization:**
   * Create B+ Tree indexes on frequently queried columns in `WHERE`, `JOIN`, and `ORDER BY` clauses.
   * Avoid indexing columns with low cardinality (e.g., Boolean `Gender`).
   * Avoid over-indexing (slows down `INSERT`, `UPDATE`, `DELETE`).
2. **Query Refactoring:**
   * Avoid `SELECT *`; retrieve only necessary columns to minimize network I/O.
   * Replace correlated subqueries with `JOIN` operations.
   * Use `EXPLAIN` / `EXPLAIN ANALYZE` to inspect execution plan cost.
3. **Buffer Pool & Memory Tuning:**
   * Allocate 70–80% of server RAM to database buffer pool (e.g., `innodb_buffer_pool_size`).
   * Aim for buffer pool hit ratio $> 99\%$.
4. **Denormalization for Read-Heavy Workloads:**
   * Selectively denormalize up to 2NF or add precomputed summary columns in data warehouses to eliminate expensive multi-table joins.
5. **Partitioning & Sharding:**
   * **Horizontal Partitioning (Sharding):** Distribute rows across nodes based on Range or Hash key.
   * **Vertical Partitioning:** Split rarely accessed large columns (e.g., `BLOB`, `TEXT`) into separate tables.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Distributed transactions execute across multiple network nodes; coordinated via **Two-Phase Commit (2PC)**.
> 2. **2PC Phase 1 (Prepare):** Coordinator queries nodes; nodes reply `VOTE_COMMIT` or `VOTE_ABORT`.
> 3. **2PC Phase 2 (Decision):** If all vote commit, coordinator broadcasts `GLOBAL_COMMIT`; else `GLOBAL_ABORT`.
> 4. 2PC can suffer from **blocking** if the coordinator crashes during Phase 2.
> 5. **TCL commands:** `COMMIT` (permanent save), `ROLLBACK` (undo), `SAVEPOINT` (partial rollback).
> 6. **Index tuning:** Add indexes on join/search columns; avoid indexing low-cardinality columns.
> 7. Performance strategies include buffer pool expansion, query refactoring with `EXPLAIN`, and sharding.

---

> ⚡ **Quick Recall**
> `Distributed Transactions → 2PC (Phase 1 Prepare & Vote → Phase 2 Global Commit/Abort) → TCL (COMMIT, ROLLBACK, SAVEPOINT) → Index & Buffer Tuning`
