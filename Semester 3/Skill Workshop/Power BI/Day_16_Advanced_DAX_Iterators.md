# Day 16: Advanced DAX Iterators (X-Functions)

---

> 📌 **Definition to Remember**
> **Iterator Functions (X-Functions)** like `SUMX`, `AVERAGEX`, and `RANKX` evaluate an expression row-by-row over a specified table, creating a Row Context before aggregating the results.

---

### 1. `SUMX()` vs `SUM()`
- `SUM(Table[Column])` only takes a single physical column.
- `SUMX(Table, Expression)` calculates a dynamic expression for every row and then sums:
```dax
Total Net Revenue = 
SUMX(
    Fact_Sales,
    Fact_Sales[Quantity] * Fact_Sales[UnitPrice] * (1 - Fact_Sales[Discount])
)
```

### 2. Dynamic Ranking: `RANKX()`
```dax
Customer Sales Rank = 
RANKX(
    ALL(Dim_Customer[CustomerName]),
    [Total Sales],
    , // Optional value
    DESC,
    Dense
)
```

### 3. DAX Variables: `VAR ... RETURN`
Variables improve performance (calculated once and cached) and enhance readability:
```dax
Executive KPI Metric = 
VAR CurrentSales = [Total Sales]
VAR PriorSales   = [Sales PY]
VAR Variance     = CurrentSales - PriorSales
VAR GrowthPct    = DIVIDE(Variance, PriorSales, 0)
RETURN
    IF(CurrentSales >= PriorSales, "▲ " & FORMAT(GrowthPct, "0.0%"), "▼ " & FORMAT(GrowthPct, "0.0%"))
```

### 4. `SELECTEDVALUE()`
Returns the single value currently selected in a slicer, or a default fallback if multiple items are selected:
```dax
Dynamic Chart Title = "Sales Analysis for " & SELECTEDVALUE(Dim_Region[RegionName], "All Regions")
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why `VAR` prevents duplicate query execution in complex branching DAX expressions.
> 2. How `RANKX` calculates dynamic ranks across table subsets.
> 3. When to use `SELECTEDVALUE()` for dynamic card titles and parameter cards.

---

> ⚡ **Quick Recall**
> `SUMX/AVERAGEX (Row-by-row iterators) + RANKX (Dynamic ranking) + VAR/RETURN (Cached clean variables)`
