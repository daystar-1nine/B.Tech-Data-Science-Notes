# Attributes and Keys

**Q. Discuss the different types of Attributes in the ER model. Explain the concepts of Super Key, Candidate Key, Primary Key, and Foreign Key with examples.**

---

> 📌 **Definition to Remember**
> An **Attribute** is a property or characteristic that describes an entity, corresponding to a column in a relational table. A **Key** is a single attribute or combination of attributes that uniquely identifies a row (tuple) in a table, maintaining data integrity.

---

### 1. Types of Attributes

| Type | Description | ER Symbol | Example |
| :--- | :--- | :--- | :--- |
| **Simple** | Cannot be subdivided further | Single Oval | `Age`, `Gender` |
| **Composite** | Can be divided into sub-parts | Single Oval (with child ovals) | `Address` → Street, City, Zip |
| **Single-Valued** | Holds one value per entity | Single Oval | `Date_of_Birth` |
| **Multi-Valued** | Holds multiple values per entity | **Double Oval** | `Phone_Number` (mobile + home) |
| **Stored** | Physically stored in the DB | Single Oval | `Date_of_Birth` |
| **Derived** | Computed from a stored attribute | **Dashed Oval** | `Age` (derived from DOB + current date) |

### 2. Types of Keys

A **Key** is essential for uniqueness and establishing relationships between tables.

#### 1. Super Key
* A set of one or more attributes that **uniquely identifies** a row in a table.
* May contain **extra, redundant attributes**.
* **Example (STUDENT table):** `{Roll_No}`, `{Roll_No, Name}`, `{Roll_No, Email, Age}` — all are Super Keys.

#### 2. Candidate Key
* A **minimal Super Key** — no redundant attributes; removing any attribute breaks uniqueness.
* A table can have **multiple** Candidate Keys.
* **Example:** `{Roll_No}` and `{Email}` are Candidate Keys. `{Roll_No, Name}` is NOT (Name is redundant).

#### 3. Primary Key
* The **one Candidate Key selected** by the designer as the official unique row identifier.
* **Cannot contain NULL** values; must be strictly unique.
* Only **one Primary Key** per table.
* Represented by an **Underlined Oval** in ER diagrams.
* **Example:** `{Roll_No}` is chosen as Primary Key from candidates `{Roll_No}` and `{Email}`.

#### 4. Foreign Key
* An attribute in one table that **refers to the Primary Key** of another table.
* Enforces **Referential Integrity** — ensures related records exist in the referenced table.
* **Example:** `Roll_No` in `ENROLLMENT` table is a Foreign Key referencing `Roll_No` (PK) in `STUDENT` table.

```
  STUDENT Table          ENROLLMENT Table
  ┌─────────┐            ┌─────────────────┐
  │ Roll_No │◄──────────│ Roll_No (FK)     │
  │ Name    │            │ Course_ID        │
  └─────────┘            └─────────────────┘
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Attribute types: Simple, Composite, Single-Valued, Multi-Valued, Stored, Derived.
> 2. Multi-Valued attribute uses Double Oval; Derived attribute uses Dashed Oval in ER diagrams.
> 3. Super Key = any set that uniquely identifies a row (may have redundant attributes).
> 4. Candidate Key = minimal Super Key (no redundant attributes); a table can have multiple.
> 5. Primary Key = the one Candidate Key selected; cannot be NULL; only one per table.
> 6. Foreign Key = references Primary Key of another table; enforces Referential Integrity.
> 7. Super Key ⊇ Candidate Key ⊇ Primary Key (each is a subset/specific case of the previous).

---

> ⚡ **Quick Recall**
> `Simple/Composite → Single/Multi-Valued (Double Oval) → Stored/Derived (Dashed Oval) → Super Key → Candidate Key (minimal) → Primary Key (chosen, no NULL) → Foreign Key (referential integrity)`
