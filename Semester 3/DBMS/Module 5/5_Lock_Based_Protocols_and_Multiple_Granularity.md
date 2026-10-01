# Lock-Based Protocols & Multiple Granularity

**Q. Explain lock-based concurrency control protocols. Describe Shared and Exclusive locks, the Two-Phase Locking (2PL) protocol with its variations (Strict and Rigorous 2PL), and Multiple Granularity Locking (MGL) with Intent locks.**

---

> 📌 **Definition to Remember**
> **Lock-Based Protocols** control concurrent access by requiring transactions to obtain **Locks** (Shared for reading, Exclusive for writing) before accessing data items. The **Two-Phase Locking (2PL) protocol** guarantees conflict serializability by ensuring transactions acquire all locks in a Growing phase before releasing any in a Shrinking phase.

---

### 1. Basic Lock Modes & Compatibility Matrix

1. **Shared Lock ($S$):** Requested for read-only operations (`Read(Q)`). Multiple transactions can concurrently hold shared locks on the same data item.
2. **Exclusive Lock ($X$):** Requested for write/update operations (`Write(Q)`). Only one transaction can hold an exclusive lock; no other transaction can read or write.

#### Lock Compatibility Matrix:
| Lock Requested by $T_2$ \ Lock Held by $T_1$ | Shared Lock ($S$) | Exclusive Lock ($X$) |
| :---: | :---: | :---: |
| **Shared Lock ($S$)** | **Compatible (TRUE)** | Incompatible (FALSE - Wait) |
| **Exclusive Lock ($X$)** | Incompatible (FALSE - Wait) | Incompatible (FALSE - Wait) |

---

### 2. Two-Phase Locking Protocol (2PL)

To guarantee conflict serializability, 2PL requires each transaction to execute in **two distinct phases**:

```
Number of
Locks Held
   ^               PHASE 1: GROWING PHASE          PHASE 2: SHRINKING PHASE
   |               (Locks acquired, none released) (Locks released, none acquired)
   |
   |                         /\ Lock Point
   |                        /     |                       /       |                      /         +---------------------+--------+---------------------------------------> Time
```

1. **Growing Phase:** Transaction may acquire new locks, but cannot release any lock.
2. **Lock Point:** The exact instant when the transaction acquires its final lock.
3. **Shrinking Phase:** Transaction may release locks, but cannot acquire any new lock.

#### 2PL Variations:
* **Basic 2PL:** Guarantees conflict serializability, but can suffer from **Cascading Aborts** (if $T_1$ releases an $X$ lock and then aborts, readers must also abort).
* **Strict 2PL:** Transaction holds all **Exclusive ($X$) locks until COMMIT or ABORT**. Prevents cascading aborts; schedules are strict and recoverable.
* **Rigorous 2PL:** Transaction holds **ALL locks (Shared and Exclusive) until COMMIT or ABORT**. Schedules are easily serialized in order of transaction commit.

---

### 3. Multiple Granularity Locking (MGL)

In large databases, locking at a single granularity (e.g., locking only whole tables or only single records) causes inefficiencies:
* Locking whole tables: Poor concurrency.
* Locking individual records: Huge lock management overhead.

**Multiple Granularity Locking (MGL)** organizes lockable data items in a **tree hierarchy**:

```
                       [ DATABASE ]
                            |
                       [   AREA   ]
                            |
                       [   FILE   ]
                            |
                       [  RECORD  ]
```

#### Intent Locks:
Before locking an explicit fine-grained node (e.g., a Record), a transaction must acquire an **Intent Lock** on all ancestor nodes to alert other transactions:
* **Intent Shared (IS):** Explicit shared locking will be performed at lower tree levels.
* **Intent Exclusive (IX):** Explicit exclusive locking will be performed at lower tree levels.
* **Shared with Intent Exclusive (SIX):** Subtree is explicitly locked in Shared mode, but fine-grained exclusive locking will occur at lower levels.

#### Multiple Granularity Lock Compatibility Matrix:
| | IS | IX | S | SIX | X |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **IS** | **TRUE** | **TRUE** | **TRUE** | **TRUE** | FALSE |
| **IX** | **TRUE** | **TRUE** | FALSE | FALSE | FALSE |
| **S** | **TRUE** | FALSE | **TRUE** | FALSE | FALSE |
| **SIX**| **TRUE** | FALSE | FALSE | FALSE | FALSE |
| **X** | FALSE | FALSE | FALSE | FALSE | FALSE |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Lock modes: **Shared ($S$)** allows concurrent reads; **Exclusive ($X$)** gives sole read/write access.
> 2. **Two-Phase Locking (2PL)** divides lock lifecycle into **Growing Phase** (acquire) and **Shrinking Phase** (release).
> 3. The **Lock Point** is the moment the transaction holds its maximum number of locks.
> 4. **Strict 2PL** holds all $X$ locks until commit, completely eliminating cascading rollbacks.
> 5. **Rigorous 2PL** holds all $S$ and $X$ locks until commit; standard in commercial engines.
> 6. 2PL guarantees serializability, but is vulnerable to **deadlocks**.
> 7. **Multiple Granularity Locking (MGL)** uses hierarchy trees and **Intent Locks (IS, IX, SIX)** to optimize locking overhead across records, files, and databases.

---

> ⚡ **Quick Recall**
> `S-Lock (Read) vs X-Lock (Write) → 2PL (Growing Phase → Lock Point → Shrinking Phase) → Strict 2PL (Hold X till Commit) → MGL Hierarchy & Intent Locks (IS, IX, SIX)`
