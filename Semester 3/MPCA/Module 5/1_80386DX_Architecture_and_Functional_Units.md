# 80386DX Architecture & Functional Units — MPCA Module 5

> **Definition:** The **Intel 80386DX** is a true **32-bit microprocessor** with a 32-bit internal architecture, a 32-bit Data Bus, and a 32-bit Address Bus, capable of addressing **4 GB of physical memory** and up to **64 Terabytes (TB) of virtual memory**.

---

## 1. Detailed Technical Explanation

### 1. Functional Block Diagram of 80386DX
The 80386DX architecture is organized into **three major sections** containing six distinct functional units:

```
                            80386DX ARCHITECTURE
 +-------------------------------------------------------------------------+
 | 1. BUS INTERFACE UNIT (BIU):                                            |
 |    - 32-bit Address Bus Drivers (A2 - A31, /BE0 - /BE3)                 |
 |    - 32-bit Data Bus Buffer (D0 - D31)                                  |
 |    - Bus Control Logic (READY, ADS, /LOCK, BS16)                        |
 |                                                                         |
 | 2. CENTRAL PROCESSING UNIT (CPU):                                       |
 |    - [ Instruction Unit ]: 16-byte Code Prefetch Queue, Instruction     |
 |                            Decoder (translates opcodes to microcode)    |
 |    - [ Execution Unit (EU) ]: 32-bit ALU, 8 General Purpose Registers,  |
 |                               Barrel Shifter (1-cycle 64-bit shift),    |
 |                               Multiply/Divide Hardware                  |
 |                                                                         |
 | 3. MEMORY MANAGEMENT UNIT (MMU):                                        |
 |    - [ Segmentation Unit ]: Translates Logical Address (Selector:Offset)|
 |                             into 32-bit Linear Address via GDT/LDT      |
 |    - [ Paging Unit ]: Translates 32-bit Linear Address into 32-bit      |
 |                       Physical Address using 2-level Page Directory     |
 +-------------------------------------------------------------------------+
```

---

## 2. Address Spaces in 80386DX
1. **Physical Address Space: 2^32 = 4 GB** of physical RAM directly addressable.
2. **Virtual Memory Space: 2^14  segments × 2^32 { bytes/segment} = 2^46 = 64{ Terabytes (TB)}** per task.
3. **Paging:** Supports fixed 4 KB page sizes for virtual memory swapping.

---

## 3. Core Concepts & Memory Keywords
- **32-bit Data & Address Bus:** Transfers 32-bit dwords in a single 2-clock bus cycle.
- **On-chip MMU:** Integrated hardware Segmentation Unit and Paging Unit on a single silicon die.
- **Barrel Shifter:** Hardware unit performing multi-bit arithmetic/logical shifts in a single clock cycle.

---

## 4. Must-Write Points for Exams
- The 80386DX has a 32-bit data bus and 32-bit address bus (unlike 80386SX which has a 16-bit data bus and 24-bit address bus).
- Hardware Paging can be dynamically enabled or disabled using the PG bit in Control Register 0 (CR0).
- The prefetch queue is 16 bytes deep, ensuring continuous pipeline instruction supply.

---

## 5. Quick Recall Flow
```
80386DX (32-bit) -> 3 Sections (BIU, CPU, MMU) -> Segmentation (Logical to Linear) -> Paging (Linear to Physical) -> 4GB RAM / 64TB Virtual
```
