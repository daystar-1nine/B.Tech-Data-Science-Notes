# Distributed Transactions, TCL & Performance Tuning

**Q. Explain the Two-Phase Commit (2PC) protocol for distributed transactions and discuss failure handling. Describe Transaction Control Language (TCL) commands with SQL examples. Explain database performance tuning strategies covering indexing, query refactoring, buffer management, and partitioning.**

---

> 📌 **Definition to Remember**
> **Distributed Transactions** execute across multiple autonomous database nodes interconnected via a network, coordinated atomically using the **Two-Phase Commit (2PC)** protocol. Application workflows control transactional boundaries via **TCL commands** and maximize system throughput through systematic **Database Performance Tuning**.

---

### 1. Two-Phase Commit (2PC) Protocol

In a distributed database system, a transaction may update data across multiple physical sites. The 2PC protocol guarantees **Global Atomicity**: either all participant nodes commit the transaction together, or all abort and roll back together.

```
COORDINATOR NODE                                  PARTICIPANT NODES (Sites 1, 2, 3)
      |                                                        |
      | ================ PHASE 1: PREPARE ===================> |
      |                                                        | (Flush undo/redo log)
      | <--------------- VOTE_COMMIT / VOTE_ABORT ------------ |
      |                                                        |
      | (If ALL participants vote COMMIT):                     |
      | ================ PHASE 2: GLOBAL COMMIT =============> |
      |                                                        | (Commit locally)
      | <--------------- ACKNOWLEDGEMENT --------------------- |
      |                                                        |
      | Writes <end T> to log                                  |
```

#### Phase 1: Prepare (Voting Phase)
1. The Coordinator site writes a `<prepare T>` record to its log and sends a `PREPARE` message to all participant sites.
2. Each participant checks local resources and transaction integrity:
   - If ready to commit: The participant flushes all undo/redo log records for `T` to stable disk and replies with a `VOTE_COMMIT` message. It enters the **Prepared State**.
   - If unable to commit (e.g., node failure or constraint violation): The participant writes `<abort T>` to its log and replies with a `VOTE_ABORT` message.

#### Phase 2: Commit / Decision Phase
1. **If ALL participants voted COMMIT:**
   - The coordinator writes `<commit T>` to its log and broadcasts a `GLOBAL_COMMIT` message to all participants.
   - Each participant commits locally, releases locks, and sends an `ACK` message back to the coordinator.
   - Upon receiving all `ACK`s, the coordinator writes `<end T>` to its log.
2. **If ANY participant voted ABORT (or if the coordinator times out waiting for a vote):**
   - The coordinator writes `<abort T>` to its log and broadcasts a `GLOBAL_ABORT` message.
   - Each participant rolls back local modifications, releases locks, and sends an `ACK`.

#### Failure Scenarios & The Blocking Problem in 2PC:
* **Participant Failure:** If a participant fails before voting, the coordinator times out and safely decides `GLOBAL_ABORT`.
* **Coordinator Failure (The Blocking Problem):**
  - If the coordinator crashes *after* participants have voted `VOTE_COMMIT` but *before* broadcasting `GLOBAL_COMMIT`, participants in the **Prepared State** are stuck!
  - They cannot abort on their own (the coordinator might have decided to commit), and they cannot commit on their own (another node might have aborted).
  - They are **BLOCKED**, holding locks indefinitely until the coordinator restarts and recovers.
* **Three-Phase Commit (3PC):** Extends 2PC by introducing an intermediate **Pre-Commit** state and non-blocking timeout protocols to prevent coordinator blocking in non-partitioned networks.

---

### 2. Transaction Control Language (TCL) Commands in SQL

TCL commands define and manage transactional boundaries in SQL:

| Command | Purpose |
| :--- | :--- |
| `START TRANSACTION` / `BEGIN` | Explicitly marks the start of a logical transactional block. |
| `COMMIT` | Makes all changes executed in the current transaction permanent and visible to other users. |
| `ROLLBACK` | Undoes all changes executed in the current transaction and restores data to the prior state. |
| `SAVEPOINT name` | Creates an intermediate marker within a transaction to allow partial rollbacks. |
| `ROLLBACK TO SAVEPOINT name` | Rolls back modifications made after the specified savepoint without canceling the entire transaction. |
| `RELEASE SAVEPOINT name` | Deletes a previously defined savepoint to free memory. |

#### Realistic Enterprise SQL Example:
```sql
-- Step 1: Start atomic transfer workflow
START TRANSACTION;

-- Step 2: Deduct funds from Sender
UPDATE Accounts 
SET Balance = Balance - 5000 
WHERE Account_ID = 101 AND Balance >= 5000;

-- Step 3: Set intermediate savepoint
SAVEPOINT after_debit;

-- Step 4: Attempt transfer to recipient
UPDATE Accounts 
SET Balance = Balance + 5000 
WHERE Account_ID = 202;

-- Step 5: Conditional check: If recipient account does not exist, rollback to savepoint
-- ROLLBACK TO SAVEPOINT after_debit;

-- Step 6: Commit entire workflow
COMMIT;
```

---

### 3. Database Performance Tuning Strategies

Database performance tuning maximizes query throughput and minimizes response latency across five key pillars:

#### 1. Index Tuning:
* **High-Cardinality Indexing:** Create B+ Tree indexes on primary keys, foreign keys, and columns heavily used in `WHERE`, `JOIN`, and `ORDER BY` clauses.
* **Avoid Low-Cardinality Indexing:** Do not create traditional indexes on columns with few distinct values (e.g. `Gender` with only 2 values), as full table scans are faster.
* **Composite Indexes & The Leftmost-Prefix Rule:** For multi-column index `(A, B, C)`, queries filtering on `(A)` or `(A, B)` can use the index, but queries filtering only on `(B)` cannot!
* **Covering Index (Index-Only Scan):** If all columns in `SELECT` and `WHERE` are present in the index, the query can be satisfied purely from the index without reading table data blocks.
* **Avoid Over-Indexing:** Every additional index slows down `INSERT`, `UPDATE`, and `DELETE` operations due to index update overhead.

#### 2. Query Rewriting & Execution Plan Analysis:
* **Inspect Plans with `EXPLAIN`:** Use `EXPLAIN` or `EXPLAIN ANALYZE` to identify expensive full table scans and nested-loop joins.
* **Eliminate `SELECT *`:** Request only specific required columns to reduce network bandwidth and memory buffer consumption.
* **Avoid Leading Wildcards:** `WHERE Name LIKE '%Smith'` cannot use an index and forces a full table scan; use `WHERE Name LIKE 'Smith%'` instead.
* **Rewrite Correlated Subqueries:** Convert nested `WHERE col IN (SELECT ...)` subqueries into set-based `JOIN` operations.

#### 3. Buffer Pool & Memory Optimization:
* **Allocate Adequate Buffer Pool:** In dedicated database servers, allocate 70% to 80% of available physical RAM to the database buffer pool (e.g., `innodb_buffer_pool_size`).
* **Buffer Cache Hit Ratio:**
  ```
  Hit Ratio = [ 1 - (Physical Disk Reads / Logical Reads) ] × 100%
  ```
  A well-tuned OLTP database maintains a buffer pool hit ratio above 99%!

#### 4. Normalization vs. Denormalization Trade-offs:
* **OLTP (High Concurrency Updates):** Normalize to 3NF/BCNF to prevent update anomalies and redundant writes.
* **OLAP / Data Warehousing (Read-Heavy Reporting):** Selectively denormalize tables or create precomputed materialized views to eliminate expensive multi-table joins.

#### 5. Database Partitioning & Sharding:
* **Horizontal Partitioning (Sharding):** Splits large tables by row into smaller sub-tables based on a partition key (e.g. Range, Hash, or List partitioning by `Year` or `Region`).
* **Vertical Partitioning:** Splits wide tables by column, moving rarely accessed large columns (such as `BLOB` or `TEXT` fields) into separate tables to optimize cache density.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Distributed transactions execute across multiple network sites, coordinated via **Two-Phase Commit (2PC)**.
> 2. **2PC Phase 1 (Prepare):** Coordinator queries nodes; nodes flush logs and reply `VOTE_COMMIT` or `VOTE_ABORT`.
> 3. **2PC Phase 2 (Decision):** If all nodes vote commit, coordinator broadcasts `GLOBAL_COMMIT`; otherwise `GLOBAL_ABORT`.
> 4. 2PC can suffer from **coordinator blocking** if the coordinator crashes during Phase 2 while nodes are prepared.
> 5. **TCL commands:** `COMMIT` (permanent save), `ROLLBACK` (undo), `SAVEPOINT` (partial rollback).
> 6. **Index tuning:** Use B+ Tree indexes on join/filter keys, leverage covering indexes, and follow the leftmost-prefix rule.
> 7. Performance optimization includes buffer pool expansion (hit ratio > 99%), `EXPLAIN` query tuning, and sharding.

---

> ⚡ **Quick Recall**
> `Distributed Transactions → 2PC (Phase 1 Prepare & Vote → Phase 2 Global Decision) → Coordinator Blocking → TCL (COMMIT, ROLLBACK, SAVEPOINT) → Index & Query Tuning (EXPLAIN, Hit Ratio > 99%)`
