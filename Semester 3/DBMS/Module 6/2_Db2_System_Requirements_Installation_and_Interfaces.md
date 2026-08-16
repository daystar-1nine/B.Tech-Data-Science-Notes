# Db2 System Requirements, Installation & Interfaces — DBMS Module 6

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
