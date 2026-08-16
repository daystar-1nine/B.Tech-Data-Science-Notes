# Day 6: Advanced Power Query Transformations

---

> 📌 **Definition to Remember**
> Advanced Power Query transformations allow reshaping wide datasets into normalized tall formats (**Unpivot**), aggregating tables (**Group By**), combining row sets (**Append**), and performing relational joins (**Merge**).

---

### 1. The Power of Unpivot Columns
- **Problem:** Financial tables often store months as separate columns (`Jan`, `Feb`, `Mar`...).
- **Solution:** Select ID columns and click **Unpivot Other Columns**.
- **Result:** Transforms wide messy spreadsheets into normalized tall format: `[Attribute: Month]` and `[Value: Amount]`.

```
WIDE FORMAT (Bad for BI):
Product | Jan_Sales | Feb_Sales | Mar_Sales
Widget  | 100       | 150       | 200

TALL FORMAT (Ideal for Data Modeling):
Product | Month | Sales
Widget  | Jan   | 100
Widget  | Feb   | 150
Widget  | Mar   | 200
```

### 2. Append vs Merge Queries

| Transformation | Type | SQL Equivalent | Description |
| :--- | :--- | :--- | :--- |
| **Append Queries** | Vertical Stacking | `UNION ALL` | Combines rows of two or more tables with identical column structures (e.g., 2024 Sales + 2025 Sales). |
| **Merge Queries** | Horizontal Join | `JOIN` | Merges columns from two tables based on matching key columns (Left Outer, Inner, Right Outer, Full Outer, Anti Join). |

### 3. Group By & Custom M Columns
- **Group By:** Aggregates row values (e.g., Total Sales per Customer) directly during ETL.
- **Custom Column:** Adding columns using custom M functions (e.g., `[UnitPrice] * [Quantity] * (1 - [Discount])`).

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why **Unpivot** is essential for dynamic time intelligence and DAX calculations.
> 2. Master the 6 Merge Join types in Power Query (especially Left Anti Join for finding orphan records).
> 3. When to aggregate in Power Query (Group By) vs calculating dynamically in DAX.

---

> ⚡ **Quick Recall**
> `Unpivot (Wide to Tall) + Append (Stack Rows / UNION) + Merge (Join Columns / JOIN) + Group By (ETL Aggregation)`
