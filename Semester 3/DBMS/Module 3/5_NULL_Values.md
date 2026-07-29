# NULL Values

**Q. Explain the concept of NULL in SQL. How do we check for NULL values, handle them in expressions, and how do they affect comparisons and aggregate functions?**

---

> 📌 **Definition to Remember**
> **NULL** in SQL is a special marker that represents **missing, unknown, or inapplicable data**. It is NOT the same as zero (0) or an empty string (""). NULL literally means "no value." SQL uses **Three-Valued Logic** (True, False, **Unknown**) when dealing with NULL in comparisons.

---

### 1. Key Rules About NULL
* **NULL ≠ 0** (zero is a number; NULL is the absence of a value)
* **NULL ≠ ""** (empty string is a valid text value)
* Any arithmetic involving NULL → result is **NULL** (e.g., `1000 + NULL = NULL`)
* Any comparison with NULL → result is **UNKNOWN** (e.g., `Age > NULL = UNKNOWN`)

### 2. Checking for NULL Values
You **cannot** use `= NULL` or `!= NULL` — these always return UNKNOWN. Use specialized operators:

```sql
-- IS NULL: find rows where a column has no value
SELECT * FROM Employee WHERE Manager_ID IS NULL;

-- IS NOT NULL: find rows where a column has a value
SELECT * FROM Employee WHERE Phone IS NOT NULL;
```

### 3. Three-Valued Logic
SQL uses True, False, and **Unknown** (instead of just True/False):

| Condition | Result |
| :--- | :--- |
| `Salary = NULL` | **Unknown** (not False!) |
| `NULL = NULL` | **Unknown** (not True!) |
| `IS NULL` check | Correct way — returns True/False |

### 4. Handling NULL with COALESCE()
`COALESCE(val1, val2, ...)` returns the **first non-NULL value** in the list — used to substitute a default value for NULLs.
```sql
-- Treat NULL commission as 0 when calculating total pay
SELECT Salary + COALESCE(Commission, 0) AS Total_Pay FROM Employee;
```

### 5. Effect on Aggregate Functions
* `SUM()`, `AVG()`, `MAX()`, `MIN()` → **automatically ignore NULL rows**.
* `COUNT(*)` → counts **all rows** including NULLs.
* `COUNT(column)` → **excludes NULL** rows.

**Example:** Salaries = [100, 200, NULL] → `AVG(Salary)` = (100+200)/2 = **150** *(NULL ignored)*

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. NULL represents **missing or unknown data** — NOT zero or empty string.
> 2. You **cannot** use `= NULL` or `!= NULL`; must use `IS NULL` or `IS NOT NULL`.
> 3. Any arithmetic expression with NULL → **result is NULL**.
> 4. Any comparison with NULL → **result is UNKNOWN** (Three-Valued Logic).
> 5. `COALESCE(col, default)` replaces NULL with a specified default value.
> 6. Aggregate functions (SUM, AVG, MAX, MIN) **ignore NULLs** automatically.
> 7. `COUNT(*)` counts all rows; `COUNT(column)` excludes NULL rows.

---

> ⚡ **Quick Recall**
> `NULL = Unknown/Missing → ≠ Zero/Empty String → IS NULL / IS NOT NULL → Arithmetic→NULL, Comparison→UNKNOWN → COALESCE (default) → Aggregates ignore NULLs (except COUNT*)`
