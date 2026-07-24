# Topic: Procedures — Self-Learning

**Q. What is a Stored Procedure? Explain how to create and execute them, discuss parameters, and highlight the advantages of using stored procedures in a database.**

---

> 📌 **Definition to Remember**
> A **Stored Procedure** is a pre-compiled, named block of SQL statements and procedural logic (IF/ELSE, loops) stored directly on the database server. Applications invoke it by name using `EXECUTE` or `CALL`, rather than sending raw SQL over the network. Used in Oracle (PL/SQL), SQL Server (T-SQL), and MySQL.

---

### 1. Creating and Executing a Stored Procedure

**Syntax:**
```sql
CREATE PROCEDURE Procedure_Name (Parameters...)
AS
BEGIN
    -- SQL statements and procedural logic
END;
```

**Execution:**
```sql
EXECUTE Procedure_Name;   -- SQL Server
CALL Procedure_Name();    -- MySQL / PostgreSQL
```

### 2. Parameters in Procedures

| Parameter Type | Direction | Description |
| :--- | :--- | :--- |
| **IN** | Caller → Procedure | Passes a value into the procedure (default) |
| **OUT** | Procedure → Caller | Returns a value back to the caller |
| **INOUT** | Both directions | Accepts and modifies a value, then returns it |

**Example:**
```sql
CREATE PROCEDURE Give_Raise (IN emp_id INT, IN raise_amount DECIMAL)
AS
BEGIN
    UPDATE Employee SET Salary = Salary + raise_amount WHERE ID = emp_id;
END;

-- Call the procedure
CALL Give_Raise(101, 5000);
```

### 3. Advantages of Stored Procedures

| Advantage | Explanation |
| :--- | :--- |
| **Pre-compilation** | Compiled once; subsequent calls use the pre-compiled plan → **faster** |
| **Reduced Network Traffic** | Client sends one procedure call instead of many SQL lines |
| **Security** | Users can EXECUTE a procedure without needing direct SELECT/UPDATE on tables → prevents SQL Injection |
| **Code Reusability** | Business logic is centralized; change the procedure once, all apps use updated logic |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Stored Procedure = named, pre-compiled block of SQL + procedural logic stored in the database.
> 2. Created with `CREATE PROCEDURE`; executed with `EXECUTE` or `CALL`.
> 3. Three parameter types: **IN** (input), **OUT** (output), **INOUT** (both).
> 4. **Pre-compilation** makes procedures faster than raw SQL queries for repeated operations.
> 5. **Reduced Network Traffic**: one call replaces hundreds of SQL lines sent over the network.
> 6. **Security**: users can execute a procedure without direct table access, preventing SQL Injection.
> 7. **Code Reusability**: centralized business logic — update once, all applications benefit.

---

> ⚡ **Quick Recall**
> `Stored Procedure → Pre-compiled → CREATE/EXECUTE → Parameters (IN/OUT/INOUT) → Advantages: Faster + Reduced Network Traffic + Security + Code Reusability`
