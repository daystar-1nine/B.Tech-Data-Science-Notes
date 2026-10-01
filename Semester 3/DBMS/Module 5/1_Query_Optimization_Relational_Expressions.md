# Query Optimization & Relational Algebra Equivalence Rules

**Q. Explain the architecture of query processing in a DBMS. What is query optimization? State and explain key relational algebra equivalence rules and describe the heuristic query optimization algorithm with an example.**

---

> 📌 **Definition to Remember**
> **Query Optimization** is the component of a Database Management System (DBMS) that evaluates multiple logically equivalent execution plans for an SQL query and selects the most efficient physical plan with the lowest estimated resource cost (Disk I/O, CPU, and memory usage).

---

### 1. Query Processing Lifecycle

```
                     High-Level SQL Query
                              |
                              v
                   +---------------------+
                   | Parser & Translator |
                   +---------------------+
                              |
                              v Relational Algebra Expression Tree
                   +---------------------+
                   | Query Optimizer     | <--- Uses Catalog Statistics
                   | (Heuristic & Cost)  | <--- Applies Equivalence Rules
                   +---------------------+
                              |
                              v Optimal Physical Execution Plan
                   +---------------------+
                   | Execution Engine    |
                   +---------------------+
                              |
                              v
                     Query Result Tuples
```

---

### 2. Relational Algebra Equivalence Rules

Two relational algebra expressions are **equivalent** ($E_1 \equiv E_2$) if they produce identical sets of tuples on every legal database instance:

1. **Commutativity of Selection:**
   $$\sigma_{\theta_1}(\sigma_{\theta_2}(E)) \equiv \sigma_{\theta_2}(\sigma_{\theta_1}(E))$$
2. **Cascading (Conjunction) of Selection:**
   $$\sigma_{\theta_1 \land \theta_2}(E) \equiv \sigma_{\theta_1}(\sigma_{\theta_2}(E))$$
3. **Commutativity of Natural / Theta Join:**
   $$E_1 \bowtie_\theta E_2 \equiv E_2 \bowtie_\theta E_1$$
4. **Associativity of Natural Join:**
   $$(E_1 \bowtie E_2) \bowtie E_3 \equiv E_1 \bowtie (E_2 \bowtie E_3)$$
5. **Pushing Selections Down Through Joins:**
   If selection condition $\theta_0$ involves only attributes of $E_1$:
   $$\sigma_{\theta_0}(E_1 \bowtie E_2) \equiv (\sigma_{\theta_0}(E_1)) \bowtie E_2$$
6. **Pushing Projections Down Through Joins:**
   $$\pi_{L_1 \cup L_2}(E_1 \bowtie E_2) \equiv \pi_{L_1 \cup L_2}(\pi_{L_1 \cup J}(E_1) \bowtie \pi_{L_2 \cup J}(E_2))$$

---

### 3. Heuristic Query Optimization Algorithm

Heuristic optimizers use rule-based transformations to generate an efficient evaluation tree:

1. **Deconstruct Conjunctions:** Break complex $\sigma_{\theta_1 \land \dots \land \theta_n}$ into individual cascade selections.
2. **Push Selections Down the Tree:** Move selections down as close to leaf nodes (base tables) as possible. Filtering rows early drastically reduces intermediate table sizes!
3. **Push Projections Down the Tree:** Drop unneeded columns early to reduce the memory footprint per tuple.
4. **Combine Selection with Cartesian Product:** Replace $\sigma_\theta(E_1 \times E_2)$ with an optimized **Theta-Join ($E_1 \bowtie_\theta E_2$)**.
5. **Order Joins by Selectivity:** Execute the most restrictive joins first to minimize intermediate pipeline memory.

---

### 4. Step-by-Step Optimization Example

#### Query:
Find employee names in Department 10 earning salary > 50,000:
```sql
SELECT Emp_Name FROM Employee JOIN Department 
ON Employee.Dept_ID = Department.Dept_ID 
WHERE Department.Dept_ID = 10 AND Employee.Salary > 50000;
```

```
UNOPTIMIZED QUERY TREE:                        HEURISTICALLY OPTIMIZED TREE:
            π(Emp_Name)                                  π(Emp_Name)
                 |                                            |
      σ(Dept_ID=10 ∧ Salary>50000)                         ⨝ (Dept_ID)
                 |                                          /         \
            ⨝ (Dept_ID)                                    /           \
             /         \                         σ(Salary>50000)    σ(Dept_ID=10)
            /           \                              |                 |
      [ Employee ]  [ Department ]                [ Employee ]     [ Department ]
 (Full tables joined first - SLOW!)             (Filtered before join - FAST!)
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Query optimization determines the lowest-cost physical execution plan for an SQL query.
> 2. Query processing stages: **Parsing/Translating $\rightarrow$ Optimization $\rightarrow$ Execution Engine**.
> 3. Equivalence rules transform expressions without altering their computational result.
> 4. **Pushing selections down:** The single most impactful heuristic; eliminates non-matching rows before costly joins.
> 5. **Pushing projections down:** Eliminates unneeded attributes, minimizing buffer pool memory consumption.
> 6. Equivalence rules convert $\sigma(E_1 \times E_2)$ into direct join operations ($E_1 \bowtie E_2$).
> 7. The final choice of evaluation plan uses database catalog statistics to calculate Disk I/O costs.

---

> ⚡ **Quick Recall**
> `SQL Query → Parse to RA Tree → Apply Equivalence Rules → Push Selections Down → Push Projections Down → Convert Cross-Product to Join → Minimal Cost Plan`
