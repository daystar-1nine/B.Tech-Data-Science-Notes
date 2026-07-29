# Entity Relationship (ER) Model

**Q. What is the Entity-Relationship (ER) Model? Discuss its basic concepts and the various symbols used in drawing an ER Diagram.**

---

> 📌 **Definition to Remember**
> The **Entity-Relationship (ER) Model** is a high-level conceptual data model used in database design, developed by **Peter Chen in 1976**. It represents the logical structure of a database graphically using entities, attributes, and relationships — serving as a blueprint before actual RDBMS implementation.

---

### 1. Basic Concepts of ER Model
The ER model is built upon three fundamental concepts:
1. **Entity:** A real-world object or concept with independent existence (e.g., a Student, a Car, a Bank Account).
2. **Attribute:** A property or characteristic that describes an entity (e.g., a Student has Name, Age, Roll_No).
3. **Relationship:** An association or link between two or more entities (e.g., a Student "Enrolls" in a Course).

### 2. ER Diagram
An **ER Diagram** is the graphical representation of the ER Model, serving as the database blueprint. Stakeholders and developers can understand the database architecture without knowing SQL.

### 3. Symbols used in ER Diagram

| Symbol Shape | Represents | Description |
| :--- | :--- | :--- |
| **Rectangle** | Strong Entity | Entity with independent existence (e.g., `Employee`) |
| **Double Rectangle** | Weak Entity | Entity dependent on a strong entity (e.g., `Dependent`) |
| **Ellipse / Oval** | Attribute | Property of an entity (e.g., `Name`) |
| **Underlined Oval** | Key Attribute | Primary key — uniquely identifies entity (e.g., `Roll_No`) |
| **Dashed Oval** | Derived Attribute | Calculated from another attribute (e.g., `Age` from DOB) |
| **Double Oval** | Multi-Valued Attribute | Holds multiple values (e.g., `Phone_Numbers`) |
| **Diamond** | Relationship | How entities interact (e.g., `Works_For`) |
| **Double Diamond** | Identifying Relationship | Connects weak entity to its identifying strong entity |
| **Lines** | Links | Connect attributes to entities and entities to relationships |

### 4. Example ER Model Construction

```
  (Roll_No)   (Name)   ((Phone))
     |           |          |
     └─────────[STUDENT]────┘
                   |
              <ENROLLS_IN>
                   |
               [COURSE]
```
*(Rectangle = Strong Entity, Oval = Attribute, Underlined = Key, Double Oval = Multi-valued, Diamond = Relationship)*

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. ER Model is a high-level conceptual model created by Peter Chen (1976) for database design.
> 2. Three basic concepts: **Entity** (real-world object), **Attribute** (property), **Relationship** (link).
> 3. Rectangle = Strong Entity; Double Rectangle = Weak Entity.
> 4. Underlined Oval = Key Attribute; Dashed Oval = Derived Attribute; Double Oval = Multi-valued Attribute.
> 5. Diamond = Relationship; Double Diamond = Identifying Relationship (for weak entities).
> 6. ER Diagram serves as a database blueprint before SQL implementation.
> 7. ER Diagram makes the database structure clear to non-technical stakeholders.

---

> ⚡ **Quick Recall**
> `ER Model (Peter Chen, 1976) → Entity (Rectangle) → Attribute (Oval types) → Relationship (Diamond) → ER Diagram (blueprint)`
