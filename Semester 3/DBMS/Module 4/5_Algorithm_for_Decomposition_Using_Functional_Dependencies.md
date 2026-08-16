# Algorithm for Decomposition Using Functional Dependencies — DBMS

> **Definition: Decomposition Algorithms** split a complex relational schema R into smaller sub-schemas (R1, R2, ..., Rn) to eliminate anomalies while preserving **Lossless-Join** and **Functional Dependencies**.

---

## 1. Detailed Technical Explanation

### 1. Attribute Closure Algorithm (F+)
The closure of an attribute set X under F, denoted **X^+**, is the set of all attributes functionally determined by X.

#### Algorithm Steps:
```
Input: Set of attributes X, Set of FDs F
Output: X+ (Closure of X)

1. Set X+ = X
2. Repeat until no more attributes are added:
   For each FD (Y -> Z) in F:
     If Y ⊆ X+:
       X+ = X+ ∪ Z
3. Return X+
```

### 2. Lossless-Join Decomposition Testing
A decomposition of R into R1 and R2 is **lossless-join** with respect to F if and only if:
```
(R1 ∩ R2) -> R1   OR   (R1 ∩ R2) -> R2
```
*(Meaning: The common attributes between R1 and R2 must form a Super Key for at least one of the decomposed relations).*

### 3. 3NF Synthesis Algorithm (Lossless-Join & Dependency Preserving)
```
Input: Relation R, Set of FDs F
Output: 3NF Decomposition of R

1. Compute Minimal Cover Fc for F.
2. For each FD (X -> Y) in Fc:
   Create a schema Ri = X ∪ Y.
3. If no schema Ri contains a candidate key of R:
   Create an additional schema containing any candidate key of R.
4. Eliminate redundant schemas (if Ri ⊆ Rj, remove Ri).
```

---

## 2. Core Concepts & Memory Keywords
- **Minimal Cover (Canonical Cover):** A simplified set of FDs with single attributes on the right-hand side and no extraneous attributes.
- **Lossless Join:** Guarantees **R = R_1 owtie R_2** (no spurious tuples created upon joining).
- **Dependency Preservation:** Checks if **(F_1 \cup F_2 \cup ... \cup F_n)^+ = F^+**.

---

## 3. Must-Write Points for Exams
- Lossless join ensures that joining decomposed tables produces the exact original dataset without fake data.
- Dependency preservation allows database engines to enforce constraints without performing expensive table joins.
- 3NF synthesis algorithm guarantees both **lossless-join** and **dependency preservation** simultaneously.

---

## 4. Quick Recall Flow
```
Find Minimal Cover Fc -> Compute Attribute Closures X+ -> Test Lossless (R1 ∩ R2 -> R1) -> Preserve FDs -> 3NF Synthesis
```
