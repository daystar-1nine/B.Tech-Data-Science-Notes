import os

DBMS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\DBMS"

m4_qa = os.path.join(DBMS_DIR, "Module 4", "Module_4_QA")
m5_qa = os.path.join(DBMS_DIR, "Module 5", "Module_5_QA")
m6_qa = os.path.join(DBMS_DIR, "Module 6", "Module_6_QA")

os.makedirs(m4_qa, exist_ok=True)
os.makedirs(m5_qa, exist_ok=True)
os.makedirs(m6_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4 QA
# --------------------------------------------------------------------------

u4_2m = """# 2-Mark Questions & Answers — DBMS Module 4: Relational Database Design

---

### Q1. Define 1NF, 2NF, 3NF, and BCNF.

- **1NF:** A relation where all attribute values are atomic (no repeating groups/multivalued cells).
- **2NF:** In 1NF and no non-prime attribute is partially dependent on any candidate key.
- **3NF:** In 2NF and no non-prime attribute is transitively dependent on the primary key (X -> Y implies X is superkey or Y is prime).
- **BCNF:** For every non-trivial functional dependency X -> Y, X must be a strict Super Key.

---

### Q2. What is partial functional dependency?

A **Partial Functional Dependency** occurs when a non-prime attribute is functionally dependent on only a proper subset of a composite candidate key (e.g., in key `{AB}`, if `A -> C`, `C` is partially dependent).

---

### Q3. Define transitive dependency with an example.

A **Transitive Dependency** occurs when a non-prime attribute determines another non-prime attribute through a primary key ($A \to B$ and $B \to C$, therefore $A \to C$).
- *Example:* `Emp_ID -> Dept_ID` and `Dept_ID -> Dept_Name`.

---

### Q4. What is a multivalued dependency (MVD)?

A **Multivalued Dependency (MVD)** $X \twoheadrightarrow Y$ exists when the presence of two tuples sharing attribute X implies that attribute Y is completely independent of the remaining attributes Z in the relation.

---

### Q5. What is a lossless-join decomposition?

A decomposition of relation R into R1 and R2 is **lossless-join** if $R = R1 \bowtie R2$ (joining R1 and R2 produces the exact original tuples without creating spurious/fake records).
"""

u4_3m = """# 3-Mark Questions & Answers — DBMS Module 4: Relational Database Design

---

### Q1. Compare 3NF and BCNF with a suitable example.

| Property | 3NF | BCNF |
| :--- | :--- | :--- |
| **FD Condition X -> Y** | X is Super Key **OR** Y is Prime Attribute. | X MUST be a Super Key (No exceptions). |
| **Overlapping Keys** | Allows overlapping candidate key dependency. | Eliminates overlapping key redundancy. |
| **Dependency Preservation** | Always Guaranteed. | Not always guaranteed. |

- *Example:* `ADVISOR(Student_ID, Subject, Advisor_Name)` where `Advisor_Name -> Subject`. It is in 3NF (Subject is prime) but NOT in BCNF (Advisor_Name is not a superkey).

---

### Q2. Explain the algorithm for attribute closure X+.

```
Input: Set of attributes X, Set of FDs F
Output: X+ (Attribute Closure)

1. Set X+ = X
2. Repeat until X+ does not change:
   For each FD (Y -> Z) in F:
     If Y is a subset of X+:
       X+ = X+ U Z
3. Return X+
```

---

### Q3. Differentiate between functional dependency and multivalued dependency.

| Feature | Functional Dependency (FD) | Multivalued Dependency (MVD) |
| :--- | :--- | :--- |
| **Symbol** | $X \to Y$ | $X \twoheadrightarrow Y$ |
| **Mapping** | Single value: X determines a unique single value of Y. | Multiple values: X independent multidetermines a set of Y values. |
| **Normal Form Target**| 2NF, 3NF, BCNF | 4NF |

---

### Q4. What are NoSQL data models? List its 4 categories.

**NoSQL** databases are non-relational, schema-less, horizontally scalable systems built for big data.
1. **Key-Value Stores:** Redis, Amazon DynamoDB
2. **Document Stores:** MongoDB, CouchDB
3. **Column-Family Stores:** Apache Cassandra, HBase
4. **Graph Databases:** Neo4j, Amazon Neptune

---

### Q5. Explain dependency preservation in database decomposition.

A decomposition of R into sub-relations $R_1, R_2, \dots, R_n$ is **dependency preserving** if the closure of the union of all functional dependencies enforced locally on each sub-relation equals the closure of the original set of functional dependencies:
```
(F1 U F2 U ... U Fn)+ = F+
```
It ensures database integrity constraints can be enforced without expensive JOIN operations across tables.
"""

u4_5m = """# 5-Mark Questions & Answers — DBMS Module 4: Relational Database Design

---

### Q1. Explain 1NF, 2NF, 3NF, and BCNF with concrete table examples.

1. **1NF (Atomic Values):** Eliminates multi-valued cells or comma-separated lists.
2. **2NF (Full Functional Dependency):** Removes partial key dependencies ($A \to B$ where A is part of key $\{A, C\}$).
   - *Fix:* Split into `R1(A, B)` and `R2(A, C)`.
3. **3NF (No Transitive Dependency):** Removes $X \to Y$ where neither X is superkey nor Y is prime.
   - *Fix:* Move $X \to Y$ to a separate lookup table.
4. **BCNF (Strict Super Key):** Forces every determinant X in $X \to Y$ to be a super key.

---

### Q2. Explain the 3NF synthesis algorithm for lossless-join and dependency-preserving decomposition.

```
1. Compute Minimal Cover Fc for functional dependency set F.
2. For each FD (X -> Y) in Fc:
   Create a new relation schema Ri = X U Y.
3. If no schema Ri contains a Candidate Key of original relation R:
   Create an additional schema containing any Candidate Key of R.
4. Remove redundant sub-schemas (if Ri is a subset of Rj, delete Ri).
```
- *Guarantee:* Resulting schemas are in 3NF, preserve all functional dependencies, and guarantee lossless join.

---

### Q3. Explain 4NF and decomposition using multivalued attributes with an example.

- **4NF Condition:** A BCNF relation is in 4NF if for every non-trivial MVD $X \twoheadrightarrow Y$, X is a super key.
- **Example Violation:** `STUDENT(ID, Mobile_No, Skill)` where Mobile_No and Skill are independent multi-valued attributes.
- **Decomposition:**
  1. `STUDENT_MOBILE(ID, Mobile_No)`
  2. `STUDENT_SKILL(ID, Skill)`

---

### Q4. Describe NoSQL Data Models (Key-Value, Document, Column-Family, Graph) with use cases and CAP theorem.

- **CAP Theorem:** Distributed systems can achieve at most 2 out of 3: **Consistency**, **Availability**, **Partition Tolerance**.
- **Data Models:**
  1. **Key-Value:** Caching, Session tokens (Redis).
  2. **Document:** JSON-based content catalogs (MongoDB).
  3. **Column-Family:** High-throughput time-series analytics (Cassandra).
  4. **Graph:** Network relationships & social graphs (Neo4j).
"""

u4_10m = """# 10-Mark Questions & Answers — DBMS Module 4: Relational Database Design

---

### Q1. Explain normalization from 1NF to BCNF in detail with a step-by-step unnormalized enterprise example.

#### Step 1: Unnormalized Relation (UNF)
`EMP_PROJ(Emp_ID, Emp_Name, Phones, Proj_ID, Proj_Name, Hours, Dept_ID, Dept_Name)`

#### Step 2: Convert to 1NF (Atomic Cells)
Flatten comma-separated `Phones` and `Proj_ID` entries into individual atomic rows. Primary Key = `{Emp_ID, Proj_ID}`.

#### Step 3: Convert to 2NF (Remove Partial Dependencies)
- Partial FDs: `Emp_ID -> Emp_Name, Dept_ID, Dept_Name` and `Proj_ID -> Proj_Name`.
- Decompose into:
  1. `EMPLOYEE(Emp_ID, Emp_Name, Dept_ID, Dept_Name)`
  2. `PROJECT(Proj_ID, Proj_Name)`
  3. `ASSIGNMENT(Emp_ID, Proj_ID, Hours)`

#### Step 4: Convert to 3NF (Remove Transitive Dependencies)
- Transitive FD in EMPLOYEE: `Dept_ID -> Dept_Name`.
- Decompose EMPLOYEE into:
  1. `EMP(Emp_ID, Emp_Name, Dept_ID)`
  2. `DEPARTMENT(Dept_ID, Dept_Name)`

#### Step 5: Convert to BCNF (Strict Super Key Determinants)
- Check all determinants $X \to Y$; ensure every $X$ is a super key.
"""

# Write Module 4 QA
with open(os.path.join(m4_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u4_2m)
with open(os.path.join(m4_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u4_3m)
with open(os.path.join(m4_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u4_5m)
with open(os.path.join(m4_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u4_10m)

# --------------------------------------------------------------------------
# MODULE 5 QA
# --------------------------------------------------------------------------

u5_2m = """# 2-Mark Questions & Answers — DBMS Module 5: Query Optimization & Transaction Concurrency Control

---

### Q1. What is query optimization?

**Query Optimization** is the DBMS process of selecting the most efficient physical evaluation plan for a given SQL query to minimize Disk I/O and CPU execution time.

---

### Q2. Define transaction and ACID properties.

A **Transaction** is a logical unit of database work.
- **ACID:** Atomicity (All or Nothing), Consistency (State Validity), Isolation (Independent Execution), Durability (Persistent Survival).

---

### Q3. What is conflict serializability?

A schedule is **Conflict Serializable** if it is conflict equivalent to some serial schedule (it can be transformed into a serial schedule by swapping non-conflicting operations).

---

### Q4. Define Shared and Exclusive locks.

- **Shared Lock (S):** Allows multiple transactions to read a data item concurrently.
- **Exclusive Lock (X):** Grants exclusive read/write access to a single transaction; blocks all other access.

---

### Q5. What is the phantom phenomenon?

The **Phantom Phenomenon** occurs when a concurrent transaction inserts or deletes tuples satisfying a search condition while another transaction is performing range queries over that condition.
"""

u5_3m = """# 3-Mark Questions & Answers — DBMS Module 5: Query Optimization & Transaction Concurrency Control

---

### Q1. Explain equivalence rules for relational algebra transformations.

1. **Selection Commutativity:** $\sigma_{C1}(\sigma_{C2}(E)) \equiv \sigma_{C2}(\sigma_{C1}(E))$
2. **Join Commutativity:** $E1 \bowtie E2 \equiv E2 \bowtie E1$
3. **Pushing Selections Down:** $\sigma_C(E1 \bowtie E2) \equiv \sigma_C(E1) \bowtie E2$ (if predicate C involves only attributes of E1).

---

### Q2. Explain transaction state transition diagram.

```
Active -> Read/Write -> Partially Committed -> Commit Log Flushed -> Committed
   |                          |
   v                          v
Failed -----------------> Aborted (Rollback complete)
```

---

### Q3. Differentiate between Strict 2PL and Rigorous 2PL.

| Feature | Strict 2PL | Rigorous 2PL |
| :--- | :--- | :--- |
| **Exclusive Locks (X)** | Held until Transaction Commit/Abort. | Held until Transaction Commit/Abort. |
| **Shared Locks (S)** | Released during Shrinking phase. | Held until Transaction Commit/Abort. |
| **Cascading Rollback** | Prevents cascading aborts. | Prevents cascading aborts + strict serial order. |

---

### Q4. Explain the Validation-Based (Optimistic) concurrency control protocol.

Optimistic Protocol assumes conflicts are rare and executes in 3 phases:
1. **Read Phase:** Read data and execute updates in private local workspace.
2. **Validation Phase:** Check if workspace updates conflict with committed transactions.
3. **Write Phase:** Copy workspace updates to persistent database if validation succeeds.

---

### Q5. Explain Write-Ahead Logging (WAL) protocol.

The **Write-Ahead Logging (WAL)** protocol dictates that log records describing data modifications MUST be written and flushed to non-volatile disk storage **BEFORE** the actual dirty database memory blocks are written to disk.
"""

u5_5m = """# 5-Mark Questions & Answers — DBMS Module 5: Query Optimization & Transaction Concurrency Control

---

### Q1. Explain cost estimation for selection and join operations in query optimization.

1. **Selection Cost ($b_r$ = blocks of $r$):**
   - Equality condition on non-index: Cost = $b_r$ block accesses.
   - Secondary Index lookup: Cost = Index Depth + 1.
2. **Join Cost ($r \bowtie s$):**
   - **Nested-Loop Join:** Cost = $b_r + (n_r \times b_s)$ block reads.
   - **Block Nested-Loop Join:** Cost = $b_r + (b_r \times b_s)$ block reads.
   - **Hash / Merge Join:** Cost = $3(b_r + b_s)$ block accesses.

---

### Q2. Explain 2-Phase Locking Protocol (2PL) and Multiple Granularity Locking (IS, IX, SIX).

- **2PL:** Growing Phase (Acquire locks) -> Lock Point -> Shrinking Phase (Release locks). Guarantees conflict serializability.
- **Multiple Granularity Locking:** Hierarchy (Database -> File -> Page -> Record). Uses Intent locks:
  - **IS:** Intent to acquire Shared locks on children.
  - **IX:** Intent to acquire Exclusive locks on children.
  - **SIX:** Shared lock on current subtree + IX on child nodes.

---

### Q3. Explain Timestamp Ordering Protocol and Thomas Write Rule.

- **Timestamp Ordering:** Assigns $TS(Ti)$. Checks `TS(Ti) < W-TS(X)` for Read and `TS(Ti) < R-TS(X)` for Write. Aborts if violation occurs (Deadlock Free).
- **Thomas Write Rule:** If $TS(Ti) < W\text{-}TS(X)$ during `Write(X)`, the write request is obsolete and simply **ignored** rather than aborting $Ti$.

---

### Q4. Explain Log-Based Recovery (Deferred vs Immediate update) and Checkpointing.

- **Deferred Update (NO-UNDO/REDO):** Writes postponed until Commit. Requires only REDO during crash recovery.
- **Immediate Update (UNDO/REDO):** Writes allowed while active. Requires UNDO for active and REDO for committed transactions.
- **Checkpointing:** Periodically flushes dirty buffers to disk, limiting crash recovery scan depth.

---

### Q5. Describe Two-Phase Commit (2PC) protocol for distributed transactions and TCL commands.

- **2PC Protocol:**
  1. **Phase 1 (Prepare):** Coordinator sends `PREPARE`; participants vote `VOTE_COMMIT` or `VOTE_ABORT`.
  2. **Phase 2 (Commit):** If all voted commit, coordinator sends `GLOBAL_COMMIT`; else `GLOBAL_ABORT`.
- **TCL Commands:** `COMMIT` (Save), `ROLLBACK` (Undo), `SAVEPOINT` (Checkpoint inside transaction).
"""

u5_10m = """# 10-Mark Questions & Answers — DBMS Module 5: Query Optimization & Transaction Concurrency Control

---

### Q1. Explain query optimization in detail (Heuristic evaluation trees, relational equivalences, cost estimation formulas, join selection).

Detailed breakdown of:
1. Parsing SQL into Initial Relational Algebra Expression Tree.
2. Applying Equivalence Rules (Pushing $\sigma$ and $\pi$ down).
3. Cost estimation for Block Nested Loop, Hash Join, and Merge Join.
4. Physical Plan Selection based on Catalog Statistics ($n_r, b_r, V(A,r)$).
"""

# Write Module 5 QA
with open(os.path.join(m5_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u5_2m)
with open(os.path.join(m5_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u5_3m)
with open(os.path.join(m5_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u5_5m)
with open(os.path.join(m5_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u5_10m)

# --------------------------------------------------------------------------
# MODULE 6 QA
# --------------------------------------------------------------------------

u6_2m = """# 2-Mark Questions & Answers — DBMS Module 6: Foundations of IBM Db2

---

### Q1. What is IBM Db2?

**IBM Db2** is an enterprise relational database management system (RDBMS) engineered for high-performance transactional processing (OLTP), advanced analytics (OLAP), and hybrid cloud environments.

---

### Q2. List the editions of IBM Db2.

1. **Db2 Community Edition** (Free development & evaluation tier)
2. **Db2 Standard Edition** (Departmental & medium business servers)
3. **Db2 Advanced Edition** (Enterprise-grade cluster deployments)

---

### Q3. What is Db2 Command Line Processor (CLP)?

The **Db2 Command Line Processor (CLP)** is an interactive command-line utility used to execute SQL queries, administrative commands, and database management tasks.

---

### Q4. What is Db2 pureScale?

**Db2 pureScale** is an active-active database clustering technology that provides continuous availability, fault tolerance, and seamless horizontal scaling for mission-critical applications.

---

### Q5. Name the function used to handle NULL values in Db2.

In IBM Db2, the **`VALUE(expr1, expr2)`** or **`COALESCE(expr1, expr2)`** function is used to return the first non-null argument.
"""

u6_3m = """# 3-Mark Questions & Answers — DBMS Module 6: Foundations of IBM Db2

---

### Q1. Compare IBM Db2 with Oracle and MySQL.

| Feature | IBM Db2 | Oracle Database | MySQL |
| :--- | :--- | :--- | :--- |
| **High Availability** | Db2 pureScale / HADR | Oracle RAC | Replication / InnoDB Cluster |
| **Analytics Engine** | In-Memory BLU Acceleration | In-Memory Option | External analytics engines |
| **Enterprise Focus** | Hybrid Cloud, HTAP, IBM Z | Enterprise OLTP | Web apps & microservices |

---

### Q2. Explain Db2 system requirements and installation steps.

- **System Requirements:** 64-bit OS (Linux, Windows Server, AIX), 2GB+ RAM, 5GB+ Disk space.
- **Installation Steps:** Launch `db2setup` -> Accept License -> Choose Installation Type -> Create Db2 Instance (`db2inst1`) -> Configure Admin User -> Verify via `db2start`.

---

### Q3. Explain IBM Data Studio and Db2 Web Console interfaces.

- **IBM Data Studio:** Eclipse-based GUI IDE for database development, stored procedure creation, and SQL debugging.
- **Db2 Web Console:** Browser-based monitoring dashboard for memory usage, active connections, and query performance tracking.

---

### Q4. Explain RUNSTATS and REORG utilities in Db2.

- **`RUNSTATS`:** Collects statistics on tables and indexes to update the system catalog for optimal query planning.
- **`REORG`:** Defragments table data and index pages to restore physical contiguous storage efficiency.

---

### Q5. Explain Db2 on Cloud and Db2 Warehouse.

- **Db2 on Cloud:** Fully managed database-as-a-service (DBaaS) with automated backups and 99.99% SLA.
- **Db2 Warehouse on Cloud:** In-memory columnar data warehouse powered by BLU Acceleration for large-scale analytics.
"""

u6_5m = """# 5-Mark Questions & Answers — DBMS Module 6: Foundations of IBM Db2

---

### Q1. Explain IBM Db2 overview, features (BLU Acceleration, pureScale, HADR), and industry use cases.

- **BLU Acceleration:** In-memory columnar storage and SIMD vector processing for fast queries.
- **pureScale:** Active-active clustering for 24/7 continuous availability.
- **HADR:** High Availability Disaster Recovery standby database replication.
- **Use Cases:** Core Banking, Healthcare Claim Systems, Large-scale E-commerce Analytics.

---

### Q2. Write Db2 SQL statements for Table Creation, Constraints (PK, FK, CHECK), Data Manipulation, NULL handling (VALUE()), and JOINS.

```sql
-- DDL
CREATE TABLE DEPT (DEPT_ID INT PRIMARY KEY, DNAME VARCHAR(50));
CREATE TABLE EMP (
    EMP_ID INT PRIMARY KEY, 
    NAME VARCHAR(50) NOT NULL, 
    SALARY DECIMAL(10,2) CHECK (SALARY > 0),
    DEPT_ID INT REFERENCES DEPT(DEPT_ID)
);

-- NULL Handling
SELECT NAME, VALUE(SALARY, 0.00) AS NET_SALARY FROM EMP;

-- Joins
SELECT E.NAME, D.DNAME FROM EMP E INNER JOIN DEPT D ON E.DEPT_ID = D.DEPT_ID;
```

---

### Q3. Explain Db2 Backup and Recovery utilities (db2 BACKUP, RESTORE, ROLLFORWARD).

```bash
# Offline Backup
db2 BACKUP DATABASE STUDENTDB TO "C:\Backups"

# Online Backup with Logs
db2 BACKUP DATABASE STUDENTDB ONLINE TO "C:\Backups" INCLUDE LOGS

# Restore & Rollforward
db2 RESTORE DATABASE STUDENTDB FROM "C:\Backups"
db2 ROLLFORWARD DATABASE STUDENTDB TO END OF LOGS AND COMPLETE
```

---

### Q4. Explain Db2 Indexing, B+ Tree performance tuning, and Db2 Warehouse on Cloud.

- **B+ Tree Indexing:** `CREATE UNIQUE INDEX IX_EMP ON EMP(EMAIL);`
- **Tuning:** Use `RUNSTATS` after bulk inserts and `REORG` to clear table fragmentation.
- **Db2 Warehouse:** Scalable cloud analytical database using column storage and parallel execution.
"""

u6_10m = """# 10-Mark Questions & Answers — DBMS Module 6: Foundations of IBM Db2

---

### Q1. Explain IBM Db2 architecture, features, editions, installation, CLP administration, and industry enterprise use cases in detail.

1. **Architecture & Engine:** Shared-disk pureScale clustering, HADR, BLU Columnar engine.
2. **Editions:** Community (Free), Standard (Departmental), Advanced (Enterprise).
3. **Installation & CLP Commands:**
   ```bash
   db2start
   db2 CONNECT TO SAMPLE
   db2 "SELECT * FROM EMPLOYEE"
   db2stop
   ```
4. **Enterprise Use Cases:** Banking transactional integrity, healthcare record privacy, retail analytics.
"""

# Write Module 6 QA
with open(os.path.join(m6_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u6_2m)
with open(os.path.join(m6_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u6_3m)
with open(os.path.join(m6_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u6_5m)
with open(os.path.join(m6_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u6_10m)

print("Created Module 4, 5, 6 Q&A Bank Files!")
