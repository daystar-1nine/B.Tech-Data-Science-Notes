# Day 11: DAX Fundamentals & Calculated Columns vs Measures

---

> 📌 **Definition to Remember**
> **DAX (Data Analysis Expressions)** is the native formula and functional expression language of Power BI used to create custom calculations, dynamic business metrics, and tabular evaluations.

---

### 1. Calculated Columns vs Explicit Measures

| Feature | Calculated Column | Explicit DAX Measure |
| :--- | :--- | :--- |
| **Evaluation Timing** | Calculated during data refresh / model load. | **Evaluated on-the-fly** dynamically when visuals render. |
| **Storage (RAM)** | Stored in memory and increases file size. | **Consumes ZERO storage**; calculated dynamically in CPU. |
| **Context** | Evaluates in **Row Context** (row-by-row). | Evaluates in **Filter Context** (respects slicers & visual filters). |
| **Best Used For** | Slicer fields, row categorizations, age buckets. | **All business KPIs, numeric metrics, ratios, & totals.** |

### 2. DAX Syntax & Operators
```dax
// Measure Syntax: MeasureName = FUNCTION(Table[Column])
Total Sales = SUM(Fact_Sales[SalesAmount])

Total Quantity = SUM(Fact_Sales[Quantity])
```
- **Arithmetic:** `+`, `-`, `*`, `/`
- **Comparison:** `=`, `==`, `<>`, `>`, `<`, `>=`, `<=`
- **Logical:** `&&` (AND), `||` (OR), `IN` (Set membership), `NOT`

### 3. Golden Rule of Power BI Development
> **Always use Explicit DAX Measures** for aggregations and numeric metrics. Avoid implicit auto-sums (`Σ Column`) and avoid unnecessary calculated columns to keep model RAM lean.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Clear distinction between Calculated Columns (static, row context, RAM heavy) and Measures (dynamic, filter context, CPU efficient).
> 2. Why explicit measures enable dynamic drilldowns and interactive visual recalculation.
> 3. Standard naming conventions for clean DAX code.

---

> ⚡ **Quick Recall**
> `Calculated Column = Stored in RAM, Row Context | DAX Measure = Computed on-the-fly, Filter Context, Gold Standard`
