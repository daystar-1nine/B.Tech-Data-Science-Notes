# Day 5: Power Query Data Cleaning Techniques

---

> 📌 **Definition to Remember**
> **Data Cleaning** in Power Query entails resolving missing values (`null`), handling data errors, deduplicating records, splitting compound strings, and creating rule-based conditional columns.

---

### 1. Core Data Cleaning Techniques
1. **Handling Missing Values (`null`):**
   - *Fill Down / Fill Up:* Replaces nulls in grouped hierarchy tables with preceding values.
   - *Replace Values:* Explicitly replaces `null` with `0` for metrics or `"Unknown"` for text categories.
2. **Error Handling:**
   - Identifying data type mismatch errors (`[Error]`).
   - Using *Remove Errors* vs *Replace Errors* with default fallback values.
3. **Removing Duplicates:**
   - Deduplicating on composite business keys (e.g., `CustomerID + OrderDate`) to guarantee dimension uniqueness.
4. **Splitting & Merging Columns:**
   - *Split by Delimiter:* Splitting `"First Last"` by space into separate First Name and Last Name columns.
   - *Merge Columns:* Combining Address, City, and Postal Code into a standardized Full Address.
5. **Conditional Columns:**
   - Visual GUI rule builder creating `IF-THEN-ELSE` classification flags (e.g., `IF Age >= 60 THEN "Senior" ELSE "Adult"`).

---

> ⭐ **Must-Master Skills & Interview Points**
> 1. What causes Power Query data type errors (e.g., text characters in numeric columns) and how to handle them.
> 2. Difference between removing duplicate rows across the whole table vs specific key columns.
> 3. Best practice: Never load raw uncleaned data into the modeling tab.

---

> ⚡ **Quick Recall**
> `Deduplicate → Fill Down Nulls → Handle Errors → Split/Merge Strings → Add Conditional Columns`
