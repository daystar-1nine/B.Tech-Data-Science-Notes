# Day 22: Bookmarks, Buttons & Dynamic Tooltips

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
