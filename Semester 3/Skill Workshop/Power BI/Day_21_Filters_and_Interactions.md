# Day 21: Filters, Slicers & Visual Interactions

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
