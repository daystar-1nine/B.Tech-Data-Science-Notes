# Entity Types & Entity Sets

**Q. Define Entity, Entity Type, and Entity Set. Clearly differentiate between a Strong Entity and a Weak Entity with examples.**

---

> 📌 **Definition to Remember**
> An **Entity** is a single real-world object that has independent existence and can be uniquely identified. An **Entity Type** is a category of entities sharing the same attributes (the blueprint), and an **Entity Set** is the actual collection of all instances of that entity type stored in the database.

---

### 1. Entity, Entity Type, and Entity Set

* **Entity:** A single, specific, real-world object that can be uniquely identified.
  * *Example:* The specific person "John Doe" or a specific car with plate "ABC-123".

* **Entity Type:** A category/template for entities sharing the same attributes. Represented by a **Rectangle** in ER diagrams.
  * *Example:* `STUDENT` is an entity type — all students share Name, Age, and Roll Number.

* **Entity Set:** The actual collection of all entities of a particular type in the database at a given moment.
  * *Example:* All 500 currently enrolled students form the `STUDENT` entity set.

### 2. Strong Entity vs. Weak Entity

Entities are classified based on their ability to be uniquely identified using their own attributes.

#### Strong Entity
* **Definition:** An entity type that possesses its own **Primary Key** to uniquely identify each entity.
* Has an **independent existence** — does not rely on any other entity.
* Represented by a **Single Rectangle** in the ER diagram.
* **Example:** `EMPLOYEE` — uniquely identified by `Employee_ID`. Exists independently.

#### Weak Entity
* **Definition:** An entity type that **does not have its own Primary Key** and cannot be uniquely identified by its own attributes alone.
* **Depends** entirely on a Strong Entity (**Identifying/Owner Entity**) for its existence.
* Its key = Identifying Entity's PK + its own **Partial Key (Discriminator)**.
* Represented by a **Double Rectangle**. Its identifying relationship uses a **Double Diamond**.
* **Example:** `DEPENDENT` (employee's child). Two employees may both have a dependent named "Sarah" — Sarah can only be identified using `Employee_ID + Name`. If the Employee is deleted, the Dependent record is also deleted.

```
  [EMPLOYEE] ══<< DEPENDENTS >>══ [[DEPENDENT]]
  (Strong)    Double Diamond       (Weak)
  Single Rect                     Double Rect
```

### 3. Summary Table

| Feature | Strong Entity | Weak Entity |
| :--- | :--- | :--- |
| **Primary Key** | Has its own Primary Key | Has only a Partial Key (Discriminator) |
| **Existence** | Independent | Depends on a Strong Entity |
| **ER Symbol** | Single Rectangle | Double Rectangle |
| **Relationship** | Single Diamond | Double Diamond (Identifying Relationship) |
| **Example** | `EMPLOYEE` (identified by `Emp_ID`) | `DEPENDENT` (identified by `Emp_ID + Name`) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Entity = single specific object; Entity Type = category template; Entity Set = all instances in DB.
> 2. Entity Types are represented by Rectangles in ER diagrams.
> 3. Strong Entity has its own Primary Key and exists independently.
> 4. Weak Entity has no Primary Key — uses a Partial Key + Owner's PK for identification.
> 5. Weak Entity is represented by a Double Rectangle; its relationship by a Double Diamond.
> 6. If the Strong (Owner) Entity is deleted, the associated Weak Entity must also be deleted.
> 7. Example: `EMPLOYEE` (strong), `DEPENDENT` (weak — relies on Employee_ID).

---

> ⚡ **Quick Recall**
> `Entity (object) → Entity Type (blueprint/Rectangle) → Entity Set (all instances) → Strong (own PK, single rect) → Weak (partial key, double rect, double diamond)`
