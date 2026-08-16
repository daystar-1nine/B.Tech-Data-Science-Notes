# Day 14: Advanced DAX Filter Modifiers

---

> 📌 **Definition to Remember**
> Filter modifier functions (`ALL`, `ALLSELECTED`, `REMOVEFILTERS`, `KEEPFILTERS`, `FILTER`) work inside `CALCULATE()` to explicitly control which dimension filters are removed, preserved, or dynamically evaluated.

---

### 1. `ALL()` vs `REMOVEFILTERS()` — Calculating % of Total
`ALL()` removes all filters from a table or column, returning all rows:
```dax
// Grand Total Sales (Ignores all product/category slicers)
Grand Total Sales = 
CALCULATE(
    [Total Sales],
    ALL(Dim_Product)
)

// Contribution % to Grand Total
Product Sales % of Total = 
DIVIDE([Total Sales], [Grand Total Sales], 0)
```

### 2. `ALLSELECTED()` — Dynamic Visual Contribution %
`ALLSELECTED()` removes visual internal axis filters while **preserving external user slicer selections**:
```dax
Sales % of Sliced Selection = 
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALLSELECTED(Dim_Product[Category])),
    0
)
```

### 3. The `FILTER()` Iterator Function
`FILTER(Table, Condition)` iterates through a table row-by-row to apply complex measure-based filtering:
```dax
Sales from High Margin Products = 
CALCULATE(
    [Total Sales],
    FILTER(
        Dim_Product,
        [Profit Margin %] > 0.25 // Filtering by a dynamic measure
    )
)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Differentiate between `ALL()` (ignores everything) and `ALLSELECTED()` (respects user slicers).
> 2. Why `REMOVEFILTERS()` is the modern, semantic replacement for `ALL()` as a filter modifier.
> 3. Performance tip: Do NOT wrap simple column comparisons inside `FILTER()` unless filtering by a dynamic measure.

---

> ⚡ **Quick Recall**
> `ALL (Clear all filters) + ALLSELECTED (Clear axis but keep slicers) + FILTER (Table iterator for complex criteria)`
