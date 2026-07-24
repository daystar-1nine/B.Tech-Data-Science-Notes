# Topic: SQL Standards

**Q. What is SQL? Discuss its features, the importance of SQL Standards, and categorize the different types of SQL commands with examples.**

---

> 📌 **Definition to Remember**
> **SQL (Structured Query Language)** is the standard **declarative language** for communicating with Relational Database Management Systems (RDBMS). It allows users to create, manipulate, manage, and query databases. SQL is governed by **ANSI** and **ISO** standards to ensure cross-platform compatibility.

---

### 1. SQL Standards
Standardizing bodies **ANSI** and **ISO** define the SQL standard to ensure compatibility across different database vendors (Oracle, MySQL, SQL Server).

| Standard | Key Feature |
| :--- | :--- |
| **SQL-86** | First official standard |
| **SQL-92** | Introduced Joins and expanded query capabilities |
| **SQL:1999 (SQL3)** | Introduced object-relational features, Recursive queries, Triggers |

**Importance:** Ensures core SQL commands work consistently across databases, **preventing vendor lock-in**.

### 2. Features of SQL
* **Declarative Language:** Users specify *what* data they want, not *how* to retrieve it.
* **Easy to Learn:** Syntax closely resembles natural English.
* **Highly Scalable:** Handles single-row queries to multi-million row analytics.
* **Comprehensive:** Covers data definition, manipulation, and access control.

### 3. Types of SQL Commands

| Category | Full Form | Purpose | Key Commands |
| :--- | :--- | :--- | :--- |
| **DDL** | Data Definition Language | Define/modify database structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** | Data Manipulation Language | Insert, update, delete, retrieve data | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | Manage user access & permissions | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manage transactions & data integrity | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

**Examples:**
```sql
-- DDL
CREATE TABLE Student (ID INT, Name VARCHAR(50));
-- DML
INSERT INTO Student VALUES (1, 'John');
-- DCL
GRANT SELECT ON Student TO user_admin;
-- TCL
COMMIT;
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. SQL = Structured Query Language; standard language for RDBMS communication.
> 2. Governed by **ANSI** and **ISO** standards (SQL-86, SQL-92, SQL:1999).
> 3. SQL is **declarative** — specifies *what* to retrieve, not *how*.
> 4. **DDL**: structure operations (CREATE, ALTER, DROP, TRUNCATE, RENAME).
> 5. **DML**: data operations (SELECT, INSERT, UPDATE, DELETE).
> 6. **DCL**: access control (GRANT, REVOKE).
> 7. **TCL**: transaction management (COMMIT, ROLLBACK, SAVEPOINT).

---

> ⚡ **Quick Recall**
> `SQL → ANSI/ISO Standards (SQL-86, SQL-92, SQL:1999) → Declarative → DDL (structure) → DML (data) → DCL (access) → TCL (transactions)`
