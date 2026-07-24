# Topic: Data Manipulation Language (DML) Commands

**Q. Discuss Data Manipulation Language (DML) commands in SQL. Write the syntax and examples for SELECT, INSERT, UPDATE, and DELETE.**

---

> 📌 **Definition to Remember**
> **Data Manipulation Language (DML)** is the subset of SQL used to insert, retrieve, modify, and delete the actual **data (records)** residing within database tables. Unlike DDL, DML commands are generally **not auto-committed** — changes can be **rolled back** until a `COMMIT` is issued. (CRUD: **C**reate = INSERT, **R**ead = SELECT, **U**pdate = UPDATE, **D**elete = DELETE)

---

### DML Commands

#### 1. INSERT
Adds new rows (records) into a table.
```sql
-- Syntax 1: Specify columns (recommended)
INSERT INTO Student (Roll_No, Name, Grade) VALUES (101, 'Alice', 'A');

-- Syntax 2: All columns in order
INSERT INTO Student VALUES (102, 'Bob', 'B');
```

#### 2. SELECT (Data Query Language — DQL)
Retrieves data from one or more tables.
```sql
-- Basic syntax
SELECT Name, Grade FROM Student WHERE Grade = 'A';

-- Select all columns
SELECT * FROM Student;
```

#### 3. UPDATE
Modifies existing records in a table.
```sql
UPDATE Student SET Grade = 'A+' WHERE Roll_No = 101;
```
⚠️ **Warning:** Omitting `WHERE` updates **ALL rows** in the table!

#### 4. DELETE
Removes existing rows from a table but **keeps the table structure**.
```sql
DELETE FROM Student WHERE Roll_No = 102;
```
⚠️ **Warning:** Omitting `WHERE` deletes **ALL rows** (table structure remains — unlike DROP).

### DML vs DDL Comparison

| Feature | DML | DDL |
| :--- | :--- | :--- |
| **Operates On** | Data (rows/records) | Structure (tables/schemas) |
| **Auto-Committed** | Usually **No** (can ROLLBACK) | **Yes** (permanent) |
| **Commands** | SELECT, INSERT, UPDATE, DELETE | CREATE, ALTER, DROP, TRUNCATE |
| **Reversible** | Yes, with ROLLBACK | No |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. DML manipulates **actual data** (rows/records) inside tables.
> 2. DML commands are **NOT auto-committed** — changes can be rolled back.
> 3. `INSERT`: adds new rows; can specify column names (recommended) or use all-column syntax.
> 4. `SELECT`: retrieves data; use `WHERE` to filter, `*` for all columns.
> 5. `UPDATE`: modifies existing rows; **MUST** use `WHERE` or all rows will be updated.
> 6. `DELETE`: removes rows; **MUST** use `WHERE` or all rows will be deleted (structure preserved).
> 7. CRUD = Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).

---

> ⚡ **Quick Recall**
> `DML → Not Auto-committed → INSERT (add rows) → SELECT (read data) → UPDATE (modify rows, use WHERE!) → DELETE (remove rows, use WHERE!) → CRUD`
