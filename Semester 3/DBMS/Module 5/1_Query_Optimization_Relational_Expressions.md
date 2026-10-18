# Query Optimization & Relational Algebra Equivalence Rules

**Q. Explain the architecture of query processing in a DBMS. What is query optimization? State and explain key relational algebra equivalence rules and describe the heuristic query optimization algorithm with a concrete example.**

---

> 📌 **Definition to Remember**
> **Query Optimization** is the process within a Database Management System (DBMS) that evaluates multiple logically equivalent execution plans for a given SQL query and selects the most efficient physical execution plan with the lowest estimated resource cost in terms of Disk Block I/O, CPU execution cycles, and memory footprint.

---

### 1. Architecture of Query Processing

Query processing transforms a declarative, high-level SQL query into a low-level procedural sequence of physical operations executed against physical disk storage blocks.

```
                      High-Level SQL Query
                               |
                               v
                    +---------------------+
                    | Parser & Translator |
                    +---------------------+
                               |
                               v Initial Relational Algebra Expression Tree
                    +---------------------+
                    |   Query Optimizer   | <--- Database System Catalog
                    | (Heuristic & Cost)  | <--- Relational Equivalence Rules
                    +---------------------+
                               |
                               v Optimal Physical Execution Plan
                    +---------------------+
                    |  Execution Engine   |
                    +---------------------+
                               |
                               v
                       Query Result Rows
```

#### The Four Stages of Query Processing:
1. **Parsing and Translation:**
   - **Syntax Checking:** Verifies that the SQL statement adheres to SQL grammatical syntax rules.
   - **Semantic Checking:** Validates that tables, columns, data types, and user access permissions exist by consulting the DBMS System Catalog.
   - **Translation:** Translates the parsed query into an initial internal representation called a **Relational Algebra Expression Tree**.
2. **Query Optimization:**
   - Explores logically equivalent query trees using **Equivalence Rules**.
   - Applies **Heuristic Transformations** (e.g., pushing filters and projections down).
   - Uses statistical catalog metadata to perform **Cost Estimation** across alternative join and scan algorithms, outputting the optimal physical evaluation plan.
3. **Code Generation / Plan Compilation:**
   - Generates executable machine code or interpreted bytecode for the chosen execution plan.
4. **Execution Engine:**
   - Executes the physical plan by reading and writing disk blocks via the buffer manager and returns resulting tuples to the client application.

---

### 2. Relational Algebra Equivalence Rules

Two relational algebra expressions `E1` and `E2` are defined as **equivalent** (`E1 ≡ E2`) if they produce the exact same set of tuples on every legal database instance.

DBMS query optimizers apply the following formal equivalence rules to transform expensive query trees into lower-cost alternatives:

#### 1. Commutativity of Selection:
Consecutive selection predicates can be evaluated in any order:
```
σ_θ1(σ_θ2(E)) ≡ σ_θ2(σ_θ1(E))
```

#### 2. Cascading (Conjunction) of Selection:
A complex conjunctive filter condition can be decomposed into a sequence of individual selections:
```
σ_(θ1 ∧ θ2)(E) ≡ σ_θ1(σ_θ2(E))
```
*Significance:* Allows individual filter predicates to be moved independently down separate branches of a join tree.

#### 3. Commutativity of Joins:
The order of relations in a natural join or theta join does not alter the output:
```
E1 ⋈_θ E2 ≡ E2 ⋈_θ E1
```

#### 4. Associativity of Joins:
Multiple joins can be grouped and ordered in any associative grouping:
```
(E1 ⋈ E2) ⋈ E3 ≡ E1 ⋈ (E2 ⋈ E3)
```
*Significance:* Enables the optimizer to join smaller, more restrictive tables first to keep intermediate results tiny.

#### 5. Pushing Selection Down Through Joins:
If a selection condition `θ0` involves only attributes belonging to relation `E1`:
```
σ_θ0(E1 ⋈ E2) ≡ (σ_θ0(E1)) ⋈ E2
```
*Significance:* Applying selection before the join dramatically reduces the number of tuples entering the join operator.

#### 6. Pushing Selection Down Through Union:
Selections distribute over union operations:
```
σ_θ(E1 ∪ E2) ≡ σ_θ(E1) ∪ σ_θ(E2)
```

#### 7. Pushing Projections Down Through Joins:
Unneeded columns can be discarded before joining two relations:
```
π_(L1 ∪ L2)(E1 ⋈ E2) ≡ π_(L1 ∪ L2)( π_(L1 ∪ J)(E1) ⋈ π_(L2 ∪ J)(E2) )
```
*(where `J` is the set of join attributes, `L1` are target attributes from `E1`, and `L2` are target attributes from `E2`)*.

#### 8. Converting Cartesian Products to Theta Joins:
A Cartesian cross-product followed by a selection on join attributes is mathematically equivalent to a Theta Join:
```
σ_θ(E1 × E2) ≡ E1 ⋈_θ E2
```

---

### 3. Heuristic Query Optimization Algorithm

Heuristic query optimization applies a systematic, rule-based sequence of transformations to minimize intermediate relation sizes without calculating explicit numerical costs:

1. **Step 1 — Deconstruct Conjunctions:**
   - Break complex `WHERE` clauses into cascades of single-predicate selections using the cascading selection rule (`σ_(θ1 ∧ θ2) ≡ σ_θ1(σ_θ2)`).
2. **Step 2 — Push Selections Down the Tree:**
   - Move selection operators down as far as possible toward the leaf nodes (base relations). Filtering tuples early is the single most effective optimization in relational databases!
3. **Step 3 — Order Leaf Joins by Selectivity:**
   - Reorder join operations so that relations producing the smallest intermediate results are joined earliest.
4. **Step 4 — Push Projections Down the Tree:**
   - Identify unneeded attributes at each intermediate step and project them out immediately. Keeping only necessary attributes minimizes tuple byte sizes and saves buffer memory.
5. **Step 5 — Replace Cartesian Products:**
   - Combine any adjacent Cartesian product (`×`) and selection (`σ`) into a direct join (`⋈`).
6. **Step 6 — Identify Common Subexpressions:**
   - If a subexpression appears multiple times in a complex query, compute it once and pipeline or cache the intermediate result.

---

### 4. Step-by-Step Optimization Example

#### SQL Query:
Find employee names in Department 10 earning a salary greater than 50,000:

```sql
SELECT Emp_Name 
FROM Employee JOIN Department 
ON Employee.Dept_ID = Department.Dept_ID 
WHERE Department.Dept_ID = 10 AND Employee.Salary > 50000;
```

#### Database Statistics:
* `Employee`: 100,000 tuples (only 500 earn > 50,000).
* `Department`: 50 tuples (only 1 tuple has `Dept_ID = 10`).

```
CANONICAL UNOPTIMIZED TREE:                    HEURISTICALLY OPTIMIZED TREE:

             π(Emp_Name)                                π(Emp_Name)
                  |                                          |
       σ(Dept_ID=10 ∧ Salary>50000)                       ⋈ (Dept_ID)
                  |                                        /        \
              ⋈ (Dept_ID)                                 /          \
               /       \                      σ(Salary>50000)      σ(Dept_ID=10)
              /         \                            |                   |
      [ Employee ]   [ Department ]             [ Employee ]      [ Department ]
      (100,000 rows)   (50 rows)                (Filtered: 500)   (Filtered: 1 row!)
```

#### Impact Comparison:
* **Unoptimized Plan:** Joins 100,000 rows with 50 rows, producing 100,000 intermediate join tuples, before filtering down.
* **Optimized Plan:** Filters `Employee` down to 500 rows and `Department` down to 1 row *first*. The join processes only `500 × 1` rows, saving massive Disk I/O and RAM!

---

### 5. Heuristic vs Cost-Based Optimization

| Feature | Heuristic Query Optimization | Cost-Based Query Optimization |
| :--- | :--- | :--- |
| **Primary Method** | Fixed rule-based equivalence rewrites | Evaluates alternative physical plans using cost models |
| **Catalog Reliance** | Minimal; uses relational algebraic identities | Heavy; uses tuple counts, block counts, and value histograms |
| **Metrics Considered** | Structural tree properties (pushing filters down) | Disk I/O transfers, CPU cycles, and buffer memory allocation |
| **Computational Time** | Very fast; deterministic | Slower; searches an exponential plan space via Dynamic Programming |
| **Commercial Usage** | Used as an initial preprocessing step | Standard core engine in modern enterprise DBMSs (PostgreSQL, Oracle, MySQL) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Query optimization determines the lowest-cost physical execution plan for a declarative SQL query.
> 2. Query processing lifecycle: **Parsing & Translation → Optimization → Code Generation → Execution Engine**.
> 3. Two relational algebra expressions are equivalent (`E1 ≡ E2`) if they generate identical tuple sets on all valid database states.
> 4. **Pushing selections down:** The most vital heuristic rule; eliminates non-matching tuples before expensive joins.
> 5. **Pushing projections down:** Eliminates unneeded attributes early to reduce tuple width and buffer pool RAM consumption.
> 6. Equivalence rules convert Cartesian products followed by selection into direct theta joins (`σ_θ(E1 × E2) ≡ E1 ⋈_θ E2`).
> 7. Modern relational engines combine heuristic rewrites (rule-based) with cost-based dynamic programming (System-R optimizer).

---

> ⚡ **Quick Recall**
> `SQL Query → Parser/Translator → RA Expression Tree → Equivalence Rules → Push Selections Down → Push Projections Down → Replace Cross Product with Join → Cost-Based Optimizer → Execution Plan`
