# Topic: Cartesian Product Operation

**Q. What is a Cartesian Product in DBMS? Explain its working mechanism and provide an example demonstrating how it combines two relations.**

---

> 📌 **Definition to Remember**
> The **Cartesian Product** (also called Cross Product, denoted $\times$) is a **binary operation** in relational algebra that pairs **every row of the first relation with every row of the second relation**, producing all possible combinations. Output columns = sum of both columns; Output rows = product of both row counts. Union Compatibility is **NOT** required.

---

### 1. Cartesian Product Operator ($\times$)
* **Binary operation** — operates on two tables (which need NOT be union compatible).
* **Syntax:** $Relation\_A \times Relation\_B$
* **Output Degree (Columns):** $Columns_A + Columns_B$
* **Output Cardinality (Rows):** $Rows_A \times Rows_B$

### 2. Working of Cartesian Product
* Takes **every single row from A** and pairs it with **every single row from B**.
* Generates all possible row combinations — most of which are **meaningless on their own**.
* On its own, the Cartesian Product produces massive redundant data.
* It is primarily used as the **first step for JOIN operations**: Apply Cartesian Product → Apply Selection ($\sigma$) to filter meaningful rows.

```
  A × B :
  Row1_A  ←→  Row1_B
  Row1_A  ←→  Row2_B
  Row2_A  ←→  Row1_B
  Row2_A  ←→  Row2_B
  (2 × 2 = 4 combinations)
```

### 3. Example

**COLORS (2 rows)**

| Color_ID | Color_Name |
| :--- | :--- |
| 1 | Red |
| 2 | Blue |

**SHAPES (2 rows)**

| Shape_ID | Shape_Name |
| :--- | :--- |
| A | Circle |
| B | Square |

**Query:** $COLORS \times SHAPES$
**Output:** 2 + 2 = **4 columns**; 2 × 2 = **4 rows**

| Color_ID | Color_Name | Shape_ID | Shape_Name |
| :--- | :--- | :--- | :--- |
| 1 | Red | A | Circle |
| 1 | Red | B | Square |
| 2 | Blue | A | Circle |
| 2 | Blue | B | Square |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Cartesian Product (×) = Cross Product — pairs every row of A with every row of B.
> 2. Output columns = Columns_A + Columns_B; Output rows = Rows_A × Rows_B.
> 3. Union Compatibility is **NOT** required — the two relations can be completely different.
> 4. On its own, produces large amounts of **meaningless data**.
> 5. It is the foundation of **JOIN operations**: Cartesian Product + Selection = Join.
> 6. If A has m rows and B has n rows, the result has m × n rows.
> 7. Cartesian Product is a basic (fundamental) operator in relational algebra.

---

> ⚡ **Quick Recall**
> `× (Cartesian Product) → Binary → All Row Combinations → Cols = A+B, Rows = A×B → No Union Compatibility Needed → Foundation of JOIN`
