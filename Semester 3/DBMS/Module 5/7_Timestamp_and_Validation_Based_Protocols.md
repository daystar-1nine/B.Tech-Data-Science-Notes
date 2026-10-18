# Timestamp & Validation-Based Concurrency Protocols

**Q. Explain the Timestamp Ordering Concurrency Control Protocol. Describe its Read and Write operational rules and the Thomas Write Rule with examples. Explain the Validation-Based (Optimistic) Concurrency Control protocol with its three phases. Compare Lock-based, Timestamp, and Validation protocols.**

---

> 📌 **Definition to Remember**
> **Timestamp Ordering Protocols** enforce conflict serializability without acquiring locks by assigning each transaction a unique, monotonically increasing timestamp `TS(T_i)` and strictly ordering conflicting operations by their timestamp sequence. **Validation-Based (Optimistic) Protocols** execute transactions in private local workspaces and validate serializability only at commit time before writing updates to the database.

---

### 1. System Timestamps

The DBMS maintains monotonic timestamps to determine the serialization order of transactions upfront:

* **Transaction Timestamp (`TS(T_i)`):**
  - Assigned when transaction `T_i` enters the system using either the **System Clock** or a **Logical Monotonic Counter**.
  - If `T1` enters before `T2`, then `TS(T1) < TS(T2)`. The protocol guarantees that the serialization order is strictly `T1 → T2`.
* **Data Item Timestamps:**
  Every data item `Q` in the database maintains two associated timestamps:
  - **`W-TS(Q)` (Write Timestamp):** The largest timestamp of any transaction that successfully executed `Write(Q)`.
  - **`R-TS(Q)` (Read Timestamp):** The largest timestamp of any transaction that successfully executed `Read(Q)`.

---

### 2. Basic Timestamp Ordering Rules

Whenever a transaction `T_i` attempts to access a data item `Q`, the DBMS Concurrency Manager tests the following rules:

#### 1. When `T_i` issues `Read(Q)`:
1. **If `TS(T_i) < W-TS(Q)`:**
   - A younger transaction has already overwritten item `Q` with a new value.
   - `T_i` is attempting to read an obsolete, overwritten value that it should have seen earlier.
   - **Action:** **Abort and Rollback `T_i`** (restart `T_i` with a new, younger timestamp).
2. **If `TS(T_i) ≥ W-TS(Q)`:**
   - The value of `Q` was produced by an older or identical transaction; the read is valid.
   - **Action:** Execute `Read(Q)` and update the read timestamp:
     ```
     R-TS(Q) = max(R-TS(Q), TS(T_i))
     ```

#### 2. When `T_i` issues `Write(Q)`:
1. **If `TS(T_i) < R-TS(Q)`:**
   - A younger transaction with timestamp `R-TS(Q)` has already read the old value of `Q`.
   - If `T_i` were allowed to write now, that younger transaction would have seen stale data.
   - **Action:** **Abort and Rollback `T_i`**.
2. **If `TS(T_i) < W-TS(Q)`:**
   - A younger transaction with timestamp `W-TS(Q)` has already overwritten `Q`.
   - **Standard Action:** Abort and Rollback `T_i`.
   - **Thomas Write Rule Optimization:** **Silently ignore the obsolete `Write(Q)` and continue execution!**
3. **Otherwise (`TS(T_i) ≥ R-TS(Q)` and `TS(T_i) ≥ W-TS(Q)`):**
   - The write is valid.
   - **Action:** Execute `Write(Q)` and update the write timestamp:
     ```
     W-TS(Q) = TS(T_i)
     ```

---

### 3. The Thomas Write Rule

The **Thomas Write Rule** is an optimization of the standard timestamp ordering write rule that allows certain non-conflict serializable schedules that are **View Serializable**:

* **Scenario:** `TS(T_i) < W-TS(Q)`.
* **Standard Rule:** Aborts `T_i`.
* **Thomas Write Rule:** Recognizes that `T_i`'s write is obsolete because a younger transaction has already overwritten `Q`. Since no subsequent transaction should read `T_i`'s intermediate value anyway, the DBMS simply **discards (ignores) `T_i`'s write** and lets `T_i` proceed without aborting!
* **Significance:** Increases concurrency by eliminating unnecessary transaction rollbacks.

```
Time   T1 (TS=10)                 T2 (TS=20)                 Item Q (W-TS, R-TS)
 1                                Write(Q)                   W-TS(Q) = 20
 2     Write(Q) [TS=10 < 20]                                 
       Standard TO : ABORTS T1!
       Thomas Rule : SILENTLY IGNORES T1's WRITE & CONTINUES!
```

---

### 4. Characteristics of Timestamp Ordering

1. **Deadlock Freedom:**
   - Timestamp ordering protocols are **100% free from deadlocks**!
   - Reason: Transactions never wait for locks held by other transactions. Conflicting operations are resolved immediately by either executing, discarding, or aborting.
2. **Starvation Risk:**
   - Long-running transactions may repeatedly conflict with younger, short transactions, suffering continuous aborts and restarts (starvation).
3. **Recoverability & Cascading Rollbacks:**
   - Basic timestamp ordering can generate unrecoverable schedules (if `T1` writes `Q` and `T2` reads `Q` and commits before `T1` commits).
   - *Solution:* Writes must be buffered in memory and applied to disk only after transaction commit (Strict Timestamp Ordering).

---

### 5. Validation-Based (Optimistic) Concurrency Protocol

Validation-based Concurrency Control is designed for **read-heavy environments** (such as online query portals) where data item contention is rare:

```
  +-------------------------+
  |    1. READ PHASE        |  Transaction reads data from shared database;
  |                         |  All updates are written ONLY to a PRIVATE LOCAL WORKSPACE.
  +-------------------------+
               |
               v
  +-------------------------+
  |  2. VALIDATION PHASE    |  DBMS checks whether local workspace modifications
  |                         |  conflict with any concurrently committed transactions.
  +-------------------------+
          /           \
    Valid/             \ Invalid (Serializability Conflict Detected)
        v               v
  +-------------+  +-------------+
  | 3. WRITE    |  |   ABORT     | Local workspace discarded;
  |    PHASE    |  |             | Transaction restarts.
  +-------------+  +-------------+
  Updates copied
  to database disk.
```

#### Validation Test Conditions:
Let `T_i` be the transaction validating, and `T_k` be any transaction committed prior to `T_i`:
* **Condition 1:** `T_k` finishes its Write Phase before `T_i` starts its Read Phase.
* **Condition 2:** `T_k` finishes its Write Phase before `T_i` enters its Validation Phase, AND:
  ```
  Writeset(T_k) ∩ Readset(T_i) = ∅
  ```
  *(Updates made by `T_k` do not overlap with any data items read by `T_i`)*.

---

### 6. Grand Concurrency Protocol Comparison Table

| Feature | Lock-Based (2PL) | Timestamp Ordering | Validation-Based (OCC) |
| :--- | :--- | :--- | :--- |
| **Concurrency Primitive** | Shared & Exclusive Locks | Transaction & Item Timestamps | Private workspace & Commit Validation |
| **Conflict Resolution** | Wait / Blocking | Abort & Restart | Abort & Restart at Commit |
| **Deadlock Occurrence** | **Possible** (requires detection/prevention) | **Impossible (Deadlock Free)** | **Impossible (Deadlock Free)** |
| **Starvation Risk** | Low | High (long transactions repeatedly restart) | High under frequent conflicts |
| **Overhead Location** | Continuous lock manager checks | Timestamp comparison on every read/write | Memory copying and end-of-transaction validation |
| **Optimal Workload** | High contention / write heavy | Distributed architectures / moderate conflicts | Low contention / read-intensive systems |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Timestamp ordering assigns monotonic timestamps `TS(T_i)` ensuring serialization in timestamp order.
> 2. Each data item maintains `W-TS(Q)` (latest write) and `R-TS(Q)` (latest read).
> 3. Read condition: If `TS(T_i) < W-TS(Q)`, reject read and abort `T_i`.
> 4. Write condition: If `TS(T_i) < R-TS(Q)`, reject write and abort `T_i`.
> 5. **Thomas Write Rule:** Silently ignores outdated write operations when `TS(T_i) < W-TS(Q)`, expanding concurrency.
> 6. Timestamp protocols are **100% deadlock-free**, but vulnerable to transaction starvation.
> 7. **Validation-based protocol** uses three phases: **Read Phase → Validation Phase → Write Phase**.

---

> ⚡ **Quick Recall**
> `Monotonic TS(Ti) → Item Timestamps (W-TS, R-TS) → Read Rule (TS < W-TS Abort) → Write Rule (TS < R-TS Abort) → Thomas Write Rule (Ignore stale write) → Deadlock Free → Validation OCC (Read, Validate, Write)`
