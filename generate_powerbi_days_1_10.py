import os

BASE_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Skill Workshop\Power BI"
os.makedirs(BASE_DIR, exist_ok=True)

DAYS_DATA = [
    (1, "Power_BI_Fundamentals", "Power BI Fundamentals", 
     "What Power BI is, Desktop vs Service, reports, dashboards, semantic models, dataflows, workspaces, basic workflow",
     """# Day 1: Power BI Fundamentals

---

> 📌 **Definition to Remember**
> **Power BI** is Microsoft's unified enterprise business intelligence and data visualization platform that connects disparate data sources, transforms messy data into relational models, and produces interactive analytical reports and cloud dashboards.

---

### 1. Power BI Ecosystem & Architecture
- **Power BI Desktop:** Free Windows authoring tool used for data connection, Power Query transformation, DAX modeling, and report creation.
- **Power BI Service (SaaS):** Cloud-hosted collaboration platform (app.powerbi.com) used for publishing reports, building real-time dashboards, sharing workspaces, and scheduling automated refreshes.
- **Power BI Mobile:** iOS and Android apps for on-the-go dashboard consumption.
- **Power BI Report Server:** On-premises report server for organizations requiring internal hosting behind firewalls.

### 2. Core Concepts & Terminology
1. **Semantic Model (formerly Dataset):** The heart of Power BI containing data tables, relationships, data types, and DAX measures.
2. **Report:** Multi-page interactive analytical document built on a single semantic model.
3. **Dashboard:** Single-page executive summary board in Power BI Service composed of pinned visual tiles from one or multiple reports.
4. **Dataflow:** Reusable ETL data preparation pipelines built in Power BI Service using Power Query Online.
5. **Workspaces:** Collaborative cloud folders (My Workspace vs Shared Workspaces) where teams manage reports, datasets, and apps.

### 3. End-to-End Power BI Workflow
```
[Data Sources] (Excel/SQL/Web)
       │
       ▼ (Extract & Clean)
[Power Query ETL]
       │
       ▼ (Model & DAX)
[Data Model & Relationships]
       │
       ▼ (Design & Visualize)
[Power BI Desktop Report]
       │
       ▼ (Publish to Cloud)
[Power BI Service (App/Workspace)]
       │
       ▼ (Consume)
[End Users / Mobile / Embedded]
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Differentiate clearly between **Report** (multi-page, single dataset, interactive slicing) and **Dashboard** (single-page, cross-report tiles, cloud only).
> 2. Explain the role of **Semantic Models** as the single source of truth.
> 3. Understand when to use **Power BI Desktop** (authoring) vs **Power BI Service** (collaboration, RLS enforcement, automated refresh).

---

> ⚡ **Quick Recall**
> `Connect Data → Clean in Power Query → Model Relationships → Calculate with DAX → Design Visuals → Publish to Service`
"""),

    (2, "Power_BI_Desktop_Interface", "Power BI Desktop Interface & Navigation",
     "Interface, Report/Data/Model views, Fields pane, Visualizations, Filters, formatting, themes",
     """# Day 2: Power BI Desktop Interface & Navigation

---

> 📌 **Definition to Remember**
> **Power BI Desktop Interface** provides a streamlined 3-view development environment (Report View, Table/Data View, and Model View) along with dedicated panes for Visualizations, Data Fields, Filters, and Format controls.

---

### 1. The Three Primary Workspace Views
1. **Report View (Canvas):** The visual design canvas where charts, cards, slicers, and interactive elements are arranged.
2. **Table / Data View:** Data grid view used to inspect underlying raw tables, preview column values, and verify calculated columns.
3. **Model View (Relationship Canvas):** Diagrammatic canvas used to define primary/foreign key relationships, set cardinality (1:*), and configure cross-filter directions.

### 2. Essential Development Panes
- **Data / Fields Pane:** Lists all imported tables, columns, hierarchies, and DAX measures.
- **Visualizations Pane:** Library of native chart types (Bar, Line, Matrix, Scatter, etc.) and visual property configuration.
- **Format Pane:** Precision formatting controls (colors, fonts, data labels, tooltips, conditional formatting).
- **Filters Pane:** Three scoping tiers:
  1. *Visual-level filters:* Affect only the selected chart.
  2. *Page-level filters:* Affect all visuals on the current page.
  3. *Report-level filters:* Affect all visuals across all report pages.

### 3. Report Canvas Formatting & Global Themes
- **Canvas Sizing:** Standard 16:9 widescreen (1280x720 or 1920x1080) vs Custom tooltip size.
- **JSON Theme Files:** Applying enterprise branding color palettes, typography, and default chart borders across the entire `.pbix` file.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Know how to switch between Report, Table, and Model views.
> 2. Understand the hierarchical evaluation order of visual, page, and report filters.
> 3. Master canvas alignment, snap-to-grid, and grouping objects in the Selection Pane.

---

> ⚡ **Quick Recall**
> `Report View (Canvas) + Table View (Data inspection) + Model View (Relationships) + 3 Filter Tiers (Visual, Page, Report)`
"""),

    (3, "Data_Sources_and_Import_Modes", "Data Sources & Storage Modes",
     "Excel, CSV, SQL Server, Web, folders, APIs, Import vs DirectQuery",
     """# Day 3: Data Sources & Storage Modes

---

> 📌 **Definition to Remember**
> Power BI connects to over 150+ data sources using three primary storage modes: **Import Mode** (in-memory VertiPaq compression), **DirectQuery** (live source pass-through), and **Dual/Composite Mode** (hybrid).

---

### 1. Common Data Sources
- **Flat Files:** Excel (`.xlsx`), CSV (`.csv`), JSON, XML.
- **Folder Connector:** Ingests and combines dozens of identical monthly/daily files into a single unified table automatically.
- **Relational Databases:** SQL Server, Oracle, PostgreSQL, MySQL, IBM Db2.
- **Web & REST APIs:** Pulling live web tables and JSON endpoints with API authentication keys.

### 2. Storage Modes Compared

| Feature | Import Mode | DirectQuery Mode | Composite / Dual Mode |
| :--- | :--- | :--- | :--- |
| **Data Location** | Loaded into memory (RAM) via VertiPaq engine. | Remains at the underlying source (SQL/Snowflake). | Tables set to Import or DirectQuery as needed. |
| **Performance** | **Blazing fast** columnar compression and in-memory cache. | Dependent on backend database speed and network latency. | Optimized: High-speed aggregations with live drilldown. |
| **DAX Capability**| Full, unrestricted DAX function support. | Limited DAX (must translate into native SQL queries). | Full DAX on import tables; translated on DirectQuery. |
| **Data Freshness**| Requires scheduled refresh. | **Real-time** live data on every visual render. | Near real-time with scheduled aggregations. |
| **Dataset Limit** | Up to 1 GB (Pro) or 400 GB (Premium). | No Power BI size limit (handles multi-terabyte data). | Combines massive tables with cached dimensions. |

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why Import Mode is preferred in 90% of BI projects (VertiPaq speed and full DAX support).
> 2. When DirectQuery is mandatory: strict regulatory security, real-time data needs, or massive petabyte datasets.
> 3. How the Folder connector eliminates manual copy-pasting for recurring data drops.

---

> ⚡ **Quick Recall**
> `Import (Fastest, in-memory, scheduled refresh) vs DirectQuery (Live SQL pass-through, real-time, query limits)`
"""),

    (4, "Power_Query_Fundamentals", "Power Query Fundamentals & Query Editor",
     "Query Editor, steps, Applied Steps, data types, rename/remove columns, filtering, sorting",
     """# Day 4: Power Query Fundamentals & Query Editor

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
"""),

    (5, "Power_Query_Data_Cleaning", "Power Query Data Cleaning Techniques",
     "Nulls, errors, duplicates, replace values, split/merge columns, fill, conditional columns",
     """# Day 5: Power Query Data Cleaning Techniques

---

> 📌 **Definition to Remember**
> **Data Cleaning** in Power Query entails resolving missing values (`null`), handling data errors, deduplicating records, splitting compound strings, and creating rule-based conditional columns.

---

### 1. Core Data Cleaning Techniques
1. **Handling Missing Values (`null`):**
   - *Fill Down / Fill Up:* Replaces nulls in grouped hierarchy tables with preceding values.
   - *Replace Values:* Explicitly replaces `null` with `0` for metrics or `"Unknown"` for text categories.
2. **Error Handling:**
   - Identifying data type mismatch errors (`[Error]`).
   - Using *Remove Errors* vs *Replace Errors* with default fallback values.
3. **Removing Duplicates:**
   - Deduplicating on composite business keys (e.g., `CustomerID + OrderDate`) to guarantee dimension uniqueness.
4. **Splitting & Merging Columns:**
   - *Split by Delimiter:* Splitting `"First Last"` by space into separate First Name and Last Name columns.
   - *Merge Columns:* Combining Address, City, and Postal Code into a standardized Full Address.
5. **Conditional Columns:**
   - Visual GUI rule builder creating `IF-THEN-ELSE` classification flags (e.g., `IF Age >= 60 THEN "Senior" ELSE "Adult"`).

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. What causes Power Query data type errors (e.g., text characters in numeric columns) and how to handle them.
> 2. Difference between removing duplicate rows across the whole table vs specific key columns.
> 3. Best practice: Never load raw uncleaned data into the modeling tab.

---

> ⚡ **Quick Recall**
> `Deduplicate → Fill Down Nulls → Handle Errors → Split/Merge Strings → Add Conditional Columns`
"""),

    (6, "Power_Query_Transformations", "Advanced Power Query Transformations",
     "Group By, Pivot/Unpivot, Merge, Append, custom columns, parameters",
     """# Day 6: Advanced Power Query Transformations

---

> 📌 **Definition to Remember**
> Advanced Power Query transformations allow reshaping wide datasets into normalized tall formats (**Unpivot**), aggregating tables (**Group By**), combining row sets (**Append**), and performing relational joins (**Merge**).

---

### 1. The Power of Unpivot Columns
- **Problem:** Financial tables often store months as separate columns (`Jan`, `Feb`, `Mar`...).
- **Solution:** Select ID columns and click **Unpivot Other Columns**.
- **Result:** Transforms wide messy spreadsheets into normalized tall format: `[Attribute: Month]` and `[Value: Amount]`.

```
WIDE FORMAT (Bad for BI):
Product | Jan_Sales | Feb_Sales | Mar_Sales
Widget  | 100       | 150       | 200

TALL FORMAT (Ideal for Data Modeling):
Product | Month | Sales
Widget  | Jan   | 100
Widget  | Feb   | 150
Widget  | Mar   | 200
```

### 2. Append vs Merge Queries

| Transformation | Type | SQL Equivalent | Description |
| :--- | :--- | :--- | :--- |
| **Append Queries** | Vertical Stacking | `UNION ALL` | Combines rows of two or more tables with identical column structures (e.g., 2024 Sales + 2025 Sales). |
| **Merge Queries** | Horizontal Join | `JOIN` | Merges columns from two tables based on matching key columns (Left Outer, Inner, Right Outer, Full Outer, Anti Join). |

### 3. Group By & Custom M Columns
- **Group By:** Aggregates row values (e.g., Total Sales per Customer) directly during ETL.
- **Custom Column:** Adding columns using custom M functions (e.g., `[UnitPrice] * [Quantity] * (1 - [Discount])`).

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why **Unpivot** is essential for dynamic time intelligence and DAX calculations.
> 2. Master the 6 Merge Join types in Power Query (especially Left Anti Join for finding orphan records).
> 3. When to aggregate in Power Query (Group By) vs calculating dynamically in DAX.

---

> ⚡ **Quick Recall**
> `Unpivot (Wide to Tall) + Append (Stack Rows / UNION) + Merge (Join Columns / JOIN) + Group By (ETL Aggregation)`
"""),

    (7, "Power_Query_M_Language", "Power Query + M Language Mastery",
     "M basics, functions, variables, custom functions, reusable transformations",
     """# Day 7: Power Query + M Language Mastery

---

> 📌 **Definition to Remember**
> **M (Mashup Language)** is the functional, case-sensitive programming language that powers all Power Query ETL operations behind the graphical user interface.

---

### 1. Structure of an M Query: `let ... in`
Every M expression is built around a `let` block (defining step variables) and an `in` block (returning final output):

```powerquery
let
    // Step 1: Connect to Source
    Source = Csv.Document(File.Contents("C:\\Data\\Sales.csv"), [Delimiter=",", Columns=4, Encoding=65001]),
    
    // Step 2: Promote Headers
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    
    // Step 3: Change Column Types
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders, {
        {"OrderID", Int64.Type}, 
        {"SalesAmount", type number}, 
        {"OrderDate", type date}
    }),
    
    // Step 4: Filter Rows
    FilteredRows = Table.SelectRows(ChangedTypes, each [SalesAmount] > 0)
in
    FilteredRows
```

### 2. Core M Language Concepts
1. **Case Sensitivity:** Function names and column identifiers are strictly case-sensitive (`Table.SelectRows` != `table.selectrows`).
2. **Immutable Variables:** Each step produces a new table variable reference; variables cannot be overwritten.
3. **Essential M Functions:**
   - `Table.SelectRows()`, `Table.TransformColumnTypes()`, `Table.NestedJoin()`
   - `Text.Proper()`, `Text.Upper()`, `Text.BetweenDelimiters()`
   - `Date.Year()`, `Date.Month()`, `Date.EndOfMonth()`

### 3. Writing Custom Reusable M Functions
Converting a sequence of cleaning steps into a parameterized reusable function:
```powerquery
(inputDate as date) as text =>
let
    FiscalYear = if Date.Month(inputDate) >= 4 
                 then "FY" & Text.End(Text.From(Date.Year(inputDate) + 1), 2) 
                 else "FY" & Text.End(Text.From(Date.Year(inputDate)), 2)
in
    FiscalYear
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Understand the `let ... in` syntax hierarchy.
> 2. How to use Advanced Editor to debug broken ETL steps and parameterize file paths.
> 3. Creating custom M functions for automated date and text parsing.

---

> ⚡ **Quick Recall**
> `let (step definitions) in (output result) — Case-sensitive, functional, non-destructive`
"""),

    (8, "Data_Modeling_Fundamentals", "Data Modeling Fundamentals",
     "Tables, relationships, primary/foreign keys, cardinality, cross-filter direction",
     """# Day 8: Data Modeling Fundamentals

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
"""),

    (9, "Star_Schema_Design", "Star Schema & Dimensional Modeling",
     "Fact vs Dimension tables, date dimension, snowflake vs star schema, model design",
     """# Day 9: Star Schema & Dimensional Modeling

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
              /        \
         [Dim_Date]    [Dim_Store]

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
"""),

    (10, "Advanced_Data_Modeling", "Advanced Data Modeling Techniques",
     "Role-playing dimensions, bridge tables, many-to-many relationships, inactive relationships",
     """# Day 10: Advanced Data Modeling Techniques

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
""")
]

# Write all days
for day_num, filename_stem, title, mastery, content in DAYS_DATA:
    fn = f"Day_{day_num:02d}_{filename_stem}.md"
    fp = os.path.join(BASE_DIR, fn)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated first batch of Power BI Skill Workshop notes in {BASE_DIR}")
