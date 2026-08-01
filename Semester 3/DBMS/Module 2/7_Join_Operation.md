# Topic: Join Operation

**Q. Explain the Join operation in Relational Algebra. Describe the different types of Joins including Theta Join, Equi Join, Natural Join, and the Outer Joins.**

---

> 📌 **Definition to Remember**
> A **Join Operation** (⋈) combines related tuples from two relations into a single relation based on a common condition. It is fundamentally a **Cartesian Product followed by a Selection** (σ). Joins are the most important and frequently used operations in normalized relational databases.

---

# Join Operations (⋈)
*(Return only rows with a matching counterpart in both tables)*

#### A. Theta Join (⋈_{θ})
* Joins two relations where tuples satisfy a condition θ (can use **any** comparison operator: =, <, >, ≠).
* **Syntax:** A ⋈_{θ} B

#### B. Equi Join
* A **special case of Theta Join** where θ uses **only equality (=)**.
* The joining attribute appears **twice** in the output (once from each table).

#### C. Natural Join (⋈)
* An **enhanced Equi Join** that automatically joins on all attributes with the **exact same name** in both tables.
* The duplicate joining column is **automatically removed** — it appears only once.

### 2. Types of Outer Joins
*(Preserve unmatched rows — missing values are filled with NULL)*

```
  STUDENT              ENROLLMENT
  ┌───────────┐        ┌───────────────┐
  │ Roll | Name│        │ Roll | Course │
  │  101 | John│───┐   │  101 | CS101  │
  │  102 | Emma│   └──►│  102 | MATH   │
  │  103 | Luke│        └───────────────┘
  └───────────┘         (Luke has no enrollment)
```

| Join Type | What is Returned |
| :--- | :--- |
| **Left Outer Join** | **All rows from LEFT** table + matched rows from Right. Unmatched right = NULL. |
| **Right Outer Join** | **All rows from RIGHT** table + matched rows from Left. Unmatched left = NULL. |
| **Full Outer Join** | **All rows from BOTH** tables. Unmatched sides = NULL. |

**Example (Left Outer Join):** STUDENT Left Join ENROLLMENT → Shows ALL students. Luke has no enrollment → his Course column = NULL.

### 3. Summary: All Join Types

| Join Type | Returns | Duplicates |
| :--- | :--- | :--- |
| **Theta Join** | Matching tuples (any condition) | Both join-columns kept |
| **Equi Join** | Matching tuples (= only) | Both join-columns kept |
| **Natural Join** | Matching tuples (same-named cols) | Duplicate column removed |
| **Left Outer** | All left + matched right | NULL for unmatched |
| **Right Outer** | All right + matched left | NULL for unmatched |
| **Full Outer** | All from both | NULL for unmatched |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Join = Cartesian Product + Selection; used to combine data from normalized tables.
> 2. **Theta Join**: general condition (any operator); **Equi Join**: equality (=) only.
> 3. **Natural Join**: automatic join on same-named columns; removes duplicate column.
> 4. Equi Join keeps the join column twice; Natural Join keeps it only once.
> 5. **Outer Joins** preserve unmatched rows — NULL is placed for missing data.
> 6. Left Outer: all rows from left; Right Outer: all rows from right; Full Outer: all from both.
> 7. Joins are essential for querying normalized databases where data is split across multiple tables.

---

> ⚡ **Quick Recall**
> `Join = Cross Product + Selection → Theta (any condition) → Equi (= only, duplicate col) → Natural (same name, no duplicate) → Left/Right/Full Outer (NULLs for unmatched)`

