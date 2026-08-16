# Second Normal Form (2NF) — Relational Database Design

> **Definition:** A relation is in **Second Normal Form (2NF)** if it is in **1NF** and **no non-prime attribute is partially dependent on any candidate key** of the relation. Every non-key attribute must be **fully functionally dependent** on the primary key.

---

## 1. Detailed Technical Explanation

### Functional Dependency Concepts:
- **Full Functional Dependency:** X -> Y is a full functional dependency if removal of any attribute A from X means the dependency no longer holds.
- **Partial Dependency:** Occurs when a non-prime attribute depends on only a *proper subset* of a composite primary key.

### Conversion Example: 1NF to 2NF

#### Relation R(Student_ID, Course_ID, Student_Name, Course_Fee)
- **Candidate Key:** {Student_ID, Course_ID}
- **Functional Dependencies:**
  1. {Student_ID, Course_ID} -> Student_Name, Course_Fee
  2. Student_ID -> Student_Name *(Partial Dependency: Student_Name depends only on part of key)*
  3. Course_ID -> Course_Fee *(Partial Dependency: Course_Fee depends only on part of key)*

#### Decomposition into 2NF:
We split table R into 3 normalized tables:

1. **STUDENT (Student_ID, Student_Name)**
   - Primary Key: `Student_ID`
2. **COURSE (Course_ID, Course_Fee)**
   - Primary Key: `Course_ID`
3. **ENROLLMENT (Student_ID, Course_ID)**
   - Primary Key: `{Student_ID, Course_ID}`
   - Foreign Keys: `Student_ID` refs STUDENT, `Course_ID` refs COURSE

---

## 2. Core Concepts & Memory Keywords
- **Non-prime Attribute:** An attribute that is not part of any candidate key.
- **Prime Attribute:** An attribute that belongs to at least one candidate key.
- **Partial Dependency Removal:** Splitting composite key attributes into separate lookup tables.

---

## 3. Must-Write Points for Exams
- 2NF is only relevant when the relation has a **composite candidate key** (candidate key containing 2 or more attributes).
- Relations with a single-attribute primary key in 1NF are **automatically in 2NF**.
- 2NF eliminates **update anomalies** caused by repeating non-key attribute values.

---

## 4. Quick Recall Flow
```
1NF Relation -> Identify Partial Dependencies (Non-Prime -> Part of Key) -> Decompose Tables -> 2NF Achieved
```
