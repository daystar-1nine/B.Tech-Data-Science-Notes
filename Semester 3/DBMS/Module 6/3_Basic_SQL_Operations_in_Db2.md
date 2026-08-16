# Basic SQL Operations in IBM Db2 — DBMS Module 6

> **Definition: SQL Operations in IBM Db2** adhere to ANSI/ISO SQL standards with specialized extensions for table creation, data manipulation, constraints enforcement, NULL handling, and complex JOIN queries.

---

## 1. Detailed Technical Explanation & Executable Statements

### 1. Database Creation & Connection

```sql
-- Create a new database named STUDENTDB
CREATE DATABASE STUDENTDB;

-- Connect to the database
CONNECT TO STUDENTDB;
```

---

### 2. Data Definition Language (DDL) & Constraints

```sql
-- Create DEPARTMENT Table
CREATE TABLE DEPARTMENT (
    DEPT_ID INT NOT NULL PRIMARY KEY,
    DEPT_NAME VARCHAR(50) NOT NULL UNIQUE,
    LOCATION VARCHAR(50) DEFAULT 'Main Campus'
);

-- Create STUDENT Table with Foreign Key & Check Constraints
CREATE TABLE STUDENT (
    STUDENT_ID INT NOT NULL PRIMARY KEY,
    FIRST_NAME VARCHAR(30) NOT NULL,
    LAST_NAME VARCHAR(30),
    EMAIL VARCHAR(100) UNIQUE,
    AGE INT CHECK (AGE >= 17),
    DEPT_ID INT,
    FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(DEPT_ID) ON DELETE SET NULL
);
```

---

### 3. Data Manipulation Language (DML)

```sql
-- Insert Records
INSERT INTO DEPARTMENT (DEPT_ID, DEPT_NAME, LOCATION) 
VALUES (1, 'Data Science', 'Building A'),
       (2, 'Computer Science', 'Building B');

INSERT INTO STUDENT (STUDENT_ID, FIRST_NAME, LAST_NAME, EMAIL, AGE, DEPT_ID) 
VALUES (101, 'Rahul', 'Sharma', 'rahul@example.com', 20, 1),
       (102, 'Anita', 'Verma', 'anita@example.com', 21, 2),
       (103, 'Suresh', NULL, 'suresh@example.com', 19, 1);

-- Update Record
UPDATE STUDENT 
SET AGE = 21 
WHERE STUDENT_ID = 101;

-- Delete Record
DELETE FROM STUDENT 
WHERE STUDENT_ID = 103;
```

---

### 4. NULL Value Handling in Db2

In Db2, `NULL` represents missing or unknown values. Standard comparison operators (`=`, `<>`) return `UNKNOWN` when evaluated against `NULL`.

```sql
-- Select students where LAST_NAME is missing
SELECT STUDENT_ID, FIRST_NAME 
FROM STUDENT 
WHERE LAST_NAME IS NULL;

-- Use VALUE() or COALESCE() to replace NULL with a default display value
SELECT FIRST_NAME, VALUE(LAST_NAME, 'Not Provided') AS LAST_NAME_DISPLAY 
FROM STUDENT;
```

---

### 5. Join Operations in Db2

```sql
-- Inner Join
SELECT S.STUDENT_ID, S.FIRST_NAME, D.DEPT_NAME
FROM STUDENT S
INNER JOIN DEPARTMENT D ON S.DEPT_ID = D.DEPT_ID;

-- Left Outer Join
SELECT S.STUDENT_ID, S.FIRST_NAME, D.DEPT_NAME
FROM STUDENT S
LEFT OUTER JOIN DEPARTMENT D ON S.DEPT_ID = D.DEPT_ID;
```

---

## 2. Core Concepts & Memory Keywords
- **PRIMARY KEY / FOREIGN KEY:** Relational integrity constraints.
- **COALESCE() / VALUE():** Db2 functions used to replace `NULL` values with fallback strings.
- **CHECK Constraint:** Enforces domain validation rules on columns.

---

## 3. Must-Write Points for Exams
- Db2 supports standard `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK` constraints.
- The `VALUE(expr1, expr2)` function in Db2 is equivalent to standard `COALESCE()`.
- Tables in Db2 are organized under schema names (e.g., `DB2ADMIN.STUDENT`).

---

## 4. Quick Recall Flow
```
CREATE TABLE -> Add Constraints (PK, FK, CHECK) -> INSERT/UPDATE/DELETE -> SELECT with Joins & VALUE(col, 'Default')
```
