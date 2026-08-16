# Lock-Based Protocols & Multiple Granularity — DBMS

> **Definition: Lock-Based Protocols** control concurrent access to data items by requiring transactions to acquire **Locks** (Shared or Exclusive) before reading or writing data.

---

## 1. Detailed Technical Explanation

### 1. Lock Modes:
1. **Shared Lock (S-Lock):** Granted for `READ` operations. Multiple transactions can hold S-locks simultaneously on the same item.
2. **Exclusive Lock (X-Lock):** Granted for `WRITE` operations. Only one transaction can hold an X-lock; no other transaction can read or write.

#### Lock Compatibility Matrix:
| Lock Requested | Shared (S) | Exclusive (X) |
| :--- | :--- | :--- |
| **Shared (S)** | **Compatible (True)** | Incompatible (False) |
| **Exclusive (X)**| Incompatible (False) | Incompatible (False) |

---

## 2. Two-Phase Locking Protocol (2PL)

2PL guarantees conflict serializability by dividing a transaction's lock lifecycle into two distinct phases:

```
Number of
Locks Held
   ^             Phase 1: Growing Phase          Phase 2: Shrinking Phase
   |             (Locks acquired, none released)  (Locks released, none acquired)
   |
   |                   /\ Lock Point
   |                  /     |                 /       |                /         +---------------+--------+-----------------------------------> Time
```

### 2PL Variants:
1. **Basic 2PL:** Transaction acquires locks as needed (Growing), releases locks (Shrinking). Can suffer from **Cascading Aborts**.
2. **Strict 2PL:** Transaction holds all **Exclusive (X) locks until COMMIT/ABORT**. Prevents cascading aborts (Strict schedules).
3. **Rigorous 2PL:** Transaction holds **ALL locks (Shared and Exclusive) until COMMIT/ABORT**.

---

## 3. Multiple Granularity Locking (MGL)

MGL allows data items of various sizes (Database -> File -> Page -> Record) to be locked in a tree hierarchy.

```
                  [ DATABASE ]
                       |
                  [   FILE   ]
                       |
                  [   PAGE   ]
                       |
                  [  RECORD  ]
```

### Intent Locks:
Before locking a fine-grained node (e.g., Record), a transaction must acquire an **Intent Lock** on its ancestor nodes:
- **IS (Intent Shared):** Intent to lock explicit child nodes with Shared locks.
- **IX (Intent Exclusive):** Intent to lock explicit child nodes with Exclusive locks.
- **SIX (Shared + Intent Exclusive):** Explicit Shared lock on current subtree plus Intent Exclusive on lower nodes.

---

## 4. Core Concepts & Memory Keywords
- **Lock Point:** Point in time where a transaction acquires its final lock in 2PL.
- **Cascading Rollback:** One transaction aborting causes multiple dependent transactions to abort.
- **Intent Locking:** Top-down locking mechanism in granularity trees.

---

## 5. Must-Write Points for Exams
- Basic 2PL guarantees **conflict serializability**, but does NOT prevent **deadlocks**.
- Strict 2PL prevents cascading aborts by holding Exclusive locks until the transaction commits.
- Multiple granularity locking improves concurrency by allowing fine-grained locks without searching entire trees.

---

## 6. Quick Recall Flow
```
Growing Phase (Acquire Locks) -> Lock Point -> Shrinking Phase (Release Locks) -> Hold X-Locks to Commit (Strict 2PL)
```
