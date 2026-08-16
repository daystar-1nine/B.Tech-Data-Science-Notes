# 80386 Operating Modes (Real, Protected & Virtual 8086) — MPCA Module 5

> **Definition:** The 80386 microprocessor supports **three distinct operating modes**: **Real Address Mode** (16-bit 8086 compatible), **Protected Virtual Address Mode** (32-bit multitasking protected environment), and **Virtual 8086 (V86) Mode** (running real-mode 8086 software inside protected mode).

---

## 1. Detailed Comparison of 80386 Operating Modes

```
+----------------------------------------------------------------------------+
|                             80386 OPERATING MODES                          |
|                                                                            |
| 1. REAL MODE:                2. PROTECTED MODE:        3. VIRTUAL 8086:    |
|    - Default upon power-on      - PE bit = 1 in CR0       - VM bit = 1     |
|    - Exact 8086 clone           - 32-bit Flat/Segmented   - Run 8086 apps  |
|    - 1 MB Physical RAM          - 4 GB RAM / 64 TB Virtual  as task under  |
|    - No memory protection       - Hardware Privilege 0-3    multitasking OS|
+----------------------------------------------------------------------------+
```

---

## 2. Deep Dive into Each Mode

### 1. Real Address Mode (Real Mode)
- Processor boots in this mode upon power-up/reset.
- Behaves as a high-speed 8086 processor:
  - Base Address = `Segment * 16 + Offset`
  - Max addressable memory = 1 MB (plus 64KB High Memory Area HMA).
  - No memory protection or privilege rings (single buggy application can crash the entire system).

### 2. Protected Virtual Address Mode (Protected Mode)
- Activated by setting **`PE = 1` in Register CR0**.
- **Features:**
  - Full 32-bit 4 GB address space with optional Paging.
  - **4 Privilege Levels (Rings 0 to 3):**
    - Ring 0 (Kernel / OS Core) - Highest Privilege.
    - Ring 1 (Device Drivers).
    - Ring 2 (OS Extensions / Middleware).
    - Ring 3 (User Applications) - Lowest Privilege.
  - Segment registers hold **16-bit Selectors** pointing to 8-byte **Descriptors** in Global Descriptor Table (GDT) or Local Descriptor Table (LDT).

### 3. Virtual 8086 Mode (V86 Mode)
- Sub-mode of Protected Mode enabled by setting **`VM = 1` in EFLAGS register**.
- Allows the multitasking OS to execute multiple legacy DOS / 8086 programs as isolated Ring 3 user tasks with hardware memory protection!

---

## 3. Operating Mode Comparison Table

| Property | Real Mode | Protected Mode | Virtual 8086 Mode |
| :--- | :--- | :--- | :--- |
| **Address Space** | 1 MB | **4 GB Physical / 64 TB Virtual** | 1 MB per V86 task |
| **Memory Protection** | None | **Full 4-Level Rings (0-3)** | Protected under Ring 3 |
| **Multitasking** | Not supported in hardware | **Hardware Task Switching (TSS)**| Multitasked by OS kernel |
| **Paging Support** | Disabled | **Full 4 KB Paging (PG bit)** | Supported via Paging MMU |

---

## 4. Quick Recall Flow
```
Power-on -> Real Mode (8086 clone 1MB) -> Set PE=1 in CR0 -> Protected Mode (4GB, Rings 0-3) -> Set VM=1 -> Virtual 8086 Mode
```
