# Set Operations in SQL

**Q. Discuss the SQL Set Operations. Explain UNION, UNION ALL, INTERSECT, and EXCEPT with examples, and list the strict rules required to use them.**

---

> 📌 **Definition to Remember**
> **SQL Set Operations** allow you to combine the result sets of two or more independent `SELECT` queries into a single output. They are based on mathematical set theory and include `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT/MINUS`. All require **Union Compatibility** between the queries.

---

### 1. Rules for Set Operations (Union Compatibility)
Both `SELECT` queries must satisfy:
1. **Same Number of Columns:** Both queries must return the same number of columns.
2. **Compatible Data Types:** Corresponding columns must have compatible data types in the same order.

### 2. Types of Set Operations

#### 1. UNION
* Combines results of two queries and **automatically removes duplicate rows**.
```sql
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;
```
*Result: All unique cities from both tables.*

#### 2. UNION ALL
* Combines results but **retains all duplicates**. Significantly **faster** than `UNION` (no sorting/deduplication step).
```sql
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers;
```
*Result: All city entries, including repeated cities.*

#### 3. INTERSECT
* Returns only rows **common to both** queries.
```sql
SELECT City FROM Customers
INTERSECT
SELECT City FROM Suppliers;
```
*Result: Only cities with both a Customer AND a Supplier.*

#### 4. EXCEPT / MINUS
* Returns rows from the **first query that are NOT in the second**.
* Oracle uses `MINUS`; SQL Server/PostgreSQL use `EXCEPT`.
```sql
SELECT City FROM Customers
EXCEPT
SELECT City FROM Suppliers;
```
*Result: Cities with Customers but NO Suppliers.*

### 3. Quick Comparison

| Operation | Duplicates | Returns |
| :--- | :--- | :--- |
| **UNION** | Removed | All from A + All from B |
| **UNION ALL** | Kept | All from A + All from B (with duplicates) |
| **INTERSECT** | Removed | Common rows only |
| **EXCEPT/MINUS** | Removed | Rows in A not in B |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Set operations combine results of two SELECT queries into a single result set.
> 2. **Union Compatibility** required: same number of columns AND compatible data types.
> 3. `UNION`: combines all rows, **removes duplicates**.
> 4. `UNION ALL`: combines all rows, **keeps duplicates** (faster than UNION).
> 5. `INTERSECT`: returns only **common rows** present in both queries.
> 6. `EXCEPT` (MINUS in Oracle): returns rows in first query **not found** in the second.
> 7. UNION ALL is preferred for performance when duplicates are acceptable.

---

> ⚡ **Quick Recall**
> `Set Ops → Union Compatibility → UNION (no duplicates) → UNION ALL (keeps duplicates, faster) → INTERSECT (common only) → EXCEPT/MINUS (A not in B)`
