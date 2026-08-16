# Boyce-Codd Normal Form (BCNF) — Relational Database Design

> **Definition:** A relation is in **Boyce-Codd Normal Form (BCNF)** (also known as 3.5NF) if and only if for **every non-trivial functional dependency X -> Y, X is a strict Super Key**.

---

## 1. Detailed Technical Explanation

BCNF is a stricter version of 3NF that handles cases where a relation has **multiple overlapping candidate keys**.

### 3NF vs BCNF Comparison:

| Property | 3NF | BCNF |
| :--- | :--- | :--- |
| **Allowed Condition X -> Y** | X is Super Key **OR** Y is Prime Attribute | X MUST be a Super Key (No exceptions!) |
| **Dependency Preservation** | Always Guaranteed | Not always guaranteed |
| **Redundancy** | Allows minor non-key redundancy | Completely eliminates functional redundancy |

### Conversion Example to BCNF

#### Relation ADVISOR(Student_ID, Subject, Advisor_Name)
- **Assumptions:**
  1. A student can choose multiple subjects.
  2. For each subject, a student is assigned one advisor.
  3. Each advisor advises only ONE subject.
- **Candidate Keys:** `{Student_ID, Subject}` and `{Student_ID, Advisor_Name}`
- **Functional Dependencies:**
  1. {Student_ID, Subject} -> Advisor_Name
  2. Advisor_Name -> Subject *(Violation! Advisor_Name determines Subject, but Advisor_Name is NOT a super key)*

#### Relation Status:
- Is it 3NF? **YES**, because Subject is a prime attribute.
- Is it BCNF? **NO**, because in `Advisor_Name -> Subject`, `Advisor_Name` is NOT a super key.

#### BCNF Decomposition:
1. **ADVISOR_SUBJECT (Advisor_Name, Subject)**
   - Primary Key: `Advisor_Name`
2. **STUDENT_ADVISOR (Student_ID, Advisor_Name)**
   - Primary Key: `{Student_ID, Advisor_Name}`

---

## 2. Core Concepts & Memory Keywords
- **Strict Super Key Rule:** Every determinant in a functional dependency must be a super key.
- **Overlapping Candidate Keys:** Candidate keys sharing common attributes.
- **3.5 Normal Form:** Stronger normalization standard than 3NF.

---

## 3. Must-Write Points for Exams
- BCNF eliminates all redundancy resulting from functional dependencies.
- Every relation in BCNF is guaranteed to be in 3NF, 2NF, and 1NF.
- Decomposing a 3NF relation into BCNF may sometimes sacrifice **dependency preservation**.

---

## 4. Quick Recall Flow
```
3NF Relation -> Inspect all FDs (X -> Y) -> Verify if X is Super Key -> Decompose non-superkey determinants -> BCNF Achieved
```
