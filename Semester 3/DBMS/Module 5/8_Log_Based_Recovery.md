# Log-Based Recovery & Checkpointing — DBMS

> **Definition: Log-Based Recovery** maintains a chronological record of all database modifications on non-volatile storage (the **Log**) to restore database Atomicity and Durability following system crashes.

---

## 1. Detailed Technical Explanation

### 1. Write-Ahead Logging (WAL) Protocol
Before any data modification is written to disk, the corresponding log record **MUST** be flushed to non-volatile log storage.

#### Log Record Formats:
- `<Tn, start>`: Transaction **T_n** started.
- `<Tn, X, V1, V2>`: Transaction **T_n** changed item **X** from Old Value **V_1** to New Value **V_2**.
- `<Tn, commit>`: Transaction **T_n** committed.
- `<Tn, abort>`: Transaction **T_n** aborted.

---

## 2. Recovery Techniques

### 1. Deferred Update Technique (NO-UNDO / REDO Algorithm)
- Database disk writes are postponed until the transaction reaches its `COMMIT` point.
- **Recovery Procedure:**
  - `REDO(Tn)`: Replays new values **V_2** for transactions with both `<Tn, start>` and `<Tn, commit>` in log.
  - No `UNDO` required because uncommitted data was never written to main database blocks!

### 2. Immediate Update Technique (UNDO / REDO Algorithm)
- Database disk writes can occur while the transaction is still active.
- **Recovery Procedure:**
  - `UNDO(Tn)`: Restores old values **V_1** for active transactions with `<Tn, start>` but NO `<Tn, commit>`.
  - `REDO(Tn)`: Replays new values **V_2** for committed transactions.

---

## 3. Checkpointing

Checkpointing reduces recovery overhead by periodically flushing all dirty buffer blocks and active transaction logs to disk.

```
                    Checkpoint Record Outputted
                              |
                              v
<T1, start> ... <T2, start> <CHECKPOINT {T1, T2}> ... <T2, commit> [CRASH!]
```
- During crash recovery, the system only needs to scan the log backwards up to the **most recent checkpoint**.

---

## 4. Core Concepts & Memory Keywords
- **WAL Protocol:** Write log to disk BEFORE writing database blocks.
- **REDO:** Replay operations (**V_2**) for committed transactions.
- **UNDO:** Reverse operations (**V_1**) for uncommitted / aborted transactions.
- **Checkpoint:** Periodic point flushing dirty RAM buffers to persistent disk.

---

## 5. Must-Write Points for Exams
- WAL guarantees Durability by ensuring committed transactions can be reconstructed via REDO log records.
- Deferred update requires only REDO operations during recovery; immediate update requires both UNDO and REDO.
- Checkpointing eliminates the need to scan the entire log file from the beginning of database creation.

---

## 6. Quick Recall Flow
```
Write Log Record to Disk (WAL) -> Modify Memory -> Checkpoint -> System Crash -> UNDO Active, REDO Committed
```
