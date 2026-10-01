# Log-Based Recovery & Checkpointing

**Q. Explain the Write-Ahead Logging (WAL) protocol in database recovery. Differentiate between Deferred Database Modification and Immediate Database Modification. Explain Checkpointing and describe the recovery algorithm after a system crash.**

---

> 📌 **Definition to Remember**
> **Log-Based Recovery** maintains an append-only sequential record of all database modifications on non-volatile storage (the **Log**) to guarantee **Atomicity** and **Durability** during system failures using the **Write-Ahead Logging (WAL)** protocol and periodic **Checkpointing**.

---

### 1. Write-Ahead Logging (WAL) Protocol

The WAL protocol enforces two fundamental rules before data is modified:
1. **Rule 1 (Undo Rule):** Before a modified database buffer page is written to disk, the log record containing the **old value** must be flushed to non-volatile log storage.
2. **Rule 2 (Redo Rule):** Before a transaction can declare itself committed, all log records for that transaction, including the `<T, commit>` record, must be flushed to non-volatile log storage.

#### Standard Log Record Formats:
* `<Ti, start>`: Transaction $T_i$ began.
* `<Ti, X, V_old, V_new>`: $T_i$ modified item $X$ from old value $V_{\text{old}}$ to new value $V_{\text{new}}$.
* `<Ti, commit>`: Transaction $T_i$ successfully committed.
* `<Ti, abort>`: Transaction $T_i$ aborted.

---

### 2. Deferred vs. Immediate Database Modification

| Feature | Deferred Modification (NO-UNDO / REDO) | Immediate Modification (UNDO / REDO) |
| :--- | :--- | :--- |
| **When are Disk Writes Allowed?** | Postponed until **AFTER** transaction reaches commit | Occur dynamically while transaction is still **ACTIVE** |
| **Log Record Content** | `<Ti, X, V_new>` (Only new values needed) | `<Ti, X, V_old, V_new>` (Both old and new values) |
| **Crash Recovery Operations**| **REDO Only** (No UNDO needed!) | **Both UNDO and REDO** required |
| **Memory Buffer Pressure** | High (All updates buffered in RAM) | Low (Buffer frames flushed to disk dynamically) |
| **Overhead** | Lower recovery time, higher runtime buffering | Higher recovery time, lower runtime buffering |

---

### 3. Checkpointing Mechanism

Scanning the entire log from the beginning of time upon a crash is computationally impossible. A **Checkpoint** bounds recovery time by periodically synchronizing database buffers:

```
[ Checkpoint Procedure ]:
1. Stop accepting new transactions temporarily.
2. Flush all modified buffer blocks (dirty pages) from RAM to Disk.
3. Write a log record: <CHECKPOINT {T_active_list}> to non-volatile log storage.
4. Flush log buffer to disk.
5. Resume normal transaction processing.
```

```
 LOG: ... <T1, start> ... <T2, start> <CHECKPOINT {T1, T2}> ... <T2, commit> ... [ SYSTEM CRASH! ]
                                            ^
                                            |-- Recovery scans backward only to this point!
```

---

### 4. Crash Recovery Procedure (Immediate Update with Checkpoint)

During restart after a system crash, the Recovery Manager processes the log in two lists:
* **REDO-List:** Transactions that have BOTH `<Ti, start>` and `<Ti, commit>` (or `<Ti, abort>`) in the log.
* **UNDO-List:** Transactions that have `<Ti, start>` but **NO `<Ti, commit>`** in the log.

#### Recovery Steps:
1. **Analysis Pass:** Scan log backwards from the end to the most recent `<CHECKPOINT>` record. Initialize UNDO-list with transactions active at checkpoint. Add new active transactions; move committed transactions to REDO-list.
2. **REDO Pass:** Scan log forward from the oldest start of any uncommitted transaction. Reapply all logged modifications ($V_{\text{new}}$) for transactions in the REDO-list.
3. **UNDO Pass:** Scan log backward. Reverse all modifications ($V_{\text{old}}$) for transactions in the UNDO-list and write an `<Ti, abort>` record for each.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Log-based recovery guarantees **Atomicity and Durability** using Write-Ahead Logging (WAL).
> 2. **WAL Rule:** Log record must reach disk BEFORE corresponding dirty database page is written.
> 3. **Deferred Update:** Disk writes happen only after commit; requires **REDO only**.
> 4. **Immediate Update:** Disk writes occur while active; requires **both UNDO and REDO**.
> 5. **Checkpointing** flushes all dirty RAM pages to disk, bounding the log search window during recovery.
> 6. Transactions with `<T, start>` and `<T, commit>` are placed in the **REDO list**.
> 7. Transactions with `<T, start>` but NO `<T, commit>` are placed in the **UNDO list** and rolled back.

---

> ⚡ **Quick Recall**
> `WAL Protocol (Log before Disk) → Deferred (REDO Only) vs Immediate (UNDO/REDO) → Checkpointing (Flush Dirty Buffers) → Crash Analysis → REDO Committed → UNDO Uncommitted`
