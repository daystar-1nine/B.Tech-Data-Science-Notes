# Estimating Statistics & Choice of Evaluation Plan — DBMS

> **Definition: Cost-Based Query Optimization** estimates the physical execution cost (Disk I/O, CPU cycles, Network latency) of candidate evaluation plans using **System Catalog Statistics** to select the minimal cost plan.

---

## 1. Detailed Technical Explanation

### 1. Catalog Statistics Kept by DBMS:
- n_r**:** Number of tuples in relation **r**.
- b_r**:** Number of disk blocks containing tuples of relation **r**.
- l_r**:** Size of a tuple in relation **r** (in bytes).
- f_r**:** Blocking factor of relation **r** (number of tuples per block).
- V(A, r)**:** Number of distinct values for attribute **A** in relation **r**.

### 2. Cost Estimation Formulas:

#### Selection Cost Estimation:
- **Equality Condition **\sigma_{A = a}(r)**:**
  - If no index exists: Cost = **b_r** block reads.
  - Expected output tuples: **E = racn_r{V(A, r)}**
- **Range Condition **\sigma_{A \ge a}(r)**:**
  - Estimated size: **E = n_r × rac{Max(A) - a}{Max(A) - Min(A)}**

#### Join Cost Estimation (**r owtie s**):
- **Nested-Loop Join:**
  - Cost = **b_r + (n_r × b_s)** block accesses.
- **Block Nested-Loop Join:**
  - Cost = **b_r + (b_r × b_s)** block accesses.
- **Indexed Nested-Loop Join:**
  - Cost = **b_r + (n_r × c)** where **c** is index access cost.
- **Hash Join / Merge Join:**
  - Cost = **3(b_r + b_s)** block accesses.

### 3. Choice of Evaluation Plan:
The query optimizer generates multiple physical evaluation plans, computes total cost = **{Disk I/O Cost} + CPU Cost**, and selects the plan with the **minimum total cost**.

---

## 2. Core Concepts & Memory Keywords
- **Catalog Statistics:** Metadata (**n_r, b_r, V(A,r)**) used for selectivity calculation.
- **Selectivity Factor:** Proportion of tuples satisfying a predicate.
- **Nested-Loop Join:** Basic join algorithm iterating over outer and inner tables.

---

## 3. Must-Write Points for Exams
- Disk I/O (number of block transfers) is the primary cost metric in database query evaluation.
- Block nested-loop join is significantly faster than tuple-nested loop join by reading outer relation blocks into memory.
- Hash joins and merge joins achieve near linear performance **O(b_r + b_s)** for large tables.

---

## 4. Quick Recall Flow
```
System Catalog Stats -> Compute Selectivity -> Estimate Disk Block Accesses -> Select Plan with Lowest Total Cost
```
