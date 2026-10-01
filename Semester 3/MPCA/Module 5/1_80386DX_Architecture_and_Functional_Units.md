# 80386DX Architecture & Functional Units

**Q. Draw and explain the internal architectural block diagram of the Intel 80386DX microprocessor. Explain its functional units, address spaces, and memory management mechanisms in detail.**

---

> 📌 **Definition to Remember**
> The **Intel 80386DX** is a true **32-bit microprocessor** featuring a 32-bit internal architecture, a 32-bit Data Bus, and a 32-bit Address Bus capable of addressing **4 GB of physical memory** and up to **64 Terabytes (TB) of virtual memory**, with integrated hardware Segmentation and Paging units on-chip.

---

### 1. Architectural Overview & Key Specifications

* **Word Size:** 32 bits (doubleword / dword).
* **Data Bus:** 32-bit bidirectional bus ($D_0 - D_{31}$), transferring 4 bytes per 2-clock bus cycle.
* **Address Bus:** 32-bit address bus ($A_2 - A_{31}$ along with Byte Enables $\overline{\text{BE}_0} - \overline{\text{BE}_3}$), addressing **4 Gigabytes ($2^{32}$ bytes)** of physical RAM.
* **Virtual Address Space:** **64 Terabytes ($2^{46}$ bytes)** organized as $2^{14}$ segments of up to 4 GB each.
* **Prefetch Queue:** 16-byte instruction prefetch queue.
* **Integrated MMU:** Hardware Segmentation and Paging units integrated directly on the processor die.

---

### 2. Functional Block Diagram of 80386DX

The 80386DX architecture is organized into **three major sections** containing **six distinct functional units**:

```
                             80386DX ARCHITECTURE
 +-------------------------------------------------------------------------+
 | 1. BUS INTERFACE UNIT (BIU):                                            |
 |    - 32-bit Address Drivers (A2 - A31) & Byte Enables (/BE0 - /BE3)     |
 |    - 32-bit Data Bus Buffer (D0 - D31)                                  |
 |    - Bus Control Logic (READY#, ADS#, W/R#, D/C#, M/IO#, BS16#)         |
 |                                                                         |
 | 2. CENTRAL PROCESSING UNIT (CPU):                                       |
 |    a. [ Instruction Unit ]:                                             |
 |       - 16-byte Code Prefetch Queue                                     |
 |       - 3-deep Instruction Decode Unit (decodes opcodes to microcode)   |
 |    b. [ Execution Unit (EU) ]:                                          |
 |       - 32-bit ALU for arithmetic and logical operations                |
 |       - 8 General-Purpose 32-bit Registers (EAX, EBX, ECX, EDX, etc.)   |
 |       - 64-bit Barrel Shifter (shifts/rotates up to 64 bits in 1 clock) |
 |       - Multiply / Divide Hardware (accelerates math routines)          |
 |                                                                         |
 | 3. MEMORY MANAGEMENT UNIT (MMU):                                        |
 |    a. [ Segmentation Unit ]:                                            |
 |       - Translates Logical Address (Selector:Offset) into               |
 |         32-bit Linear Address using GDT / LDT descriptor tables         |
 |       - Enforces 4-level privilege ring protection (Rings 0-3)          |
 |    b. [ Paging Unit ]:                                                  |
 |       - Translates 32-bit Linear Address into 32-bit Physical Address   |
 |       - 2-level paging mechanism with 4 KB page frames                  |
 |       - 32-entry Translation Lookaside Buffer (TLB) cache               |
 +-------------------------------------------------------------------------+
```

---

### 3. Address Spaces & Address Translation Mechanism

Memory translation occurs in two sequential hardware steps:

```
  Logical Address (Selector : Offset)
            |
            v
  +-----------------------+
  |  SEGMENTATION UNIT    |  ---> Uses GDT/LDT Descriptor Table
  +-----------------------+
            |
            v 32-bit Linear Address (4 GB space)
  +-----------------------+
  |     PAGING UNIT       |  ---> Uses CR3, Page Directory & Page Table (if PG=1)
  +-----------------------+
            |
            v 32-bit Physical Address (4 GB Physical RAM)
  +-----------------------+
  |   SYSTEM MEMORY/BUS   |
  +-----------------------+
```

1. **Logical to Linear:** The Segmentation Unit adds the segment base address (retrieved from the descriptor in GDT/LDT pointed to by the 16-bit selector) to the 32-bit offset to produce a **32-bit Linear Address**.
2. **Linear to Physical:** If paging is disabled ($PG = 0$ in CR0), Linear Address = Physical Address. If paging is enabled ($PG = 1$ in CR0), the Paging Unit maps the linear address to a **32-bit Physical Address** using a 2-level page directory/page table hierarchy.

---

### 4. 80386DX vs. 80386SX Comparison

| Feature | 80386DX | 80386SX |
| :--- | :--- | :--- |
| **Data Bus Width** | **32 bits** ($D_0 - D_{31}$) | **16 bits** ($D_0 - D_{15}$) |
| **Address Bus Width** | **32 bits** ($A_2 - A_{31} + 4 \times \overline{\text{BE}}$) | **24 bits** ($A_0 - A_{23}$) |
| **Physical Memory Limit** | **4 GB** | **16 MB** |
| **Virtual Memory Limit** | **64 TB** | **64 TB** |
| **Pin Count / Package** | 132-pin PGA / PQFP | 100-pin QFP |
| **Target Market** | High-end workstations, servers | Low-cost entry-level PCs |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 80386DX is a true **32-bit microprocessor** with 32-bit data and 32-bit address buses.
> 2. It supports **4 GB physical memory** and up to **64 TB virtual memory**.
> 3. Organized into three sections: **BIU, CPU (Instruction + Execution Units), and MMU (Segmentation + Paging Units)**.
> 4. The **Barrel Shifter** performs multi-bit shifts/rotates (up to 64 bits) in a single clock cycle.
> 5. **Two-stage address translation:** Logical Address $\rightarrow$ Linear Address (via Segmentation) $\rightarrow$ Physical Address (via Paging).
> 6. Contains a **16-byte prefetch queue** and pipelined instruction decode stage.
> 7. The 80386SX variant has a 16-bit data bus and 24-bit address bus (16 MB physical RAM).

---

> ⚡ **Quick Recall**
> `32-bit Data & Addr → 4GB RAM / 64TB Virtual → 3 Sections (BIU, CPU, MMU) → Segmentation (Logical to Linear) → Paging (Linear to Physical) → 16-byte Queue`
