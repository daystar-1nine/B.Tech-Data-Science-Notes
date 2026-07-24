# Topic: Union Operation

**Q. Explain the Union operation in Relational Algebra. What is Union Compatibility? Provide an example to illustrate how the Union operator works.**

---

> 📌 **Definition to Remember**
> The **Union Operation** ($\cup$) is a **binary set operation** in relational algebra that combines all tuples (rows) from two relations into a single result, automatically **eliminating duplicate rows**. The two relations must be **Union Compatible** (same number of columns and matching data types).

---

### 1. Union Operator ($\cup$)
* **Binary operation** — operates on two tables.
* **Syntax:** $Relation\_A \cup Relation\_B$
* **Duplicate Elimination:** If a tuple exists in both A and B, it appears only **once** in the output.
* Equivalent to the `UNION` keyword in SQL.

### 2. Union Compatibility (Required Condition)
For Union (and also Intersection and Set Difference) to be valid, both relations **MUST be Union Compatible**:

| Condition | Meaning |
| :--- | :--- |
| **Same Degree** | Both relations must have the **same number of columns**. |
| **Same Domain** | Corresponding columns must have **matching data types** (int with int, string with string, etc.). |

### 3. Example

**CRICKET_TEAM**

| Student_ID | Name |
| :--- | :--- |
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

**FOOTBALL_TEAM**

| Student_ID | Name |
| :--- | :--- |
| 3 | Charlie |
| 4 | David |
| 5 | Eve |

**Query:** Find all students who play Cricket OR Football or both.
$$CRICKET\_TEAM \cup FOOTBALL\_TEAM$$

**Result:** Alice, Bob, Charlie, David, Eve — **5 rows** *(Charlie appeared in both tables but appears only once — duplicate eliminated).*

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Union (∪) is a binary set operation that combines rows from two relations.
> 2. Duplicate rows are automatically eliminated from the result.
> 3. **Union Compatibility** is required: same number of columns AND matching data types.
> 4. If |A| = m rows and |B| = n rows, |A ∪ B| ≤ m + n (due to duplicate removal).
> 5. Equivalent to SQL `UNION` (which also removes duplicates).
> 6. Same Union Compatibility condition applies to Intersection and Set Difference.
> 7. Union is used to merge data from similar tables (e.g., combining employee lists from two branches).

---

> ⚡ **Quick Recall**
> `∪ (Union) → Binary → Combines All Rows → Removes Duplicates → Union Compatibility (same degree + same domain) → SQL UNION`
