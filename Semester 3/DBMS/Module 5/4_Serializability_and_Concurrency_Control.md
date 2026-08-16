# Serializability & Concurrency Control — DBMS

> **Definition: Serializability** is the correctness criterion for concurrent transaction execution. A non-serial schedule is **serializable** if its execution outcome is equivalent to executing the transactions sequentially one after another (a Serial Schedule).

---

## 1. Detailed Technical Explanation

### 1. Types of Schedules:
- **Serial Schedule:** Transactions execute strictly one after another (No interleaving). Guaranteed to be correct, but offers poor CPU utilization.
- **Concurrent (Interleaved) Schedule:** Operations of multiple transactions interleave. High performance, but requires concurrency control.

### 2. Conflict Serializability:
Two operations **O_i** and **O_j** in a schedule are in **conflict** if and only if:
1. They belong to **different transactions**.
2. They access the **same data item**.
3. At least one of the operations is a **WRITE** (`W(X)`).

#### Conflicting Operations Matrix:
| Operation **T_1** | Operation **T_2** | Conflict Status |
| :--- | :--- | :--- |
| `Read(X)` | `Read(X)` | **No Conflict** |
| `Read(X)` | `Write(X)` | **CONFLICT** |
| `Write(X)` | `Read(X)` | **CONFLICT** |
| `Write(X)` | `Write(X)` | **CONFLICT** |

### 3. Precedence Graph (Serialization Graph) Test:
A directed graph **G = (V, E)** used to test Conflict Serializability:
- **Vertices (V):** All transactions in schedule.
- **Edges (E):** Directed edge **T_i -> T_j** if **T_i** performs a conflicting operation on data item **X** before **T_j**.

```
PRECEDENCE GRAPH RULE:
- If Precedence Graph contains NO CYCLES -> Schedule is CONFLICT SERIALIZABLE.
- If Precedence Graph contains CYCLES    -> Schedule is NOT Conflict Serializable (Concurrency Anomaly!).
```

```
Example (Cycle detected):
  [ T1 ] ---- Read(X), Write(X) ----> [ T2 ]
    ^                                   |
    |--------- Write(Y), Read(Y) -------|  (Cycle! Not Serializable)
```

---

## 2. Core Concepts & Memory Keywords
- **Conflict Equivalent:** Two schedules can be transformed into one another by swapping non-conflicting operations.
- **Serialization Graph:** Directed graph used to test conflict serializability for cycles.
- **View Serializability:** Broader class of serializability accounting for blind writes.

---

## 3. Must-Write Points for Exams
- A schedule is conflict serializable if it is conflict equivalent to some serial schedule.
- Checking for cycles in a precedence graph using Topological Sorting validates conflict serializability.
- Conflict serializability is a sufficient condition for view serializability.

---

## 4. Quick Recall Flow
```
Concurrent Operations -> Identify Conflicts (R-W, W-R, W-W) -> Draw Precedence Graph -> No Cycles? -> Serializable!
```
