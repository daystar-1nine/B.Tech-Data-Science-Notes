# Relationship Types and Relationship Sets

**Q. Explain the concepts of Relationship Types and Relationship Sets. Discuss the Degree of Relationship and Mapping Cardinalities (1:1, 1:N, M:N) with examples.**

---

> 📌 **Definition to Remember**
> A **Relationship Type** defines a meaningful association between two or more entity types, represented by a **Diamond** in ER diagrams. A **Relationship Set** is the actual collection of specific relationship instances existing in the database at any given moment.

---

### 1. Relationship Type and Relationship Set

* **Relationship Type:** Association between entity types. E.g., `WORKS_FOR` links `EMPLOYEE` and `DEPARTMENT`.
* **Relationship Set:** All specific instances of that relationship. E.g., "John works for IT Dept." is one instance.

### 2. Degree of Relationship

The **Degree** = number of entity types participating in the relationship.

| Degree | Name | Example |
| :--- | :--- | :--- |
| 1 | **Unary** | Employee `Manages` another Employee |
| 2 | **Binary** | Student `Enrolls_In` Course (most common) |
| 3 | **Ternary** | Doctor, Patient, Drug connected by `Prescribes` |

### 3. Mapping Cardinalities

**Mapping Cardinality** defines the maximum number of relationship instances an entity can participate in.

#### 1. One-to-One (1:1)
* One entity in A associates with **at most one** in B, and vice versa.
* **Example:** One `MANAGER` manages one `DEPARTMENT`; one `DEPARTMENT` has one `MANAGER`.

#### 2. One-to-Many (1:N)
* One entity in A associates with **multiple** entities in B; but each B associates with **one** A.
* **Example:** One `DEPARTMENT` has many `EMPLOYEE`s; each `EMPLOYEE` belongs to one `DEPARTMENT`.

#### 3. Many-to-One (N:1)
* Multiple entities in A associate with **one** entity in B.
* **Example:** Many `STUDENT`s belong to one `COURSE`.

#### 4. Many-to-Many (M:N)
* Entities in A can associate with **multiple** in B, and vice versa.
* **Example:** A `STUDENT` enrolls in many `COURSE`s; a `COURSE` has many `STUDENT`s.

```
  1:1  →  A ──── <R> ──── B
  1:N  →  A ════ <R> ──── B
  M:N  →  A ══════<R>════ B
```

### 4. Participation Constraints

| Type | Description | ER Symbol |
| :--- | :--- | :--- |
| **Total Participation** | Every entity in the set MUST participate | Double Line (══) |
| **Partial Participation** | Entity may or may not participate | Single Line (──) |

* **Total Example:** Every `EMPLOYEE` must belong to a `DEPARTMENT`.
* **Partial Example:** A `STUDENT` may or may not live in a `HOSTEL`.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Relationship Type = association between entity types (Diamond); Relationship Set = collection of all instances.
> 2. Degree: Unary (1), Binary (2 — most common), Ternary (3).
> 3. Mapping Cardinalities: 1:1, 1:N, N:1, M:N — define how many entities can participate.
> 4. 1:1: one entity maps to exactly one (e.g., Manager → Department).
> 5. 1:N: one on one side, many on the other (e.g., Department → Employees).
> 6. M:N: many on both sides — requires a Junction Table in the relational model.
> 7. Total Participation (double line): every entity MUST participate; Partial (single line): optional.

---

> ⚡ **Quick Recall**
> `Relationship Type (Diamond) → Degree (Unary/Binary/Ternary) → Cardinality (1:1, 1:N, M:N) → Participation (Total=double line, Partial=single line)`
