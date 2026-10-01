# Third Normal Form (3NF)

**Q. Define Third Normal Form (3NF). What is a transitive functional dependency? State the formal conditions for 3NF and demonstrate the decomposition of a relation from 2NF to 3NF with a complete example.**

---

> 📌 **Definition to Remember**
> A relation is in **Third Normal Form (3NF)** if it is in **2NF** and **no non-prime attribute is transitively dependent on the primary key**. Formally, for every non-trivial functional dependency $X \rightarrow Y$, either **$X$ is a Super Key** OR **$Y$ is a Prime Attribute**.

---

### 1. Transitive Functional Dependency Concept

A **transitive dependency** occurs when a non-prime attribute is indirectly determined by the primary key through another non-prime attribute:

$$\text{Primary Key } (A) \longrightarrow \text{Non-Prime } (B) \longrightarrow \text{Non-Prime } (C)$$

```
[ Primary Key A ] -------------> [ Non-Prime Attribute B ]
      |                                     |
      |                                     v
      +-------------------------> [ Non-Prime Attribute C ]
                                   (Transitive Dependency!)
```

* Here, $A \rightarrow C$ is a transitive dependency through $B$.
* Storing $C$ alongside $A$ causes update anomalies because if $B$'s relationship with $C$ changes, multiple rows must be modified.

---

### 2. Formal Definition of 3NF

A relation schema $R$ is in 3NF with respect to a set of functional dependencies $F$ if, for every non-trivial functional dependency $X \rightarrow Y \in F^+$:
1. $Y \subseteq X$ ($X \rightarrow Y$ is trivial), **OR**
2. **$X$ is a Super Key** of $R$, **OR**
3. **$Y$ is a Prime Attribute** (each attribute in $Y$ belongs to at least one candidate key of $R$).

---

### 3. Conversion Example: 2NF to 3NF Decomposition

#### Relation Schema:
$$\text{EMP\_DEPT}(\underline{\text{Emp\_ID}}, \text{Emp\_Name}, \text{Dept\_ID}, \text{Dept\_Name}, \text{Dept\_Head})$$

* **Candidate Key:** `Emp_ID` (Single attribute $\implies$ Table is in 2NF).
* **Functional Dependencies:**
  1. `\text{Emp\_ID} \rightarrow \text{Emp\_Name}, \text{Dept\_ID}` *(Emp_ID is Super Key $\implies$ 3NF Valid)*
  2. `\text{Dept\_ID} \rightarrow \text{Dept\_Name}, \text{Dept\_Head}` *(Dept_ID is NOT a Super Key, Dept_Name/Dept_Head are non-prime $\implies$ **3NF Violation!**)*

#### Anomalies Present:
* **Insertion Anomaly:** Cannot record a new department until an employee is hired into it.
* **Deletion Anomaly:** Deleting the only employee in a department erases the department's name and head!
* **Update Anomaly:** If department head changes, every employee record in that department must be updated.

#### Decomposition into 3NF Relations:
We split the transitive dependency into two separate tables:

```
1. EMPLOYEE Table:
   Attributes: (Emp_ID, Emp_Name, Dept_ID)
   Primary Key: Emp_ID
   Foreign Key: Dept_ID references DEPARTMENT(Dept_ID)

2. DEPARTMENT Table:
   Attributes: (Dept_ID, Dept_Name, Dept_Head)
   Primary Key: Dept_ID
```

---

### 4. Comparison Table: 1NF vs. 2NF vs. 3NF

| Normal Form | Elimination Target | Condition Required | Common Anomaly Resolved |
| :--- | :--- | :--- | :--- |
| **1NF** | Multi-valued & composite attributes | All attributes must be atomic | Storage of nested collections |
| **2NF** | Partial dependencies | Non-prime attributes must depend on entire candidate key | Redundancy from composite keys |
| **3NF** | **Transitive dependencies** | For $X \rightarrow Y$: $X$ is Super Key OR $Y$ is Prime | Redundancy from non-key associations |

---

### 5. Why 3NF is the Commercial Standard

Almost all real-world enterprise databases normalize schemas to **3NF** because:
1. It guarantees **Lossless-Join Decomposition** (no fake data generated upon joining).
2. It guarantees **Dependency Preservation** (all business rules enforced without expensive joins).
3. It achieves an optimal trade-off between eliminating anomalies and maintaining SQL join query performance.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 3NF requires a relation to be in **2NF with NO transitive functional dependencies**.
> 2. Formal rule: For every $X \rightarrow Y$, either **$X$ is a super key** or **$Y$ is a prime attribute**.
> 3. Transitive dependency: $A \rightarrow B$ and $B \rightarrow C$ implies $A \rightarrow C$ via non-key attribute $B$.
> 4. Decomposing into 3NF isolates non-key determinants into independent lookup tables.
> 5. Eliminates insertion and deletion anomalies where entity records depend on unrelated non-key data.
> 6. 3NF guarantees both **lossless join** and **functional dependency preservation**.
> 7. Serves as the industry-standard design balance between query performance and data integrity.

---

> ⚡ **Quick Recall**
> `2NF Relation → Check X → Y → Is X a Super Key? (Yes: OK) → Is Y a Prime Attribute? (Yes: OK) → Else: Transitive Violation → Split Tables → 3NF Achieved`
