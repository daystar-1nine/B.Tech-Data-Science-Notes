import os

DBMS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\DBMS"
m6_dir = os.path.join(DBMS_DIR, "Module 6")
os.makedirs(m6_dir, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 6: FOUNDATIONS OF IBM DB2
# --------------------------------------------------------------------------

m6_files = {
    "1_IBM_Db2_Overview_Architecture_Use_Cases.md": """# IBM Db2 Overview, Architecture & Use Cases — DBMS Module 6

> **Definition:** **IBM Db2** is an enterprise-grade Relational Database Management System (RDBMS) developed by IBM, engineered for high-performance transactional processing (OLTP), analytical workloads (OLAP), and hybrid data management (HTAP) across hybrid cloud environments.

---

## 1. Detailed Technical Explanation

### 1. Key Features of IBM Db2:
- **BLU Acceleration:** In-memory columnar processing for multi-fold speedup in analytical queries.
- **pureScale Technology:** High-availability fault tolerance providing continuous cluster availability.
- **AI-Powered Query Optimizer:** Machine learning-assisted cost estimation and execution path optimization.
- **Native JSON & XML Support (pureXML):** Hybrid relational and document storage capabilities within the same engine.

---

## 2. IBM Db2 Product Editions

| Db2 Edition | Target Environment | Hardware / Resource Limits | Key Features |
| :--- | :--- | :--- | :--- |
| **Db2 Community Edition** | Developers, Academic Learning, Micro-services | Free tier (up to 4 vCPUs, 16 GB RAM) | Full database engine features for evaluation and small projects. |
| **Db2 Standard Edition** | Mid-market businesses, department servers | Up to 16 vCPUs, 128 GB RAM | Enterprise RDBMS features, pureXML, high availability disaster recovery (HADR). |
| **Db2 Advanced Edition** | Large enterprises, data warehouses | Unlimited vCPUs & RAM | Includes BLU Acceleration, pureScale clustering, advanced security & compression. |

---

## 3. Industry Use Cases
1. **Banking & Financial Services:** Core banking transactions, real-time credit card fraud detection using pureScale high availability.
2. **Healthcare & Insurance:** Patient record management, compliance tracking, and secure claim processing.
3. **Retail & Supply Chain:** Real-time inventory tracking and analytical data warehousing using BLU Acceleration.

---

## 4. Comparison: IBM Db2 vs Other RDBMS

| Feature | IBM Db2 | Oracle Database | MySQL / PostgreSQL |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Enterprise HTAP, Hybrid Cloud, IBM Z/Linux | Enterprise OLTP/OLAP | Web applications, open-source microservices |
| **High Availability** | Db2 pureScale / HADR | Oracle RAC / Data Guard | Master-Slave / Active-Passive Replication |
| **Analytics Engine** | Integrated BLU Columnar | Oracle In-Memory Option | External extensions / Read Replicas |
| **Cloud Integration** | Native IBM Cloud, AWS, Azure, Red Hat OpenShift | Oracle Cloud Infrastructure (OCI) | Multi-cloud managed services |

---

## 5. Core Concepts & Memory Keywords
- **pureScale:** IBM active-active database clustering for zero downtime.
- **BLU Acceleration:** In-memory column-oriented query processing engine.
- **HADR:** High Availability Disaster Recovery standby replication mechanism.

---

## 6. Must-Write Points for Exams
- IBM Db2 supports Hybrid Transactional and Analytical Processing (HTAP) in a single engine.
- Db2 Community Edition is a free edition provided for academic and non-production development.
- BLU acceleration leverages vectorized SIMD instructions and in-memory column storage for fast analytics.

---

## 7. Quick Recall Flow
```
IBM Db2 -> Enterprise HTAP Database -> Editions: Community, Standard, Advanced -> Features: pureScale, BLU Acceleration, HADR
```
""",

    "2_Db2_System_Requirements_Installation_and_Interfaces.md": """# Db2 System Requirements, Installation & Interfaces — DBMS Module 6

> **Definition:** Setting up **IBM Db2** requires verifying operating system and hardware prerequisites, performing installation via IBM DB2 Setup Wizard, and interacting with the database using **CLP (Command Line Processor)**, **IBM Data Studio**, or **Db2 Web Console**.

---

## 1. Detailed Technical Explanation

### 1. System Requirements for IBM Db2 (v11.5)
- **Supported OS:** Red Hat Enterprise Linux (RHEL), SUSE Linux, Ubuntu, Windows Server / Windows 10/11 (64-bit), IBM AIX.
- **Minimum Memory (RAM):** Minimum 2 GB (16 GB recommended for production).
- **Disk Space:** Minimum 5 GB for binary installation files; additional space for database tablespaces.
- **Processor:** 64-bit x86-64 (Intel/AMD) or IBM POWER processor.

---

## 2. Step-by-Step Db2 Installation Process

```
1. Download Db2 Installation Package (e.g., v11.5 Community Edition)
       |
       v
2. Run Setup Executable (setup.exe on Windows, ./db2setup on Linux)
       |
       v
3. Select Installation Type (Typical / Compact / Custom)
       |
       v
4. Set Up Db2 Instance (Default instance: DB2 / db2inst1)
       |
       v
5. Configure Administrator Credentials (Username: db2admin / db2inst1)
       |
       v
6. Complete Installation & Verify Service Status via Command Line
```

---

## 3. IBM Db2 Management Interfaces

### 1. Db2 Command Line Processor (CLP)
The primary command-line tool for executing SQL statements, system commands, and database management utilities.

```bash
# Start Db2 Command Line Processor
db2cmd

# Connect to database SAMPLE
db2 CONNECT TO SAMPLE USER db2admin USING password123

# Execute SQL Query via CLP
db2 "SELECT * FROM EMPLOYEE WHERE DEPTNO = 'D11'"

# Disconnect from database
db2 CONNECT RESET
```

### 2. IBM Data Studio
An Eclipse-based GUI tool for database administration, SQL query building, stored procedure debugging, and schema modeling.

### 3. Db2 Console / Web Console
A modern browser-based web dashboard providing real-time database monitoring, performance alerts, memory usage metrics, and query execution execution plan visualizers.

---

## 4. Core Concepts & Memory Keywords
- **Db2 Instance:** A logical execution environment that manages database files, memory buffers, and configuration parameters.
- **CLP:** Command Line Processor interactive terminal.
- **IBM Data Studio:** Graphical IDE for database developers and administrators.

---

## 5. Must-Write Points for Exams
- A Db2 Instance must be created and started (`db2start`) before creating or connecting to databases.
- The default instance name on Windows is `DB2`, and on Linux/Unix is `db2inst1`.
- CLP commands can be issued directly in interactive mode or passed as string arguments (`db2 "statement"`).

---

## 6. Quick Recall Flow
```
System Check -> Run db2setup -> Create Instance (db2inst1) -> Start Service (db2start) -> Interact via CLP / Data Studio
```
""",

    "3_Basic_SQL_Operations_in_Db2.md": """# Basic SQL Operations in IBM Db2 — DBMS Module 6

> **Definition:** **SQL Operations in IBM Db2** adhere to ANSI/ISO SQL standards with specialized extensions for table creation, data manipulation, constraints enforcement, NULL handling, and complex JOIN queries.

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
""",

    "4_Self_Learning_Db2_Cloud_Backup_Indexing_Warehouse.md": """# Self-Learning: Db2 on Cloud, Backup & Recovery, Indexing & Warehouse — DBMS Module 6

> **Definition:** Enterprise Db2 deployments utilize **Db2 on Cloud**, **Db2 Warehouse**, automated **Backup & Recovery utilities**, and **B+ Tree Indexing** for cloud scalability, data protection, and high-performance warehousing.

---

## 1. Detailed Technical Explanation

### 1. Db2 Backup & Recovery Utilities

IBM Db2 provides command-line utilities to perform full, incremental, and delta backups to protect against hardware failures and data corruption.

```bash
# 1. Offline Database Backup (Database must be disconnected)
db2 BACKUP DATABASE STUDENTDB TO "C:\Db2Backups"

# 2. Online Database Backup (Allows active user transactions while backing up)
db2 BACKUP DATABASE STUDENTDB ONLINE TO "C:\Db2Backups" INCLUDE LOGS

# 3. Database Restore Operation
db2 RESTORE DATABASE STUDENTDB FROM "C:\Db2Backups" TAKEN AT 20260816120000

# 4. Rollforward Recovery (Replays transaction log records after restore)
db2 ROLLFORWARD DATABASE STUDENTDB TO END OF LOGS AND COMPLETE
```

---

## 2. Db2 Indexing & Performance Tuning

Indexes in Db2 use **B+ Tree data structures** to accelerate lookup performance.

```sql
-- Create a Unique Index on Email
CREATE UNIQUE INDEX IX_STUDENT_EMAIL ON STUDENT(EMAIL);

-- Create a Composite Index for fast searching on Last Name & First Name
CREATE INDEX IX_STUDENT_NAME ON STUDENT(LAST_NAME, FIRST_NAME);

-- Reorganize table data to reclaim fragmented space
db2 REORG TABLE DB2ADMIN.STUDENT;

-- Update optimizer statistics for accurate query planning
db2 RUNSTATS ON TABLE DB2ADMIN.STUDENT WITH DISTRIBUTION AND DETAILED INDEXES ALL;
```

---

## 3. Db2 on Cloud & Db2 Warehouse on Cloud

### 1. IBM Db2 on Cloud:
- Fully managed Cloud Database-as-a-Service (DBaaS) hosted on IBM Cloud and AWS.
- Features automatic scaling, automated daily backups, end-to-end data encryption, and 99.99% SLA availability.

### 2. IBM Db2 Warehouse on Cloud:
- High-performance columnar analytics warehouse powered by **BLU Acceleration**.
- Engineered for massive data processing, machine learning integration (with Python/R), and complex OLAP queries across petabyte-scale datasets.

---

## 4. Core Concepts & Memory Keywords
- **`db2 BACKUP` / `RESTORE`:** Core command line utilities for disaster recovery.
- **`RUNSTATS`:** Updates system catalog statistics for the query optimizer.
- **`REORG`:** Defragments table and index disk pages to improve I/O efficiency.
- **Db2 Warehouse:** Columnar data warehouse leveraging BLU Acceleration on cloud.

---

## 5. Must-Write Points for Exams
- `RUNSTATS` must be executed after major data loads so the Db2 query optimizer can choose optimal execution plans.
- Online backups allow 24/7 continuous operation without shutting down database access.
- Db2 Warehouse uses in-memory column-oriented technology for fast analytical aggregation queries.

---

## 6. Quick Recall Flow
```
Backup/Restore Utilities -> RUNSTATS & REORG Tuning -> B+ Tree Indexes -> Db2 Warehouse Cloud Columnar Analytics
```
"""
}

# Write Module 6 files
for fname, content in m6_files.items():
    with open(os.path.join(m6_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Module 6 Files!")
