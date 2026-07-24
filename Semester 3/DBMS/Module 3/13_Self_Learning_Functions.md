# Topic: Functions — Self-Learning

**Q. What is a User-Defined Function (UDF) in SQL? Explain how functions differ from Stored Procedures regarding parameters, return values, and execution contexts.**

---

> 📌 **Definition to Remember**
> A **User-Defined Function (UDF)** is a stored program that encapsulates SQL and procedural logic to perform a specific computation and **must return a single value** (scalar or table). Unlike procedures, functions are embedded directly inside SQL statements like `SELECT`, making them ideal for **read-only calculations and data transformation**.

---

### 1. Creating and Calling Functions

**Creation:** Must declare the return type explicitly.
```sql
CREATE FUNCTION Calculate_Bonus (salary DECIMAL)
RETURNS DECIMAL
AS
BEGIN
    RETURN salary * 0.10;   -- Must use RETURN
END;
```

**Calling:** Functions return a value, so they are embedded inside SQL — NOT called via `CALL`.
```sql
SELECT Name, Salary, Calculate_Bonus(Salary) AS Bonus FROM Employee;
```

### 2. Parameters and Return Values
* **Parameters:** Functions only accept **IN parameters** (input only — no OUT or INOUT).
* **Return Value:** A function **MUST** return a value using `RETURN`.
  * **Scalar Function:** Returns a single value (integer, string, decimal, etc.)
  * **Table-Valued Function:** Returns an entire table (supported in some RDBMS).

### 3. Procedures vs Functions

| Feature | Stored Procedure | User-Defined Function |
| :--- | :--- | :--- |
| **Return Value** | Optional; can return via OUT params | **Mandatory** — must return a value |
| **Called Using** | `EXEC` or `CALL` | Embedded in SQL (`SELECT`, `WHERE`) |
| **DML Operations** | Can INSERT, UPDATE, DELETE | **Read-only** — cannot modify data |
| **Transactions** | Can use COMMIT/ROLLBACK | Cannot manage transactions |
| **Parameters** | IN, OUT, INOUT | IN only |
| **Best For** | Workflows, data modification | Calculations, formatting, read-only logic |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. UDF = User-Defined Function — extends SQL with custom calculations.
> 2. Created with `CREATE FUNCTION`; **MUST** declare return type and use `RETURN`.
> 3. Functions accept only **IN parameters** (no OUT or INOUT).
> 4. Functions are embedded directly inside SQL statements (not called with `CALL`).
> 5. Functions are **read-only** — they CANNOT perform INSERT, UPDATE, or DELETE.
> 6. Procedures are optional return; Functions have **mandatory** return.
> 7. Scalar function → single value; Table-valued function → returns a table.

---

> ⚡ **Quick Recall**
> `UDF → MUST return value (RETURNS + RETURN) → IN params only → Embedded in SELECT/WHERE → Read-only (no DML) → vs Procedure: optional return, CALL, DML allowed`
