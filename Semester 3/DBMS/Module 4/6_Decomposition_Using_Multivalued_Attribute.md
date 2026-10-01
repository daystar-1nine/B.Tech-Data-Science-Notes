# Fourth Normal Form (4NF) & Multivalued Dependencies

**Q. Define Multivalued Dependency (MVD) and Fourth Normal Form (4NF). Explain why independent multivalued attributes violate BCNF and cause tuple redundancy. Demonstrate 4NF decomposition with a complete practical example.**

---

> 📌 **Definition to Remember**
> A relation schema $R$ is in **Fourth Normal Form (4NF)** if and only if it is in **BCNF** and for every non-trivial **Multivalued Dependency (MVD)** $X \twoheadrightarrow Y$, **$X$ is a Super Key** of $R$.

---

### 1. Concept of Multivalued Dependency (MVD)

A **Multivalued Dependency** $X \twoheadrightarrow Y$ (read as "$X$ multi-determines $Y$") exists in schema $R$ when a single attribute $X$ determines a **set of independent values of $Y$**, irrespective of the values of the remaining attributes $Z = R - (X \cup Y)$.

#### Formal Mathematical Definition:
$X \twoheadrightarrow Y$ holds in $R$ if, for any two tuples $t_1$ and $t_2$ such that $t_1[X] = t_2[X]$, there must also exist tuples $t_3$ and $t_4$ in $R$ such that:
$$t_3[X] = t_4[X] = t_1[X]$$
$$t_3[Y] = t_1[Y] \quad \text{and} \quad t_3[Z] = t_2[Z]$$
$$t_4[Y] = t_2[Y] \quad \text{and} \quad t_4[Z] = t_1[Z]$$

---

### 2. Why MVD Violates BCNF: The Combinatorial Explosion

When two independent 1-to-many relationships are forced into the same relation, BCNF is powerless to eliminate redundancy because all attributes form a single composite candidate key!

#### Example Schema:
$$\text{STUDENT\_INFO}(\text{Student\_ID}, \text{Mobile\_No}, \text{Skill})$$

* A student can have multiple mobile numbers.
* A student can possess multiple independent programming skills.
* `Mobile_No` and `Skill` are completely independent of each other.
* **Dependencies:**
  1. `\text{Student\_ID} \twoheadrightarrow \text{Mobile\_No}`
  2. `\text{Student\_ID} \twoheadrightarrow \text{Skill}`
* **Candidate Key:** `{\text{Student\_ID}, \text{Mobile\_No}, \text{Skill}}` (Entire table is the key!).

#### Redundant Tuple Table (BCNF Compliant but Anomaly Prone):
| Student_ID | Mobile_No | Skill |
| :---: | :---: | :--- |
| **101** | 9876543210 | Java |
| **101** | 9876543210 | Python |
| **101** | 9123456789 | Java |
| **101** | 9123456789 | Python |

* **The Anomaly:** Student 101 has 2 phone numbers and 2 skills $\implies 2 \times 2 = \mathbf{4 \text{ rows}}$. If the student adds a 3rd phone number, **3 new rows must be inserted** (one for every skill)!

---

### 3. 4NF Decomposition Algorithm

If a non-trivial MVD $X \twoheadrightarrow Y$ violates 4NF in relation $R$:
1. Decompose $R$ into **$R_1 = X \cup Y$**.
2. Decompose $R$ into **$R_2 = R - Y$**.

#### Resulting 4NF Normalized Tables:

```
                  STUDENT_INFO (Violates 4NF)
           {Student_ID, Mobile_No, Skill} (4 rows)
                              |
            +-----------------+-----------------+
            |                                   |
            v                                   v
  [ STUDENT_PHONE (4NF) ]             [ STUDENT_SKILL (4NF) ]
(Student_ID, Mobile_No)             (Student_ID, Skill)
  101 | 9876543210                    101 | Java
  101 | 9123456789                    101 | Python
  (Only 2 rows!)                      (Only 2 rows!)
```

* **Outcome:** $2 + 2 = 4$ rows total. Adding a new phone number now requires inserting **only 1 row** into `STUDENT_PHONE`, completely eliminating the combinatorial insertion anomaly!

---

### 4. Relational Normalization Hierarchy

```
   1NF: Eliminate Non-Atomic Values & Repeating Groups
    |
   2NF: Eliminate Partial Functional Dependencies
    |
   3NF: Eliminate Transitive Functional Dependencies
    |
  BCNF: Ensure ALL Determinants are Strict Super Keys
    |
   4NF: Eliminate Multivalued Dependencies (MVDs)
    |
   5NF: Eliminate Join Dependencies (Project-Join Normal Form PJNF)
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 4NF requires the relation to be in **BCNF with NO non-trivial multivalued dependencies (MVDs)**.
> 2. MVD $X \twoheadrightarrow Y$ indicates that $X$ determines a set of values for $Y$ independently of other attributes.
> 3. An MVD is non-trivial if $Y \not\subseteq X$ and $X \cup Y \neq R$.
> 4. Occurs when two independent 1-to-many relationships share a single primary key.
> 5. BCNF cannot eliminate MVD anomalies because all attributes together form the candidate key.
> 6. MVD causes a **combinatorial Cartesian explosion** of duplicate records.
> 7. Decomposing $R$ into $R_1(X \cup Y)$ and $R_2(R - Y)$ eliminates MVD update anomalies.

---

> ⚡ **Quick Recall**
> `BCNF Table → Detect Independent 1:N Relationships (X ->-> Y) → Combinatorial Row Explosion → Decompose R into (X U Y) and (R - Y) → 4NF Achieved`
