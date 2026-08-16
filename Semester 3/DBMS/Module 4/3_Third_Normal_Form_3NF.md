# Third Normal Form (3NF) — Relational Database Design

> **Definition:** A relation is in **Third Normal Form (3NF)** if it is in **2NF** and **no non-prime attribute is transitively dependent on the primary key**. For every non-trivial functional dependency X -> Y, either **X is a super key** or **Y is a prime attribute**.

---

## 1. Detailed Technical Explanation

### Transitive Dependency Concept:
A transitive dependency exists if A -> B and B -> C hold, which implies A -> C through non-key attribute B.

```
[ Primary Key A ] -------------> [ Non-Prime Attribute B ]
                                            |
                                            v
                                 [ Non-Prime Attribute C ]
                                 (Transitive Dependency!)
```

### Conversion Example: 2NF to 3NF

#### Relation EMP_DEPT(Emp_ID, Emp_Name, Dept_ID, Dept_Name, Dept_Head)
- **Candidate Key:** `Emp_ID`
- **Functional Dependencies:**
  1. Emp_ID -> Emp_Name, Dept_ID
  2. Dept_ID -> Dept_Name, Dept_Head *(Transitive Dependency: Dept_ID is not a super key, Dept_Name is non-prime)*

#### Decomposition into 3NF:
We decompose EMP_DEPT into 2 distinct tables:

1. **EMPLOYEE (Emp_ID, Emp_Name, Dept_ID)**
   - Primary Key: `Emp_ID`
   - Foreign Key: `Dept_ID`
2. **DEPARTMENT (Dept_ID, Dept_Name, Dept_Head)**
   - Primary Key: `Dept_ID`

---

## 2. Core Concepts & Memory Keywords
- **Transitive Dependency:** Non-key attribute determining another non-key attribute.
- **3NF Formal Condition:** For all X -> Y:
  1. X -> Y is trivial (Y ⊆ X), OR
  2. X is a Super Key, OR
  3. Y is a Prime Attribute (part of a candidate key).

---

## 3. Must-Write Points for Exams
- 3NF guarantees **lossless-join decomposition** and **dependency preservation**.
- 3NF removes insertion and deletion anomalies associated with transitive attribute relationships.
- Most practical commercial enterprise databases are normalized up to 3NF.

---

## 4. Quick Recall Flow
```
2NF Relation -> Check X -> Y -> Ensure X is Super Key OR Y is Prime -> Remove Transitive Dependencies -> 3NF Achieved
```
