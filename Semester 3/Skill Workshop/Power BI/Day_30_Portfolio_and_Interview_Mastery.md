# Day 30: Portfolio & Interview Mastery

---

> 📌 **Definition to Remember**
> Landing top Power BI and Data Analytics roles requires a polished GitHub & NovyPro portfolio, comprehensive project case studies, and mastery of top technical DAX, SQL, and modeling interview questions.

---

### 1. Building a Standout BI Portfolio
1. **Interactive Hosting on NovyPro:**
   - Host live, clickable Power BI reports using web embeds with background device frames.
2. **GitHub Project Case Study Documentation:**
   - **Business Problem Statement:** What operational inefficiency was solved.
   - **Data Architecture Diagram:** Star schema model screenshot.
   - **Key DAX Formulas:** Code snippets with explanation of filter context handling.
   - **Business Insights & Impact:** 3-5 actionable decisions uncovered by the dashboard.

### 2. Top 10 Power BI Interview Questions & Model Answers

#### Q1. What is the difference between Calculated Columns and Measures?
- *Answer:* Calculated columns evaluate during data refresh in row context and consume RAM. Measures evaluate dynamically on visual query render in filter context and consume zero storage.

#### Q2. Explain `CALCULATE()` and Context Transition.
- *Answer:* `CALCULATE()` modifies the active filter context. Context transition occurs when a measure is invoked inside a row context, converting the current row keys into equivalent filter context constraints.

#### Q3. What is the difference between `ALL()` and `ALLSELECTED()`?
- *Answer:* `ALL()` removes all filters from a table or column unconditionally. `ALLSELECTED()` removes internal visual grouping filters while preserving external slicer selections.

#### Q4. Why is Star Schema preferred over Snowflake Schema in Power BI?
- *Answer:* Power BI's VertiPaq engine optimizes memory scan speed when relationships are shallow. Star schemas require fewer joins, resulting in faster DAX performance and simpler measures.

#### Q5. How does Dynamic Row-Level Security work?
- *Answer:* Dynamic RLS matches the current logged-in user email via `USERPRINCIPALNAME()` against an internal security mapping table, filtering fact table data automatically.

---

> ⭐ **Must-Master Skills & Final Checklist**
> 1. Complete all 30 Days of hands-on practice.
> 2. Build and publish at least 2 end-to-end dashboards to your online portfolio.
> 3. Master DAX filter context explanation with confidence in technical interviews.

---

> ⚡ **Quick Recall**
> `NovyPro Live Dashboards + GitHub Case Studies + Core DAX / Modeling Interview Mastery = Job Ready!`
