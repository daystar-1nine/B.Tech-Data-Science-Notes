# Timestamp & Validation-Based Concurrency Protocols

**Q. Explain the Timestamp Ordering Concurrency Control Protocol. Describe its Read and Write operational rules and the Thomas Write Rule. Explain the Validation-Based (Optimistic) Concurrency Control protocol with its three phases.**

---

> 📌 **Definition to Remember**
> **Timestamp Ordering Protocols** enforce conflict serializability without using locks by assigning each transaction a monotonic timestamp $TS(T_i)$ and ordering conflicting operations by timestamp sequence. **Validation-Based (Optimistic) Protocols** execute transactions in local memory and validate serializability only at commit time.

---

### 1. System Timestamps

* **Transaction Timestamp ($TS(T_i)$):** Unique monotonic identifier assigned when transaction $T_i$ enters the system (using system clock or logical counter).
* Each data item $Q$ maintains two timestamps:
  * **$W\text{-}TS(Q)$:** The largest timestamp of any transaction that successfully executed `Write(Q)`.
  * **$R\text{-}TS(Q)$:** The largest timestamp of any transaction that successfully executed `Read(Q)`.

---

### 2. Basic Timestamp Ordering Rules

#### 1. When $T_i$ issues `Read(Q)`:
1. If **$TS(T_i) < W\text{-}TS(Q)$**: $T_i$ is attempting to read an overwritten value.
   * **Action:** **Abort and Rollback $T_i$** (restart with new timestamp).
2. If **$TS(T_i) \ge W\text{-}TS(Q)$**: The read is valid.
   * **Action:** Execute `Read(Q)` and update:
     $$R\text{-}TS(Q) = \max(R\text{-}TS(Q), TS(T_i))$$

#### 2. When $T_i$ issues `Write(Q)`:
1. If **$TS(T_i) < R\text{-}TS(Q)$**: A younger transaction has already read the older value; $T_i$'s write is obsolete.
   * **Action:** **Abort and Rollback $T_i$**.
2. If **$TS(T_i) < W\text{-}TS(Q)$**: A younger transaction has already written to $Q$.
   * **Standard Action:** Abort and Rollback $T_i$.
   * **Thomas Write Rule Optimization:** **Ignore the obsolete write and continue execution!** (Because the younger write would overwrite it anyway).
3. Otherwise: Execute `Write(Q)` and update:
   $$W\text{-}TS(Q) = TS(T_i)$$

---

### 3. Deadlock Freedom vs. Starvation

* **Deadlock Freedom:** Timestamp protocols are **100% free from deadlocks** because transactions never wait for locks; conflicting transactions are immediately aborted and restarted!
* **Starvation Risk:** Long-running transactions may repeatedly conflict with younger transactions, causing continuous aborts (starvation).

---

### 4. Validation-Based (Optimistic) Protocol

Used in read-heavy workloads where data conflicts are rare. Transactions execute in three distinct phases:

```
  +-------------------------+
  |    1. READ PHASE        |  Reads data from database; writes made to
  |                         |  PRIVATE LOCAL WORKSPACE.
  +-------------------------+
               |
               v
  +-------------------------+
  |  2. VALIDATION PHASE    |  Checks if updates conflict with any
  |                         |  concurrent committed transactions.
  +-------------------------+
          /           \
    Valid/             \ Invalid (Conflict detected)
        v               v
  +-------------+  +-------------+
  | 3. WRITE    |  |   ABORT     | Local workspace discarded;
  |    PHASE    |  |             | transaction restarted.
  +-------------+  +-------------+
  Updates copied
  to database disk.
```

#### Validation Test Condition:
For all transactions $T_k$ committed before $T_i$, validation succeeds if:
1. $T_k$ completes its Write Phase before $T_i$ starts its Read Phase, **OR**
2. $T_k$ completes before $T_i$ enters Validation, and:
   $$\text{Writeset}(T_k) \cap \text{Readset}(T_i) = \emptyset$$

---

### 5. Concurrency Protocol Comparison Table

| Feature | Lock-Based (2PL) | Timestamp Ordering | Validation-Based (Optimistic) |
| :--- | :--- | :--- | :--- |
| **Concurrency Mechanism** | Shared/Exclusive locks | Monotonic Timestamps | Private workspace validation |
| **Deadlock Occurrence** | **Possible** (requires detection) | **Impossible** (Deadlock Free) | **Impossible** (Deadlock Free) |
| **Starvation Risk** | Low | High (Cascading restarts) | High for long transactions |
| **Ideal Workload** | High contention / write heavy | Distributed architectures | Low contention / read heavy |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Timestamp ordering assigns unique monotonically increasing timestamps $TS(T_i)$ to transactions.
> 2. Each data item maintains **$R\text{-}TS(Q)$** (latest read) and **$W\text{-}TS(Q)$** (latest write).
> 3. Read condition: If $TS(T_i) < W\text{-}TS(Q)$, reject read and abort $T_i$.
> 4. Write condition: If $TS(T_i) < R\text{-}TS(Q)$, reject write and abort $T_i$.
> 5. **Thomas Write Rule:** Silently ignores outdated write operations instead of aborting, expanding concurrency.
> 6. Timestamp protocols are **completely deadlock-free**, but vulnerable to transaction starvation.
> 7. **Validation-based protocol** uses three phases: **Read Phase $\rightarrow$ Validation Phase $\rightarrow$ Write Phase**.

---

> ⚡ **Quick Recall**
> `Monotonic TS(Ti) → R-TS & W-TS per item → Check TS against Item TS → Thomas Write Rule (Ignore stale writes) → Deadlock Free → Validation (Read, Validate, Write)`
