import os

BASE_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Skill Workshop\Power BI"
os.makedirs(BASE_DIR, exist_ok=True)

DAYS_DATA = [
    (11, "DAX_Fundamentals", "DAX Fundamentals & Calculated Columns vs Measures",
     "Measures vs calculated columns, syntax, operators, basic aggregation functions",
     r"""# Day 11: DAX Fundamentals & Calculated Columns vs Measures

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
"""),

    (12, "Essential_DAX_Functions", "Essential DAX Aggregation & Logical Functions",
     "SUM, AVERAGE, COUNT, DISTINCTCOUNT, MIN, MAX, DIVIDE, IF, SWITCH",
     r"""# Day 12: Essential DAX Aggregation & Logical Functions

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
"""),

    (13, "DAX_Filter_Context_and_CALCULATE", "DAX Filter Context & CALCULATE() Mastery",
     "Row context, filter context, context transition, CALCULATE()",
     r"""# Day 13: DAX Filter Context & CALCULATE() Mastery

---

> 📌 **Definition to Remember**
> **CALCULATE()** is the single most powerful function in DAX. It is the only function that can modify, override, expand, or clear the existing **Filter Context** of a visual.

---

### 1. The Two Evaluation Contexts in DAX
1. **Row Context (Iterative):** Knowing the values of the *current single row*. Present in calculated columns and iterator functions (`SUMX`).
2. **Filter Context (Analytical):** The set of active filters applied by slicers, report pages, chart axes, and cross-visual selections.

### 2. Anatomy of `CALCULATE()`
```dax
CALCULATE(
    <Expression / Measure>,
    <Filter_Modifier_1>,
    <Filter_Modifier_2>,
    ...
)
```

### 3. Modifying Filter Context Examples
```dax
// Example 1: Overriding Category Filter
Audio Product Sales = 
CALCULATE(
    [Total Sales],
    Dim_Product[Category] = "Audio"
)

// Example 2: Multiple Filter Conditions (AND logic)
US High Value Sales = 
CALCULATE(
    [Total Sales],
    Dim_Customer[Country] = "United States",
    Fact_Sales[Quantity] > 5
)
```

### 4. Context Transition
When a DAX measure is invoked inside a Row Context (like inside a calculated column or `SUMX`), DAX automatically initiates **Context Transition**, transforming the current row's key into an active Filter Context.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. `CALCULATE()` evaluates all filter arguments *in parallel* first, then evaluates the main expression under the newly modified filter context.
> 2. Explain Context Transition: how invoking a measure turns a row context into a filter context.
> 3. Why `CALCULATE` is the core building block of all advanced BI metrics.

---

> ⚡ **Quick Recall**
> `CALCULATE = Modifies Active Filter Context | Context Transition = Row Context → Filter Context`
"""),

    (14, "Advanced_DAX_Filtering", "Advanced DAX Filter Modifiers",
     "FILTER, ALL, ALLSELECTED, REMOVEFILTERS, KEEPFILTERS",
     r"""# Day 14: Advanced DAX Filter Modifiers

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
"""),

    (15, "DAX_Time_Intelligence", "DAX Time Intelligence Mastery",
     "YTD, MTD, QTD, previous year, previous month, YoY %, rolling averages",
     r"""# Day 15: DAX Time Intelligence Mastery

---

> 📌 **Definition to Remember**
> **Time Intelligence functions** in DAX calculate metrics over specific calendar periods including Year-To-Date (**YTD**), Prior Year comparisons (**YoY Growth**), and moving rolling averages.

---

### 1. Prerequisites for Time Intelligence
- Dedicated Date Table (`Dim_Date`) with contiguous, unbroken dates.
- Mark as Date Table verified in Power BI Desktop.

### 2. Year-To-Date (YTD) & Month-To-Date (MTD)
```dax
// Year To Date Sales
Sales YTD = TOTALYTD([Total Sales], Dim_Date[Date])

// Month To Date Sales
Sales MTD = TOTALMTD([Total Sales], Dim_Date[Date])
```

### 3. Prior Year & YoY Growth % Calculations
```dax
// Previous Year Sales (Same Period Last Year)
Sales PY = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)

// Year-over-Year (YoY) Sales Variance
YoY Sales Growth $ = [Total Sales] - [Sales PY]

// Year-over-Year (YoY) Sales Growth %
YoY Sales Growth % = 
DIVIDE([YoY Sales Growth $], [Sales PY], 0)
```

### 4. Moving Rolling Averages (30-Day Rolling Sales)
```dax
Rolling 30 Days Sales = 
CALCULATE(
    [Total Sales],
    DATESINPERIOD(Dim_Date[Date], MAX(Dim_Date[Date]), -30, DAY)
)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. `SAMEPERIODLASTYEAR()` vs `DATEADD(..., -1, YEAR)`.
> 2. How `DATESYTD` / `TOTALYTD` automatically handle leap years and fiscal year-ends (`"3/31"`).
> 3. Formatting YoY growth with dynamic up/down color indicators (`▲` / `▼`).

---

> ⚡ **Quick Recall**
> `TOTALYTD / TOTALMTD + SAMEPERIODLASTYEAR (Prior Year) + DATESINPERIOD (Rolling Averages)`
"""),

    (16, "Advanced_DAX_Iterators", "Advanced DAX Iterators (X-Functions)",
     "SUMX, AVERAGEX, RANKX, TOPN, VALUES, SELECTEDVALUE, variables",
     r"""# Day 16: Advanced DAX Iterators (X-Functions)

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
"""),

    (17, "DAX_Design_Patterns", "DAX Design Patterns & Dynamic Metrics",
     "Dynamic measures, percentage calculations, ranking, segmentation, Pareto analysis",
     r"""# Day 17: DAX Design Patterns & Dynamic Metrics

---

> 📌 **Definition to Remember**
> **DAX Design Patterns** are standardized, battle-tested architectural templates for solving recurring analytical challenges such as dynamic metric switching, customer segmentation (RFM), and 80/20 Pareto analysis.

---

### 1. Dynamic Metric Selection via Disconnected Tables / Field Parameters
Allow end users to toggle visual metrics (Sales, Profit, Quantity, Margin) from a single slicer:
```dax
Dynamic Metric Value = 
SWITCH(
    SELECTEDVALUE(MetricSelection[MetricName]),
    "Total Sales",   [Total Sales],
    "Total Profit",  [Total Profit],
    "Order Volume",  [Total Quantity],
    "Profit Margin", [Profit Margin %],
    [Total Sales] // Default fallback
)
```

### 2. Dynamic Customer Segmentation
Classifying customers dynamically without hardcoding static columns:
```dax
Customer Segment = 
VAR CustSales = [Total Sales]
RETURN
    SWITCH(
        TRUE(),
        CustSales >= 100000, "Tier 1: High Value",
        CustSales >= 25000,  "Tier 2: Medium Value",
        "Tier 3: Low Value"
    )
```

### 3. Pareto 80/20 Analysis Pattern
Calculating cumulative contribution % to identify the top 20% of products driving 80% of total revenue:
```dax
Cumulative Sales % = 
VAR CurrentSales = [Total Sales]
VAR TotalRevenue = CALCULATE([Total Sales], ALLSELECTED(Dim_Product))
VAR CumulativeSum = 
    CALCULATE(
        [Total Sales],
        FILTER(
            ALLSELECTED(Dim_Product),
            [Total Sales] >= CurrentSales
        )
    )
RETURN
    DIVIDE(CumulativeSum, TotalRevenue, 0)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Creating Field Parameters in Power BI Desktop for seamless visual metric switching.
> 2. How dynamic segmentation responds in real time to date and region slicers.
> 3. Implementing Pareto 80/20 curves on combo charts.

---

> ⚡ **Quick Recall**
> `Field Parameters (Dynamic Metrics) + Dynamic Segmentation + Cumulative Pareto 80/20 Analysis`
"""),

    (18, "Visualization_Fundamentals", "Power BI Visualization Fundamentals",
     "Bar, line, column, area, pie/donut, cards, tables, matrices, KPI visuals",
     r"""# Day 18: Power BI Visualization Fundamentals

---

> 📌 **Definition to Remember**
> **Data Visualization** in Power BI transforms analytical numbers into visual charts to communicate trends, comparisons, proportions, and key performance indicators (KPIs) at a glance.

---

### 1. Core Visual Types & When to Use Them

| Visual Type | Primary Use Case | Best Practices |
| :--- | :--- | :--- |
| **Bar / Column Chart** | Comparing categorical values (e.g., Sales by Region). | Horizontal Bar for long text labels; Vertical Column for time intervals. |
| **Line Chart** | Continuous time-series trends (Monthly Sales YoY). | Keep line count under 4 to avoid visual clutter. |
| **Card / Multi-Row Card** | Prominent executive headline metrics (Total Revenue, Orders). | Pair with dynamic YoY delta indicator and clean typography. |
| **Table vs Matrix** | Tabular data display. | **Matrix** supports multi-level row/column hierarchies & subtotals (Pivot Table). |
| **Donut / Pie Chart** | Part-to-whole proportions. | **Limit to 2-4 slices max**. Never use for fine comparisons. |
| **Area Chart** | Volume trends over time. | Stacked area shows total magnitude along with component contributions. |

### 2. The New Card Visual (Callout Cards)
- Modern multi-metric card supporting custom subtitle micro-text, accent accent bars, dynamic SVGs, and sparklines.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Choosing the right visual for the analytical question (Comparison vs Trend vs Distribution vs Composition).
> 2. Matrix visual features: Drill down, stepped layout, row subtotals, and conditional formatting.
> 3. Eliminating chart junk: Removing unnecessary gridlines, unformatted decimal places, and duplicate axis titles.

---

> ⚡ **Quick Recall**
> `Bar/Column (Comparison) + Line (Trend over time) + Matrix (Hierarchies) + Cards (Headline KPIs)`
"""),

    (19, "Advanced_Visualizations", "Advanced & Specialized Visualizations",
     "Combo charts, decomposition tree, waterfall, funnel, scatter, maps, gauges",
     r"""# Day 19: Advanced & Specialized Visualizations

---

> 📌 **Definition to Remember**
> Advanced visualizations unlock deeper exploratory analysis through multi-axis correlation (**Combo Charts**), variance breakdown (**Waterfall**), AI-powered root-cause discovery (**Decomposition Tree**), and pipeline conversion (**Funnel Charts**).

---

### 1. Specialized Visual Types
1. **Line and Clustered Column (Combo Chart):**
   - Displays volume bars (Sales Revenue) on Primary Y-Axis and margin % line on Secondary Y-Axis.
2. **Waterfall Chart (Variance Walk):**
   - Breaks down financial variances from Budget to Actuals, or Prior Year to Current Year showing positive/negative bridge steps.
3. **Decomposition Tree (AI Visual):**
   - Allows users to dynamically drill down into root-cause dimensions (e.g., Drill into Revenue by Region → Category → Salesperson).
4. **Scatter / Bubble Plot:**
   - Visualizes correlations across 3 dimensions ($X$-Axis, $Y$-Axis, and Bubble Size) with anomaly clustering.
5. **Funnel Chart:**
   - Tracks stage-by-stage drop-off in conversion pipelines (e.g., Lead → Qualified → Demo → Closed Won).
6. **Geographic Maps:**
   - Filled Maps (Choropleth), Bubble Maps, and Azure Map layers with geographic coordinates.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. How to configure Secondary Y-Axis scales on combo charts without misleading readers.
> 2. Use cases for Waterfall charts in financial quarterly earnings reports.
> 3. Leveraging the Decomposition Tree's "High Value / Low Value" AI explainers.

---

> ⚡ **Quick Recall**
> `Combo (Dual Axis) + Waterfall (Variance Walk) + Decomposition Tree (Root Cause AI) + Funnel (Conversion)`
"""),

    (20, "Dashboard_UI_UX_Design", "Dashboard UI/UX & Data Storytelling",
     "Layout, hierarchy, colors, typography, whitespace, navigation, storytelling",
     r"""# Day 20: Dashboard UI/UX & Data Storytelling

---

> 📌 **Definition to Remember**
> **Dashboard UI/UX Design** is the science and art of structuring visual reports to enable effortless cognitive comprehension, clear visual hierarchy, and actionable data-driven decision making.

---

### 1. Principles of Enterprise Dashboard Layout
1. **F-Pattern / Z-Pattern Visual Flow:**
   - Executive eye tracking starts at the **Top-Left** (place primary KPI cards here) and moves to bottom-right (place granular tables here).
2. **Visual Hierarchy:**
   - *Tier 1 (Top):* Headline KPIs (Sales, Margin, YoY Growth).
   - *Tier 2 (Middle):* Diagnostic charts (Trends over time, regional breakdown).
   - *Tier 3 (Bottom):* Operational details (Granular product matrix, transaction tables).
3. **Intentional Color Theory:**
   - Use neutral backgrounds (`#121212` dark or `#F8F9FA` light).
   - Reserve bright accent colors strictly for key insights, targets, and negative alerts (e.g., Red for missed SLA, Green for exceeded target).
   - Never use more than 2-3 primary accent hues.

### 2. Navigation Architecture & Storytelling
- **Page Tabs vs Custom Icon Navigation:** Building sidebar nav bars with bookmark buttons.
- **Micro-Copy & Tooltip Guides:** Providing clear definitions and data refresh timestamps so business users understand metrics without confusion.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. The 5-Second Rule: An executive must understand overall business performance within 5 seconds of opening the dashboard.
> 2. Master whitespace balance, consistent padding, and standard font sizing (Headers 18-20pt, KPI values 24-32pt, Labels 9-10pt).
> 3. Designing accessible, high-contrast dashboards for all users.

---

> ⚡ **Quick Recall**
> `Top-Left KPIs (Tier 1) → Middle Trends (Tier 2) → Bottom Tables (Tier 3) | 5-Second Executive Rule`
""")
]

# Write all days 11-20
for day_num, filename_stem, title, mastery, content in DAYS_DATA:
    fn = f"Day_{day_num:02d}_{filename_stem}.md"
    fp = os.path.join(BASE_DIR, fn)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated second batch of Power BI Skill Workshop notes (Days 11-20) in {BASE_DIR}")
