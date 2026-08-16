import os

DBMS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\DBMS"

m4_dir = os.path.join(DBMS_DIR, "Module 4")
m5_dir = os.path.join(DBMS_DIR, "Module 5")
m6_dir = os.path.join(DBMS_DIR, "Module 6")

os.makedirs(m4_dir, exist_ok=True)
os.makedirs(m5_dir, exist_ok=True)
os.makedirs(m6_dir, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4: RELATIONAL DATABASE DESIGN
# --------------------------------------------------------------------------

m4_files = {
    "1_First_Normal_Form_1NF.md": """# First Normal Form (1NF) — Relational Database Design

> **Definition:** A relation is in **First Normal Form (1NF)** if and only if all attributes contain only **atomic (indivisible) values**, and there are no repeating groups or arrays stored within a single field.

---

## 1. Detailed Technical Explanation

Normalization is the systematic process of organizing relational database schemas to eliminate data redundancy and anomalies (Insertion, Deletion, and Update anomalies).

### Key Rules of 1NF:
1. **Atomic Values:** Each column must store a single value (no multi-valued attributes like comma-separated phone numbers).
2. **Unique Column Names:** Each column in a table must have a unique attribute name.
3. **Unique Rows:** Each row must be uniquely identifiable (using a Primary Key).
4. **Order Indifference:** The order of rows and columns does not affect data meaning.

### Conversion Example: Unnormalized Table to 1NF

#### Unnormalized Relation (UNF):
| Student_ID | Student_Name | Phone_Numbers | Courses |
| :--- | :--- | :--- | :--- |
| 101 | Rahul Sharma | 9876543210, 9123456789 | DBMS, DSA, MPCA |
| 102 | Anita Verma | 9988776655 | DBMS, Python |

#### Normalized 1NF Relation:
| Student_ID | Student_Name | Phone_Number | Course |
| :--- | :--- | :--- | :--- |
| 101 | Rahul Sharma | 9876543210 | DBMS |
| 101 | Rahul Sharma | 9876543210 | DSA |
| 101 | Rahul Sharma | 9876543210 | MPCA |
| 101 | Rahul Sharma | 9123456789 | DBMS |
| 101 | Rahul Sharma | 9123456789 | DSA |
| 101 | Rahul Sharma | 9123456789 | MPCA |
| 102 | Anita Verma | 9988776655 | DBMS |
| 102 | Anita Verma | 9988776655 | Python |

---

## 2. Core Concepts & Memory Keywords
- **Atomic Domains:** Fields storing single indivisible values.
- **Repeating Groups:** Storing lists or multiple values in a single cell (violates 1NF).
- **Primary Key:** A minimal set of attributes uniquely identifying each record in 1NF.

---

## 3. Must-Write Points for Exams
- 1NF eliminates **multi-valued attributes** and **composite attributes** from relation instances.
- In 1NF, every attribute value in a row must be a single scalar value from the domain.
- 1NF does not eliminate all redundancy; partial and transitive dependencies can still cause anomalies.

---

## 4. Quick Recall Flow
```
Unnormalized Table -> Remove Comma-Separated Values -> Ensure Atomic Cells -> 1NF Form Achieved
```
""",

    "2_Second_Normal_Form_2NF.md": """# Second Normal Form (2NF) — Relational Database Design

> **Definition:** A relation is in **Second Normal Form (2NF)** if it is in **1NF** and **no non-prime attribute is partially dependent on any candidate key** of the relation. Every non-key attribute must be **fully functionally dependent** on the primary key.

---

## 1. Detailed Technical Explanation

### Functional Dependency Concepts:
- **Full Functional Dependency:** X -> Y is a full functional dependency if removal of any attribute A from X means the dependency no longer holds.
- **Partial Dependency:** Occurs when a non-prime attribute depends on only a *proper subset* of a composite primary key.

### Conversion Example: 1NF to 2NF

#### Relation R(Student_ID, Course_ID, Student_Name, Course_Fee)
- **Candidate Key:** {Student_ID, Course_ID}
- **Functional Dependencies:**
  1. {Student_ID, Course_ID} -> Student_Name, Course_Fee
  2. Student_ID -> Student_Name *(Partial Dependency: Student_Name depends only on part of key)*
  3. Course_ID -> Course_Fee *(Partial Dependency: Course_Fee depends only on part of key)*

#### Decomposition into 2NF:
We split table R into 3 normalized tables:

1. **STUDENT (Student_ID, Student_Name)**
   - Primary Key: `Student_ID`
2. **COURSE (Course_ID, Course_Fee)**
   - Primary Key: `Course_ID`
3. **ENROLLMENT (Student_ID, Course_ID)**
   - Primary Key: `{Student_ID, Course_ID}`
   - Foreign Keys: `Student_ID` refs STUDENT, `Course_ID` refs COURSE

---

## 2. Core Concepts & Memory Keywords
- **Non-prime Attribute:** An attribute that is not part of any candidate key.
- **Prime Attribute:** An attribute that belongs to at least one candidate key.
- **Partial Dependency Removal:** Splitting composite key attributes into separate lookup tables.

---

## 3. Must-Write Points for Exams
- 2NF is only relevant when the relation has a **composite candidate key** (candidate key containing 2 or more attributes).
- Relations with a single-attribute primary key in 1NF are **automatically in 2NF**.
- 2NF eliminates **update anomalies** caused by repeating non-key attribute values.

---

## 4. Quick Recall Flow
```
1NF Relation -> Identify Partial Dependencies (Non-Prime -> Part of Key) -> Decompose Tables -> 2NF Achieved
```
""",

    "3_Third_Normal_Form_3NF.md": """# Third Normal Form (3NF) — Relational Database Design

> **Definition:** A relation is in **Third Normal Form (3NF)** if it is in **2NF** and **no non-prime attribute is transitively dependent on the primary key**. For every non-trivial functional dependency X -> Y, either **X is a super key** or **Y is a prime attribute**.

---

## 1. Detailed Technical Explanation

### Transitive Dependency Concept:
A transitive dependency exists if A -> B and B -> C hold, which implies A -> C through non-key attribute B.

```
[ Primary Key A ] -------------> [ Non-Prime Attribute B ]
                                            |
                                            v
                                 [ Non-Prime Attribute C ]
                                 (Transitive Dependency!)
```

### Conversion Example: 2NF to 3NF

#### Relation EMP_DEPT(Emp_ID, Emp_Name, Dept_ID, Dept_Name, Dept_Head)
- **Candidate Key:** `Emp_ID`
- **Functional Dependencies:**
  1. Emp_ID -> Emp_Name, Dept_ID
  2. Dept_ID -> Dept_Name, Dept_Head *(Transitive Dependency: Dept_ID is not a super key, Dept_Name is non-prime)*

#### Decomposition into 3NF:
We decompose EMP_DEPT into 2 distinct tables:

1. **EMPLOYEE (Emp_ID, Emp_Name, Dept_ID)**
   - Primary Key: `Emp_ID`
   - Foreign Key: `Dept_ID`
2. **DEPARTMENT (Dept_ID, Dept_Name, Dept_Head)**
   - Primary Key: `Dept_ID`

---

## 2. Core Concepts & Memory Keywords
- **Transitive Dependency:** Non-key attribute determining another non-key attribute.
- **3NF Formal Condition:** For all X -> Y:
  1. X -> Y is trivial (Y ⊆ X), OR
  2. X is a Super Key, OR
  3. Y is a Prime Attribute (part of a candidate key).

---

## 3. Must-Write Points for Exams
- 3NF guarantees **lossless-join decomposition** and **dependency preservation**.
- 3NF removes insertion and deletion anomalies associated with transitive attribute relationships.
- Most practical commercial enterprise databases are normalized up to 3NF.

---

## 4. Quick Recall Flow
```
2NF Relation -> Check X -> Y -> Ensure X is Super Key OR Y is Prime -> Remove Transitive Dependencies -> 3NF Achieved
```
""",

    "4_Boyce_Codd_Normal_Form_BCNF.md": """# Boyce-Codd Normal Form (BCNF) — Relational Database Design

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
""",

    "5_Algorithm_for_Decomposition_Using_Functional_Dependencies.md": """# Algorithm for Decomposition Using Functional Dependencies — DBMS

> **Definition:** **Decomposition Algorithms** split a complex relational schema R into smaller sub-schemas (R1, R2, ..., Rn) to eliminate anomalies while preserving **Lossless-Join** and **Functional Dependencies**.

---

## 1. Detailed Technical Explanation

### 1. Attribute Closure Algorithm (F+)
The closure of an attribute set X under F, denoted $X^+$, is the set of all attributes functionally determined by X.

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
- **Lossless Join:** Guarantees $R = R_1 \bowtie R_2$ (no spurious tuples created upon joining).
- **Dependency Preservation:** Checks if $(F_1 \cup F_2 \cup ... \cup F_n)^+ = F^+$.

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
""",

    "6_Decomposition_Using_Multivalued_Attribute.md": """# Decomposition Using Multivalued Attribute (4NF) — DBMS

> **Definition:** A relation is in **Fourth Normal Form (4NF)** if it is in **BCNF** and for every non-trivial **Multivalued Dependency (MVD) X ->-> Y**, **X is a Super Key**.

---

## 1. Detailed Technical Explanation

### Multivalued Dependency (MVD):
A multivalued dependency $X \twoheadrightarrow Y$ (read as "X multidetermines Y") exists in schema R if the presence of a pair of tuples $(t_1, t_2)$ with $t_1[X] = t_2[X]$ implies that there must also exist tuples $t_3$ and $t_4$ combining $X$, $Y$, and the remaining attributes $Z = R - (X \cup Y)$.

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
If $X \twoheadrightarrow Y$ violates 4NF in R, decompose R into:
1. $R_1 = X \cup Y$
2. $R_2 = R - Y$

#### Decomposed 4NF Tables:
1. **STUDENT_MOBILE (Student_ID, Mobile_No)**
2. **STUDENT_SKILL (Student_ID, Skill)**

---

## 2. Core Concepts & Memory Keywords
- **Multivalued Dependency (MVD):** Independence between two multi-valued attributes associated with the same key.
- **Spurious Combinations:** Combinatorial explosion of duplicate tuples caused by MVDs.
- **4NF Condition:** Every non-trivial MVD $X \twoheadrightarrow Y$ must have $X$ as a super key.

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
""",

    "7_Self_Learning_NoSQL_Data_Models.md": """# Self-Learning: NoSQL Data Models — DBMS

> **Definition:** **NoSQL (Not Only SQL)** refers to non-relational database management systems designed for horizontal scalability, high-velocity big data, flexible schema-less data models, and high availability.

---

## 1. Detailed Technical Explanation

NoSQL databases trade traditional ACID strict transactional guarantees for high performance and horizontal scaling across distributed clusters (governed by the **CAP Theorem**).

### CAP Theorem:
A distributed database system can guarantee at most **two out of three** properties simultaneously:
1. **Consistency (C):** All nodes read the latest data at the same time.
2. **Availability (A):** Every non-failing request receives a non-error response.
3. **Partition Tolerance (P):** System continues to operate despite network communication failures.

---

## 2. The Four Major NoSQL Data Models

| NoSQL Category | Data Model | Key Features | Popular Industry Tools | Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Key-Value Store** | Hash Table (Key -> Value Blob) | Fast lookup by key, ultra-high performance. | Redis, Amazon DynamoDB, Riak | Caching, session management, user shopping carts. |
| **Document Store** | JSON / BSON / XML Documents | Schema-free nested documents, rich indexing. | MongoDB, CouchDB | Content management, e-commerce product catalogs. |
| **Column-Family Store**| Sparse tables indexed by Rows & Column Families | Optimized for heavy write throughput and analytical queries. | Apache Cassandra, HBase | Time-series data, IoT analytics, financial logs. |
| **Graph Database** | Nodes, Edges (Properties) | Graph traversal queries for interconnected data. | Neo4j, Amazon Neptune | Social networks, fraud detection, recommendation engines. |

---

## 3. SQL vs NoSQL Architecture Comparison

| Feature | Relational SQL Databases | NoSQL Databases |
| :--- | :--- | :--- |
| **Data Schema** | Fixed, predefined rigid schema. | Dynamic, schema-less / flexible. |
| **Scaling** | Vertical scaling (Scale-up: bigger CPU/RAM). | Horizontal scaling (Scale-out: sharding across commodity nodes). |
| **Transactions** | Strict ACID Compliance. | BASE Model (Basically Available, Soft-state, Eventual consistency). |
| **Joins** | Native SQL `JOIN` operations. | Denormalized data / Application-side joins. |

---

## 4. Quick Recall Flow
```
NoSQL -> Scale-Out Horizontal Architecture -> CAP Theorem Tradeoffs -> Key-Value | Document | Column-Family | Graph
```
"""
}

# Write Module 4 files
for fname, content in m4_files.items():
    with open(os.path.join(m4_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Module 4 Files!")
