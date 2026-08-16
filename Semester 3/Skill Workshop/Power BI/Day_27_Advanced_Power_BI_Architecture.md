# Day 27: Enterprise Architecture & Semantic Models

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
