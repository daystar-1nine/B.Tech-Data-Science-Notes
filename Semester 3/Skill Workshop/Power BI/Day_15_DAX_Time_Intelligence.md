# Day 15: DAX Time Intelligence Mastery

---

> 📌 **Definition to Remember**
> **Time Intelligence functions** in DAX calculate metrics over specific calendar periods including Year-To-Date (**YTD**), Prior Year comparisons (**YoY Growth**), and moving rolling averages.

---

### 1. Prerequisites for Time Intelligence
- Dedicated Date Table (`Dim_Date`) with contiguous, unbroken dates.
- Mark as Date Table verified in Power BI Desktop.

### 2. Year-To-Date (YTD) & Month-To-Date (MTD)
```dax
// Year To Date Sales
Sales YTD = TOTALYTD([Total Sales], Dim_Date[Date])

// Month To Date Sales
Sales MTD = TOTALMTD([Total Sales], Dim_Date[Date])
```

### 3. Prior Year & YoY Growth % Calculations
```dax
// Previous Year Sales (Same Period Last Year)
Sales PY = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)

// Year-over-Year (YoY) Sales Variance
YoY Sales Growth $ = [Total Sales] - [Sales PY]

// Year-over-Year (YoY) Sales Growth %
YoY Sales Growth % = 
DIVIDE([YoY Sales Growth $], [Sales PY], 0)
```

### 4. Moving Rolling Averages (30-Day Rolling Sales)
```dax
Rolling 30 Days Sales = 
CALCULATE(
    [Total Sales],
    DATESINPERIOD(Dim_Date[Date], MAX(Dim_Date[Date]), -30, DAY)
)
```

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. `SAMEPERIODLASTYEAR()` vs `DATEADD(..., -1, YEAR)`.
> 2. How `DATESYTD` / `TOTALYTD` automatically handle leap years and fiscal year-ends (`"3/31"`).
> 3. Formatting YoY growth with dynamic up/down color indicators (`▲` / `▼`).

---

> ⚡ **Quick Recall**
> `TOTALYTD / TOTALMTD + SAMEPERIODLASTYEAR (Prior Year) + DATESINPERIOD (Rolling Averages)`
