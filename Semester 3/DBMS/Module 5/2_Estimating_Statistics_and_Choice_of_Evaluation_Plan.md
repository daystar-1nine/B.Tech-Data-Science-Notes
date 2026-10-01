# Cost Estimation & Choice of Query Evaluation Plan

**Q. Explain cost-based query optimization. What database catalog statistics are used for cost estimation? State the cost formulas for Selection and Join algorithms (Nested Loop, Block Nested Loop, Indexed Nested Loop, Hash Join, and Merge Join).**

---

> 📌 **Definition to Remember**
> **Cost-Based Query Optimization** estimates the physical execution cost—dominated by **Disk Block I/O transfers**, CPU cycles, and buffer memory allocation—of competing execution plans using statistical metadata stored in the **DBMS System Catalog** to select the plan with minimal total cost.

---

### 1. Catalog Statistics Kept by the DBMS

The system catalog periodically stores statistical metadata for each relation $r$:
* $n_r$: Number of tuples in relation $r$.
* $b_r$: Number of disk blocks containing tuples of relation $r$.
* $l_r$: Size of a tuple in relation $r$ (in bytes).
* $f_r$: Blocking factor of relation $r$ ($f_r = \lfloor \text{BlockSize} / l_r \rfloor$).
* $V(A, r)$: Number of **distinct values** for attribute $A$ in relation $r$.
* $H_i$: Height of index $i$ (number of levels in a B+ Tree index).

---

### 2. Selectivity Factor & Cost Estimation for Selections

The **Selectivity Factor ($S$)** is the estimated fraction of tuples satisfying a predicate:

1. **Equality Selection ($\sigma_{A = a}(r)$):**
   * Expected tuples:
     $$E = \frac{n_r}{V(A, r)}$$
   * Cost without index (Full Table Scan): $b_r$ block transfers.
   * Cost with B+ Tree Primary Index: $H_i + 1$ block transfers.
2. **Range Selection ($\sigma_{A \ge a}(r)$):**
   $$E = n_r \times \frac{\max(A) - a}{\max(A) - \min(A)}$$
3. **Conjunctive Condition ($\theta_1 \land \theta_2$):**
   $$S = S(\theta_1) \times S(\theta_2)$$

---

### 3. Join Algorithms Cost Formulas ($r \bowtie s$)

Assume $r$ is the **outer relation** and $s$ is the **inner relation**:

| Join Algorithm | Mechanism | Worst-Case Block I/O Cost | Best-Case Memory Condition |
| :--- | :--- | :--- | :--- |
| **Nested-Loop Join** | For each tuple in $r$, scan all tuples in $s$. | $\mathbf{b_r + (n_r \times b_s)}$ | Extremely slow; used only for tiny tables. |
| **Block Nested-Loop Join** | For each block in $r$, scan each block in $s$. | $\mathbf{b_r + (b_r \times b_s)}$ | Reduces I/O by factor of $f_r$ over tuple nested loop. |
| **Indexed Nested-Loop Join** | For each tuple in $r$, look up matching tuples in $s$ using index. | $\mathbf{b_r + (n_r \times c)}$ *(where $c$ is B+ Tree lookup cost)* | Optimal when outer relation $r$ is small and $s$ has index. |
| **Merge Join (Sort-Merge)** | Both relations sorted on join attribute; merged linearly. | $\mathbf{b_r + b_s}$ *(plus sort cost $O(b \log b)$ if unsorted)* | Highly efficient when relations are pre-sorted or indexed. |
| **Hash Join** | Partition $r$ and $s$ into hash buckets; match in-memory. | $\mathbf{3(b_r + b_s)}$ | Fastest algorithm for large unsorted equi-joins. |

---

### 4. Choice of Evaluation Plan: The System-R Approach

```
Candidate Plan 1 (Table Scan + Nested-Loop Join)  ---> Cost: 10,500 I/Os
Candidate Plan 2 (Index Scan + Hash Join)         ---> Cost:    420 I/Os  <-- CHOSEN!
Candidate Plan 3 (Merge Join with Sort)           ---> Cost:  1,250 I/Os
```

1. **Plan Space Enumeration:** The optimizer generates candidate evaluation trees.
2. **Cost Calculation:** Computes:
   $$\text{Total Cost} = (\text{Block I/O Cost} \times t_{I/O}) + (\text{CPU Instructions} \times t_{CPU})$$
3. **Pruning:** Employs **Dynamic Programming** (System-R algorithm) to discard expensive sub-plans early, outputting the globally optimal plan.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Cost-based query optimization minimizes physical resource cost, primarily **Disk Block I/O**.
> 2. System catalog tracks $n_r$ (tuples), $b_r$ (blocks), and $V(A, r)$ (distinct values).
> 3. Selectivity for equality condition on uniform distribution is **$n_r / V(A, r)$**.
> 4. Tuple Nested-Loop cost is $b_r + (n_r \times b_s)$; Block Nested-Loop reduces this to $b_r + (b_r \times b_s)$.
> 5. **Indexed Nested-Loop Join** has cost $b_r + (n_r \times c)$, ideal when inner table has a B+ Tree index.
> 6. **Hash Join** and **Merge Join** achieve linear execution cost $O(b_r + b_s)$ for large tables.
> 7. Dynamic programming is used to efficiently search the exponential search space of join trees.

---

> ⚡ **Quick Recall**
> `Catalog Stats (nr, br, V(A,r)) → Selectivity Factor → Join Cost (Nested-Loop vs Block vs Hash vs Merge) → Total I/O Cost → Dynamic Programming Plan Selection`
