# Decomposition Using Multivalued Attribute (4NF) — DBMS

> **Definition:** A relation is in **Fourth Normal Form (4NF)** if it is in **BCNF** and for every non-trivial **Multivalued Dependency (MVD) X ->-> Y**, **X is a Super Key**.

---

## 1. Detailed Technical Explanation

### Multivalued Dependency (MVD):
A multivalued dependency **X 	woheadrightarrow Y** (read as "X multidetermines Y") exists in schema R if the presence of a pair of tuples **(t_1, t_2)** with **t_1[X] = t_2[X]** implies that there must also exist tuples **t_3** and **t_4** combining **X**, **Y**, and the remaining attributes **Z = R - (X \cup Y)**.

```
MVD Symbol: X ->-> Y (X independent multidetermines Y)
```

### Example: 4NF Decomposition

#### Relation STUDENT_INFO(Student_ID, Mobile_No, Skill)
- A student can have multiple mobile numbers AND multiple independent skills.
- **Multivalued Dependencies:**
  1. Student_ID ->-> Mobile_No
  2. Student_ID ->-> Skill

#### Data Tuple Redundancy (UNF/BCNF Violation):
| Student_ID | Mobile_No | Skill |
| :--- | :--- | :--- |
| 101 | 9876543210 | Java |
| 101 | 9876543210 | Python |
| 101 | 9123456789 | Java |
| 101 | 9123456789 | Python |

*(Note: Adding 1 new skill for student 101 requires inserting 2 new rows because Mobile_No and Skill are independent!)*

#### 4NF Decomposition Algorithm:
If **X 	woheadrightarrow Y** violates 4NF in R, decompose R into:
1. **R_1 = X \cup Y**
2. **R_2 = R - Y**

#### Decomposed 4NF Tables:
1. **STUDENT_MOBILE (Student_ID, Mobile_No)**
2. **STUDENT_SKILL (Student_ID, Skill)**

---

## 2. Core Concepts & Memory Keywords
- **Multivalued Dependency (MVD):** Independence between two multi-valued attributes associated with the same key.
- **Spurious Combinations:** Combinatorial explosion of duplicate tuples caused by MVDs.
- **4NF Condition:** Every non-trivial MVD **X 	woheadrightarrow Y** must have **X** as a super key.

---

## 3. Must-Write Points for Exams
- 4NF handles independent multi-valued attributes that BCNF cannot resolve.
- MVDs occur when two independent 1-to-many relationships are combined in a single relation.
- Decomposing MVDs into separate 2-column tables eliminates combinatorial row insertion anomalies.

---

## 4. Quick Recall Flow
```
BCNF Table -> Identify Independent Multi-Valued Attributes (X ->-> Y) -> Split into R1(X, Y) & R2(X, Z) -> 4NF Achieved
```
