# Day 13: DAX Filter Context & CALCULATE() Mastery

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
