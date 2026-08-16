# Day 3: Data Sources & Storage Modes

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
