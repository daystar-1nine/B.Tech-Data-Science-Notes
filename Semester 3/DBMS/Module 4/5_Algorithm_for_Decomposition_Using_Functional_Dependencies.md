# Algorithm for Decomposition Using Functional Dependencies

**Q. Explain the Attribute Closure algorithm ($X^+$) and its application in finding candidate keys. Explain the algorithms for testing Lossless-Join Decomposition and Dependency Preservation, and describe the 3NF synthesis algorithm.**

---

> 📌 **Definition to Remember**
> **Decomposition Algorithms** systematically partition a universal relational schema $R$ into smaller normalized sub-schemas ($R_1, R_2, \dots, R_k$) to eliminate anomalies while strictly satisfying two mathematical correctness criteria: **Lossless-Join Decomposition** ($R = R_1 \bowtie R_2$) and **Functional Dependency Preservation** ($(\bigcup F_i)^+ = F^+$).

---

### 1. Attribute Closure Algorithm ($X^+$)

The **closure of attribute set $X$ under $F$**, denoted **$X^+$**, is the complete set of attributes that are functionally determined by $X$ under $F$.

#### Pseudo-Code:
```
Input:  Set of attributes X, Set of Functional Dependencies F
Output: X+ (Attribute Closure)

1. Set Closure = X
2. Repeat until no new attributes can be added to Closure:
     For each FD (Y -> Z) in F:
       If Y ⊆ Closure:
         Closure = Closure ∪ Z
3. Return Closure
```

#### Application: Finding Candidate Keys
* If $X^+$ contains all attributes of relation $R$, then $X$ is a **Super Key**.
* If no proper subset of $X$ is a super key, then $X$ is a **Candidate Key**.

---

### 2. Testing Lossless-Join Decomposition

A decomposition of $R$ into sub-relations $R_1$ and $R_2$ is **Lossless-Join** with respect to $F$ if and only if the common attributes form a super key of at least one sub-relation:

$$(R_1 \cap R_2) \longrightarrow R_1 \quad \mathbf{OR} \quad (R_1 \cap R_2) \longrightarrow R_2$$

```
           Relation R(A, B, C) with F = { A -> B }
                        Decomposed into:
                 R1(A, B)      and      R2(A, C)
                         R1 ∩ R2 = { A }
                     Check: Is A -> R1?
                    A -> {A, B} holds true!
            Conclusion: DECOMPOSITION IS LOSSLESS-JOIN!
```

* **Lossy Join Danger:** If common attributes are not a super key, executing a natural join ($R_1 \bowtie R_2$) produces **spurious (fake) tuples** that never existed in the original relation!

---

### 3. Testing Dependency Preservation

A decomposition $D = \{R_1, R_2, \dots, R_n\}$ is **Dependency Preserving** if the union of projections of $F$ on all sub-relations covers all original dependencies in $F$:

$$(F_1 \cup F_2 \cup \dots \cup F_n)^+ = F^+$$

* **Why it matters:** If dependencies are preserved, the database engine enforces integrity constraints locally within each table without requiring expensive multi-table `JOIN` operations.

---

### 4. 3NF Synthesis Algorithm (Lossless + Dependency Preserving)

This algorithm guarantees a 3NF decomposition that is **simultaneously Lossless-Join AND Dependency Preserving**:

```
Input:  Relation R, Set of Functional Dependencies F
Output: 3NF Decomposition of R

Step 1: Compute Minimal (Canonical) Cover Fc of F:
        - Ensure single attribute on RHS of each FD.
        - Eliminate extraneous LHS attributes using closure.
        - Eliminate redundant FDs.

Step 2: For each FD (X -> Y) in Fc:
        Create a relation schema Ri = X ∪ Y.

Step 3: Check Candidate Key:
        If no schema Ri contains a candidate key of original relation R:
          Create an additional schema R_key containing any candidate key of R.

Step 4: Schema Simplification:
        Eliminate redundant sub-schemas (if Ri ⊆ Rj, drop Ri).
```

---

### 5. Summary Table: Decomposition Properties

| Normal Form | Decomposition Method | Lossless-Join Guaranteed? | Dependency Preservation Guaranteed? |
| :--- | :--- | :---: | :---: |
| **3NF** | 3NF Synthesis Algorithm | **YES** | **YES** |
| **BCNF** | BCNF Decomposition Algorithm | **YES** | **NO** (May be lost) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Attribute closure $X^+$ calculates all attributes functionally determined by $X$.
> 2. If $X^+$ contains all attributes of $R$, then $X$ is a super key.
> 3. **Lossless-join test:** $(R_1 \cap R_2) \rightarrow R_1$ OR $(R_1 \cap R_2) \rightarrow R_2$ must hold in $F^+$.
> 4. Lossy decomposition creates **spurious tuples** upon natural join, corrupting data integrity.
> 5. **Dependency preservation:** Ensures all original FDs can be checked without computing joins.
> 6. **3NF synthesis algorithm** uses the canonical cover $F_c$ to guarantee both lossless join and dependency preservation.
> 7. BCNF decomposition guarantees lossless join, but cannot always preserve all functional dependencies.

---

> ⚡ **Quick Recall**
> `Attribute Closure (X+) → Candidate Key Test → Lossless Join ((R1 ∩ R2) -> R1 or R2) → Dependency Preservation ((UF_i)+ = F+) → 3NF Synthesis Algorithm`
