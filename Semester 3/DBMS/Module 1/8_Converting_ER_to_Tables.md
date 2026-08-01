# Converting ER Model to Relational Tables

**Q. How is an ER Diagram mapped into a Relational Database schema? Explain the rules for converting Entities, Attributes, and the various Relationships (1:1, 1:N, M:N) into database tables.**

---

> 📌 **Definition to Remember**
> **ER-to-Relational Mapping** is the process of converting a conceptual ER diagram into a physical Relational Model consisting of Tables, Columns, and Keys. Each entity, attribute, and relationship must be transformed using a specific set of mapping rules.

---

### 1. Rule 1: Strong Entities and Attributes
* Every **Strong Entity Type** → becomes a separate **Table**.
* Simple Attributes of the entity → become **Columns**.
* The **Key Attribute** → becomes the **Primary Key** of the table.
* **Composite Attributes:** Only the sub-components become columns (e.g., `Address` → `Street`, `City`, `Zip`).

### 2. Rule 2: Multi-Valued Attributes
* Cannot store a multi-valued attribute in the main table (relational tables require **atomic** values).
* **Solution:** Create a **new separate table** with:
  * The entity's Primary Key (as a **Foreign Key**)
  * The multi-valued attribute
  * Both together form the **Primary Key** of this new table.

### 3. Rule 3: Weak Entities
* Weak Entity → converted into a **separate table** with its own attributes.
* Add the **Primary Key of the Identifying Strong Entity** as a **Foreign Key**.
* The new table's PK = **FK + Partial Key** (discriminator) of the weak entity.

### 4. Rule 4: Mapping Binary Relationships

| Cardinality | New Table Needed? | Action |
| :--- | :--- | :--- |
| **1:1** | No | Add PK of one table as FK in the other (prefer total participation side) |
| **1:N** | No | Add PK of the "One" side as FK in the "Many" side table |
| **M:N** | **Yes** | Create a Junction Table with both PKs as FKs; their combination = new PK |

```
  1:1 Mapping:
  MANAGER (Mgr_ID) ──── DEPARTMENT (Dept_ID, Mgr_ID as FK)

  1:N Mapping:
  DEPARTMENT (Dept_ID) ──── EMPLOYEE (Emp_ID, Dept_ID as FK)

  M:N Mapping:
  STUDENT (Roll_No)  ──── ENROLLS (Roll_No FK, Course_ID FK) ──── COURSE (Course_ID)
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. ER-to-Relational Mapping converts ER blueprints into physical Tables, Columns, and Keys.
> 2. Every Strong Entity → one Table; its Key Attribute → Primary Key.
> 3. Multi-Valued Attributes cannot exist in the main table — a new table is created.
> 4. Weak Entity → new table; PK = Owner Entity's PK (FK) + Partial Key.
> 5. 1:1 relationship → no new table; place one PK as FK in the other.
> 6. 1:N relationship → no new table; place "One" side's PK as FK in "Many" side.
> 7. M:N relationship → **requires a Junction (Associative) Table** with both PKs as FKs.

---

> ⚡ **Quick Recall**
> `Strong Entity→Table (PK) → Multi-valued→New Table → Weak Entity→Table (FK+Partial Key) → 1:1 (FK) → 1:N (FK on Many) → M:N (Junction Table)`
