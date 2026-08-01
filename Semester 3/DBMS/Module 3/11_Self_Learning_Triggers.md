# Database Triggers (Self-Learning)

**Q. What is a Trigger in SQL? Discuss the different types of triggers (BEFORE and AFTER) and explain their primary uses.**

---

> 📌 **Definition to Remember**
> A **Trigger** is a special stored procedure in a database that **automatically fires (executes)** in response to a DML event (`INSERT`, `UPDATE`, or `DELETE`) on a specific table. Unlike regular procedures, **triggers are never called explicitly** — the RDBMS engine activates them automatically.

---

### 1. Types of Triggers

Triggers are classified by **when** they execute relative to the triggering DML event:

#### A. BEFORE Trigger
* Executes **immediately before** the INSERT, UPDATE, or DELETE completes.
* **Purpose:** Validates or modifies incoming data before it is saved.
* **Use Cases:** Data validation, enforcing complex constraints, transforming input data.

**Example:** Before inserting into the `Employee` table, a BEFORE trigger checks if the incoming salary is below minimum wage. If so, it **raises an error and aborts** the insert.

#### B. AFTER Trigger
* Executes **immediately after** the INSERT, UPDATE, or DELETE has successfully completed.
* **Purpose:** Reacts to committed changes — used for auditing and cascading operations.
* **Use Cases:** Audit logging, cascading updates to related tables, sending notifications.

**Example:** After an update to `Employee`, an AFTER trigger inserts a record into `Employee_Audit` logging the user, timestamp, and what changed.

*(Some systems also support **INSTEAD OF Triggers** — primarily used on Views to enable update operations on non-updatable views.)*

### 2. Trigger Event Classification

| | BEFORE | AFTER |
| :--- | :--- | :--- |
| **Timing** | Before data is saved | After data is saved |
| **Purpose** | Validate / modify input | React / audit / cascade |
| **Can Abort?** | Yes — can raise error to stop | No — data already committed |

### 3. Uses and Advantages

| Use Case | Explanation |
| :--- | :--- |
| **Business Rule Enforcement** | Complex rules that `CHECK` constraints can't handle |
| **Auditing** | Auto-log who changed what and when |
| **Task Automation** | Calculate derived columns, update balances automatically |
| **Referential Integrity** | Enforce complex FK rules beyond standard constraints |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A Trigger automatically fires on a DML event (INSERT, UPDATE, DELETE) — never called explicitly.
> 2. **BEFORE Trigger**: fires before the DML; used for data validation and input modification.
> 3. **AFTER Trigger**: fires after the DML; used for auditing and cascading operations.
> 4. BEFORE triggers can abort the operation by raising an error; AFTER triggers cannot.
> 5. Key uses: business rule enforcement, audit logging, task automation, referential integrity.
> 6. INSTEAD OF triggers are used on Views to allow updates on non-updatable views.
> 7. Poorly designed triggers can cause cascading errors and severe performance degradation.

---

> ⚡ **Quick Recall**
> `Trigger → Auto-fires on INSERT/UPDATE/DELETE → BEFORE (validate/abort) → AFTER (audit/cascade) → Uses: Business Rules, Auditing, Automation → Never explicitly called`
