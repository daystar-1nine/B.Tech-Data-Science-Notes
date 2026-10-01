# Second Normal Form (2NF)

**Q. Define Second Normal Form (2NF). What is partial functional dependency? Explain with an example how a relation in 1NF is decomposed into 2NF relations, and describe the anomalies eliminated.**

---

> 📌 **Definition to Remember**
> A relation is in **Second Normal Form (2NF)** if and only if it is in **1NF** and **no non-prime attribute is partially dependent on any candidate key**. Every non-prime attribute must be **fully functionally dependent** on the entire primary key.

---

### 1. Key Concepts: Full vs. Partial Functional Dependency

* **Prime Attribute:** An attribute that is a member of at least one candidate key.
* **Non-Prime Attribute:** An attribute that does NOT belong to any candidate key.
* **Full Functional Dependency:** In a dependency $X \rightarrow Y$, $Y$ is fully dependent on $X$ if removal of any attribute from $X$ causes the dependency to no longer hold.
* **Partial Functional Dependency:** Occurs when a non-prime attribute depends on only a **proper subset** of a composite candidate key.

```
Composite Key: { A, B }
  { A, B } ---------> C   (Full Functional Dependency: C depends on BOTH A and B)
  { A } ------------> D   (Partial Dependency: D depends on ONLY A, violating 2NF!)
```

> **Crucial Rule:** 2NF is only violated when the relation has a **composite candidate key** (2 or more attributes). Any relation with a **single-attribute candidate key** that is in 1NF is **automatically in 2NF**!

---

### 2. Conversion Example: 1NF to 2NF Decomposition

#### Relation Schema:
$$\text{STUDENT\_COURSE}(\underline{\text{Student\_ID}}, \underline{\text{Course\_ID}}, \text{Student\_Name}, \text{Course\_Fee}, \text{Grade})$$

* **Candidate Key:** `{\text{Student\_ID}, \text{Course\_ID}}`
* **Functional Dependencies:**
  1. `{\text{Student\_ID}, \text{Course\_ID}} \rightarrow \text{Grade}` *(Full dependency)*
  2. `\text{Student\_ID} \rightarrow \text{Student\_Name}` *(Partial Dependency: depends only on part of key)*
  3. `\text{Course\_ID} \rightarrow \text{Course\_Fee}` *(Partial Dependency: depends only on part of key)*

#### Anomalies Present in 1NF:
* **Insertion Anomaly:** Cannot insert a new course fee without enrolling a student.
* **Deletion Anomaly:** If student 101 drops the course, the course fee info is deleted.
* **Update Anomaly:** If course fee changes, multiple rows must be modified.

---

### 3. Decomposition into 2NF Relations

To achieve 2NF, we split the partial dependencies into separate normalized relations:

```
                          STUDENT_COURSE (1NF)
                       {Student_ID, Course_ID}
                                  |
            +---------------------+---------------------+
            |                     |                     |
            v                     v                     v
     [ STUDENT ]             [ COURSE ]          [ ENROLLMENT ]
  (Student_ID, Name)     (Course_ID, Fee)      (Student_ID, Course_ID, Grade)
   PK: Student_ID         PK: Course_ID         PK: {Student_ID, Course_ID}
```

1. **`STUDENT` Table:**
   * Attributes: `(Student_ID, Student_Name)`
   * Primary Key: `Student_ID`
2. **`COURSE` Table:**
   * Attributes: `(Course_ID, Course_Fee)`
   * Primary Key: `Course_ID`
3. **`ENROLLMENT` Table:**
   * Attributes: `(Student_ID, Course_ID, Grade)`
   * Primary Key: `{Student_ID, Course_ID}`
   * Foreign Keys: `Student_ID` references `STUDENT`, `Course_ID` references `COURSE`

---

### 4. SQL Implementation for 2NF

```sql
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Course (
    Course_ID VARCHAR(10) PRIMARY KEY,
    Course_Fee DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Enrollment (
    Student_ID INT,
    Course_ID VARCHAR(10),
    Grade CHAR(2),
    PRIMARY KEY (Student_ID, Course_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 2NF requires a relation to be in **1NF with NO partial functional dependencies**.
> 2. **Partial dependency:** A non-prime attribute depending on a proper subset of a composite candidate key.
> 3. 2NF is only violated when candidate keys are **composite**; relations with single-attribute primary keys in 1NF are automatically in 2NF.
> 4. 2NF decomposition moves partially dependent attributes into separate tables with their determining subset as primary key.
> 5. Eliminates insertion and deletion anomalies related to partial attributes.
> 6. Decomposed tables preserve connections via **Foreign Key constraints**.
> 7. Transitive dependencies may still exist in 2NF, requiring progression to 3NF.

---

> ⚡ **Quick Recall**
> `1NF Relation → Identify Composite Key → Check for Partial FDs (Non-Prime → Subset of Key) → Split into Independent Lookup Tables → 2NF Achieved`
