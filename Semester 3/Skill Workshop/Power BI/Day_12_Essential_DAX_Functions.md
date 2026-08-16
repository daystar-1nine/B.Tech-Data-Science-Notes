# Day 12: Essential DAX Aggregation & Logical Functions

---

> 📌 **Definition to Remember**
> Essential DAX functions provide standard mathematical aggregations (`SUM`, `AVERAGE`, `COUNT`), safe division (`DIVIDE`), and conditional branching logic (`IF`, `SWITCH`).

---

### 1. Core Mathematical & Aggregation Functions
```dax
// Sum and Average
Total Revenue = SUM(Fact_Sales[Revenue])
Average Order Value = AVERAGE(Fact_Sales[Revenue])

// Row Counts
Total Orders = COUNT(Fact_Sales[OrderID])
Unique Customers = DISTINCTCOUNT(Fact_Sales[CustomerID])
Total Rows = COUNTROWS(Fact_Sales)
```

### 2. Safe Mathematical Division: `DIVIDE()`
Always use `DIVIDE()` instead of the standard `/` operator to eliminate divide-by-zero crashes:
```dax
Profit Margin % = 
DIVIDE(
    [Total Profit], 
    [Total Revenue], 
    0 // Alternate fallback result when denominator is 0 or null
)
```

### 3. Conditional Logical Branching: `IF()` vs `SWITCH()`
```dax
// Using IF for single condition
Discount Tier = 
IF(
    [Total Sales] > 100000, 
    "Platinum", 
    "Standard"
)

// Using SWITCH(TRUE(), ...) for multi-condition evaluation (Cleaner than nested IFs)
Customer Performance Rating = 
SWITCH(
    TRUE(),
    [Total Sales] >= 500000, "Tier 1: Enterprise Leader",
    [Total Sales] >= 100000, "Tier 2: Key Strategic Account",
    [Total Sales] >= 25000,  "Tier 3: Growth Customer",
    "Tier 4: Standard Customer"
)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why `DIVIDE(A, B, 0)` is safer and faster than `IF(B = 0, 0, A / B)`.
> 2. Difference between `COUNT()` (ignores blanks), `COUNTROWS()` (table row count), and `DISTINCTCOUNT()`.
> 3. Mastering `SWITCH(TRUE(), ...)` for clean multi-tier business logic.

---

> ⚡ **Quick Recall**
> `SUM / AVERAGE / DISTINCTCOUNT + DIVIDE(Safe Division) + SWITCH(TRUE(), conditions)`
