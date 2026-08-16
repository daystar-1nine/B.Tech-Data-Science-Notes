import os

DBMS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\DBMS"
m5_dir = os.path.join(DBMS_DIR, "Module 5")
os.makedirs(m5_dir, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 5: QUERY OPTIMIZATION AND TRANSACTION CONCURRENCY CONTROL
# --------------------------------------------------------------------------

m5_files = {
    "1_Query_Optimization_Relational_Expressions.md": """# Query Optimization: Transformation of Relational Expressions — DBMS

> **Definition:** **Query Optimization** is the component of a Database Management System (DBMS) that attempts to determine the most efficient execution plan for evaluating a given query by transforming relational algebra expressions into equivalent, lower-cost evaluation trees.

---

## 1. Detailed Technical Explanation

### Query Processing Steps:
```
High-Level SQL Query
       |
       v
[ Parser & Translator ]  ---> Generates Relational Algebra Expression Tree
       |
       v
[ Optimizer Engine ]     ---> Applies Equivalence Rules & Cost Formulas
       |
       v
[ Execution Engine ]     ---> Runs Physical Evaluation Plan on Disk Blocks
```

### Key Relational Algebra Equivalence Rules:
1. **Commutativity of Selection:**
   - $\sigma_{\theta_1}(\sigma_{\theta_2}(E)) \equiv \sigma_{\theta_2}(\sigma_{\theta_1}(E))$
2. **Cascading of Selection:**
   - $\sigma_{\theta_1 \land \theta_2}(E) \equiv \sigma_{\theta_1}(\sigma_{\theta_2}(E))$
3. **Commutativity of Join:**
   - $E_1 \bowtie_{\theta} E_2 \equiv E_2 \bowtie_{\theta} E_1$
4. **Associativity of Join:**
   - $(E_1 \bowtie E_2) \bowtie E_3 \equiv E_1 \bowtie (E_2 \bowtie E_3)$
5. **Pushing Selections Down Trees:**
   - Perform selection operations ($\sigma$) as early as possible before joins ($\bowtie$) to reduce intermediate table size.

### Heuristic Optimization Algorithm:
1. Break down complex query conditions into simple selections.
2. **Push Selections Down:** Move $\sigma$ down the query tree towards leaf nodes.
3. **Push Projections Down:** Move $\pi$ down to keep only required attributes.
4. Replace Cartesian products followed by selections ($\sigma(\times)$) with Join operations ($\bowtie$).

---

## 2. Core Concepts & Memory Keywords
- **Equivalence Rules:** Algebraic identities ensuring two query trees return identical tuple results.
- **Pushing Selections:** Filtering rows early to minimize intermediate memory usage.
- **Heuristic Optimization:** Rule-based query tree transformation.

---

## 3. Must-Write Points for Exams
- Query optimization chooses the physical execution path with minimal disk I/O cost.
- Pushing selection operators down relational trees dramatically reduces intermediate table sizes before joins.
- Applying equivalence rules guarantees that equivalent relational expressions yield identical query results.

---

## 4. Quick Recall Flow
```
SQL Query -> Parse Relational Tree -> Push Selections Down -> Replace Cartesian Product with Join -> Optimal Execution Plan
```
""",

    "2_Estimating_Statistics_and_Choice_of_Evaluation_Plan.md": """# Estimating Statistics & Choice of Evaluation Plan — DBMS

> **Definition:** **Cost-Based Query Optimization** estimates the physical execution cost (Disk I/O, CPU cycles, Network latency) of candidate evaluation plans using **System Catalog Statistics** to select the minimal cost plan.

---

## 1. Detailed Technical Explanation

### 1. Catalog Statistics Kept by DBMS:
- **$n_r$:** Number of tuples in relation $r$.
- **$b_r$:** Number of disk blocks containing tuples of relation $r$.
- **$l_r$:** Size of a tuple in relation $r$ (in bytes).
- **$f_r$:** Blocking factor of relation $r$ (number of tuples per block).
- **$V(A, r)$:** Number of distinct values for attribute $A$ in relation $r$.

### 2. Cost Estimation Formulas:

#### Selection Cost Estimation:
- **Equality Condition $\sigma_{A = a}(r)$:**
  - If no index exists: Cost = $b_r$ block reads.
  - Expected output tuples: $E = \frac{n_r}{V(A, r)}$
- **Range Condition $\sigma_{A \ge a}(r)$:**
  - Estimated size: $E = n_r \times \frac{\text{Max}(A) - a}{\text{Max}(A) - \text{Min}(A)}$

#### Join Cost Estimation ($r \bowtie s$):
- **Nested-Loop Join:**
  - Cost = $b_r + (n_r \times b_s)$ block accesses.
- **Block Nested-Loop Join:**
  - Cost = $b_r + (b_r \times b_s)$ block accesses.
- **Indexed Nested-Loop Join:**
  - Cost = $b_r + (n_r \times c)$ where $c$ is index access cost.
- **Hash Join / Merge Join:**
  - Cost = $3(b_r + b_s)$ block accesses.

### 3. Choice of Evaluation Plan:
The query optimizer generates multiple physical evaluation plans, computes total cost = $\text{Disk I/O Cost} + \text{CPU Cost}$, and selects the plan with the **minimum total cost**.

---

## 2. Core Concepts & Memory Keywords
- **Catalog Statistics:** Metadata ($n_r, b_r, V(A,r)$) used for selectivity calculation.
- **Selectivity Factor:** Proportion of tuples satisfying a predicate.
- **Nested-Loop Join:** Basic join algorithm iterating over outer and inner tables.

---

## 3. Must-Write Points for Exams
- Disk I/O (number of block transfers) is the primary cost metric in database query evaluation.
- Block nested-loop join is significantly faster than tuple-nested loop join by reading outer relation blocks into memory.
- Hash joins and merge joins achieve near linear performance $O(b_r + b_s)$ for large tables.

---

## 4. Quick Recall Flow
```
System Catalog Stats -> Compute Selectivity -> Estimate Disk Block Accesses -> Select Plan with Lowest Total Cost
```
""",

    "3_Transaction_Concept_and_ACID_Properties.md": """# Transaction Concept & ACID Properties — DBMS

> **Definition:** A **Transaction** is a logical unit of database processing that includes one or more database operations (READ, WRITE). To preserve data integrity, transactions must satisfy all four **ACID Properties**.

---

## 1. Detailed Technical Explanation

### The ACID Properties:

```
A - ATOMICITY      : All operations complete successfully, or ALL are undone ("All-or-Nothing").
C - CONSISTENCY    : Transaction transforms database from one valid state to another valid state.
I - ISOLATION      : Concurrent transactions execute independently without interfering with each other.
D - DURABILITY     : Once committed, updates persist permanently in non-volatile storage even after system failure.
```

### 1. Atomicity
- Enforced by the **Recovery Manager** using Write-Ahead Logging (WAL) and Rollback mechanisms.
- Operations: `COMMIT` (permanent save) or `ROLLBACK` (undo changes).

### 2. Consistency
- Enforced by database schema constraints (Primary Key, Foreign Key, `CHECK` constraints) and application logic.

### 3. Isolation
- Enforced by the **Concurrency Control Manager** using locking or timestamping.
- Prevents anomalies: Dirty Reads, Non-Repeatable Reads, Phantom Reads.

### 4. Durability
- Enforced by **Log Recovery & Checkpointing** writing updates to non-volatile disk/SSD storage.

---

## 2. Transaction State Diagram

```
                 +--------------+
                 |    ACTIVE    | (Initial state: reading/writing)
                 +--------------+
                  /            \
                 /              \
                v                v
      +------------------+     +-------------------+
      | PARTIALLY        |     |      FAILED       |
      | COMMITTED        |     +-------------------+
      +------------------+               |
                |                        v
                v              +-------------------+
      +------------------+     |     ABORTED       | (Rollback complete)
      |    COMMITTED     |     +-------------------+
      +------------------+
     (Successfully saved)
```

---

## 3. Core Concepts & Memory Keywords
- **ACID:** Atomicity, Consistency, Isolation, Durability.
- **Commit Point:** The exact moment transaction updates become permanent.
- **Rollback / Abort:** Undoing all operations of an incomplete transaction.

---

## 4. Must-Write Points for Exams
- Atomicity guarantees that partial execution of a transaction is impossible.
- Isolation ensures that concurrent execution yields the same state as serial execution.
- The transaction state transitions from Active -> Partially Committed -> Committed, or Active -> Failed -> Aborted.

---

## 5. Quick Recall Flow
```
Active -> Read/Write -> Partially Committed -> Commit Log Written -> Committed (Or Aborted on Failure)
```
""",

    "4_Serializability_and_Concurrency_Control.md": """# Serializability & Concurrency Control — DBMS

> **Definition:** **Serializability** is the correctness criterion for concurrent transaction execution. A non-serial schedule is **serializable** if its execution outcome is equivalent to executing the transactions sequentially one after another (a Serial Schedule).

---

## 1. Detailed Technical Explanation

### 1. Types of Schedules:
- **Serial Schedule:** Transactions execute strictly one after another (No interleaving). Guaranteed to be correct, but offers poor CPU utilization.
- **Concurrent (Interleaved) Schedule:** Operations of multiple transactions interleave. High performance, but requires concurrency control.

### 2. Conflict Serializability:
Two operations $O_i$ and $O_j$ in a schedule are in **conflict** if and only if:
1. They belong to **different transactions**.
2. They access the **same data item**.
3. At least one of the operations is a **WRITE** (`W(X)`).

#### Conflicting Operations Matrix:
| Operation $T_1$ | Operation $T_2$ | Conflict Status |
| :--- | :--- | :--- |
| `Read(X)` | `Read(X)` | **No Conflict** |
| `Read(X)` | `Write(X)` | **CONFLICT** |
| `Write(X)` | `Read(X)` | **CONFLICT** |
| `Write(X)` | `Write(X)` | **CONFLICT** |

### 3. Precedence Graph (Serialization Graph) Test:
A directed graph $G = (V, E)$ used to test Conflict Serializability:
- **Vertices (V):** All transactions in schedule.
- **Edges (E):** Directed edge $T_i \to T_j$ if $T_i$ performs a conflicting operation on data item $X$ before $T_j$.

```
PRECEDENCE GRAPH RULE:
- If Precedence Graph contains NO CYCLES -> Schedule is CONFLICT SERIALIZABLE.
- If Precedence Graph contains CYCLES    -> Schedule is NOT Conflict Serializable (Concurrency Anomaly!).
```

```
Example (Cycle detected):
  [ T1 ] ---- Read(X), Write(X) ----> [ T2 ]
    ^                                   |
    |--------- Write(Y), Read(Y) -------|  (Cycle! Not Serializable)
```

---

## 2. Core Concepts & Memory Keywords
- **Conflict Equivalent:** Two schedules can be transformed into one another by swapping non-conflicting operations.
- **Serialization Graph:** Directed graph used to test conflict serializability for cycles.
- **View Serializability:** Broader class of serializability accounting for blind writes.

---

## 3. Must-Write Points for Exams
- A schedule is conflict serializable if it is conflict equivalent to some serial schedule.
- Checking for cycles in a precedence graph using Topological Sorting validates conflict serializability.
- Conflict serializability is a sufficient condition for view serializability.

---

## 4. Quick Recall Flow
```
Concurrent Operations -> Identify Conflicts (R-W, W-R, W-W) -> Draw Precedence Graph -> No Cycles? -> Serializable!
```
""",

    "5_Lock_Based_Protocols_and_Multiple_Granularity.md": """# Lock-Based Protocols & Multiple Granularity — DBMS

> **Definition:** **Lock-Based Protocols** control concurrent access to data items by requiring transactions to acquire **Locks** (Shared or Exclusive) before reading or writing data.

---

## 1. Detailed Technical Explanation

### 1. Lock Modes:
1. **Shared Lock (S-Lock):** Granted for `READ` operations. Multiple transactions can hold S-locks simultaneously on the same item.
2. **Exclusive Lock (X-Lock):** Granted for `WRITE` operations. Only one transaction can hold an X-lock; no other transaction can read or write.

#### Lock Compatibility Matrix:
| Lock Requested | Shared (S) | Exclusive (X) |
| :--- | :--- | :--- |
| **Shared (S)** | **Compatible (True)** | Incompatible (False) |
| **Exclusive (X)**| Incompatible (False) | Incompatible (False) |

---

## 2. Two-Phase Locking Protocol (2PL)

2PL guarantees conflict serializability by dividing a transaction's lock lifecycle into two distinct phases:

```
Number of
Locks Held
   ^             Phase 1: Growing Phase          Phase 2: Shrinking Phase
   |             (Locks acquired, none released)  (Locks released, none acquired)
   |
   |                   /\ Lock Point
   |                  /  \
   |                 /    \
   |                /      \
   +---------------+--------+-----------------------------------> Time
```

### 2PL Variants:
1. **Basic 2PL:** Transaction acquires locks as needed (Growing), releases locks (Shrinking). Can suffer from **Cascading Aborts**.
2. **Strict 2PL:** Transaction holds all **Exclusive (X) locks until COMMIT/ABORT**. Prevents cascading aborts (Strict schedules).
3. **Rigorous 2PL:** Transaction holds **ALL locks (Shared and Exclusive) until COMMIT/ABORT**.

---

## 3. Multiple Granularity Locking (MGL)

MGL allows data items of various sizes (Database -> File -> Page -> Record) to be locked in a tree hierarchy.

```
                  [ DATABASE ]
                       |
                  [   FILE   ]
                       |
                  [   PAGE   ]
                       |
                  [  RECORD  ]
```

### Intent Locks:
Before locking a fine-grained node (e.g., Record), a transaction must acquire an **Intent Lock** on its ancestor nodes:
- **IS (Intent Shared):** Intent to lock explicit child nodes with Shared locks.
- **IX (Intent Exclusive):** Intent to lock explicit child nodes with Exclusive locks.
- **SIX (Shared + Intent Exclusive):** Explicit Shared lock on current subtree plus Intent Exclusive on lower nodes.

---

## 4. Core Concepts & Memory Keywords
- **Lock Point:** Point in time where a transaction acquires its final lock in 2PL.
- **Cascading Rollback:** One transaction aborting causes multiple dependent transactions to abort.
- **Intent Locking:** Top-down locking mechanism in granularity trees.

---

## 5. Must-Write Points for Exams
- Basic 2PL guarantees **conflict serializability**, but does NOT prevent **deadlocks**.
- Strict 2PL prevents cascading aborts by holding Exclusive locks until the transaction commits.
- Multiple granularity locking improves concurrency by allowing fine-grained locks without searching entire trees.

---

## 6. Quick Recall Flow
```
Growing Phase (Acquire Locks) -> Lock Point -> Shrinking Phase (Release Locks) -> Hold X-Locks to Commit (Strict 2PL)
```
""",

    "6_Insertion_Deletion_and_Predicate_Reads.md": """# Insertion-Deletion & Predicate Reads (Phantoms) — DBMS

> **Definition:** The **Phantom Phenomenon** occurs when a concurrent transaction inserts or deletes tuples satisfying a search predicate while another transaction is executing range queries over the same predicate.

---

## 1. Detailed Technical Explanation

### 1. The Phantom Problem Scenario
Suppose Transaction $T_1$ reads all employees in `Dept_ID = 10` twice within its execution:

```
Transaction T1                             Transaction T2
----------------------------------------   ------------------------------------
Select * from Emp where Dept_ID = 10;
(Returns 5 rows)
                                           Insert into Emp values (106, 'Raj', 10);
                                           Commit;
Select * from Emp where Dept_ID = 10;
(Returns 6 rows! Phantom Row detected!)
```

Standard tuple-level locking fails to prevent this because the new tuple `106` did not exist when $T_1$ acquired its locks!

---

## 2. Solutions to Phantom Phenomenon

### 1. Predicate Locking (Logical Locking)
- Transaction $T_1$ acquires a lock on a **predicate condition** (e.g., `Dept_ID = 10`).
- Any attempt by $T_2$ to insert, delete, or update a tuple that satisfies the predicate condition will conflict with $T_1$'s predicate lock and be blocked.
- *Drawback:* Extremely high computational overhead to evaluate arbitrary predicate intersections.

### 2. Index Locking (Physical Granularity Solution)
- If an index exists on `Dept_ID`, $T_1$ locks the **index bucket / page** corresponding to `Dept_ID = 10`.
- $T_2$ cannot insert a new tuple with `Dept_ID = 10` because inserting requires updating the locked index page.
- *Advantage:* Fast physical check with minimal overhead.

### 3. Next-Key Locking (B+ Tree Index Lock)
- Locks both the target index record AND the gap immediately preceding/following it in the B+ Tree index, preventing insertions into the range.

---

## 3. Core Concepts & Memory Keywords
- **Phantom Tuple:** A newly inserted row appearing in a repeated range query.
- **Predicate Lock:** Lock placed on logical search conditions instead of physical record IDs.
- **Index-Range Lock:** Locking B+ Tree index leaf pages to prevent phantom inserts.

---

## 4. Must-Write Points for Exams
- Standard tuple locks cannot prevent phantom rows because phantom tuples do not exist at lock request time.
- Predicate locking guarantees full isolation for dynamic databases but has high runtime overhead.
- Practical databases (e.g., InnoDB, Db2) implement Next-Key / Index-Range locking for ISO Serializable isolation.

---

## 5. Quick Recall Flow
```
Range Query -> Concurrent Insert -> Phantom Row Appears -> Resolve via Predicate Locks or Next-Key Index Locks
```
""",

    "7_Timestamp_and_Validation_Based_Protocols.md": """# Timestamp & Validation-Based Protocols — DBMS

> **Definition:** **Timestamp Ordering Protocols** ensure conflict serializability without using locks by assigning a unique monotonic timestamp $TS(T_i)$ to each transaction upon start and enforcing operation ordering according to timestamp sequence.

---

## 1. Detailed Technical Explanation

### 1. System Timestamps
Each data item $X$ maintains two timestamps:
- **`W-TS(X)`:** Largest timestamp of any transaction that executed `Write(X)`.
- **`R-TS(X)`:** Largest timestamp of any transaction that executed `Read(X)`.

### 2. Basic Timestamp Ordering Rules

#### Read Operation `Read(X)` by Transaction $T_i$:
1. If $TS(T_i) < W\text{-}TS(X)$: $T_i$ is attempting to read an overwritten value. **Abort and Rollback $T_i$**.
2. Else: Execute `Read(X)` and update $R\text{-}TS(X) = \max(R\text{-}TS(X), TS(T_i))$.

#### Write Operation `Write(X)` by Transaction $T_i$:
1. If $TS(T_i) < R\text{-}TS(X)$: $T_i$ is attempting to write a value needed by a younger transaction. **Abort and Rollback $T_i$**.
2. If $TS(T_i) < W\text{-}TS(X)$: $T_i$ is writing an obsolete value (**Thomas Write Rule**: Ignore write and continue).
3. Else: Execute `Write(X)` and update $W\text{-}TS(X) = TS(T_i)$.

---

## 2. Validation-Based (Optimistic) Protocol

Used when read operations dominate write operations (low conflict rate). Execution is split into 3 phases:

```
+-------------------+      +-------------------+      +-------------------+
| 1. READ PHASE     | ---> | 2. VALIDATION     | ---> | 3. WRITE PHASE    |
| Read & Write to   |      | Check for conflict|      | Copy workspace to |
| private workspace |      | with committed Tx |      | database storage  |
+-------------------+      +-------------------+      +-------------------+
```

### Validation Test Condition:
For all $T_k$ committed before $T_i$:
- $\text{Finish}(T_k) < \text{StartValidation}(T_i)$, OR
- $\text{Writeset}(T_k) \cap \text{Readset}(T_i) = \emptyset$.

---

## 3. Core Concepts & Memory Keywords
- **Monotonic Timestamps:** Unique growing values (System clock or global counter).
- **Thomas Write Rule:** Optimization ignoring outdated write requests rather than aborting.
- **Optimistic Concurrency Control:** Read -> Validate -> Write phases.

---

## 4. Must-Write Points for Exams
- Timestamp ordering protocols guarantee **freedom from deadlocks** because transactions are never made to wait indefinitely.
- Starvation can occur under timestamp ordering if a long transaction is repeatedly aborted by younger transactions.
- Validation protocols perform all modifications on local workspaces before validating.

---

## 5. Quick Recall Flow
```
Compare TS(Ti) with W-TS(X)/R-TS(X) -> Valid? Proceed : Outdated? Abort & Restart with New Timestamp
```
""",

    "8_Log_Based_Recovery.md": """# Log-Based Recovery & Checkpointing — DBMS

> **Definition:** **Log-Based Recovery** maintains a chronological record of all database modifications on non-volatile storage (the **Log**) to restore database Atomicity and Durability following system crashes.

---

## 1. Detailed Technical Explanation

### 1. Write-Ahead Logging (WAL) Protocol
Before any data modification is written to disk, the corresponding log record **MUST** be flushed to non-volatile log storage.

#### Log Record Formats:
- `<Tn, start>`: Transaction $T_n$ started.
- `<Tn, X, V1, V2>`: Transaction $T_n$ changed item $X$ from Old Value $V_1$ to New Value $V_2$.
- `<Tn, commit>`: Transaction $T_n$ committed.
- `<Tn, abort>`: Transaction $T_n$ aborted.

---

## 2. Recovery Techniques

### 1. Deferred Update Technique (NO-UNDO / REDO Algorithm)
- Database disk writes are postponed until the transaction reaches its `COMMIT` point.
- **Recovery Procedure:**
  - `REDO(Tn)`: Replays new values $V_2$ for transactions with both `<Tn, start>` and `<Tn, commit>` in log.
  - No `UNDO` required because uncommitted data was never written to main database blocks!

### 2. Immediate Update Technique (UNDO / REDO Algorithm)
- Database disk writes can occur while the transaction is still active.
- **Recovery Procedure:**
  - `UNDO(Tn)`: Restores old values $V_1$ for active transactions with `<Tn, start>` but NO `<Tn, commit>`.
  - `REDO(Tn)`: Replays new values $V_2$ for committed transactions.

---

## 3. Checkpointing

Checkpointing reduces recovery overhead by periodically flushing all dirty buffer blocks and active transaction logs to disk.

```
                    Checkpoint Record Outputted
                              |
                              v
<T1, start> ... <T2, start> <CHECKPOINT {T1, T2}> ... <T2, commit> [CRASH!]
```
- During crash recovery, the system only needs to scan the log backwards up to the **most recent checkpoint**.

---

## 4. Core Concepts & Memory Keywords
- **WAL Protocol:** Write log to disk BEFORE writing database blocks.
- **REDO:** Replay operations ($V_2$) for committed transactions.
- **UNDO:** Reverse operations ($V_1$) for uncommitted / aborted transactions.
- **Checkpoint:** Periodic point flushing dirty RAM buffers to persistent disk.

---

## 5. Must-Write Points for Exams
- WAL guarantees Durability by ensuring committed transactions can be reconstructed via REDO log records.
- Deferred update requires only REDO operations during recovery; immediate update requires both UNDO and REDO.
- Checkpointing eliminates the need to scan the entire log file from the beginning of database creation.

---

## 6. Quick Recall Flow
```
Write Log Record to Disk (WAL) -> Modify Memory -> Checkpoint -> System Crash -> UNDO Active, REDO Committed
```
""",

    "9_Self_Learning_Distributed_Transactions_TCL_Performance_Tuning.md": """# Self-Learning: Distributed Transactions, TCL & Performance Tuning — DBMS

> **Definition:** **Distributed Transactions** execute across multiple independent database nodes connected over a network, managed using the **Two-Phase Commit (2PC)** protocol.

---

## 1. Detailed Technical Explanation

### 1. Two-Phase Commit (2PC) Protocol
Coordinates atomic commit/abort decisions across multiple distributed node participants.

```
COORDINATOR                                  PARTICIPANTS (Nodes 1, 2, 3)
   |                                                    |
   | -------- Phase 1: PREPARE Message ---------------> |
   |                                                    | (Check local log & resources)
   | <------- VOTE_COMMIT / VOTE_ABORT ---------------- |
   |                                                    |
   | (If all VOTE_COMMIT):                              |
   | -------- Phase 2: GLOBAL_COMMIT Message ---------> |
   |                                                    | (Write commit to local disk)
   | <------- ACKNOWLEDGEMENT ------------------------- |
```

---

## 2. Transaction Control Language (TCL) Commands

```sql
-- 1. Start a explicitly scoped transaction
START TRANSACTION;

-- 2. Modify data
UPDATE Accounts SET Balance = Balance - 5000 WHERE Acc_No = 101;

-- 3. Set a rollback checkpoint
SAVEPOINT sp1;

UPDATE Accounts SET Balance = Balance + 5000 WHERE Acc_No = 102;

-- 4. Rollback to Savepoint if error occurs
ROLLBACK TO SAVEPOINT sp1;

-- 5. Commit remaining updates permanently
COMMIT;
```

---

## 3. Database Performance Tuning Strategies

1. **Indexing Optimization:**
   - Create B+ Tree indexes on frequently queried `WHERE`, `JOIN`, and `ORDER BY` columns.
   - Avoid over-indexing (slows down `INSERT`, `UPDATE`, `DELETE` operations).
2. **Query Refactoring:**
   - Avoid `SELECT *`; specify explicit columns to reduce I/O bandwidth.
   - Replace correlated subqueries with explicit `JOIN` operations.
3. **Buffer Pool & Memory Tuning:**
   - Allocate adequate RAM to database buffer pool to maximize cache hit ratio (>95%).
4. **Partitioning & Sharding:**
   - Range/Hash partition large tables to distribute disk I/O bottlenecks.

---

## 4. Quick Recall Flow
```
2PC -> Prepare Phase (Vote) -> Commit Phase (Global ACK) | TCL -> COMMIT, ROLLBACK, SAVEPOINT | Tuning -> B+ Tree Indexes
```
"""
}

# Write Module 5 files
for fname, content in m5_files.items():
    with open(os.path.join(m5_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Module 5 Files!")
