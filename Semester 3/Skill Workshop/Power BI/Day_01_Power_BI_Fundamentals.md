# Day 1: Power BI Fundamentals

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
