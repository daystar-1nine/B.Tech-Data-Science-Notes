# Data Control Language (DCL) Commands

**Q. What is Data Control Language (DCL)? Explain the concept of user privileges and demonstrate the use of GRANT and REVOKE commands.**

---

> 📌 **Definition to Remember**
> **Data Control Language (DCL)** is a subset of SQL used by **Database Administrators (DBAs)** to control user access and maintain database security. It contains two commands: `GRANT` (give permissions) and `REVOKE` (remove permissions). DCL enforces the **Principle of Least Privilege**.

---

### 1. User Privileges and Access Control
A **Privilege** is a specific permission to perform an action on a database object.

| Privilege Type | Description | Examples |
| :--- | :--- | :--- |
| **System Privileges** | Administrative tasks | `CREATE TABLE`, `CREATE USER` |
| **Object Privileges** | Actions on specific tables/views | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |

### 2. GRANT Command
Gives specific privileges to a user or role.

**Syntax:**
```sql
GRANT privilege_name ON object_name TO user_name [WITH GRANT OPTION];
```
* `WITH GRANT OPTION` allows the receiving user to further grant the privilege to others.

**Examples:**
```sql
-- Grant SELECT and INSERT on Employee table to user 'john'
GRANT SELECT, INSERT ON Employee TO john;

-- Grant all privileges to a manager role
GRANT ALL ON Employee TO manager_role;
```

### 3. REVOKE Command
Removes previously granted privileges from a user or role.

**Syntax:**
```sql
REVOKE privilege_name ON object_name FROM user_name;
```

**Examples:**
```sql
-- Remove INSERT from 'john' (he can still SELECT)
REVOKE INSERT ON Employee FROM john;

-- Remove all privileges from a former employee
REVOKE ALL ON Employee FROM ex_employee_user;
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. DCL controls **who can access** which database objects and **what actions** they can perform.
> 2. Two DCL commands: **GRANT** (give privileges) and **REVOKE** (remove privileges).
> 3. Two types of privileges: **System Privileges** (admin tasks) and **Object Privileges** (table actions).
> 4. `GRANT privilege ON object TO user` — grants specific access.
> 5. `WITH GRANT OPTION` allows the user to further pass the privilege to others.
> 6. `REVOKE privilege ON object FROM user` — removes a specific privilege.
> 7. DCL enforces the **Principle of Least Privilege** — give only the access needed.

---

> ⚡ **Quick Recall**
> `DCL → Security Control → Privileges (System + Object) → GRANT (give access, WITH GRANT OPTION) → REVOKE (remove access) → Principle of Least Privilege`
