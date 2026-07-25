# Topic: Projection Operation

**Q. Discuss the Projection operation in Relational Algebra. Describe its syntax and explain its behavior regarding duplicate elimination, using suitable examples.**

---

> 📌 **Definition to Remember**
> The **Projection Operation** (denoted by π) is a **unary operation** in relational algebra that filters specific **columns (attributes)** from a relation while discarding the rest. It performs **vertical filtering** and automatically **eliminates duplicate rows** in the result. It is equivalent to the `SELECT column_name` in SQL.

---

### 1. Projection Operator (π — Pi)
* Operates on a **single table** (unary).
* Filters **vertically** — returns all rows, but only selected columns.
* **Key Property:** Automatically **eliminates duplicate rows** from the output (because a relation is a mathematical set — no duplicates allowed).

### 2. Syntax of Projection
$π_{<attribute_list>}(Relation_Name)$

* **attribute_list:** Comma-separated column names to retain.

### 3. Examples

**Input Relation: STUDENT**

| Roll_No | Name | Major | City |
| :--- | :--- | :--- | :--- |
| 101 | John | CS | New York |
| 102 | Emma | Math | Boston |
| 103 | Luke | CS | New York |
| 104 | Mia | Physics | Chicago |

#### Example 1: Simple Projection
**Query:** Get names and majors of all students.
$π_{Name, Major}(STUDENT)$
**Result:** 4 rows, 2 columns (Name, Major).

#### Example 2: Duplicate Elimination
**Query:** List all unique majors.
$π_{Major}(STUDENT)$
**Result:** CS, Math, Physics — *only 3 rows* (CS appeared twice in the original table but appears once in the result after duplicate elimination).

#### Example 3: Composition — Selection + Projection
**Query:** Find names of CS major students.
$π_{Name}(σ_{Major = 'CS'}(STUDENT))$
**Execution:**
1. **Step 1:** σ_{Major='CS'} filters rows → John and Luke.
2. **Step 2:** π_{Name} extracts the Name column → John, Luke.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Projection is a **unary operation** — operates on one relation.
> 2. Denoted by **π (Pi)**; equivalent to SQL's `SELECT column_name`.
> 3. Performs **vertical filtering** — selects specific columns, discards others.
> 4. Critical feature: **automatically eliminates duplicate rows** from the result.
> 5. The number of columns in output = number of columns listed in the attribute list.
> 6. Can be **composed with Selection** — Selection applied first, Projection second.
> 7. Duplicate elimination is automatic because a relation is a mathematical set.

---

> ⚡ **Quick Recall**
> `π (Pi) → Unary → Vertical Filtering (columns) → Duplicate Elimination (set) → Equivalent to SQL SELECT → Composable with σ`

