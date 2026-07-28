# DataSci Notes Studio — B.Tech Data Science Academic Notes Portal

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-A90E02?style=for-the-badge&logo=github)](https://daystar-1nine.github.io/B.Tech-Data-Science-Notes)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Multi-Semester](https://img.shields.io/badge/Semesters-Multi--Semester-green.svg?style=for-the-badge)](#)

A high-performance, responsive academic study portal and solved examination question bank specifically designed for **B.Tech Data Science** students.

---

## 🌟 Key Platform Features

* 🚀 **Multi-Semester Architecture:** Dynamically organizes and indexes notes across semesters (`Semester 3`, `Semester 4`, etc.).
* 📚 **2-Level Collapsible Accordion Reader:** Nested Subject $\rightarrow$ Module accordion navigation with sidebar search and Focus Mode toggle.
* ⚡ **Rapid Revision Flashcards:** Interactive flashcards featuring 📌 Definitions, ⭐ Must-Write Points, and ⚡ Quick Recall memory sequences with subject filtering.
* 🔍 **Spotlight Search (`Ctrl+K`):** Instant search overlay across all 98+ topics and question banks.
* 📑 **1-Click PDF Downloads:** Printed PDF companion downloads generated for every markdown file.
* 📋 **1-Click Code Snippet Copying:** Integrated copy button on all code blocks with instant feedback.
* ⏱️ **Reading Time & Sequential Pagination:** Reading time estimation and `← Previous Topic` / `Next Topic →` navigation buttons.
* 🎨 **Custom Theme Engine:** Palette based on **Crimson Red (`#A90E02`)** and **Warm Cream (`#FFFBD4`)** with Dark and Light Mode support.

---

## 📂 Repository Structure

```text
📁 Semester 3 (Markdown Source Notes)
 ├── 📁 DBMS (Module 1, Module 2, Module 3, Module_1_QA)
 ├── 📁 Data Structure (Module 1, Module 2, Module 3)
 └── 📁 MPCA (Module 1, Module 2, Module 3, Module_1_QA, Module_2_QA)

📁 PDF_Notes (Publication-Ready PDF Copies)
 └── 📁 Semester 3 (Mirrors exact semester & module hierarchy)

📁 web-app-files (Production Single-Page Application)
 ├── index.html
 ├── index.css
 ├── app.js
 ├── notes_data.js
 └── build_site_data.py
```

---

## 🛠️ Local Setup & Development

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/daystar-1nine/B.Tech-Data-Science-Notes.git
   cd B.Tech-Data-Science-Notes
   ```

2. **Re-index Markdown Notes into Web Database:**
   ```bash
   python build_site_data.py
   ```

3. **Start Local Server:**
   ```bash
   python -m http.server 8080
   ```
   Open `http://localhost:8080` in your web browser.

---

## 👤 Developer Profile

**Suraj** — *Data Science Student & Software Developer*  
Passionate about building highly aesthetic, high-performance web applications and desktop-class user experiences in the browser.

* 🌐 **Portfolio:** [suraj1nine.vercel.app](https://suraj1nine.vercel.app/)
* 💻 **GitHub:** [@daystar-1nine](https://github.com/daystar-1nine)
* 👔 **LinkedIn:** [surajsawant19062005](https://www.linkedin.com/in/surajsawant19062005/)
* 📷 **Instagram:** [@daystar.drafts](https://www.instagram.com/daystar.drafts/)
* ⚡ **LeetCode:** [daystar-onenine](https://leetcode.com/u/daystar-onenine/)
* ✉️ **Email:** `surajonenine@gmail.com`

---

## 📜 Disclaimer

These notes are compiled as an open-source supplementary study aid for academic revision. While every effort has been made to ensure technical accuracy, students are advised to cross-reference with their official university syllabus and prescribed textbooks.

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
