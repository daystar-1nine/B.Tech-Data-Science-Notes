# Serializability & Concurrency Control

**Q. What is serializability? Differentiate between conflict serializability and view serializability. Explain how a precedence graph (serialization graph) is constructed and tested for conflict serializability with an example.**

---

> 📌 **Definition to Remember**
> **Serializability** is the fundamental correctness criterion for concurrent transaction schedules. A concurrent schedule is **serializable** if its execution outcome is computationally equivalent to some serial schedule in which transactions execute sequentially one after another without interleaving.

---

### 1. Types of Transaction Schedules

1. **Serial Schedule:** Transactions execute strictly one after another (e.g., $T_1$ finishes completely before $T_2$ begins).
   * *Pros:* 100% consistent; no concurrency anomalies.
   * *Cons:* Terrible throughput; CPU sits idle during disk I/O.
2. **Concurrent (Interleaved) Schedule:** Operations from multiple transactions interleave.
   * *Pros:* High CPU/Disk utilization and fast response times.
   * *Cons:* Can create race conditions if not serializable.

---

### 2. Conflict Serializability

Two operations $I_i$ and $I_j$ in a schedule are in **conflict** if and only if:
1. They belong to **different transactions** ($T_i \neq T_j$).
2. They access the **same data item** ($Q$).
3. **At least one of the operations is a WRITE** (`Write(Q)`).

#### Conflicting Operations Matrix:
| Operation in $T_1$ | Operation in $T_2$ | Conflict Status | Explanation |
| :---: | :---: | :---: | :--- |
| `Read(Q)` | `Read(Q)` | **No Conflict** | Multiple transactions can read concurrently. |
| `Read(Q)` | `Write(Q)` | **CONFLICT** | Changing execution order alters read value. |
| `Write(Q)` | `Read(Q)` | **CONFLICT** | Changing execution order causes dirty/stale read. |
| `Write(Q)` | `Write(Q)` | **CONFLICT** | Changing execution order overwrites final value. |

> A schedule $S$ is **Conflict Serializable** if it can be transformed into a serial schedule by a series of swaps of non-conflicting adjacent operations.

---

### 3. Precedence Graph (Serialization Graph) Algorithm

A **Precedence Graph** is a directed graph $G = (V, E)$ used to test Conflict Serializability:
* **Vertices ($V$):** Each active transaction in the schedule.
* **Edges ($E$):** Draw a directed edge **$T_i \longrightarrow T_j$** if $T_i$ performs an operation that conflicts with an operation performed later by $T_j$ on the same data item.

#### The Fundamental Serializability Theorem:
* **A schedule $S$ is Conflict Serializable IF AND ONLY IF its Precedence Graph contains NO CYCLES (Directed Acyclic Graph - DAG).**
* If the graph is acyclic, a valid serial order is obtained by **Topological Sorting** of the graph.

---

### 4. Precedence Graph Construction Example

#### Given Schedule $S$:
```
Time   T1            T2
 1   Read(X)
 2                 Write(X)   --> Conflict on X: T1 reads before T2 writes ==> Edge: T1 -> T2
 3   Write(Y)
 4                 Read(Y)    --> Conflict on Y: T1 writes before T2 reads ==> Edge: T1 -> T2
```

```
PRECEDENCE GRAPH:
      [ T1 ] --------------> [ T2 ]
```
* **Evaluation:** Contains NO cycles $\implies$ **Schedule is Conflict Serializable**.
* **Equivalent Serial Order:** $T_1 \rightarrow T_2$.

#### Non-Serializable Cycle Example:
```
Time   T1            T2
 1   Read(X)
 2                 Write(X)   --> Edge: T1 -> T2
 3                 Write(Y)
 4   Read(Y)                  --> Conflict on Y: T2 writes before T1 reads ==> Edge: T2 -> T1!
```

```
PRECEDENCE GRAPH (CYCLE DETECTED):
      [ T1 ] --------------> [ T2 ]
        ^                      |
        +----------------------+  (CYCLE! NOT Conflict Serializable!)
```

---

### 5. Conflict vs. View Serializability

| Parameter | Conflict Serializability | View Serializability |
| :--- | :--- | :--- |
| **Criterion** | Preserves conflicting operation order | Preserves initial read, final write, and read-from relationships |
| **Class Size** | Subset of View Serializable schedules | **Broader class** (includes schedules with blind writes) |
| **Testing Complexity**| **Fast: $O(V + E)$** cycle check | **NP-Complete** (exponentially hard to test) |
| **Implementation** | Practical commercial DBMSs enforce this | Theoretical concept; not used directly in engines |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Serializability is the fundamental correctness standard for concurrent database schedules.
> 2. Operations conflict if they belong to different transactions, access the same item, and at least one is a **Write**.
> 3. Conflict serializability allows transformation to a serial schedule by swapping non-conflicting instructions.
> 4. **Precedence graph test:** Draw edge $T_i \rightarrow T_j$ for conflicting operations.
> 5. **Cycle check:** A schedule is conflict serializable **if and only if its precedence graph is acyclic**.
> 6. Topological sorting of the acyclic graph gives the equivalent serial schedule order.
> 7. View serializability is broader than conflict serializability, but testing it is **NP-Complete**.

---

> ⚡ **Quick Recall**
> `Concurrent Schedule → Identify Conflicting Ops (At least one Write) → Construct Precedence Graph (Ti -> Tj) → Check for Cycles (Acyclic = Serializable) → Topological Sort`
