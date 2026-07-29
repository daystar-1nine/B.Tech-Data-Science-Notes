# Data Definition Language (DDL) Commands

**Q. Explain the various Data Definition Language (DDL) commands in SQL. Provide the syntax and a clear example for CREATE, ALTER, DROP, TRUNCATE, and RENAME.**

---

> 📌 **Definition to Remember**
> **Data Definition Language (DDL)** is the subset of SQL used to define, modify, and delete the structural elements (schema) of a database — such as tables, views, and indexes. DDL commands are **auto-committed**, meaning changes are saved permanently and **cannot be rolled back**.

---

### DDL Commands

#### 1. CREATE
Used to create a new database or table.
```sql
CREATE TABLE Employee (
    Emp_ID INT PRIMARY KEY,
    Name   VARCHAR(50),
    Salary DECIMAL(10,2)
);
```

#### 2. ALTER
Used to modify an existing table structure — add, delete, or modify columns.
```sql
-- Add a new column
ALTER TABLE Employee ADD Department VARCHAR(30);

-- Modify column size
ALTER TABLE Employee MODIFY Name VARCHAR(100);
```

#### 3. DROP
Used to **completely delete** a table — removes structure AND all data permanently.
```sql
DROP TABLE Employee;
```
⚠️ *Once dropped, the table cannot be recovered without a backup.*

#### 4. TRUNCATE
Used to **delete all rows** from a table but **keeps the table structure** intact. Faster than DELETE because it does not log individual row deletions.
```sql
TRUNCATE TABLE Employee;
```

#### 5. RENAME
Used to rename an existing table.
```sql
RENAME TABLE Employee TO Staff;   -- MySQL
-- Oracle: ALTER TABLE Employee RENAME TO Staff;
```

### Summary Table

| Command | Affects | Data Lost? | Auto-Committed? |
| :--- | :--- | :--- | :--- |
| **CREATE** | Creates table structure | N/A | Yes |
| **ALTER** | Modifies table structure | No | Yes |
| **DROP** | Deletes table + all data | **Yes (completely)** | Yes |
| **TRUNCATE** | Deletes all rows | **Yes (data only)** | Yes |
| **RENAME** | Renames table/column | No | Yes |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. DDL commands define the schema (structure) of a database.
> 2. All DDL commands are **auto-committed** — changes cannot be rolled back.
> 3. **CREATE**: creates a new table/database with specified columns and constraints.
> 4. **ALTER**: modifies existing table — add/drop/modify columns without losing data.
> 5. **DROP**: permanently deletes the entire table structure AND all its data.
> 6. **TRUNCATE**: deletes all rows but preserves the table structure; faster than DELETE.
> 7. **DROP** removes structure + data; **TRUNCATE** removes data only (structure remains).

---

> ⚡ **Quick Recall**
> `DDL → Auto-committed → CREATE (make table) → ALTER (modify structure) → DROP (delete all) → TRUNCATE (delete rows, keep structure) → RENAME (change name)`
