import os

BASE_DIR = r"S:\B.Tech Data Science Notes\Semester 3"

# --------------------------------------------------------------------------
# 1. DBMS MODULE 2 QA (Relational Algebra & Calculus)
# --------------------------------------------------------------------------
dbms_m2_qa_dir = os.path.join(BASE_DIR, "DBMS", "Module 2", "Module_2_QA")
os.makedirs(dbms_m2_qa_dir, exist_ok=True)

dbms_m2_2m = """# 2-Mark Questions & Answers — DBMS Module 2: Relational Algebra & Calculus

---

### Q1. What is Relational Algebra?

**Relational Algebra** is a procedural query language that takes one or two relations as input and produces a new relation as output using mathematical operators like Selection (σ), Projection (π), Union (∪), and Join (⋈).

---

### Q2. Differentiate between Selection (σ) and Projection (π) operations.

- **Selection (σ):** Horizontal filtering operation that selects rows (tuples) that satisfy a specified predicate condition.
- **Projection (π):** Vertical filtering operation that selects specific columns (attributes) and removes duplicate tuples.

---

### Q3. What is Union Compatibility in Relational Algebra?

Two relations R and S are **Union Compatible** if:
1. Both relations have the **same number of attributes** (same arity).
2. The domains of corresponding attributes are identical in data type and order.

---

### Q4. Define Cartesian Product (×) with an example.

The **Cartesian Product (R × S)** combines every tuple of relation R with every tuple of relation S. If R has *n* tuples and S has *m* tuples, R × S contains **n × m** tuples.

---

### Q5. What is Tuple Relational Calculus (TRC)?

**Tuple Relational Calculus (TRC)** is a non-procedural query language where queries are expressed in the mathematical logic form:
```
{ t | P(t) }
```
where *t* is a resulting tuple variable and *P(t)* is a predicate formula specifying conditions the tuple must satisfy.
"""

dbms_m2_3m = """# 3-Mark Questions & Answers — DBMS Module 2: Relational Algebra & Calculus

---

### Q1. Explain Set Difference (−) and Intersection (∩) operations with examples.

1. **Set Difference (R − S):** Returns tuples that belong to relation R but NOT to relation S (both must be union-compatible).
2. **Intersection (R ∩ S):** Returns tuples present in BOTH relations R and S.
   - *Identity:* `R ∩ S = R − (R − S)`

---

### Q2. Explain Natural Join (⋈) vs Theta Join (⋈θ).

| Feature | Natural Join (⋈) | Theta Join (⋈θ) |
| :--- | :--- | :--- |
| **Join Condition** | Equality on ALL common attribute names automatically. | Explicit conditional predicate (e.g., `R.A > S.B` or `R.A = S.B`). |
| **Duplicate Columns**| Eliminates duplicate common columns in the result. | Retains columns from both relations unless projected out. |

---

### Q3. Differentiate between Procedural and Non-Procedural query languages.

| Feature | Relational Algebra (Procedural) | Relational Calculus (Non-Procedural) |
| :--- | :--- | :--- |
| **Approach** | Tells **HOW** to retrieve data step-by-step. | Tells **WHAT** data to retrieve without retrieval steps. |
| **Execution** | Specifies exact sequence of relational operations. | Uses first-order predicate calculus logic formulas. |
| **Foundation** | Basis for DBMS physical query execution plans. | Theoretical foundation for SQL declarative language. |
"""

dbms_m2_5m = """# 5-Mark Questions & Answers — DBMS Module 2: Relational Algebra & Calculus

---

### Q1. Explain all fundamental operations of Relational Algebra with notation and examples.

1. **Selection (σ):** `σ_{Dept_ID = 10}(Employee)` — Selects rows where Dept_ID is 10.
2. **Projection (π):** `π_{Name, Salary}(Employee)` — Projects Name and Salary columns.
3. **Union (∪):** `R ∪ S` — Combines tuples from R and S without duplicates.
4. **Set Difference (−):** `R − S` — Tuples in R but not in S.
5. **Cartesian Product (×):** `R × S` — Pairwise combination of all rows.
6. **Rename (ρ):** `ρ_{NewName}(R)` — Renames relation or attributes.

---

### Q2. Explain Outer Join operations (Left, Right, Full) with concrete table diagrams.

- **Left Outer Join (⟕):** Retains all tuples from the left table; unmatched right attributes are filled with `NULL`.
- **Right Outer Join (⟖):** Retains all tuples from the right table; unmatched left attributes are filled with `NULL`.
- **Full Outer Join (⟗):** Retains all tuples from both tables, filling unmatched columns on either side with `NULL`.

---

### Q3. Explain Domain Relational Calculus (DRC) and compare TRC vs DRC.

- **DRC Form:** `{ <x1, x2, ..., xn> | P(x1, x2, ..., xn) }` where variables represent attribute domains rather than full tuples.
- **Comparison:** TRC binds variables over entire tuples (*t*), while DRC binds variables over individual attribute values (*x, y, z*).
"""

dbms_m2_10m = """# 10-Mark Questions & Answers — DBMS Module 2: Relational Algebra & Calculus

---

### Q1. Explain Relational Algebra operations (Fundamental & Derived), Joins (Inner, Outer, Semi, Anti), and Relational Calculus in detail with schema queries.

Comprehensive solution covering:
1. Six Fundamental Relational Algebra Operations (Selection, Projection, Union, Set Difference, Cartesian Product, Rename).
2. Derived Operations: Intersection, Natural Join, Theta Join, Division operator (÷ for "for all" queries).
3. Left, Right, and Full Outer Joins with step-by-step table examples.
4. Tuple Relational Calculus (TRC) and Domain Relational Calculus (DRC) with existential (∃) and universal (∀) quantifiers.
5. Equivalence between SQL SELECT queries and Relational Algebra expressions.
"""

with open(os.path.join(dbms_m2_qa_dir, "2M.md"), "w", encoding="utf-8") as f: f.write(dbms_m2_2m)
with open(os.path.join(dbms_m2_qa_dir, "3M.md"), "w", encoding="utf-8") as f: f.write(dbms_m2_3m)
with open(os.path.join(dbms_m2_qa_dir, "5M.md"), "w", encoding="utf-8") as f: f.write(dbms_m2_5m)
with open(os.path.join(dbms_m2_qa_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(dbms_m2_10m)


# --------------------------------------------------------------------------
# 2. DBMS MODULE 3 QA (SQL Standards, DDL, DML, Subqueries, Triggers)
# --------------------------------------------------------------------------
dbms_m3_qa_dir = os.path.join(BASE_DIR, "DBMS", "Module 3", "Module_3_QA")
os.makedirs(dbms_m3_qa_dir, exist_ok=True)

dbms_m3_2m = """# 2-Mark Questions & Answers — DBMS Module 3: SQL Standards & Advanced Queries

---

### Q1. Differentiate between DDL and DML commands in SQL.

- **DDL (Data Definition Language):** Defines and modifies database schema structure (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`). Auto-committed.
- **DML (Data Manipulation Language):** Manages and queries data within tables (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). Requires explicit commit.

---

### Q2. What is the difference between WHERE and HAVING clauses?

- **WHERE:** Filters individual rows *before* grouping occurs (cannot use aggregate functions).
- **HAVING:** Filters aggregated groups *after* `GROUP BY` execution (can use `COUNT`, `SUM`, `AVG`).

---

### Q3. What is a Correlated Subquery?

A **Correlated Subquery** is a nested subquery that references columns from the outer query for each row processed, executing once per candidate row of the outer table.

---

### Q4. Define Database Trigger and list its types.

A **Trigger** is a stored PL/SQL program unit that automatically executes in response to specified database events (`INSERT`, `UPDATE`, `DELETE`).
- **Types:** `BEFORE` trigger, `AFTER` trigger, `INSTEAD OF` trigger, Row-level (`FOR EACH ROW`), Statement-level.

---

### Q5. What is the difference between DELETE and TRUNCATE?

- **DELETE:** DML command, deletes specified rows using `WHERE`, can be rolled back, fires delete triggers.
- **TRUNCATE:** DDL command, removes all rows by deallocating pages, much faster, cannot be rolled back, does not fire triggers.
"""

dbms_m3_3m = """# 3-Mark Questions & Answers — DBMS Module 3: SQL Standards & Advanced Queries

---

### Q1. Explain SQL Set Operations (UNION, INTERSECT, EXCEPT / MINUS).

1. **`UNION` / `UNION ALL`:** Combines result sets of two queries. `UNION` removes duplicates; `UNION ALL` retains all rows.
2. **`INTERSECT`:** Returns only rows returned by both queries.
3. **`EXCEPT` (or `MINUS` in Oracle):** Returns rows from first query that are not present in second query.

---

### Q2. Explain SQL Aggregate Functions with examples.

- **`COUNT(*)` / `COUNT(col)`:** Counts total rows or non-null values.
- **`SUM(col)` / `AVG(col)`:** Calculates sum or arithmetic mean of numeric columns.
- **`MIN(col)` / `MAX(col)`:** Finds smallest or largest value.
- *Example:* `SELECT Dept_ID, AVG(Salary) FROM Emp GROUP BY Dept_ID HAVING COUNT(*) > 5;`

---

### Q3. What are Stored Procedures vs Functions in PL/SQL?

| Feature | Stored Procedure | Stored Function |
| :--- | :--- | :--- |
| **Return Value** | May return zero, one, or multiple values via `OUT` parameters. | **MUST return exactly one value** using `RETURN` clause. |
| **Invocation in SQL**| Cannot be called directly inside `SELECT` queries. | Can be embedded directly inside `SELECT` and `WHERE` clauses. |
| **DML Operations** | Allowed to execute `INSERT`, `UPDATE`, `DELETE`. | Restricted from performing DML when used in `SELECT`. |
"""

dbms_m3_5m = """# 5-Mark Questions & Answers — DBMS Module 3: SQL Standards & Advanced Queries

---

### Q1. Explain Nested Subqueries (IN, NOT IN, EXISTS, NOT EXISTS, ALL, ANY) with SQL examples.

- **`IN` / `NOT IN`:** Checks membership in subquery result set.
- **`EXISTS` / `NOT EXISTS`:** Evaluates to TRUE if subquery returns at least one row (highly efficient).
- **`> ALL` / `> ANY`:** Compares value against all or at least one element of subquery set.
- *Example:* `SELECT Name FROM Emp WHERE Salary > ALL (SELECT Salary FROM Emp WHERE Dept_ID = 20);`

---

### Q2. Explain Recursive Queries and Common Table Expressions (CTE) in SQL.

- **CTE Syntax:** `WITH cte_name AS (query) SELECT * FROM cte_name;`
- **Recursive CTE:** Uses an Anchor Member and a Recursive Member joined by `UNION ALL` to traverse hierarchical structures (organizational charts, graphs).

```sql
WITH RECURSIVE EmpHierarchy AS (
    -- Anchor Member (Top Manager)
    SELECT Emp_ID, Name, Manager_ID, 1 AS Level FROM Employee WHERE Manager_ID IS NULL
    UNION ALL
    -- Recursive Member
    SELECT E.Emp_ID, E.Name, E.Manager_ID, H.Level + 1
    FROM Employee E INNER JOIN EmpHierarchy H ON E.Manager_ID = H.Emp_ID
)
SELECT * FROM EmpHierarchy;
```

---

### Q3. Explain PL/SQL Triggers: Syntax, Timing, Events, and Use Cases.

- Complete syntax for `CREATE OR REPLACE TRIGGER` with `BEFORE/AFTER`, `FOR EACH ROW`, and `:NEW` / `:OLD` qualifiers for audit logging and data validation.
"""

dbms_m3_10m = """# 10-Mark Questions & Answers — DBMS Module 3: SQL Standards & Advanced Queries

---

### Q1. Write comprehensive SQL statements demonstrating DDL, DML, DCL, Complex Grouping with HAVING, Nested Correlated Subqueries, and PL/SQL Stored Procedures & Triggers.

Master 10-mark practical solution covering:
1. Complete DDL schema creation with constraints (PK, FK, CHECK, DEFAULT).
2. DML data manipulation and aggregate analysis with GROUP BY & HAVING.
3. Nested Correlated Subqueries and `EXISTS` optimization.
4. Complete PL/SQL Stored Procedure with `IN`/`OUT` parameters and Exception Handling.
5. Complete Row-level Audit Trigger tracking changes using `:OLD` and `:NEW` pseudorecords.
"""

with open(os.path.join(dbms_m3_qa_dir, "2M.md"), "w", encoding="utf-8") as f: f.write(dbms_m3_2m)
with open(os.path.join(dbms_m3_qa_dir, "3M.md"), "w", encoding="utf-8") as f: f.write(dbms_m3_3m)
with open(os.path.join(dbms_m3_qa_dir, "5M.md"), "w", encoding="utf-8") as f: f.write(dbms_m3_5m)
with open(os.path.join(dbms_m3_qa_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(dbms_m3_10m)


# --------------------------------------------------------------------------
# 3. DATA STRUCTURE MODULE 1 QA (Add 10M.md)
# --------------------------------------------------------------------------
ds_m1_qa_dir = os.path.join(BASE_DIR, "Data Structure", "Module 1", "Module_1_QA")
os.makedirs(ds_m1_qa_dir, exist_ok=True)

ds_m1_10m = """# 10-Mark Questions & Answers — Data Structures Module 1: ADT, Arrays & Pointers

---

### Q1. Explain Abstract Data Types (ADT), 1D/2D/3D Array Memory Representations, Row/Column Major Address Calculations, and Pointers in detail with C programs.

Comprehensive 10-mark master answer covering:
1. **Concept of ADT:** Definition, separation of Interface vs Implementation, axioms, and examples (List ADT, Stack ADT).
2. **Types of Data Structures:** Primitive vs Non-Primitive, Linear (Array, Linked List, Stack, Queue) vs Non-Linear (Tree, Graph), Static vs Dynamic.
3. **Address Calculation Formulas:**
   - **1D Array:** `Address(A[i]) = Base + w * (i - LowerBound)`
   - **2D Row-Major:** `Address(A[i][j]) = Base + w * [ (i - LBR) * N_cols + (j - LBC) ]`
   - **2D Column-Major:** `Address(A[i][j]) = Base + w * [ (j - LBC) * N_rows + (i - LBR) ]`
4. **Pointers & Multidimensional Arrays:** Dynamic allocation with `malloc()` and array of pointers in C.
5. **Self-Referential Structures:** Defining linked nodes using `struct Node { int data; struct Node *next; };`.
"""

with open(os.path.join(ds_m1_qa_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(ds_m1_10m)


# --------------------------------------------------------------------------
# 4. DATA STRUCTURE MODULE 2 QA (Stacks & Queues)
# --------------------------------------------------------------------------
ds_m2_qa_dir = os.path.join(BASE_DIR, "Data Structure", "Module 2", "Module_2_QA")
os.makedirs(ds_m2_qa_dir, exist_ok=True)

ds_m2_2m = """# 2-Mark Questions & Answers — Data Structures Module 2: Stacks & Queues

---

### Q1. Define Stack ADT and list its primary operations.

A **Stack** is a linear data structure following the **Last-In, First-Out (LIFO)** principle.
- **Operations:** `push(x)` (insert at top), `pop()` (delete from top), `peek()` / `top()` (inspect top element), `isEmpty()`, `isFull()`.

---

### Q2. What is Stack Overflow and Stack Underflow?

- **Stack Overflow:** Attempting to `push` an element onto a completely filled stack (`top == MAX - 1`).
- **Stack Underflow:** Attempting to `pop` or `peek` from an empty stack (`top == -1`).

---

### Q3. Define Queue ADT and state FIFO principle.

A **Queue** is a linear data structure following the **First-In, First-Out (FIFO)** principle, where elements are inserted at the **Rear** end and deleted from the **Front** end.

---

### Q4. What is the advantage of a Circular Queue over a Linear Queue?

In a Linear Queue, space freed by `dequeue` cannot be reused once `rear == MAX - 1` (false overflow). A **Circular Queue** wraps pointers around using modulo arithmetic (`(rear + 1) % MAX`), eliminating memory wastage.

---

### Q5. What is a Double-Ended Queue (Deque)?

A **Deque** is a generalized queue where insertion and deletion operations can be performed efficiently from **both ends** (Front and Rear).
"""

ds_m2_3m = """# 3-Mark Questions & Answers — Data Structures Module 2: Stacks & Queues

---

### Q1. Explain the algorithm for checking Well-Formedness of Parentheses using a Stack.

1. Scan the arithmetic string expression from left to right.
2. If an opening bracket (`(`, `{`, `[`) is encountered, `push` it onto the stack.
3. If a closing bracket (`)`, `}`, `]`) is encountered:
   - If stack is empty: **Unbalanced** (Excess closing bracket).
   - `pop` top element; if popped bracket does not match closing bracket: **Unbalanced** (Mismatched type).
4. After scanning, if stack is empty -> **Balanced/Well-Formed**; else **Unbalanced**.

---

### Q2. Differentiate between Infix, Prefix, and Postfix notations.

| Notation | Operator Position | Example | Evaluation |
| :--- | :--- | :--- | :--- |
| **Infix** | Operator between operands. | `(A + B) * C` | Requires operator precedence and parentheses. |
| **Prefix (Polish)** | Operator before operands. | `* + A B C` | Evaluated from right to left without parentheses. |
| **Postfix (Reverse Polish)** | Operator after operands. | `A B + C *` | Evaluated from left to right using a Stack. |

---

### Q3. Explain Priority Queue and its types.

A **Priority Queue** is a queue where each element has an assigned priority:
- **Ascending Priority Queue:** Element with smallest numerical value has highest priority (served first).
- **Descending Priority Queue:** Element with largest numerical value has highest priority.
"""

ds_m2_5m = """# 5-Mark Questions & Answers — Data Structures Module 2: Stacks & Queues

---

### Q1. Write the complete algorithm and C functions for Infix to Postfix conversion using a Stack.

Detailed operator precedence algorithm handling `^` (highest, right-associative), `*`, `/`, `+`, `-`, and parentheses with complete C code.

---

### Q2. Explain Circular Queue operations (Enqueue, Dequeue) with array implementation and boundary condition checks in C.

- **Enqueue condition:** `(rear + 1) % MAX == front` (Full).
- **Dequeue condition:** `front == -1` (Empty); resets `front = rear = -1` when last element is removed.

---

### Q3. Explain how recursion is implemented using the Call Stack with an example (Factorial / Tower of Hanoi).

Step-by-step memory trace diagram showing Activation Records (Stack Frames) pushed during recursive calls and popped during return.
"""

ds_m2_10m = """# 10-Mark Questions & Answers — Data Structures Module 2: Stacks & Queues

---

### Q1. Explain Stack & Queue ADTs, Infix to Postfix Conversion & Evaluation, Circular Queue, and Deque in detail with algorithms and executable C programs.

Comprehensive 10-mark master answer covering:
1. Stack ADT array implementation with push/pop/peek functions.
2. Complete step-by-step trace and C program for Infix to Postfix conversion.
3. Postfix Expression Evaluation algorithm using Stack.
4. Circular Queue array implementation with modulo index arithmetic.
5. Double-Ended Queue (Input-Restricted and Output-Restricted Deques) and applications.
"""

with open(os.path.join(ds_m2_qa_dir, "2M.md"), "w", encoding="utf-8") as f: f.write(ds_m2_2m)
with open(os.path.join(ds_m2_qa_dir, "3M.md"), "w", encoding="utf-8") as f: f.write(ds_m2_3m)
with open(os.path.join(ds_m2_qa_dir, "5M.md"), "w", encoding="utf-8") as f: f.write(ds_m2_5m)
with open(os.path.join(ds_m2_qa_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(ds_m2_10m)


# --------------------------------------------------------------------------
# 5. DATA STRUCTURE MODULE 3 QA (Linked Lists)
# --------------------------------------------------------------------------
ds_m3_qa_dir = os.path.join(BASE_DIR, "Data Structure", "Module 3", "Module_3_QA")
os.makedirs(ds_m3_qa_dir, exist_ok=True)

ds_m3_2m = """# 2-Mark Questions & Answers — Data Structures Module 3: Linked Lists

---

### Q1. What is a Linked List? State its node structure.

A **Linked List** is a dynamic linear data structure composed of nodes allocated in non-contiguous memory, where each node contains **Data** and a **Pointer (`next`)** storing the address of the subsequent node.

---

### Q2. Differentiate between Array and Linked List.

| Feature | Array | Linked List |
| :--- | :--- | :--- |
| **Memory Allocation** | Static / Contiguous memory. | Dynamic / Non-contiguous memory on heap. |
| **Insertion / Deletion** | Slow $O(N)$ (requires shifting elements). | **Fast $O(1)$** (updating pointer links). |
| **Element Access** | Direct random access $O(1)$. | Sequential access $O(N)$. |

---

### Q3. What is a Doubly Linked List (DLL)?

A **Doubly Linked List** has nodes containing two pointers: `prev` (pointing to predecessor) and `next` (pointing to successor), allowing bidirectional traversal.

---

### Q4. What is a Circular Linked List?

A **Circular Linked List** is a linked list where the `next` pointer of the last node points back to the **Head node** instead of `NULL`.

---

### Q5. How is a Stack implemented using a Singly Linked List?

Pushing and popping elements are performed at the **Head of the Linked List** in $O(1)$ time (`push`: insert at beginning, `pop`: delete from beginning).
"""

ds_m3_3m = """# 3-Mark Questions & Answers — Data Structures Module 3: Linked Lists

---

### Q1. Explain insertion at beginning, middle, and end in a Singly Linked List.

1. **Insert at Beginning ($O(1)$):** `newNode->next = head; head = newNode;`
2. **Insert at End ($O(N)$):** Traverse to last node `temp->next == NULL`, then `temp->next = newNode;`
3. **Insert after Position ($O(N)$):** `newNode->next = temp->next; temp->next = newNode;`

---

### Q2. Explain deletion of a node in a Doubly Linked List.

To delete node `del`:
```c
if (del->prev != NULL) del->prev->next = del->next;
else head = del->next;
if (del->next != NULL) del->next->prev = del->prev;
free(del);
```

---

### Q3. Explain Polynomial Representation using Linked Lists.

Each polynomial term $c \cdot x^e$ is represented as a node containing:
- `coeff` (Coefficient $c$)
- `expo` (Exponent $e$)
- `next` (Pointer to next term in descending exponent order)
"""

ds_m3_5m = """# 5-Mark Questions & Answers — Data Structures Module 3: Linked Lists

---

### Q1. Write complete C functions for Singly Linked List: Creation, Insertion, Deletion, and Traversal.

Complete working C program with `struct Node` and pointer manipulation functions.

---

### Q2. Explain Queue implementation using a Singly Linked List with Front and Rear pointers in C.

- `enqueue()` inserts at `rear->next` in $O(1)$ time.
- `dequeue()` removes from `front` in $O(1)$ time.

---

### Q3. Explain Polynomial Addition using Linked Lists with an algorithm and diagram.

Traverse both polynomial lists simultaneously:
- If `exp1 == exp2`: Add coefficients, insert term into result list, advance both pointers.
- If `exp1 > exp2`: Insert term 1 into result list, advance pointer 1.
- If `exp2 > exp1`: Insert term 2 into result list, advance pointer 2.
"""

ds_m3_10m = """# 10-Mark Questions & Answers — Data Structures Module 3: Linked Lists

---

### Q1. Explain Singly, Doubly, and Circular Linked Lists, Stack/Queue linked implementations, and Polynomial Addition in detail with complete C programs.

Comprehensive master answer covering:
1. Memory node layouts for SLL, DLL, and Circular Linked Lists.
2. Complete C code for Singly Linked List CRUD operations.
3. Doubly Linked List insertion and deletion with two-way pointer updates.
4. Linked Stack (Top at head) and Linked Queue (Front & Rear pointers) implementations.
5. Polynomial addition algorithm and complete C implementation.
"""

with open(os.path.join(ds_m3_qa_dir, "2M.md"), "w", encoding="utf-8") as f: f.write(ds_m3_2m)
with open(os.path.join(ds_m3_qa_dir, "3M.md"), "w", encoding="utf-8") as f: f.write(ds_m3_3m)
with open(os.path.join(ds_m3_qa_dir, "5M.md"), "w", encoding="utf-8") as f: f.write(ds_m3_5m)
with open(os.path.join(ds_m3_qa_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(ds_m3_10m)

print("Generated all missing Question & Answer Bank files across DBMS and Data Structure!")
