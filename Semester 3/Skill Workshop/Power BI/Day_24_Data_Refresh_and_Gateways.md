# Day 24: Data Refresh & On-Premises Gateways

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
