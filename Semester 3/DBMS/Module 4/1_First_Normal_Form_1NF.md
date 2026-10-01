# First Normal Form (1NF)

**Q. What is First Normal Form (1NF)? Explain why normalization is necessary in relational database design. Give an example of an unnormalized relation and demonstrate step-by-step conversion into 1NF.**

---

> 📌 **Definition to Remember**
> A relation is in **First Normal Form (1NF)** if and only if all attributes contain only **atomic (indivisible) scalar values**, and there are no repeating groups, arrays, or composite attributes stored within any field. Every row must also be uniquely identifiable via a Primary Key.

---

### 1. Why Normalization is Necessary: The Three Update Anomalies

Without normalization, database schemas suffer from massive data redundancy, leading to three destructive update anomalies:

1. **Insertion Anomaly:** Cannot insert information about an entity without redundantly supplying data for unrelated entities (e.g., cannot add a new course if no student has enrolled in it yet).
2. **Deletion Anomaly:** Deleting one piece of information unintentionally deletes other vital independent data (e.g., deleting the last student enrolled in a course inadvertently erases the entire course record).
3. **Modification (Update) Anomaly:** Modifying a duplicated data item requires updating every duplicate row; if any row is missed, data becomes inconsistent.

---

### 2. Core Rules of First Normal Form (1NF)

1. **Atomic Values Only:** Each column must hold exactly one value per row (no comma-separated strings or arrays).
2. **No Repeating Groups:** Do not create columns like `Phone1`, `Phone2`, `Phone3`.
3. **Unique Column Names:** Every column in a relation must have a unique identifier.
4. **Unique Records:** Every table must have a Primary Key so no two rows are identical duplicates.
5. **Order Independence:** The physical sequence of rows and columns has no bearing on database semantics.

---

### 3. Step-by-Step Conversion: UNF to 1NF

#### Step 1: Inspect Unnormalized Relation (UNF)
Consider a student enrollment table where students have multiple phone numbers and enroll in multiple courses:

| Student_ID | Student_Name | Phone_Numbers | Courses |
| :---: | :--- | :--- | :--- |
| **101** | Rahul Sharma | 9876543210, 9123456789 | DBMS, DSA, MPCA |
| **102** | Anita Verma | 9988776655 | DBMS, Python |

* **Violations:** `Phone_Numbers` and `Courses` contain multi-valued non-atomic lists.

#### Step 2: Flatten into 1NF Atomic Records
We expand multi-valued lists into distinct rows such that every cell contains exactly one scalar value:

| Student_ID | Student_Name | Phone_Number | Course |
| :---: | :--- | :---: | :--- |
| **101** | Rahul Sharma | 9876543210 | DBMS |
| **101** | Rahul Sharma | 9876543210 | DSA |
| **101** | Rahul Sharma | 9876543210 | MPCA |
| **101** | Rahul Sharma | 9123456789 | DBMS |
| **101** | Rahul Sharma | 9123456789 | DSA |
| **101** | Rahul Sharma | 9123456789 | MPCA |
| **102** | Anita Verma | 9988776655 | DBMS |
| **102** | Anita Verma | 9988776655 | Python |

* **Composite Primary Key in 1NF:** `{Student_ID, Phone_Number, Course}`.

---

### 4. SQL Implementation for 1NF

```sql
-- Creating 1NF Compliant Table
CREATE TABLE Student_Enrollment_1NF (
    Student_ID INT NOT NULL,
    Student_Name VARCHAR(50) NOT NULL,
    Phone_Number VARCHAR(15) NOT NULL,
    Course VARCHAR(50) NOT NULL,
    PRIMARY KEY (Student_ID, Phone_Number, Course)
);
```

---

### 5. Limitations of 1NF

While 1NF eliminates nested collections, it creates significant row redundancy (`Rahul Sharma` is repeated 6 times!). This redundancy can only be eliminated by advancing to **2NF** (removing partial dependencies) and **3NF** (removing transitive dependencies).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Normalization eliminates **Insertion, Deletion, and Update anomalies**.
> 2. 1NF requires **atomic values** in every attribute domain (no multi-valued or composite values).
> 3. Eliminates **repeating groups** and array columns (e.g., `Phone1, Phone2`).
> 4. Requires a valid **Primary Key** to uniquely identify every row.
> 5. Unnormalized tables are converted to 1NF by creating individual tuples for each multi-valued element.
> 6. 1NF alone does not eliminate data redundancy; duplicate data remains due to partial dependencies.
> 7. The primary key in a 1NF flattened table is often a composite key.

---

> ⚡ **Quick Recall**
> `UNF Table → Remove Comma-Separated Values → Ensure Atomic Cells → Assign Primary Key → 1NF Achieved (Partial Redundancy Remains)`
