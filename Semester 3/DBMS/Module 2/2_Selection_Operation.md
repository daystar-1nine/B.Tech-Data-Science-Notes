# Topic: Selection Operation

**Q. Explain the Selection operation in Relational Algebra. Write its syntax and provide examples demonstrating how it filters tuples.**

---

> 📌 **Definition to Remember**
> The **Selection Operation** (denoted by σ) is a **unary operation** in relational algebra that filters and returns specific **rows (tuples)** from a relation that satisfy a given logical condition (predicate). It is equivalent to the `WHERE` clause in SQL.

---

# Selection Operator (σ — Sigma)
* Operates on a **single table** (unary).
* Filters **horizontally** — returns same columns, but only matching rows.
* Output automatically eliminates duplicate rows (set behavior).

### 2. Syntax of Selection
$σ_{<predicate>}(Relation_Name)$

* **Predicate:** Uses comparison operators (=, ≠, <, ≤, >, ≥) and logical operators (AND AND, OR OR, NOT NOT).

### 3. Examples

**Input Relation: EMPLOYEE**

| Emp_ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | IT | 50000 |
| 2 | Bob | HR | 40000 |
| 3 | Charlie | IT | 60000 |
| 4 | David | Sales | 45000 |

#### Example 1: Simple Condition
**Query:** Find all IT department employees.
$σ_{Department = 'IT'}(EMPLOYEE)$
**Result:** Returns rows for Alice (ID 1) and Charlie (ID 3).

#### Example 2: AND Condition (AND)
**Query:** IT employees with salary > 55000.
$σ_{Department = 'IT' AND Salary > 55000}(EMPLOYEE)$
**Result:** Returns only Charlie (IT, 60000).

#### Example 3: OR Condition (OR)
**Query:** Employees in HR or Sales.
$σ_{Department = 'HR' OR Department = 'Sales'}(EMPLOYEE)$
**Result:** Returns Bob (HR) and David (Sales).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Selection is a **unary operation** — operates on one relation.
> 2. Denoted by **σ (Sigma)**; equivalent to SQL's `WHERE` clause.
> 3. Filters **rows (tuples)** based on a logical predicate — horizontal filtering.
> 4. Output has the same columns as input but only matching rows.
> 5. Predicates use comparison operators (=, ≠, <, >) and logical operators (∧, ∨, ¬).
> 6. Can be **nested**: apply selection to the result of another operation.
> 7. Automatically eliminates duplicate rows (set semantics).

---

> ⚡ **Quick Recall**
> `σ (Sigma) → Unary → Horizontal Filtering (rows) → Predicate (=, ≠, ∧, ∨) → Equivalent to SQL WHERE → Can be nested`

