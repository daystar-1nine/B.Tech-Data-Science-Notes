# Day 17: DAX Design Patterns & Dynamic Metrics

---

> 📌 **Definition to Remember**
> **DAX Design Patterns** are standardized, battle-tested architectural templates for solving recurring analytical challenges such as dynamic metric switching, customer segmentation (RFM), and 80/20 Pareto analysis.

---

### 1. Dynamic Metric Selection via Disconnected Tables / Field Parameters
Allow end users to toggle visual metrics (Sales, Profit, Quantity, Margin) from a single slicer:
```dax
Dynamic Metric Value = 
SWITCH(
    SELECTEDVALUE(MetricSelection[MetricName]),
    "Total Sales",   [Total Sales],
    "Total Profit",  [Total Profit],
    "Order Volume",  [Total Quantity],
    "Profit Margin", [Profit Margin %],
    [Total Sales] // Default fallback
)
```

### 2. Dynamic Customer Segmentation
Classifying customers dynamically without hardcoding static columns:
```dax
Customer Segment = 
VAR CustSales = [Total Sales]
RETURN
    SWITCH(
        TRUE(),
        CustSales >= 100000, "Tier 1: High Value",
        CustSales >= 25000,  "Tier 2: Medium Value",
        "Tier 3: Low Value"
    )
```

### 3. Pareto 80/20 Analysis Pattern
Calculating cumulative contribution % to identify the top 20% of products driving 80% of total revenue:
```dax
Cumulative Sales % = 
VAR CurrentSales = [Total Sales]
VAR TotalRevenue = CALCULATE([Total Sales], ALLSELECTED(Dim_Product))
VAR CumulativeSum = 
    CALCULATE(
        [Total Sales],
        FILTER(
            ALLSELECTED(Dim_Product),
            [Total Sales] >= CurrentSales
        )
    )
RETURN
    DIVIDE(CumulativeSum, TotalRevenue, 0)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. Creating Field Parameters in Power BI Desktop for seamless visual metric switching.
> 2. How dynamic segmentation responds in real time to date and region slicers.
> 3. Implementing Pareto 80/20 curves on combo charts.

---

> ⚡ **Quick Recall**
> `Field Parameters (Dynamic Metrics) + Dynamic Segmentation + Cumulative Pareto 80/20 Analysis`
