# Lock-Based Protocols & Multiple Granularity

**Q. Explain lock-based concurrency control protocols. Describe Shared and Exclusive locks with their compatibility matrix. Explain the Two-Phase Locking (2PL) protocol and its variations (Basic, Conservative, Strict, and Rigorous 2PL). Describe Deadlock Handling (Wait-Die, Wound-Wait, and Wait-For Graph) and Multiple Granularity Locking (MGL) with Intent locks.**

---

> 📌 **Definition to Remember**
> **Lock-Based Protocols** regulate concurrent access to data items by requiring transactions to obtain authorization privileges called **Locks** (Shared for read operations, Exclusive for write operations) prior to data access. The **Two-Phase Locking (2PL)** protocol guarantees conflict serializability by requiring transactions to acquire all locks during a Growing phase before releasing any lock in a Shrinking phase.

---

### 1. Basic Lock Modes & Compatibility Matrix

Before accessing a data item `Q`, a transaction must issue a lock request to the DBMS Lock Manager:

1. **Shared Lock (`S`):**
   - Acquired for read-only operations (`Read(Q)`).
   - Multiple concurrent transactions can hold shared locks on the same data item simultaneously.
2. **Exclusive Lock (`X`):**
   - Acquired for read and write operations (`Write(Q)`).
   - Only one transaction can hold an exclusive lock on an item. No other transaction can hold any lock (`S` or `X`) on that item until the exclusive lock is released.

#### Lock Compatibility Matrix:
| Lock Requested by `T2` \ Lock Held by `T1` | Shared Lock (`S`) | Exclusive Lock (`X`) |
| :---: | :---: | :---: |
| **Shared Lock (`S`)** | **Compatible (TRUE - Granted)** | Incompatible (FALSE - `T2` Waits) |
| **Exclusive Lock (`X`)** | Incompatible (FALSE - `T2` Waits) | Incompatible (FALSE - `T2` Waits) |

#### Lock Conversion:
* **Lock Upgrade:** Converting an existing Shared lock (`S`) to an Exclusive lock (`X`) when a transaction decides to write to an item it was previously only reading (allowed only during the Growing Phase).
* **Lock Downgrade:** Converting an Exclusive lock (`X`) to a Shared lock (`S`) when a transaction finishes writing but still needs to read (allowed during the Shrinking Phase).

---

### 2. Two-Phase Locking (2PL) Protocol

To guarantee conflict serializability, the **Two-Phase Locking (2PL)** protocol mandates that every transaction divides its locking lifecycle into two distinct, non-overlapping phases:

```
Number of
Locks Held
   ^
   |                    LOCK POINT
   |                   (Peak Locks)
   |                        /\
   |                       /  \
   |                      /    \
   |                     /      \
   |                    /        \
   |                   /          \
   |  GROWING PHASE   /            \   SHRINKING PHASE
   |  (Acquires locks;              \  (Releases locks;
   |   Releases NONE)                \  Acquires NONE)
   |                  /                \
   +-----------------+------------------+-------------------> Time
```

1. **Phase 1 — Growing Phase (Expansion Phase):**
   - The transaction may acquire new locks (or upgrade `S` to `X`).
   - The transaction **cannot release any lock**.
2. **The Lock Point:**
   - The exact moment in time when the transaction acquires its final lock.
   - The serialization order of transactions in 2PL is determined strictly by the chronological sequence of their lock points!
3. **Phase 2 — Shrinking Phase (Contraction Phase):**
   - The transaction may release locks (or downgrade `X` to `S`).
   - The transaction **cannot acquire any new lock** once the first lock is released.

#### The 4 Variations of 2PL:

1. **Basic 2PL:**
   - Follows standard growing and shrinking phases.
   - *Advantage:* Guarantees conflict serializability.
   - *Disadvantage:* Vulnerable to **deadlocks** and **cascading aborts** (if `T1` releases an `X` lock on item `Q` in its shrinking phase and later aborts, all transactions that read dirty `Q` must also abort).
2. **Conservative 2PL (Static 2PL):**
   - The transaction must declare and acquire **all required locks** before starting execution. If any lock is unavailable, it acquires none and waits.
   - *Advantage:* Completely **deadlock-free**!
   - *Disadvantage:* Severely limits concurrency; predicting all required data items in advance is difficult in dynamic applications.
3. **Strict 2PL:**
   - Transaction follows 2PL rules and holds **ALL Exclusive (`X`) locks until COMMIT or ABORT**. Shared locks can be released gradually in the shrinking phase.
   - *Advantage:* Completely prevents cascading aborts! Guarantees recoverable and cascadeless schedules.
4. **Rigorous 2PL:**
   - Transaction holds **ALL locks (both Shared `S` and Exclusive `X`) until COMMIT or ABORT**.
   - *Advantage:* Transactions are serialized in the exact order in which they commit. Most widely implemented locking protocol in modern relational database engines!

#### 2PL Variations Comparison Table:
| 2PL Variation | Lock Holding Policy | Conflict Serializable? | Cascading Abort Free? | Deadlock Free? |
| :--- | :--- | :---: | :---: | :---: |
| **Basic 2PL** | Normal Growing / Shrinking | **Yes** | No | No |
| **Conservative 2PL** | Acquire all locks upfront | **Yes** | No | **Yes** |
| **Strict 2PL** | Hold all `X` locks until Commit | **Yes** | **Yes** | No |
| **Rigorous 2PL** | Hold all `S` and `X` locks until Commit | **Yes** | **Yes** | No |

---

### 3. Deadlock Handling in Lock-Based Systems

A **Deadlock** occurs when two or more transactions are in a simultaneous circular wait state, each waiting for a lock currently held by another transaction in the cycle:

```
Transaction T1: Holds Lock on X, Waiting for Lock on Y
Transaction T2: Holds Lock on Y, Waiting for Lock on X
Result        : Both blocked indefinitely!
```

#### 1. Deadlock Prevention (Timestamp-Based Schemes):
Assign unique monotonically increasing timestamps `TS(T_i)` when transactions enter the system. Assume `T_i` requests a lock held by `T_j`:

* **Wait-Die Scheme (Non-Preemptive):**
  - If `TS(T_i) < TS(T_j)` (`T_i` is older than `T_j`): `T_i` is allowed to **wait**.
  - If `TS(T_i) > TS(T_j)` (`T_i` is younger than `T_j`): `T_i` **dies** (aborts and restarts with its original timestamp).
  - *Rule:* Older transactions wait; younger transactions die.

* **Wound-Wait Scheme (Preemptive):**
  - If `TS(T_i) < TS(T_j)` (`T_i` is older than `T_j`): `T_i` **wounds** `T_j` (`T_j` is aborted and forced to yield the lock).
  - If `TS(T_i) > TS(T_j)` (`T_i` is younger than `T_j`): `T_i` is allowed to **wait**.
  - *Rule:* Older transactions preempt/wound younger transactions; younger transactions wait. Generally incurs fewer aborts than Wait-Die.

#### 2. Deadlock Detection (Wait-For Graph - WFG):
Construct a dynamic directed graph `WFG = (V, E)`:
* **Vertices (`V`):** Active transactions.
* **Edges (`E`):** Directed edge `T_i → T_j` if `T_i` is waiting for a lock held by `T_j`.
* **Detection Rule:** Periodically run a cycle-detection algorithm (e.g. Tarjan's or DFS). **A deadlock exists if and only if the Wait-For Graph contains a cycle!**

#### 3. Deadlock Recovery:
When a cycle is detected, the DBMS must:
1. **Victim Selection:** Choose the transaction whose abort incurs minimal cost (fewest updates, lowest CPU time consumed).
2. **Rollback Degree:** Perform a total rollback (abort) or partial rollback to the most recent savepoint that eliminates the lock contention.
3. **Starvation Prevention:** Ensure the same transaction is not repeatedly chosen as victim (track number of aborts and prioritize older transactions).

---

### 4. Multiple Granularity Locking (MGL)

Locking at a single level of granularity (e.g. only entire tables or only individual records) causes trade-offs:
* Locking whole tables: Severe concurrency bottleneck for multi-user workloads.
* Locking individual rows: Millions of locks causing massive lock manager memory overhead.

**Multiple Granularity Locking (MGL)** arranges lockable database entities in a tree hierarchy:

```
                       [  DATABASE  ]
                             |
                       [ TABLESPACE ]
                             |
                       [   TABLE    ]
                             |
                       [    PAGE    ]
                             |
                       [   RECORD   ]
```

#### Intent Locks:
Before a transaction can acquire an explicit lock (`S` or `X`) on a fine-grained node (such as a Record), it must first acquire an **Intent Lock** on all ancestor nodes (Table, Database) to signal its intentions to other transactions:

* **Intent Shared (`IS`):** Indicates explicit shared locking will be performed at lower levels.
* **Intent Exclusive (`IX`):** Indicates explicit exclusive locking will be performed at lower levels.
* **Shared with Intent Exclusive (`SIX`):** The entire subtree rooted at this node is explicitly locked in Shared mode, but fine-grained exclusive locking will occur on descendant nodes.

#### Multiple Granularity Lock Compatibility Matrix:
| Lock Held \ Lock Requested | `IS` | `IX` | `S` | `SIX` | `X` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **`IS`** | **Compatible** | **Compatible** | **Compatible** | **Compatible** | Incompatible |
| **`IX`** | **Compatible** | **Compatible** | Incompatible | Incompatible | Incompatible |
| **`S`** | **Compatible** | Incompatible | **Compatible** | Incompatible | Incompatible |
| **`SIX`** | **Compatible** | Incompatible | Incompatible | Incompatible | Incompatible |
| **`X`** | Incompatible | Incompatible | Incompatible | Incompatible | Incompatible |

#### MGL Locking Protocol Rules:
1. Lock acquisitions must proceed from the **root downwards (Top-Down)**.
2. To acquire `S` or `IS` on a node, the transaction must hold `IS` or `IX` on its parent.
3. To acquire `X`, `IX`, or `SIX` on a node, the transaction must hold `IX` or `SIX` on its parent.
4. Lock releases must proceed in reverse order: from the **leaves upwards (Bottom-Up)**.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Lock modes: **Shared (`S`)** for concurrent reads; **Exclusive (`X`)** for exclusive read/write.
> 2. **Two-Phase Locking (2PL)** divides execution into **Growing Phase** (acquire only) and **Shrinking Phase** (release only).
> 3. The **Lock Point** is the moment a transaction holds its peak number of locks and defines its serial order.
> 4. **Strict 2PL** holds all `X` locks until commit/abort, eliminating cascading rollbacks.
> 5. **Rigorous 2PL** holds all `S` and `X` locks until commit/abort; standard in commercial engines.
> 6. Deadlock prevention schemes: **Wait-Die** (non-preemptive: older waits, younger dies) vs **Wound-Wait** (preemptive: older wounds younger).
> 7. **Multiple Granularity Locking (MGL)** uses hierarchy trees and **Intent Locks (`IS`, `IX`, `SIX`)** to eliminate fine-grained traversal overhead.

---

> ⚡ **Quick Recall**
> `S-Lock (Read) vs X-Lock (Write) → 2PL (Growing → Lock Point → Shrinking) → Strict 2PL (Hold X) → Rigorous 2PL (Hold All) → Deadlock (Wait-Die vs Wound-Wait vs WFG) → MGL Hierarchy & Intent Locks (IS, IX, SIX)`
