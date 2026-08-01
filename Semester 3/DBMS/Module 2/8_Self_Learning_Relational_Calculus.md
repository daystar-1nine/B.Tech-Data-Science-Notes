# Topic: Relational Calculus — Self-Learning

**Q. What is Relational Calculus? Differentiate between Tuple Relational Calculus (TRC) and Domain Relational Calculus (DRC), and compare Relational Calculus with Relational Algebra.**

---

> 📌 **Definition to Remember**
> **Relational Calculus** is a **non-procedural (declarative)** query language where the user specifies *what* data is needed without specifying *how* to retrieve it. It is based on **mathematical predicate logic** and comes in two forms: **Tuple Relational Calculus (TRC)** and **Domain Relational Calculus (DRC)**.

---

# Relational Calculus (Self-Learning)

#### A. Tuple Relational Calculus (TRC)
* Variables range over **entire tuples (rows)**.
* **Syntax:** \{ T \mid P(T) \}
  * T = resulting tuple variable
  * P(T) = predicate (condition) that the tuple must satisfy
* **Read as:** "Find all tuples T such that P(T) is true."
* **Example:** Find names of employees in the IT department:
  $\{ T.Name \mid Employee(T) AND T.Department = 'IT' \}$

#### B. Domain Relational Calculus (DRC)
* Variables range over **individual attribute values (domains)** — not whole tuples.
* **Syntax:** \{ <x_1, x_2, ..., x_n> \mid P(x_1, x_2, ..., x_n) \}
  * <x_1, x_2...> = domain variables (individual column values)
  * P = condition on those variables
* **Example:** Find names of IT employees:
  $\{ <Name> \mid ∃ ID, Salary (<ID, Name, 'IT', Salary> ∈ Employee) \}$

### 2. Relational Algebra vs Relational Calculus

| Feature | Relational Algebra | Relational Calculus |
| :--- | :--- | :--- |
| **Nature** | **Procedural** | **Non-Procedural (Declarative)** |
| **Specifies** | *What* AND *How* to retrieve | *What* to retrieve only |
| **Foundation** | Mathematical **Set Theory** | Mathematical **Predicate Logic** |
| **Variables** | Operators on Relations | Tuple variables (TRC) or Domain variables (DRC) |
| **Execution Order** | Order of operations matters | DBMS optimizer determines execution |
| **SQL Equivalent** | Maps to query execution plans | Maps to SQL query syntax |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Relational Calculus is **non-procedural** — specifies *what* to retrieve, not *how*.
> 2. Based on **mathematical predicate logic** (unlike Algebra, which is based on Set Theory).
> 3. Two types: **TRC** (variables = whole tuples) and **DRC** (variables = individual attribute values).
> 4. TRC syntax: \{T \mid P(T)\} — find all tuples T where predicate P(T) is true.
> 5. DRC syntax: \{<x_1, x_2...> \mid P(x_1, x_2...)\} — find specific domain values satisfying P.
> 6. Relational Algebra is procedural; Relational Calculus is declarative (like SQL).
> 7. Both are **relationally complete** — anything expressible in one can be expressed in the other.

---

> ⚡ **Quick Recall**
> `Relational Calculus → Declarative (What, not How) → Predicate Logic → TRC (tuple variables) → DRC (domain/attribute variables) → Foundation of SQL`

