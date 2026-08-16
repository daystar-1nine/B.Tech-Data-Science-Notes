# Day 9: Star Schema & Dimensional Modeling

---

> 📌 **Definition to Remember**
> A **Star Schema** is the gold-standard dimensional data modeling architecture for Power BI where a central **Fact Table** (containing numeric measures and keys) is surrounded by multiple **Dimension Tables** (containing descriptive business context).

---

### 1. Fact Tables vs Dimension Tables

| Feature | Fact Table | Dimension Table |
| :--- | :--- | :--- |
| **Content** | Quantitative metrics, transactions, numbers. | Descriptive text attributes, categories, hierarchies. |
| **Examples** | `Fact_Sales`, `Fact_Orders`, `Fact_Inventory`. | `Dim_Customer`, `Dim_Product`, `Dim_Date`, `Dim_Store`. |
| **Granularity**| Transactional event level (e.g., one row per line item). | Entity level (e.g., one row per unique customer). |
| **Row Count** | Millions / Billions of rows (Tall & Narrow). | Hundreds / Thousands of rows (Short & Wide). |

### 2. Star Schema vs Snowflake Schema

```
STAR SCHEMA (Recommended for Power BI):
       [Dim_Product]    [Dim_Customer]
              \        /
               [Fact_Sales]
              /                 [Dim_Date]    [Dim_Store]

SNOWFLAKE SCHEMA (Normalized dimensions — sub-tables):
    [Dim_Category] → [Dim_SubCat] → [Dim_Product] → [Fact_Sales]
```

### 3. The Dedicated Date Dimension Table (`Dim_Date`)
- Mandatory for all Power BI models to support accurate DAX Time Intelligence.
- Must cover full contiguous years without missing dates.
- Key columns: `Date`, `Year`, `MonthNumber`, `MonthName`, `Quarter`, `DayOfWeek`, `FiscalYear`.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why Power BI's VertiPaq engine is heavily optimized for Star Schema architectures.
> 2. Why Snowflake schemas should be flattened into a Star Schema in Power Query.
> 3. Why every professional BI model must have a dedicated, marked Date table.

---

> ⚡ **Quick Recall**
> `Central Fact Table + Surrounding Dimension Tables + Dedicated Date Dimension = Peak Power BI Performance`
