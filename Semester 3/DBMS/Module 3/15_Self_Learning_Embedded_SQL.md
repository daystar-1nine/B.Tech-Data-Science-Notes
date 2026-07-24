# Topic: Embedded SQL — Self-Learning

**Q. What is Embedded SQL? Discuss how SQL statements interact with host programming languages using Host Variables and Cursors. Differentiate between Static and Dynamic SQL.**

---

> 📌 **Definition to Remember**
> **Embedded SQL** is a technique where SQL statements are **inserted directly into the source code** of a general-purpose host programming language (C, C++, Java, COBOL). It bridges the gap between application logic and database interaction. A **pre-compiler** processes the embedded SQL before the host language compiler.

---

### 1. Why Embedded SQL?
SQL alone lacks general-purpose constructs (UI, file I/O, loops, networking). Embedding SQL in a host language allows full-featured applications to interact with databases.

### 2. Key Mechanisms

#### A. Host Variables
Variables declared in the host language (e.g., C), prefixed with a **colon (`:`)** when used inside SQL statements.
* **Purpose:** Bridge data between the application and the SQL query (input AND output).
```c
int emp_id = 101;
EXEC SQL DELETE FROM Employee WHERE ID = :emp_id;
```

#### B. Cursors
A standard SQL `SELECT` returns many rows at once, but a host variable holds only one value. A **Cursor** solves this mismatch.
* Acts as a **row-by-row pointer** over a multi-row result set.
* Steps:

```
  ① DECLARE cursor   → Define the cursor + SELECT query
  ② OPEN cursor      → Execute the query
  ③ FETCH (in loop)  → Retrieve one row at a time into host variables
  ④ CLOSE cursor     → Release resources
```

### 3. Static SQL vs Dynamic SQL

| Feature | Static SQL | Dynamic SQL |
| :--- | :--- | :--- |
| **SQL text known at** | **Compile time** (hard-coded) | **Runtime** (built as strings) |
| **Pre-compilation** | Yes — validated and optimized before execution | No — compiled at execution time |
| **Performance** | **Faster** (pre-optimized plan) | **Slower** (compiled on-the-fly) |
| **Security** | **Very Secure** (immune to SQL Injection) | **Risky** (vulnerable to SQL Injection if input is unsanitized) |
| **Flexibility** | Low — cannot adapt SQL at runtime | **High** — can build any query dynamically |
| **Use Case** | Standard reports, fixed operations | User-driven search screens, flexible queries |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Embedded SQL = SQL statements inserted directly into a host language (C, Java, COBOL).
> 2. A **pre-compiler** processes embedded SQL before the host language compiler runs.
> 3. **Host Variables** (prefixed with `:`) bridge data between the app and SQL.
> 4. **Cursors** handle multi-row result sets row by row: DECLARE → OPEN → FETCH → CLOSE.
> 5. **Static SQL**: hard-coded at compile time; pre-optimized, secure, fast, inflexible.
> 6. **Dynamic SQL**: built at runtime; flexible, but slower and vulnerable to SQL Injection.
> 7. Static SQL is preferred for security; Dynamic SQL is used when query structure must change.

---

> ⚡ **Quick Recall**
> `Embedded SQL → Host Language + SQL → Host Variables (:prefix, bridges data) → Cursors (row-by-row: DECLARE→OPEN→FETCH→CLOSE) → Static (compile-time, fast, secure) → Dynamic (runtime, flexible, injection risk)`
