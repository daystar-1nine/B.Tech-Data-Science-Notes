# Serializability & Schedule Recoverability

**Q. What is serializability? Differentiate between conflict serializability and view serializability. Explain the precedence graph (serialization graph) algorithm for testing conflict serializability with examples. Classify schedules based on recoverability (Unrecoverable, Recoverable, Cascadeless, and Strict schedules).**

---

> 📌 **Definition to Remember**
> **Serializability** is the fundamental correctness criterion for concurrent transaction schedules. A concurrent schedule is **serializable** if its computational outcome is identical to that of some serial schedule in which the transactions execute sequentially, one after another, without any interleaving of operations.

---

### 1. Types of Transaction Schedules

A **Schedule** (or history) represents the chronological sequence in which operations (`Read`, `Write`, `Commit`, `Abort`) from multiple concurrent transactions are executed by the DBMS.

1. **Serial Schedule:**
   - Transactions execute strictly one after another without any interleaved operations (e.g., all instructions of `T1` finish before `T2` starts).
   - *Advantage:* Guaranteed 100% consistent and free from concurrency anomalies.
   - *Disadvantage:* Terrible system throughput and high latency; the CPU sits idle while a transaction waits for disk I/O.
2. **Concurrent (Interleaved) Schedule:**
   - Operations from multiple active transactions interleave to maximize CPU and disk utilization.
   - *Advantage:* High throughput and fast response times.
   - *Requirement:* Must be proved **serializable** to prevent race conditions and dirty data corruption.

---

### 2. Conflicting Operations & Conflict Serializability

Two operations `I_i` and `I_j` within a schedule are in **conflict** if and only if all three conditions are satisfied:
1. They belong to **different transactions** (`T_i ≠ T_j`).
2. They access the **same data item** (`Q`).
3. **At least one of the operations is a WRITE** (`Write(Q)`).

#### Conflicting Operations Matrix:
| Operation in `T1` | Operation in `T2` | Conflict Status | Concurrency Reason |
| :---: | :---: | :---: | :--- |
| `Read(Q)` | `Read(Q)` | **No Conflict** | Multiple transactions can safely read the same data simultaneously. |
| `Read(Q)` | `Write(Q)` | **CONFLICT** | Changing execution order alters the value read by `T1`. |
| `Write(Q)` | `Read(Q)` | **CONFLICT** | Changing execution order causes `T2` to read dirty/stale data. |
| `Write(Q)` | `Write(Q)` | **CONFLICT** | Changing execution order overwrites the final state of item `Q`. |

> **Conflict Equivalence:** Two schedules `S` and `S'` are **conflict equivalent** if `S'` can be transformed into `S` by a series of swaps of non-conflicting adjacent operations.
> 
> **Conflict Serializability:** A schedule is **conflict serializable** if it is conflict equivalent to some serial schedule.

---

### 3. Precedence Graph (Serialization Graph) Algorithm

The **Precedence Graph** is a directed graph `G = (V, E)` used to systematically test whether a concurrent schedule is conflict serializable:
* **Vertices (`V`):** Each transaction `T_i` participating in the schedule.
* **Directed Edges (`E`):** Draw a directed edge **`T_i → T_j`** if `T_i` performs an operation that conflicts with an operation performed *later* by `T_j` on the same data item.

#### Edge Drawing Rules:
1. **Read-Write Conflict:** `T_i` executes `Read(Q)` before `T_j` executes `Write(Q)`.
2. **Write-Read Conflict:** `T_i` executes `Write(Q)` before `T_j` executes `Read(Q)`.
3. **Write-Write Conflict:** `T_i` executes `Write(Q)` before `T_j` executes `Write(Q)`.

#### The Fundamental Serializability Theorem:
* **A schedule `S` is Conflict Serializable IF AND ONLY IF its Precedence Graph contains NO CYCLES (it is a Directed Acyclic Graph - DAG).**
* If the graph is acyclic, a valid equivalent serial execution order is produced by performing a **Topological Sort** on the graph.

---

### 4. Step-by-Step Graph Examples

#### Example 1: Conflict Serializable Schedule

```
Time   Transaction T1             Transaction T2
 1     Read(X)
 2                                Write(X)   --> Conflict on X: T1 reads before T2 writes ==> Edge: T1 -> T2
 3     Write(Y)
 4                                Read(Y)    --> Conflict on Y: T1 writes before T2 reads ==> Edge: T1 -> T2
```

```
PRECEDENCE GRAPH:
      [ T1 ] --------------> [ T2 ]
```
* **Analysis:** The precedence graph contains only one directed edge (`T1 → T2`) and **NO CYCLES**.
* **Verdict:** The schedule is **Conflict Serializable**.
* **Equivalent Serial Order:** `T1 → T2`.

---

#### Example 2: Non-Serializable Schedule (Cycle Detected)

```
Time   Transaction T1             Transaction T2
 1     Read(X)
 2                                Write(X)   --> Conflict on X: T1 reads before T2 writes ==> Edge: T1 -> T2
 3                                Write(Y)
 4     Read(Y)                               --> Conflict on Y: T2 writes before T1 reads ==> Edge: T2 -> T1!
```

```
PRECEDENCE GRAPH (CYCLE DETECTED):
      [ T1 ] --------------> [ T2 ]
        ^                      |
        +----------------------+  (CYCLE: T1 -> T2 -> T1!)
```
* **Analysis:** A cycle exists between `T1` and `T2` (`T1 → T2 → T1`). `T1` must execute before `T2` and simultaneously `T2` must execute before `T1`, which is logically impossible!
* **Verdict:** The schedule is **NOT Conflict Serializable**.

---

### 5. Conflict Serializability vs. View Serializability

Two schedules `S` and `S'` are **view equivalent** if they satisfy three conditions:
1. **Initial Read:** For each item `Q`, if `T_i` reads the initial value of `Q` in `S`, it must also read the initial value in `S'`.
2. **Updated Read (Read-From):** If `T_j` reads a value of `Q` produced by `Write(Q)` of `T_i` in `S`, it must also read the value produced by `T_i` in `S'`.
3. **Final Write:** For each item `Q`, if `T_i` performs the final `Write(Q)` in `S`, it must also perform the final `Write(Q)` in `S'`.

#### Comparison Table:
| Parameter | Conflict Serializability | View Serializability |
| :--- | :--- | :--- |
| **Criterion** | Preserves order of adjacent conflicting operations | Preserves initial read, read-from, and final write relationships |
| **Blind Writes** | Does NOT accommodate blind writes (`Write(Q)` without prior read) | Accommodates schedules with **blind writes** |
| **Testing Complexity**| **Fast: `O(V + E)`** using cycle detection in Precedence Graph | **NP-Complete**; exponentially hard to test |
| **Class Relationship** | Strict subset: Every conflict serializable schedule is view serializable | Broader class: Includes non-conflict serializable schedules with blind writes |
| **Practical Use** | Used in commercial DBMS concurrency engines | Primarily a theoretical concept; impractical to verify in real-time |

---

### 6. Classification of Schedules Based on Recoverability

In addition to being serializable, concurrent schedules must be recoverable to ensure database consistency upon failures:

```
+-------------------------------------------------------+
| All Schedules                                         |
|  +-------------------------------------------------+  |
|  | Recoverable Schedules                           |  |
|  |  +-------------------------------------------+  |  |
|  |  | Cascadeless Schedules (ACA)               |  |  |
|  |  |  +-------------------------------------+  |  |  |
|  |  |  | Strict Schedules                    |  |  |  |
|  |  |  +-------------------------------------+  |  |  |
|  |  +-------------------------------------------+  |  |
|  +-------------------------------------------------+  |
+-------------------------------------------------------+
```

#### 1. Unrecoverable Schedule:
* Occurs when transaction `T_j` reads a dirty value written by `T_i`, and `T_j` **commits BEFORE `T_i` commits**.
* If `T_i` subsequently aborts, `T_j` has committed dirty, non-existent data that cannot be rolled back (violating Durability). The DBMS cannot allow unrecoverable schedules!

#### 2. Recoverable Schedule:
* For every pair of transactions where `T_j` reads a data item previously written by `T_i`, **`T_i` MUST commit BEFORE `T_j` commits**.

#### 3. Cascading Aborts (Cascading Rollback):
* In a recoverable schedule, if `T1` writes `X` and aborts, all uncommitted transactions (`T2`, `T3`) that read `X` must also be rolled back in a cascading chain, causing wasted CPU resources.

#### 4. Cascadeless Schedule (Avoids Cascading Aborts - ACA):
* Every transaction in the schedule reads data items **ONLY AFTER the transaction that wrote them has successfully COMMITTED**.
* Eliminates cascading aborts completely: if a writing transaction aborts, no other active transaction has read its dirty values.

#### 5. Strict Schedule:
* A transaction can **neither read nor write** a data item until the previous transaction that wrote that data item has either committed or aborted.
* Makes undo operations trivial: the rollback of an aborted transaction simply requires restoring the before-image from the log.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Serializability guarantees that concurrent execution produces results identical to some serial execution.
> 2. Conflicting operations belong to different transactions, access the same item, and at least one is a **Write**.
> 3. Conflict serializability is tested using a **Precedence Graph (Serialization Graph)** with vertices for transactions and directed edges for conflicts.
> 4. **Cycle Theorem:** A schedule is conflict serializable **if and only if its precedence graph contains no cycles (is a DAG)**.
> 5. Topological sorting of the acyclic graph yields the equivalent serial execution order.
> 6. Testing conflict serializability is polynomial `O(V + E)`, whereas testing view serializability is **NP-Complete**.
> 7. Schedule recoverability hierarchy: **Strict ⊂ Cascadeless (ACA) ⊂ Recoverable ⊂ All Schedules**.

---

> ⚡ **Quick Recall**
> `Concurrent Schedule → Conflicting Ops (At least one Write) → Precedence Graph (Ti → Tj) → Acyclic = Conflict Serializable → Topological Sort Order → Recoverability (Strict ⊂ Cascadeless ⊂ Recoverable)`
