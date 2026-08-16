# Day 25: Row-Level Security (Static & Dynamic RLS)

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
