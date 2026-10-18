# Log-Based Recovery, WAL & Checkpointing

**Q. Explain the Write-Ahead Logging (WAL) protocol in database recovery. Differentiate between Deferred Database Modification and Immediate Database Modification with log record formats. Explain the Checkpointing mechanism and detail the step-by-step Crash Recovery procedure (Analysis, REDO, and UNDO passes) with a concrete log trace. Explain Shadow Paging as an alternative recovery technique.**

---

> 📌 **Definition to Remember**
> **Log-Based Recovery** maintains an append-only, sequential history of all database modifications on non-volatile stable storage (the **Log**) to guarantee **Atomicity** and **Durability** across system crashes and power failures using the **Write-Ahead Logging (WAL)** protocol and periodic **Checkpointing**.

---

### 1. Types of Failures & Storage Hierarchy

To design effective recovery mechanisms, a DBMS must handle three categories of failures:

1. **Transaction Failure:**
   - Logical error (e.g., bad user input, divide by zero, balance check failure).
   - System error (e.g., transaction aborted as deadlock victim or timeout).
2. **System Crash (Soft Failure):**
   - Hardware malfunction, power cut, operating system kernel panic.
   - Volatile main memory (RAM buffer pool) contents are lost, but non-volatile disk contents remain intact.
3. **Media / Disk Failure (Hard Failure):**
   - Disk head crash, bad sectors, RAID array failure.
   - Handled via tape/cloud backups, disk mirroring, and RAID redundancy.

#### Storage Hierarchy:
* **Volatile Storage:** RAM, CPU cache. Extremely fast, but erased upon system power cut.
* **Non-Volatile Storage:** Magnetic hard drives, SSDs. Survives system crashes, but disk pages may be left half-written.
* **Stable Storage:** Replicated, failure-resilient storage (e.g., mirrored write-ahead log files across independent disk controllers). Survives all single-point hardware failures.

---

### 2. Write-Ahead Logging (WAL) Protocol

The **Write-Ahead Logging (WAL)** protocol enforces two strict operational invariants to guarantee that the database can always be restored to a consistent state:

1. **Rule 1 — The Undo Rule (WAL-1):**
   - Before any modified dirty page in the RAM buffer pool is written to non-volatile disk storage, the log record containing the **old value (before-image)** of the updated data item must be written and flushed to stable storage.
   - *Why?* Ensures Atomicity: if the system crashes, the DBMS can roll back the dirty update.
2. **Rule 2 — The Redo Rule (WAL-2):**
   - Before a transaction can be acknowledged as successfully **COMMITTED**, all of its log records—including the final `<T, commit>` record—must be flushed to non-volatile stable storage.
   - *Why?* Ensures Durability: if power fails a millisecond after commit, the updates can be reconstructed from the log.

#### Standard Log Record Formats:
* `<Ti, start>`: Transaction `T_i` has begun execution.
* `<Ti, X, V_old, V_new>`: Transaction `T_i` updated item `X` from old value `V_old` to new value `V_new`.
* `<Ti, commit>`: Transaction `T_i` has successfully committed.
* `<Ti, abort>`: Transaction `T_i` has aborted.

---

### 3. Deferred vs. Immediate Database Modification

| Feature | Deferred Modification (NO-UNDO / REDO) | Immediate Modification (UNDO / REDO) |
| :--- | :--- | :--- |
| **When are Disk Writes Allowed?** | Postponed strictly until **AFTER** the transaction commits. | Allowed dynamically at any time while the transaction is **ACTIVE**. |
| **Log Record Structure** | `<Ti, X, V_new>` (Only new values required). | `<Ti, X, V_old, V_new>` (Both old and new values required). |
| **Crash Recovery Operations** | **REDO Only** (No uncommitted data ever touched disk!). | **Both UNDO and REDO** required. |
| **Buffer Pool RAM Pressure** | High: Buffer manager must hold all modified pages in RAM until commit. | Low: Dirty buffer pages can be flushed to disk at any time via LRU eviction. |
| **Commercial Adoption** | Rarely used in large OLTP systems due to high memory overhead. | Standard architecture in enterprise DBMSs (PostgreSQL, Oracle, MySQL InnoDB). |

---

### 4. Checkpointing Mechanism

Scanning the entire transaction log from the beginning of database history during crash restart is computationally prohibitive. A **Checkpoint** bounds the recovery time by periodically synchronizing RAM buffers with disk:

```
[ Checkpoint Procedure ]:
1. Temporarily pause new transaction creation.
2. Flush all dirty database buffer blocks from RAM to Disk.
3. Flush all log buffer blocks to stable log storage.
4. Write a checkpoint record to log: <CHECKPOINT {T_active_list}> (listing all currently active transactions).
5. Flush checkpoint log record to disk and resume normal operations.
```

```
LOG TIMELINE:
... <T1, start> ... <T2, start> <CHECKPOINT {T1, T2}> ... <T2, commit> ... <T3, start> [ SYSTEM CRASH! ]
                                       ^
                                       |-- Recovery scans backward ONLY to this point!
```

---

### 5. Step-by-Step Crash Recovery Algorithm (3-Pass Model)

Upon restart following a system crash, the DBMS Recovery Manager processes the log using two lists:
* **REDO-List:** Transactions that have BOTH `<Ti, start>` and `<Ti, commit>` (or `<Ti, abort>`) in the log. Their updates must be reapplied.
* **UNDO-List:** Transactions that have `<Ti, start>` but **NO `<Ti, commit>`** in the log. Their updates must be rolled back.

#### The Three Recovery Passes:
1. **Pass 1 — Analysis Pass:**
   - Scans the log backwards from the crash point to the most recent `<CHECKPOINT>` record.
   - Identifies active uncommitted transactions at checkpoint and tracks transactions started after checkpoint.
   - Populates the **UNDO-List** and **REDO-List**.
2. **Pass 2 — REDO Pass (Roll-Forward):**
   - Scans the log forward from the oldest start of any uncommitted transaction.
   - Reapplies all logged new values (`V_new`) for all transactions in the REDO-list, restoring the database to the exact state it was in at the instant of crash.
3. **Pass 3 — UNDO Pass (Roll-Backward):**
   - Scans the log backward from the crash point.
   - Undoes all modifications made by transactions in the UNDO-list by restoring their old values (`V_old`).
   - Writes `<Ti, abort>` records for each rolled-back transaction.

#### Concrete Trace Example:
Suppose the log contains the following entries at the moment of crash:
```
1. <T1, start>
2. <T1, A, 100, 200>
3. <T2, start>
4. <T2, B, 50, 80>
5. <CHECKPOINT {T1, T2}>
6. <T1, commit>
7. <T3, start>
8. <T3, C, 300, 450>
9. [ SYSTEM CRASH! ]
```

* **Analysis:**
  - `T1` has `<T1, start>` and `<T1, commit>` ⇒ Place in **REDO-List**.
  - `T2` has `<T2, start>` but NO commit ⇒ Place in **UNDO-List**.
  - `T3` has `<T3, start>` but NO commit ⇒ Place in **UNDO-List**.
* **REDO Pass:** Re-execute `T1` update: set `A = 200`.
* **UNDO Pass:** Revert `T3` update: restore `C = 300`, write `<T3, abort>`. Revert `T2` update: restore `B = 50`, write `<T2, abort>`.
* **Result:** Complete database consistency restored!

---

### 6. Shadow Paging Technique

**Shadow Paging** is an alternative, log-less crash recovery technique based on maintaining two page tables:

```
  +--------------------+         +--------------------+
  | Current Page Table |         | Shadow Page Table  |
  +--------------------+         +--------------------+
            |                              |
            +------------+    +------------+
                         |    |
                         v    v
                 [ Database Disk Blocks ]
```

1. **Mechanism:**
   - When a transaction begins, the **Current Page Table** is an exact duplicate of the **Shadow Page Table**.
   - Read operations use the Current Page Table.
   - When a page is modified, a *new* disk block is allocated and updated; the Current Page Table points to this new block while the Shadow Page Table continues pointing to the unmodified original block.
2. **Commit:**
   - The DBMS writes the Current Page Table to disk and atomically updates a pointer in a fixed disk location to point to the new Current Page Table (which now becomes the new Shadow Page Table).
3. **Recovery:**
   - If a crash occurs before commit, recovery simply discards the Current Page Table and re-points to the unmodified Shadow Page Table! Recovery is instantaneous!
4. **Drawbacks:**
   - Causes severe data page fragmentation on disk.
   - High overhead to copy entire page tables for large databases.
   - Garbage collection needed to reclaim abandoned disk blocks.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Log-based recovery enforces **Atomicity and Durability** using Write-Ahead Logging (WAL).
> 2. **Undo Rule (WAL-1):** Log record with old value must reach stable storage BEFORE dirty disk page is written.
> 3. **Redo Rule (WAL-2):** All transaction log records including `<T, commit>` must reach stable storage before commit acknowledgment.
> 4. **Deferred Update:** Disk writes delayed until commit; requires **REDO only**.
> 5. **Immediate Update:** Disk writes allowed during active state; requires **both UNDO and REDO**.
> 6. **Checkpointing** flushes all dirty RAM pages to disk, limiting the crash recovery log search window.
> 7. Recovery uses 3 passes: **Analysis Pass** (build lists), **REDO Pass** (roll forward), and **UNDO Pass** (roll backward).

---

> ⚡ **Quick Recall**
> `WAL Protocol (Log Before Disk) → Deferred (REDO Only) vs Immediate (UNDO/REDO) → Checkpointing (Flush Dirty Buffers) → Crash Analysis → REDO Committed → UNDO Uncommitted → Shadow Paging`
