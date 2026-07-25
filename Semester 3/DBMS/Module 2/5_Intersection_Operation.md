# Topic: Intersection Operation

**Q. Describe the Intersection operation in Relational Algebra. What are the required conditions for applying it? Illustrate its use with a suitable example.**

---

> 📌 **Definition to Remember**
> The **Intersection Operation** (∩) is a **binary set operation** in relational algebra that returns only those tuples (rows) that are **common to both** input relations. It is a **derived operator** (can be expressed as A ∩ B = A - (A - B)) and requires both relations to be **Union Compatible**.

---

### 1. Intersection Operator (∩)
* **Binary operation** — operates on two tables.
* **Syntax:** Relation_A ∩ Relation_B
* Returns only tuples that appear in **both** relations simultaneously.
* It is a **derived operator**: A ∩ B = A - (A - B)
* Equivalent to `INTERSECT` in SQL.

### 2. Required Conditions (Union Compatibility)
Both relations must be **Union Compatible**:
1. **Same Degree:** Same number of columns.
2. **Same Domain:** Corresponding columns have matching data types.

### 3. Example

**TOP_IN_MATH**

| Roll_No | Name | Grade |
| :--- | :--- | :--- |
| 101 | John | A |
| 102 | Emma | A |
| 104 | Mia | B |

**TOP_IN_SCIENCE**

| Roll_No | Name | Grade |
| :--- | :--- | :--- |
| 102 | Emma | A |
| 105 | Noah | A |
| 101 | John | B |

**Query:** Find students with **identical records** (same Roll_No, Name, and Grade) in both tables.
$TOP_IN_MATH ∩ TOP_IN_SCIENCE$

**Result:** Only **Emma (102, A)** — her entire tuple (Roll_No=102, Name=Emma, Grade=A) is identical in both tables.

*(Note: John appears in both tables but with different grades — A in Math, B in Science — so his full tuple is NOT identical, and he is excluded.)*

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Intersection (∩) returns only rows that are **identical in both** relations.
> 2. It is a **derived operator**: A ∩ B = A - (A - B).
> 3. **Union Compatibility** required: same number of columns AND matching data types.
> 4. The **entire tuple** must be identical — not just one column — for a row to be included.
> 5. If |A| = m and |B| = n, result size ≤ min(m, n).
> 6. Equivalent to SQL `INTERSECT`.
> 7. Used to find commonalities between two datasets (e.g., students excelling in both Math and Science).

---

> ⚡ **Quick Recall**
> `∩ (Intersection) → Binary → Returns Common Rows Only → Derived from Set Difference → Union Compatibility → SQL INTERSECT`

