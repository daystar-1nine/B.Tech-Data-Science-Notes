# Cost Estimation & Choice of Query Evaluation Plan

**Q. Explain cost-based query optimization. What database catalog statistics are used for cost estimation? State and derive the cost formulas for Selection and Join algorithms (Nested Loop, Block Nested Loop, Indexed Nested Loop, Sort-Merge Join, and Hash Join). Describe the System-R dynamic programming approach to evaluation plan selection.**

---

> 📌 **Definition to Remember**
> **Cost-Based Query Optimization** is the process where a DBMS evaluates alternative physical execution plans by quantitatively estimating their resource consumption—dominated by **Disk Block I/O transfers**, disk head seeks, CPU cycles, and buffer memory allocation—using statistical metadata stored in the **DBMS System Catalog** to select the plan with the minimal total cost.

---

### 1. Catalog Statistics Kept by the DBMS

The DBMS system catalog continuously maintains statistical metadata for each relation `r` and its associated indexes:

* `n_r`: Total number of tuples (records) in relation `r`.
* `b_r`: Total number of disk blocks containing tuples of relation `r`.
* `l_r`: Size of a single record in relation `r` (in bytes).
* `f_r`: Blocking factor of relation `r` (`f_r = ⌊BlockSize / l_r⌋`), which is the number of records fitting into one disk block.
* `V(A, r)`: Number of **distinct values** for attribute `A` in relation `r`.
* `SC(A, r)`: Selection Cardinality of attribute `A` in relation `r`, representing the expected number of records matching a given equality condition.
* `H_i`: Height of index `i` (number of levels in a B+ Tree index, typically 2 to 4).
* `HT_i`: Total number of index blocks in B+ Tree index `i`.

---

### 2. Selectivity Factor & Selection Cost Estimation

The **Selectivity Factor (S)** represents the fraction of tuples in a relation expected to satisfy a given selection condition `σ_θ(r)`:
```
Selectivity S = (Expected Matching Tuples) / (Total Tuples n_r)
```

#### 1. Equality Condition on Key Attribute (`σ_(A = a)(r)` where `A` is a Key):
* Expected matching tuples: Exactly 1 tuple.
* **Cost without Index (Linear File Scan):**
  - Average case: `b_r / 2` block transfers (stops upon finding the record).
  - Worst case: `b_r` block transfers (if record is at the end or not found).
* **Cost with Primary B+ Tree Index:**
  - `Cost = H_i + 1` block transfers (traverse index levels to leaf + 1 data block read).
* **Cost with Hash Key Index:**
  - `Cost = 1` block transfer (direct hash bucket lookup).

#### 2. Equality Condition on Non-Key Attribute (`σ_(A = a)(r)`):
Assuming a uniform distribution of values across distinct values:
```
Expected Tuples = n_r / V(A, r)
```
* **Cost without Index:** Requires a complete relation scan = `b_r` block transfers.
* **Cost with Clustered B+ Tree Index:**
  - `Cost = H_i + ⌈(n_r / V(A, r)) / f_r⌉` block transfers (matching rows are contiguous on disk).
* **Cost with Non-Clustered (Secondary) B+ Tree Index:**
  - `Cost = H_i + (n_r / V(A, r))` block transfers (each matching tuple may reside in a distinct disk block!).

#### 3. Range Selections (`σ_(A ≥ v)(r)`):
Assuming uniform distribution between minimum value `min(A)` and maximum value `max(A)`:
```
Expected Tuples = n_r × [ (max(A) - v) / (max(A) - min(A)) ]
```

#### 4. Complex Conditions:
* **Conjunction (`θ1 ∧ θ2`):** `Selectivity = S(θ1) × S(θ2)` (assuming independent attributes).
* **Disjunction (`θ1 ∨ θ2`):** `Selectivity = S(θ1) + S(θ2) - [S(θ1) × S(θ2)]`.
* **Negation (`¬θ`):** `Selectivity = 1 - S(θ)`.

---

### 3. Join Algorithms and Cost Formulas (`r ⋈ s`)

Assume `r` is the **outer relation** and `s` is the **inner relation**, with `b_r` and `b_s` disk blocks, and `n_r` and `n_s` tuples respectively. Assume the memory buffer has `M` available disk frames:

#### 1. Nested-Loop Join (Tuple-by-Tuple)
For each tuple `t_r` in `r`, scan every tuple `t_s` in `s` and test the join condition.
* **Worst-Case Cost (Buffer has 1 block for r, 1 block for s):**
  ```
  Cost = b_r + (n_r × b_s) block transfers + (b_r + n_r) seeks
  ```
* **Best-Case Cost (Both relations fit entirely in RAM):**
  ```
  Cost = b_r + b_s block transfers
  ```
* *Verdict:* Extremely inefficient for large relations; used only when one relation has very few tuples.

#### 2. Block Nested-Loop Join
For each block `B_r` of relation `r`, scan each block `B_s` of relation `s`.
* **Worst-Case Cost (Buffer has only 1 block for r, 1 block for s):**
  ```
  Cost = b_r + (b_r × b_s) block transfers
  ```
* **General Case (Buffer has M frames; (M - 2) frames allocated to outer relation r):**
  ```
  Cost = b_r + ⌈b_r / (M - 2)⌉ × b_s block transfers
  ```
* *Verdict:* Dramatically reduces I/O by a factor of `f_r` compared to tuple nested-loop join.

#### 3. Indexed Nested-Loop Join
For each tuple in outer relation `r`, look up matching tuples in inner relation `s` using an existing index on the join attribute.
* **Cost Formula:**
  ```
  Cost = b_r + (n_r × c) block transfers
  ```
  *(where `c` is the single index traversal and lookup cost on relation `s`, typically `H_i + 1`)*.
* *Verdict:* Outstandingly fast when `n_r` is small and `s` has a clustered index on the join attribute.

#### 4. Merge Join (Sort-Merge Join)
Both relations are sorted on the join attribute, then merged via a single synchronized linear scan.
* **Cost Formula (when already sorted):**
  ```
  Cost = b_r + b_s block transfers
  ```
* **Cost Formula (when unsorted):** Must first sort both relations using external merge sort:
  ```
  Cost = Cost_sort(r) + Cost_sort(s) + (b_r + b_s)
  ```
* *Verdict:* Highly efficient for large tables, especially when an index already provides pre-sorted input or when results need to be ordered.

#### 5. Hash Join
Partitions both relations into `k` matching hash buckets using a hash function `h` on the join attribute. Matching occurs in-memory bucket-by-bucket:
* **Cost Formula (Standard Grace Hash Join):**
  ```
  Cost = 3 × (b_r + b_s) block transfers
  ```
  - **Partitioning Phase:** Reads both tables and writes partitions to disk = `2 × (b_r + b_s)`.
  - **Probe Phase:** Reads each partition once into memory to perform join matching = `b_r + b_s`.
* *Verdict:* Fastest algorithm for large, unsorted equi-joins where neither table fits in memory.

---

### 4. Comprehensive Join Cost Comparison Table

| Join Algorithm | Mechanism | Worst-Case Block Transfer Cost | Best-Case Memory Cost | When to Use? |
| :--- | :--- | :--- | :--- | :--- |
| **Nested-Loop Join** | For each tuple in `r`, scan all tuples in `s` | `b_r + (n_r × b_s)` | `b_r + b_s` | Only when `r` has very few rows (e.g. < 50) |
| **Block Nested-Loop** | For each block in `r`, scan all blocks in `s` | `b_r + (b_r × b_s)` | `b_r + ⌈b_r / (M-2)⌉ × b_s` | Medium tables with no indexes available |
| **Indexed Nested-Loop** | For each tuple in `r`, search index on `s` | `b_r + (n_r × c)` | `b_r + (n_r × c)` | Outer table `r` is small, inner table `s` indexed |
| **Sort-Merge Join** | Sort both on join key, then linear merge | `b_r + b_s` *(if sorted)* | `b_r + b_s` | Large tables; output required in sorted order |
| **Hash Join** | Partition into hash buckets, match in RAM | `3 × (b_r + b_s)` | `b_r + b_s` *(if 1 table fits in RAM)* | Massive unsorted tables with equi-join condition |

---

### 5. Choice of Evaluation Plan: The System-R Approach

Query optimizers must select the global lowest-cost evaluation plan from an exponential number of possible join trees:

```
Candidate Plan 1: Full Table Scan + Block Nested-Loop Join  ---> Cost: 12,400 I/Os
Candidate Plan 2: Primary Index Scan + Sort-Merge Join      ---> Cost:  2,150 I/Os
Candidate Plan 3: Secondary Index Scan + Hash Join          ---> Cost:    380 I/Os  <-- OPTIMAL!
```

#### System-R Dynamic Programming Algorithm:
1. **Plan Space Restriction (Left-Deep Trees):**
   - The optimizer restricts the search space primarily to **Left-Deep Join Trees**, where the right child of every join operator is a base relation.
   - Left-deep trees allow pipelining intermediate results without materializing them on disk.
2. **Dynamic Programming Strategy:**
   - To join a set of relations `{R1, R2, ..., Rn}`, the optimizer first finds the best single-relation access paths (index scan vs table scan).
   - It then computes the best 2-relation joins, using their lowest costs to compute the best 3-relation joins, pruning expensive sub-plans at each stage.
3. **Interesting Orders:**
   - A sub-plan with higher intermediate cost is NOT pruned if it outputs tuples in an "interesting order" (e.g. sorted on a column needed by a subsequent `ORDER BY` or `GROUP BY` clause), as it eliminates a costly later sort!

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Cost-based query optimization selects the physical execution plan with minimal estimated **Disk Block I/O transfers**.
> 2. System catalog stores: `n_r` (tuples), `b_r` (blocks), `f_r` (blocking factor), and `V(A, r)` (distinct values).
> 3. Selectivity for equality on non-key attribute with uniform distribution is **`n_r / V(A, r)`**.
> 4. Tuple Nested-Loop cost is `b_r + (n_r × b_s)`; Block Nested-Loop reduces this to `b_r + (b_r × b_s)`.
> 5. **Indexed Nested-Loop Join** cost is `b_r + (n_r × c)`, which is optimal when the outer relation is small and the inner has an index.
> 6. **Hash Join** requires `3 × (b_r + b_s)` block transfers, making it the most efficient algorithm for large unsorted equi-joins.
> 7. The **System-R dynamic programming algorithm** restricts search to left-deep join trees and retains sub-plans with interesting orders.

---

> ⚡ **Quick Recall**
> `Catalog Statistics (nr, br, V(A,r)) → Selectivity Factor → Selection Access Paths → Join Cost (Nested vs Block vs Index vs Merge vs Hash) → Left-Deep Join Trees → System-R Dynamic Programming`
