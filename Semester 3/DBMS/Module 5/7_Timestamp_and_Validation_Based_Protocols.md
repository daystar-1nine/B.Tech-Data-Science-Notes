# Timestamp & Validation-Based Protocols — DBMS

> **Definition: Timestamp Ordering Protocols** ensure conflict serializability without using locks by assigning a unique monotonic timestamp **TS(T_i)** to each transaction upon start and enforcing operation ordering according to timestamp sequence.

---

## 1. Detailed Technical Explanation

### 1. System Timestamps
Each data item **X** maintains two timestamps:
- **`W-TS(X)`:** Largest timestamp of any transaction that executed `Write(X)`.
- **`R-TS(X)`:** Largest timestamp of any transaction that executed `Read(X)`.

### 2. Basic Timestamp Ordering Rules

#### Read Operation `Read(X)` by Transaction **T_i**:
1. If **TS(T_i) < W-TS(X)**: **T_i** is attempting to read an overwritten value. **Abort and Rollback **T_i.
2. Else: Execute `Read(X)` and update **R-TS(X) = \max(R-TS(X), TS(T_i))**.

#### Write Operation `Write(X)` by Transaction **T_i**:
1. If **TS(T_i) < R-TS(X)**: **T_i** is attempting to write a value needed by a younger transaction. **Abort and Rollback **T_i.
2. If **TS(T_i) < W-TS(X)**: **T_i** is writing an obsolete value (**Thomas Write Rule**: Ignore write and continue).
3. Else: Execute `Write(X)` and update **W-TS(X) = TS(T_i)**.

---

## 2. Validation-Based (Optimistic) Protocol

Used when read operations dominate write operations (low conflict rate). Execution is split into 3 phases:

```
+-------------------+      +-------------------+      +-------------------+
| 1. READ PHASE     | ---> | 2. VALIDATION     | ---> | 3. WRITE PHASE    |
| Read & Write to   |      | Check for conflict|      | Copy workspace to |
| private workspace |      | with committed Tx |      | database storage  |
+-------------------+      +-------------------+      +-------------------+
```

### Validation Test Condition:
For all **T_k** committed before **T_i**:
- **Finish(T_k) < StartValidation(T_i)**, OR
- **Writeset(T_k) \cap Readset(T_i) = \emptyset**.

---

## 3. Core Concepts & Memory Keywords
- **Monotonic Timestamps:** Unique growing values (System clock or global counter).
- **Thomas Write Rule:** Optimization ignoring outdated write requests rather than aborting.
- **Optimistic Concurrency Control:** Read -> Validate -> Write phases.

---

## 4. Must-Write Points for Exams
- Timestamp ordering protocols guarantee **freedom from deadlocks** because transactions are never made to wait indefinitely.
- Starvation can occur under timestamp ordering if a long transaction is repeatedly aborted by younger transactions.
- Validation protocols perform all modifications on local workspaces before validating.

---

## 5. Quick Recall Flow
```
Compare TS(Ti) with W-TS(X)/R-TS(X) -> Valid? Proceed : Outdated? Abort & Restart with New Timestamp
```
