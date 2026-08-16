import os

BASE_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Skill Workshop\Power BI"
os.makedirs(BASE_DIR, exist_ok=True)

DAYS_DATA = [
    (21, "Filters_and_Interactions", "Filters, Slicers & Visual Interactions",
     "Slicers, visual/page/report filters, drillthrough, cross-filtering, edit interactions",
     r"""# Day 21: Filters, Slicers & Visual Interactions

---

> 📌 **Definition to Remember**
> **Visual Interactions and Slicers** govern how user selections on one visual filter or highlight related charts across report pages, configured via **Edit Interactions** and **Drillthrough filters**.

---

### 1. The 3 Interaction Modes (Edit Interactions)
When an element is selected on Chart A, Chart B can behave in one of three ways:
1. **Filter (Icon: Filter funnel):** Filters Chart B to show *only* data matching the selection.
2. **Highlight (Icon: Pie chart):** Keeps all data visible in Chart B but visually highlights the selected proportion (default behavior for bar charts).
3. **None (Icon: Blocked circle):** Ignores selections on Chart A completely.

### 2. Page-to-Page Drillthrough
- Allows users to right-click a data point (e.g., Customer "Acme Corp") and navigate to a dedicated **Customer Deep-Dive Page** with all visual filters automatically carried over.
- Configured by placing target dimension fields in the **Drillthrough Well** of the destination page.

### 3. Slicer Types & Enhancements
- Hierarchy Slicers, Tile Slicers, Between Date Sliders, Relative Date Slicers (e.g., "Last 30 Days", "This Quarter").

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why switching visual interactions from Highlight to Filter creates cleaner reports for executive users.
> 2. How to configure cross-report and intra-report Drillthrough.
> 3. Disabling slicer interaction on static benchmark cards.

---

> ⚡ **Quick Recall**
> `Edit Interactions (Filter vs Highlight vs None) + Drillthrough (Deep-Dive Pages) + Slicers`
"""),

    (22, "Advanced_Report_Features", "Bookmarks, Buttons & Dynamic Tooltips",
     "Bookmarks, buttons, tooltips, field parameters, page navigation, conditional formatting",
     r"""# Day 22: Bookmarks, Buttons & Dynamic Tooltips

---

> 📌 **Definition to Remember**
> Advanced report authoring features turn static dashboards into rich, app-like interactive experiences using **Bookmarks**, **Action Buttons**, **Report Page Tooltips**, and **Rules-Based Conditional Formatting**.

---

### 1. Bookmarks & Selection Pane Workflows
- **Bookmark State:** Captures visual visibility (hide/show in Selection pane), active slicers, and sort order.
- **Common Bookmark Use Cases:**
  - *Slide-out Filter Panels / Popover Drawers.*
  - *Chart Switchers (Toggle between Bar Chart and Matrix Table views).*
  - *Clear All Filters Button.*

### 2. Custom Report Page Tooltips
- Creating a tiny, dedicated tooltip canvas (e.g., 320x240 px) with micro-charts.
- When hovering over a customer or product in a main chart, the custom tooltip renders a live 12-month sales trend specifically for that hovered entity.

### 3. Dynamic Conditional Formatting
- Formatting background colors, font colors, data bars, and icons based on DAX rules or hex color code measures:
```dax
KPI Background Color = 
IF([YoY Sales Growth %] >= 0, "#00C853", "#D50000")
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Difference between Bookmark Data property checked (saves slicer state) vs unchecked (UI toggle only).
> 2. Creating custom Report Page Tooltips.
> 3. Hex code measure-driven conditional formatting.

---

> ⚡ **Quick Recall**
> `Bookmarks (State capture) + Buttons (Actions) + Report Page Tooltips (Hover charts) + Hex DAX Formatting`
"""),

    (23, "Power_BI_Service", "Power BI Service & Collaboration",
     "Publishing, workspaces, apps, sharing, permissions, dashboards, subscriptions",
     r"""# Day 23: Power BI Service & Collaboration

---

> 📌 **Definition to Remember**
> **Power BI Service** is the cloud SaaS platform (app.powerbi.com) where published semantic models and reports are organized into workspaces, packaged into enterprise **Power BI Apps**, and shared securely across organizations.

---

### 1. Workspaces & Workspace Roles
- **Workspaces:** Staging and development environments for BI teams.

| Workspace Role | Permissions & Capabilities |
| :--- | :--- |
| **Admin** | Full control: delete workspace, manage user access, update gateway connections. |
| **Member** | Add/edit reports, build apps, manage permissions for lower roles. |
| **Contributor** | Create, edit, and publish reports and datasets (cannot publish apps or manage users). |
| **Viewer** | Read-only access: interact with reports and visuals (cannot edit or see underlying DAX). |

### 2. Power BI Apps vs Direct Sharing
- **Power BI App:** The official enterprise distribution mechanism. Packages approved reports into a unified portal with customized left-hand navigation and role-based audience management.
- **Direct Sharing:** Quick sharing with individual email addresses (best for ad-hoc reviews).

### 3. Automated Subscriptions & Alerts
- Email snapshot subscriptions delivered to executives daily at 8:00 AM.
- Data-driven threshold alerts triggered when KPI metrics breach thresholds.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Why enterprise deployments distribute reports via **Power BI Apps** instead of giving users direct workspace access.
> 2. Explaining the 4 Workspace Roles (Admin, Member, Contributor, Viewer).
> 3. Setting up data-driven alert notifications.

---

> ⚡ **Quick Recall**
> `Desktop (Author) → Workspaces (Dev Team Roles) → Power BI Apps (End-User Distribution)`
"""),

    (24, "Data_Refresh_and_Gateways", "Data Refresh & On-Premises Gateways",
     "Scheduled refresh, on-premises gateway, credentials, refresh failures, incremental refresh",
     r"""# Day 24: Data Refresh & On-Premises Gateways

---

> 📌 **Definition to Remember**
> The **On-Premises Data Gateway** acts as a secure cryptographic bridge that enables Power BI Service cloud datasets to query and refresh data from local on-premises databases and network file shares.

---

### 1. Gateway Types & Architecture
- **Standard Mode (Enterprise Gateway):** Installed on a dedicated server; supports multiple users, scheduled refreshes, and DirectQuery live connections across enterprise SQL and Oracle servers.
- **Personal Mode:** Installed on a single developer's workstation; supports only scheduled refresh for one user.

```
[Power BI Service Cloud]
         │ (Encrypted HTTPS Port 443)
         ▼
[On-Premises Gateway Service] (Behind Corporate Firewall)
         │ (Local Network Query)
         ▼
[Local SQL Server / Excel Files]
```

### 2. Scheduled Refresh Limits
- **Power BI Pro:** Up to **8 scheduled refreshes per day** per semantic model.
- **Power BI Premium / Fabric:** Up to **48 scheduled refreshes per day** (or sub-minute with incremental refresh).

### 3. Incremental Refresh
- Instead of reloading 10 years of historical data on every daily refresh, Incremental Refresh:
  - Archives historical partitions (read-only).
  - Only queries and refreshes the last *N* days of modified data (`RangeStart` and `RangeEnd` parameters).

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. How the On-Premises Gateway works without opening inbound corporate firewall ports.
> 2. Diagnosing common refresh failures (expired credentials, network timeouts, M query folding breaks).
> 3. Configuring Incremental Refresh with `RangeStart` and `RangeEnd`.

---

> ⚡ **Quick Recall**
> `Enterprise Gateway (Secure Firewall Bridge) + Scheduled Refresh (8x Pro / 48x Premium) + Incremental Refresh`
"""),

    (25, "Row_Level_Security_RLS", "Row-Level Security (Static & Dynamic RLS)",
     "Roles, DAX filters, dynamic RLS, USERPRINCIPALNAME, security testing",
     r"""# Day 25: Row-Level Security (Static & Dynamic RLS)

---

> 📌 **Definition to Remember**
> **Row-Level Security (RLS)** restricts data access for given users at the dataset level, ensuring that regional managers or sales reps only see the specific rows of data they are authorized to view in a single shared report.

---

### 1. Static RLS (Hardcoded Role Rules)
- Creating fixed roles in Power BI Desktop (Modeling → Manage Roles):
```dax
// Role: US_East_Manager (Filter on Dim_Store)
Dim_Store[Region] = "US East"

// Role: EMEA_Sales (Filter on Dim_Geography)
Dim_Geography[Continent] = "Europe"
```
- In Power BI Service: Assign user security groups or emails to each defined role.

### 2. Dynamic RLS (User-Driven via `USERPRINCIPALNAME()`)
- Scales to thousands of users with a single unified security role using an **User Access Mapping Table**:

```
[UserSecurityTable]
Email                  | AllowedRegion
john.doe@company.com   | US East
maria.garcia@company.com| LATAM
```

- **Dynamic DAX Filter on User Security Table:**
```dax
[UserEmail] = USERPRINCIPALNAME()
```
- Filters propagate through relationships from the security table down to fact tables automatically.

### 3. Testing RLS in Desktop & Service
- *Power BI Desktop:* Modeling → **View as Roles** → Enter test user email.
- *Power BI Service:* Dataset Security → **Test as role**.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Static RLS vs Dynamic RLS: Why dynamic RLS is essential for scalable enterprise deployments.
> 2. Functions: `USERPRINCIPALNAME()` (returns `user@domain.com`) vs `USERNAME()`.
> 3. RLS applies strictly to users with **Viewer** permissions; Admins/Members bypass RLS.

---

> ⚡ **Quick Recall**
> `Static RLS (Fixed Roles) vs Dynamic RLS (USERPRINCIPALNAME() + Security Mapping Table)`
"""),

    (26, "Performance_Optimization", "Performance Optimization & VertiPaq Engine",
     "Performance Analyzer, DAX optimization, model size, cardinality, query performance",
     r"""# Day 26: Performance Optimization & VertiPaq Engine

---

> 📌 **Definition to Remember**
> **Performance Optimization** in Power BI involves reducing semantic model memory footprint and tuning DAX queries to ensure visual rendering completes in **under 1-2 seconds**.

---

### 1. Using the Performance Analyzer
- Built-in diagnostic tool (View → Performance Analyzer) recording 3 visual cost components:
  1. **DAX Query Time:** Time taken by the VertiPaq engine to evaluate calculations.
  2. **Visual Display Time:** Time taken by the frontend browser to render charts.
  3. **Other (Queue Wait):** Background thread concurrency delays.

### 2. Column Cardinality & VertiPaq Compression
- VertiPaq stores data **column-by-column** using Dictionary, Run-Length (RLE), and Bit-Packed compression.
- **Cardinality (Number of Unique Values):** High cardinality columns (e.g., timestamps with milliseconds, GUID transaction keys) destroy compression and bloat model RAM.
- **Optimization:** Split `DateTime` into separate `Date` and `Time` columns, or remove high-cardinality surrogate keys from the fact table.

### 3. DAX Optimization Best Practices
- Avoid iterating full tables with `FILTER(AllTable, ...)` when simple column filters suffice.
- Store repeated calculations in `VAR` to prevent double evaluations.
- Use `COUNTROWS(Table)` instead of `COUNT(Table[Column])`.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. How to diagnose visual rendering lag with Performance Analyzer.
> 2. What column cardinality is and why reducing it drastically shrinks `.pbix` file size.
> 3. Using DAX Studio and Tabular Editor for advanced query plan and VertiPaq metrics analysis.

---

> ⚡ **Quick Recall**
> `Performance Analyzer + Reduce Column Cardinality + Split DateTimes + Cache VARs in DAX`
"""),

    (27, "Advanced_Power_BI_Architecture", "Enterprise Architecture & Semantic Models",
     "Import vs DirectQuery vs Composite models, aggregations, semantic models, deployment concepts",
     r"""# Day 27: Enterprise Architecture & Semantic Models

---

> 📌 **Definition to Remember**
> **Enterprise Power BI Architecture** decouples data modeling from report visualization through **Golden Semantic Models (Hub-and-Spoke)**, User Aggregations, and Deployment Pipelines.

---

### 1. Hub-and-Spoke Architecture (Thin Reports)
- **Anti-Pattern (Siloed):** 20 separate `.pbix` files, each connecting to SQL and duplicating ETL and DAX logic.
- **Enterprise Best Practice (Hub-and-Spoke):**
  - **Hub:** One single, centralized, certified **Golden Semantic Model** maintained by BI engineers.
  - **Spokes (Thin Reports):** Dozens of department reports connect live to the Golden Model via **Power BI Dataset Live Connection**.

```
             [Golden Semantic Model] (Single Source of Truth)
                      │
     ┌────────────────┼────────────────┐
     ▼                ▼                ▼
[Sales Report] [Finance Report] [Operations Report]
```

### 2. User-Defined Aggregations
- Pair a massive DirectQuery fact table (billions of rows) with an in-memory Import aggregation table (summarized by month/region).
- Queries automatically hit the blazing-fast in-memory aggregation table, only querying the live database when drilling down to individual transaction seconds.

### 3. Deployment Pipelines (Dev → Test → Prod)
- Automated lifecycle management promoting reports and datasets across Development, Staging/Test, and Production workspaces.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Benefits of the Hub-and-Spoke architecture for enterprise governance and metric consistency.
> 2. How User-Defined Aggregations deliver in-memory speed over big data lakes.
> 3. Implementing Dev/Test/Prod Deployment Pipelines in Power BI Service.

---

> ⚡ **Quick Recall**
> `Golden Semantic Model (Single Source of Truth) + Thin Reports + Deployment Pipelines (Dev → Test → Prod)`
"""),

    (28, "AI_and_Advanced_Analytics", "AI & Advanced Analytics in Power BI",
     "Forecasting, anomaly detection, Q&A, decomposition tree, Key Influencers, Copilot concepts",
     r"""# Day 28: AI & Advanced Analytics in Power BI

---

> 📌 **Definition to Remember**
> Power BI integrates native Machine Learning and Generative AI capabilities to automate insight discovery, time-series forecasting, automated anomaly detection, and natural language querying (**Q&A & Copilot**).

---

### 1. Built-in Machine Learning Visuals
1. **Key Influencers Visual:**
   - Uses logistic/linear regression to rank what factors drive a specific business outcome (e.g., "What factors influence a customer churn status being True?").
2. **Decomposition Tree with AI Splits:**
   - Automatically finds the dimension with the highest or lowest contribution to a metric drilldown.
3. **Smart Narrative:**
   - Auto-generates dynamic text summaries of active charts that recalculate when slicers change.

### 2. Time-Series Forecasting & Anomaly Detection
- **Forecasting:** Adds predictive confidence bands (70%, 80%, 95% confidence intervals) to line charts based on exponential smoothing algorithms.
- **Anomaly Detection:** Identifies statistically significant outliers in time-series data with automated diagnostic explainers.

### 3. Q&A & Copilot Integration
- **Q&A Natural Language Visual:** Allows non-technical stakeholders to type plain-English questions (e.g., "Show top 5 sales reps by profit in 2025 as a bar chart").
- **Copilot in Power BI:** AI assistant capable of drafting DAX measures, summarizing report pages, and suggesting chart layouts.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Configuring the Key Influencers visual for churn, lead conversion, or CSAT scoring.
> 2. Tuning time-series forecasting seasonality and confidence intervals.
> 3. Optimizing the Semantic Model Q&A linguistic schema with synonyms.

---

> ⚡ **Quick Recall**
> `Key Influencers (Regression drivers) + Anomaly Detection (Outliers) + Smart Narrative + Q&A / Copilot`
"""),

    (29, "Real_World_Project", "End-to-End Professional BI Project",
     "Build a complete professional business intelligence dashboard from raw data",
     r"""# Day 29: End-to-End Professional BI Project

---

> 📌 **Definition to Remember**
> Building a production-grade Business Intelligence dashboard requires executing the complete lifecycle: raw data ingestion, dimensional star schema modeling, core DAX metric development, executive UI design, and cloud deployment.

---

### 1. Project Scenario: Global Enterprise Executive Sales Dashboard
- **Objective:** Enable the C-Suite and regional directors to monitor $50M+ in annual revenue, gross margins, customer retention, and regional performance.

### 2. Step-by-Step Implementation Roadmap

#### Step 1: Power Query ETL
- Connect to raw multi-table CSV and SQL staging extracts.
- Unpivot monthly targets; clean and standardize product categories.
- Build contiguous `Dim_Date` dimension with Fiscal Year logic.

#### Step 2: Star Schema Modeling
- Link `Fact_Sales` and `Fact_Targets` to `Dim_Product`, `Dim_Customer`, `Dim_Date`, and `Dim_Region` using strict 1:* single cross-filter relationships.

#### Step 3: DAX Core Measures Suite
```dax
// 1. Total Revenue & Margin
Total Revenue = SUM(Fact_Sales[SalesAmount])
Total Cost = SUM(Fact_Sales[CostAmount])
Gross Profit = [Total Revenue] - [Total Cost]
Margin % = DIVIDE([Gross Profit], [Total Revenue], 0)

// 2. Target Variance
Target Revenue = SUM(Fact_Targets[TargetAmount])
Variance to Target $ = [Total Revenue] - [Target Revenue]
Target Achievement % = DIVIDE([Total Revenue], [Target Revenue], 0)

// 3. Time Intelligence
Revenue PY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(Dim_Date[Date]))
YoY Growth % = DIVIDE([Total Revenue] - [Revenue PY], [Revenue PY], 0)
```

#### Step 4: UI/UX Dashboard Layout
- **Header:** Executive summary cards (Revenue, Gross Margin, Target Achievement %, YoY Growth %).
- **Left:** Interactive sidebar filter drawer.
- **Center:** Monthly Revenue vs Target combo chart & Waterfall variance bridge.
- **Bottom:** Top 10 Product Matrix & Regional performance filled map.

#### Step 5: Service Deployment & RLS
- Configure Dynamic RLS by Regional Manager.
- Publish to Production Workspace, set up daily 7:00 AM Gateway scheduled refresh, and publish the Power BI App.

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Ability to walk an interviewer through the entire architecture from raw data to published app.
> 2. How you handled messy edge cases during ETL and optimized DAX calculation times.
> 3. Documenting business requirements and stakeholder KPIs.

---

> ⚡ **Quick Recall**
> `Raw Data → Power Query ETL → Star Schema → DAX Measure Suite → Executive UI → RLS & App Publish`
"""),

    (30, "Portfolio_and_Interview_Mastery", "Portfolio & Interview Mastery",
     "Project documentation, dashboard presentation, DAX interview questions, SQL + Power BI questions, portfolio",
     r"""# Day 30: Portfolio & Interview Mastery

---

> 📌 **Definition to Remember**
> Landing top Power BI and Data Analytics roles requires a polished GitHub & NovyPro portfolio, comprehensive project case studies, and mastery of top technical DAX, SQL, and modeling interview questions.

---

### 1. Building a Standout BI Portfolio
1. **Interactive Hosting on NovyPro:**
   - Host live, clickable Power BI reports using web embeds with background device frames.
2. **GitHub Project Case Study Documentation:**
   - **Business Problem Statement:** What operational inefficiency was solved.
   - **Data Architecture Diagram:** Star schema model screenshot.
   - **Key DAX Formulas:** Code snippets with explanation of filter context handling.
   - **Business Insights & Impact:** 3-5 actionable decisions uncovered by the dashboard.

### 2. Top 10 Power BI Interview Questions & Model Answers

#### Q1. What is the difference between Calculated Columns and Measures?
- *Answer:* Calculated columns evaluate during data refresh in row context and consume RAM. Measures evaluate dynamically on visual query render in filter context and consume zero storage.

#### Q2. Explain `CALCULATE()` and Context Transition.
- *Answer:* `CALCULATE()` modifies the active filter context. Context transition occurs when a measure is invoked inside a row context, converting the current row keys into equivalent filter context constraints.

#### Q3. What is the difference between `ALL()` and `ALLSELECTED()`?
- *Answer:* `ALL()` removes all filters from a table or column unconditionally. `ALLSELECTED()` removes internal visual grouping filters while preserving external slicer selections.

#### Q4. Why is Star Schema preferred over Snowflake Schema in Power BI?
- *Answer:* Power BI's VertiPaq engine optimizes memory scan speed when relationships are shallow. Star schemas require fewer joins, resulting in faster DAX performance and simpler measures.

#### Q5. How does Dynamic Row-Level Security work?
- *Answer:* Dynamic RLS matches the current logged-in user email via `USERPRINCIPALNAME()` against an internal security mapping table, filtering fact table data automatically.

---

> ⭐ **Must-Master Skills & Final Checklist**
> 1. Complete all 30 Days of hands-on practice.
> 2. Build and publish at least 2 end-to-end dashboards to your online portfolio.
> 3. Master DAX filter context explanation with confidence in technical interviews.

---

> ⚡ **Quick Recall**
> `NovyPro Live Dashboards + GitHub Case Studies + Core DAX / Modeling Interview Mastery = Job Ready!`
""")
]

# Write all days 21-30
for day_num, filename_stem, title, mastery, content in DAYS_DATA:
    fn = f"Day_{day_num:02d}_{filename_stem}.md"
    fp = os.path.join(BASE_DIR, fn)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated third batch of Power BI Skill Workshop notes (Days 21-30) in {BASE_DIR}")
