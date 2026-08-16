# Day 10: Advanced Data Modeling Techniques

---

> 📌 **Definition to Remember**
> Advanced data modeling addresses complex relational patterns including **Role-Playing Dimensions** (multiple date keys), **Inactive Relationships** (activated via `USERELATIONSHIP`), and **Bridge Tables** for Many-to-Many resolution.

---

### 1. Role-Playing Dimensions & Inactive Relationships
- **Problem:** `Fact_Sales` has both `OrderDate`, `ShipDate`, and `DeliveryDate`, all needing the `Dim_Date` table.
- **Solution 1 (Recommended):** Create one Active relationship (`OrderDate` to `Date`) and multiple **Inactive Relationships** (dotted lines) for `ShipDate` and `DeliveryDate`.
- **Activating via DAX:**
```dax
Shipped Sales = 
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Fact_Sales[ShipDateKey], Dim_Date[DateKey])
)
```

### 2. Resolving Many-to-Many (*:*) Relationships via Bridge Tables
- Instead of using native direct Many-to-Many relationships, introduce an intermediate distinct **Bridge Table** with 1:* relationships on both sides:
```
[Table_Students] (1) ──> (*) [Bridge_Enrollment] (*) <── (1) [Table_Courses]
```

### 3. Parent-Child Hierarchies (Organization Charts)
- Flattening manager-employee hierarchies using DAX `PATH()` and `PATHITEM()` functions.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. When to use `USERELATIONSHIP()` with inactive relationships vs duplicating the Date dimension table.
> 2. How Bridge tables prevent Cartesian product inflation in Many-to-Many scenarios.
> 3. Best practice for handling multiple transaction dates in fact tables.

---

> ⚡ **Quick Recall**
> `Active Relationship (Default) + Inactive Relationship (Activated via USERELATIONSHIP) + Bridge Table (*:*)`
