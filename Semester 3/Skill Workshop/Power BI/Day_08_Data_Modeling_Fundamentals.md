# Day 8: Data Modeling Fundamentals

---

> 📌 **Definition to Remember**
> **Data Modeling** in Power BI is the process of connecting multiple tables through relationship keys to enable accurate cross-table analytical querying and DAX measure evaluations.

---

### 1. Keys & Relationships
- **Primary Key (PK):** A column containing unique values that uniquely identifies each entity in a dimension table (e.g., `CustomerID`).
- **Foreign Key (FK):** A column in a fact table referencing the primary key of a dimension table (e.g., `Orders[CustomerID]`).

### 2. Cardinality Types
1. **One-to-Many (1:*) [Standard & Best Practice]:** One unique record in the Dimension table matches multiple records in the Fact table.
2. **Many-to-One (*:1):** Mirror of 1:*.
3. **One-to-One (1:1):** Both tables share unique matching keys (usually merged into a single table).
4. **Many-to-Many (*:*):** Multiple rows in Table A relate to multiple rows in Table B (requires caution; best resolved using a Bridge table).

### 3. Cross-Filter Direction
- **Single (One-Way):** Filter flows from the **1-side (Dimension)** down to the **\*-side (Fact)**. This is the optimal, performant default.
- **Both (Bi-Directional):** Filter flows in both directions. Can create performance bottlenecks and ambiguous calculation paths.

```
       [Dim_Customer] (1)
              │
              │ (Filter flows DOWN)
              ▼
        [Fact_Sales] (*)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Always prefer Single cross-filter direction over Bi-directional to avoid ambiguous relationship paths.
> 2. Know how to check relationship validity in Model View.
> 3. Understand why a clean relational model is 10x more important than writing complex DAX workarounds.

---

> ⚡ **Quick Recall**
> `Dimension (1) → Fact (*) | Single Cross-Filter Direction | Clean PK-FK Relational Architecture`
