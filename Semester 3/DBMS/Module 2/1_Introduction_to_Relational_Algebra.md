# Topic: Introduction to Relational Algebra

**Q. What is Relational Algebra in DBMS? Explain its basic concepts and categorize the primary relational algebra operators.**

---

> 📌 **Definition to Remember**
> **Relational Algebra** is a **procedural query language** that forms the theoretical foundation of SQL. It specifies both *what* data is needed and *how* to retrieve it through a sequence of operations on relations (tables), where every operation takes one or two relations as input and produces a new relation as output.

---

### 1. Basic Concepts

| Concept | Explanation |
| :--- | :--- |
| **Input/Output** | Every operation takes 1 or 2 **relations (tables)** as input and produces a **new relation** as output. |
| **Closure Property** | Since output is always a relation, operations can be **nested and chained** in sequence. |
| **No Side Effects** | Operations only **query** data — they never modify, insert, or delete from the original tables. |

### 2. Relational Algebra Operators

#### A. Basic (Fundamental) Operators
*(All other operators can be derived from these)*

| Operator | Symbol | Description |
| :--- | :--- | :--- |
| **Selection** | σ | Extracts specific **rows** satisfying a condition |
| **Projection** | π | Extracts specific **columns**, discarding others |
| **Union** | ∪ | Combines rows from two relations, removes duplicates |
| **Set Difference** | - | Rows in first relation NOT in the second |
| **Cartesian Product** | × | Combines every row of A with every row of B |
| **Rename** | ρ | Renames a relation or its attributes |

#### B. Derived Operators
*(Combinations of basic operators for convenience)*

| Operator | Symbol | Description |
| :--- | :--- | :--- |
| **Intersection** | ∩ | Rows present in **both** relations (derived from -) |
| **Join** | ⋈ | Combines related tuples from two relations (Cartesian × Selection) |
| **Division** | ÷ | Answers "for all" queries (e.g., students who took **all** courses) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Relational Algebra is a procedural query language — the mathematical foundation of SQL.
> 2. Every operation takes 1 or 2 relations as input and always outputs a new relation (**Closure Property**).
> 3. Operations do not modify the original tables — they are read-only.
> 4. Basic operators: Selection (σ), Projection (π), Union (∪), Set Difference (−), Cartesian Product (×), Rename (ρ).
> 5. Derived operators: Intersection (∩), Join (⋈), Division (÷).
> 6. Derived operators can be expressed using combinations of basic operators.
> 7. Understanding Relational Algebra helps understand how the DBMS engine executes and optimizes SQL queries.

---

> ⚡ **Quick Recall**
> `Procedural Language → Closure Property → Basic (σ, π, ∪, −, ×, ρ) → Derived (∩, ⋈, ÷) → Foundation of SQL`

