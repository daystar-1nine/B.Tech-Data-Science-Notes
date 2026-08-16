# Day 23: Power BI Service & Collaboration

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
