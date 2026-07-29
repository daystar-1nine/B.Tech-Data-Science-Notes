# Aggregate Functions

**Q. What are Aggregate Functions in SQL? Explain the functions COUNT(), SUM(), AVG(), MAX(), and MIN() with syntax and appropriate examples.**

---

> 📌 **Definition to Remember**
> **Aggregate Functions** in SQL operate on a set of values (an entire column) and return a **single summarizing value**. They are used for data analysis and reporting, typically combined with the `GROUP BY` clause. With the exception of `COUNT(*)`, **all aggregate functions ignore NULL values**.

---

### The Five Standard Aggregate Functions

| Function | Returns | Works On |
| :--- | :--- | :--- |
| **COUNT()** | Number of rows | Any type |
| **SUM()** | Total sum | Numeric only |
| **AVG()** | Arithmetic mean | Numeric only |
| **MAX()** | Highest value | Numeric, Text, Date |
| **MIN()** | Lowest value | Numeric, Text, Date |

#### 1. COUNT()
Returns the total number of rows matching a criterion.
* `COUNT(*)` → Counts **all rows** (including NULLs).
* `COUNT(column)` → Counts rows where that column is **NOT NULL**.
```sql
SELECT COUNT(*) FROM Employee;              -- total rows
SELECT COUNT(Manager_ID) FROM Employee;    -- rows where Manager_ID is not null
SELECT COUNT(DISTINCT Department) FROM Employee;  -- unique departments
```

#### 2. SUM()
Calculates the total sum of a numeric column.
```sql
SELECT SUM(Salary) FROM Employee;   -- total monthly salary payout
```

#### 3. AVG()
Calculates the arithmetic mean of a numeric column.
```sql
SELECT AVG(Salary) FROM Employee WHERE Department = 'IT';
```

#### 4. MAX()
Returns the maximum (highest) value. Works on numbers, text (alphabetically), and dates.
```sql
SELECT MAX(Salary) FROM Employee;   -- highest salary
SELECT MAX(Name) FROM Employee;     -- last name alphabetically
```

#### 5. MIN()
Returns the minimum (lowest) value.
```sql
SELECT MIN(Salary) FROM Employee;   -- lowest salary
```

### NULL Behavior in Aggregate Functions
* `SUM()`, `AVG()`, `MAX()`, `MIN()` — **ignore NULL values**.
* `COUNT(*)` — **counts all rows** including those with NULLs.
* **Example:** Salaries = [100, 200, NULL] → `AVG(Salary)` = (100+200)/2 = **150** (NULL ignored).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Aggregate functions compute a single value from a set of values (a column).
> 2. `COUNT(*)` counts all rows including NULLs; `COUNT(column)` excludes NULLs.
> 3. `SUM()` and `AVG()` work on **numeric** columns only.
> 4. `MAX()` and `MIN()` work on numeric, text (alphabetical), and date values.
> 5. All aggregate functions **ignore NULL values** — except `COUNT(*)`.
> 6. Use `DISTINCT` inside aggregate functions to calculate on unique values only.
> 7. Aggregate functions are most powerful when combined with `GROUP BY` and `HAVING`.

---

> ⚡ **Quick Recall**
> `Aggregate Functions → COUNT(*) / COUNT(col) → SUM (numeric) → AVG (numeric) → MAX / MIN (any type) → Ignore NULLs (except COUNT*) → Used with GROUP BY`
