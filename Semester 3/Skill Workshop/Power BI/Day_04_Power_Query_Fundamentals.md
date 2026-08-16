# Day 4: Power Query Fundamentals & Query Editor

---

> 📌 **Definition to Remember**
> **Power Query** is the ETL (Extract, Transform, Load) data preparation engine in Power BI used to clean, reshape, and transform raw data before loading it into the data model.

---

### 1. Power Query Editor Interface
- **Queries Pane (Left):** Lists all data connections and staging queries.
- **Data Preview Grid (Center):** Interactive tabular preview of transformations.
- **Applied Steps Pane (Right):** Sequential recorded pipeline of transformations executed from top to bottom.
- **Formula Bar (Top):** Displays the underlying **M Language code** for the selected transformation step.

### 2. Fundamental Transformation Operations
1. **Promote First Row as Headers:** Converts top data row into official column names.
2. **Explicit Data Typing:** Setting accurate types (`Int64`, `Decimal`, `Text`, `Date`, `DateTime`, `True/False`) to avoid memory bloat and calculation bugs.
3. **Remove / Keep Columns:** Eliminating unnecessary columns at the ETL stage to minimize semantic model size.
4. **Row Filtering & Sorting:** Filtering out irrelevant historical years, test records, or blank rows.
5. **Rename & Reorder Columns:** Creating clean, business-friendly attribute names for end-user clarity.

### 3. Query Properties
- **Enable Load:** Unchecking prevents staging/temporary lookup queries from consuming RAM in the report model.
- **Include in Report Refresh:** Disabling static tables (e.g., country codes) to accelerate daily refresh times.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. All Power Query steps are non-destructive and replayable via the **Applied Steps** chain.
> 2. Always filter and remove unused columns as early as possible in Power Query.
> 3. Understand why explicit data typing prevents silent DAX type coercion errors.

---

> ⚡ **Quick Recall**
> `Extract → Promote Headers → Enforce Data Types → Filter & Drop Columns → Applied Steps Pipeline → Load`
