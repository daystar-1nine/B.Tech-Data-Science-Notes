# Nested Queries & Subqueries

**Q. What are Nested Queries (Subqueries) in SQL? Differentiate between Single-Row, Multiple-Row, and Correlated subqueries with examples.**

---

> 📌 **Definition to Remember**
> A **Nested Query** (or **Subquery**) is a complete SQL query placed **inside another SQL query** (the outer query). The inner query executes first and provides data to the outer query. Subqueries can be placed in `WHERE`, `HAVING`, or `FROM` clauses.

---

### 1. Types of Subqueries

#### A. Single-Row Subquery
* Returns exactly **one row and one column** to the outer query.
* Uses single-value comparison operators: `=`, `>`, `<`, `>=`, `<=`, `!=`.
```sql
-- Find employees who earn more than the average salary
SELECT Name, Salary FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee);
```
*The inner query returns one value (e.g., 45000). The outer query uses it.*

#### B. Multiple-Row Subquery
* Returns **more than one row** to the outer query.
* Must use multi-row operators: **`IN`**, **`ANY`**, **`ALL`** (not `=`).
```sql
-- Find employees in departments located in 'New York'
SELECT Name FROM Employee
WHERE Dept_ID IN (SELECT Dept_ID FROM Department WHERE City = 'New York');
```

#### C. Correlated Subquery
* The inner query **references a column from the outer query** — they are linked.
* The inner query is **re-executed for every single row** of the outer query.
* More powerful but **computationally expensive**.
```sql
-- Find employees earning above their OWN department's average salary
SELECT e1.Name, e1.Salary, e1.Dept_ID
FROM Employee e1
WHERE e1.Salary > (
    SELECT AVG(Salary)
    FROM Employee e2
    WHERE e2.Dept_ID = e1.Dept_ID  -- Correlation: ties inner to outer
);
```

### 2. Comparison of Subquery Types

| Feature | Single-Row | Multiple-Row | Correlated |
| :--- | :--- | :--- | :--- |
| **Rows Returned** | Exactly 1 | More than 1 | Varies per outer row |
| **Operators** | `=`, `>`, `<` | `IN`, `ANY`, `ALL` | `=`, `>`, `<` |
| **Execution** | Once | Once | Once per outer row |
| **Performance** | Fast | Moderate | Slow (re-executes per row) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A Subquery/Nested Query is a SELECT query placed inside another SQL query.
> 2. The **inner query executes first** and provides data to the outer query.
> 3. Single-Row Subquery: returns one value; uses operators like `=`, `>`, `<`.
> 4. Multiple-Row Subquery: returns multiple rows; must use `IN`, `ANY`, or `ALL`.
> 5. Correlated Subquery: inner query references outer query — re-runs for every outer row.
> 6. Correlated subqueries are more powerful but slower (expensive execution).
> 7. Subqueries can be placed in `WHERE`, `HAVING`, or `FROM` clauses.

---

> ⚡ **Quick Recall**
> `Subquery (inner executes first) → Single-Row (=,>,< operators) → Multi-Row (IN/ANY/ALL) → Correlated (references outer, re-runs per row, expensive)`
