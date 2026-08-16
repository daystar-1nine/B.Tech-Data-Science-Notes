import os

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

m5_dir = os.path.join(MPCA_DIR, "Module 5")
m5_qa = os.path.join(m5_dir, "Module_5_QA")

os.makedirs(m5_dir, exist_ok=True)
os.makedirs(m5_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 5: 80386DX PROCESSOR AND PENTIUM PROCESSOR
# --------------------------------------------------------------------------

m5_files = {
    "1_80386DX_Architecture_and_Functional_Units.md": """# 80386DX Architecture & Functional Units — MPCA Module 5

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
1. **Physical Address Space:** $2^{32} = 4\\text{ GB}$ of physical RAM directly addressable.
2. **Virtual Memory Space:** $2^{14} \\text{ segments} \\times 2^{32} \\text{ bytes/segment} = 2^{46} = 64\\text{ Terabytes (TB)}$ per task.
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
""",

    "2_80386_Register_Organization.md": """# 80386 Register Organization — MPCA Module 5

> **Definition:** The **80386 Register Set** consists of thirty-two 32-bit and 16-bit registers categorized into General-Purpose Registers, Segment Registers, Status and Instruction Registers (EFLAGS & EIP), Control Registers, and Debug/Test Registers.

---

## 1. Detailed Technical Explanation

### 1. General-Purpose Registers (32-bit Extended)
All 16-bit registers of 8086 were extended to 32 bits with the `E` prefix:

```
  31                 16 15        8 7          0
 +---------------------+-----------+-----------+
 |                     |    AH     |    AL     |  EAX (Accumulator)
 +---------------------+-----------+-----------+
 |                     |    BH     |    BL     |  EBX (Base Register)
 +---------------------+-----------+-----------+
 |                     |    CH     |    CL     |  ECX (Count Register)
 +---------------------+-----------+-----------+
 |                     |    DH     |    DL     |  EDX (Data Register)
 +---------------------+-----------+-----------+
 |                     |          SI           |  ESI (Source Index)
 +---------------------+-----------------------+
 |                     |          DI           |  EDI (Destination Index)
 +---------------------+-----------------------+
 |                     |          BP           |  EBP (Base Pointer)
 +---------------------+-----------------------+
 |                     |          SP           |  ESP (Stack Pointer)
 +---------------------+-----------------------+
```

---

### 2. Segment Registers (16-bit)
The 80386 has **6 Segment Selectors** (added FS and GS for additional data segment access):
- `CS` (Code Segment), `SS` (Stack Segment), `DS` (Data Segment), `ES` (Extra Segment), `FS` (General Data Segment 2), `GS` (General Data Segment 3).

---

### 3. EFLAGS Register (32-bit Extended Flags)
Extends the 8086 flags with critical operating system mode control bits:

```
 31             18  17  16  14 13-12  11  10  9   8   7   6   4   2   0
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
| Reserved (0) |AC |VM |RF | 0 |IOPL |OF |DF |IF |TF |SF |ZF |AF |PF |CF |
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
```
- **VM (Virtual 8086 Mode, Bit 17):** When set (1), processor switches to Virtual 8086 mode.
- **RF (Resume Flag, Bit 16):** Used with debug breakpoints to disable debug exceptions on the next instruction.
- **IOPL (I/O Privilege Level, Bits 12-13):** 2-bit field (00 to 11) indicating minimum privilege required to execute I/O instructions.
- **NT (Nested Task, Bit 14):** Set when a task is invoked via a `CALL` instruction with a Task State Segment (TSS).

---

### 4. Control Registers (CR0 - CR3)
- **CR0 (Machine Status Word Extended):**
  - `PE` (Bit 0 - Protection Enable): 1 = Protected Mode, 0 = Real Mode.
  - `PG` (Bit 31 - Paging Enable): 1 = Enable Paging MMU, 0 = Disable Paging.
- **CR2 (Page Fault Linear Address):** Stores the 32-bit linear address that caused the last page fault exception.
- **CR3 (Page Directory Base Register PDBR):** Stores the 32-bit physical base address of the top-level Page Directory.

---

## 2. Quick Recall Flow
```
80386 Registers -> 8 GPRs (EAX-ESP) -> 6 Segments (CS, DS, SS, ES, FS, GS) -> EFLAGS (VM, RF, IOPL, NT) -> Control (CR0: PE/PG, CR3: Page Directory)
```
""",

    "3_80386_Operating_Modes.md": """# 80386 Operating Modes (Real, Protected & Virtual 8086) — MPCA Module 5

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
""",

    "4_Pentium_Processor_Architecture_and_Superscalar_Pipelining.md": """# Pentium Processor Architecture & Superscalar Operation — MPCA Module 5

> **Definition:** The **Intel Pentium Processor** is a 32-bit superscalar CISC microprocessor capable of executing **two instructions per clock cycle** using two parallel 5-stage integer pipelines (**U-Pipe** and **V-Pipe**), an integrated on-chip Floating-Point Unit (FPU), and **Dynamic Branch Prediction Logic**.

---

## 1. Detailed Technical Explanation

### 1. Pentium Architecture Block Diagram

```
                           PENTIUM INTERNAL ARCHITECTURE
 +----------------------------------------------------------------------------+
 |  64-bit External Data Bus  <=====>  32-bit Address Bus (4 GB Address Space)|
 |                                                                            |
 |  [ 8 KB Code Cache (I-Cache) ]         [ 8 KB Data Cache (D-Cache) ]       |
 |                                                                            |
 |  [ Branch Target Buffer (BTB) ] ------> 2-bit Dynamic Branch Prediction    |
 |                                                                            |
 |  [ Instruction Decode Unit ]                                               |
 |        /                \\                                                 |
 |  [ U-Pipeline (5-Stage) ]  [ V-Pipeline (5-Stage) ]  [ Pipelined 80-bit FPU]|
 |  (Executes any instruction) (Executes simple pairable) (8-stage math unit)  |
 +----------------------------------------------------------------------------+
```

---

## 2. Superscalar Integer Pipelines (U and V Pipes)

The Pentium can issue two integer instructions simultaneously in parallel if they meet **Instruction Pairing Rules**:
1. **U-Pipeline:** Can execute any instruction from the x86 instruction set.
2. **V-Pipeline:** Executes simple integer instructions (e.g., `MOV`, `ADD`, `SUB`, `INC`, `DEC`, `CMP`, `JMP`, `CALL`).

### The 5 Pipeline Stages:
```
1. PF (Prefetch)     : Fetches instructions from 8 KB Code Cache into prefetch buffers.
2. D1 (Decode-1)     : Decodes instruction opcode, determines pairability between U & V.
3. D2 (Decode-2)     : Computes Effective Memory Address (Displacement + Base + Index).
4. EX (Execute)      : ALU executes integer operations; accesses Data Cache if needed.
5. WB (Writeback)    : Updates destination registers and status flags.
```

---

## 3. Dynamic Branch Prediction & Branch Target Buffer (BTB)
- **Branch Target Buffer (BTB):** An on-chip cache storing branch instructions, target jump addresses, and branch history bits.
- **2-bit Branch History State Machine:**
  - `00`: Strongly Not-Taken
  - `01`: Weakly Not-Taken
  - `10`: Weakly Taken
  - `11`: Strongly Taken
- Achieves over **90% branch prediction accuracy**, eliminating branch penalty stalls from pipeline flushing.

---

## 4. Must-Write Points for Exams
- Pentium has a **64-bit external data bus** and **32-bit address bus**.
- It features separate Harvard-style **8 KB Code Cache** and **8 KB Data Cache** on-chip.
- Dual-issue U and V pipelines achieve execution throughput of up to 2 instructions per clock cycle ($IPC = 2$).

---

## 5. Quick Recall Flow
```
Pentium -> Superscalar -> U & V Dual Pipelines (5-stages: PF, D1, D2, EX, WB) -> 8KB Code/Data Caches -> BTB 2-bit Branch Prediction
```
""",

    "5_Self_Learning_80386_Memory_Management_Paging_and_MESI_Cache.md": """# Self-Learning: 80386 Memory Management & MESI Cache Protocol — MPCA Module 5

> **Definition:** The 80386 Memory Management Unit (MMU) provides two-stage address translation (**Segmentation & Paging**), while multiprocessor systems maintain cache consistency using the **MESI (Illinois) Protocol**.

---

## 1. 80386 Protected Mode Memory Translation

```
Logical Address (Selector:Offset)
        |
        v
[ SEGMENTATION UNIT ]  ---> Checks Descriptor in GDT/LDT -> Produces 32-bit Linear Address
        |
        v
[ PAGING UNIT (PG=1)]  ---> Uses CR3, Page Directory & Page Table -> Produces 32-bit Physical Address
```

### 1. Descriptor Tables (GDT, LDT, IDT):
- **GDT (Global Descriptor Table):** Holds segment descriptors accessible by all system tasks.
- **LDT (Local Descriptor Table):** Holds segment descriptors private to an individual application task.
- **IDT (Interrupt Descriptor Table):** Holds Gate Descriptors for 256 interrupt vectors.

### 2. Two-Level Paging Scheme (4 KB Pages):
A 32-bit Linear Address is split into:
```
  31              22 21              12 11                     0
 +------------------+------------------+------------------------+
 | Directory Index  |    Table Index   |     Offset in Page     |
 | (10 bits: 1024)  | (10 bits: 1024)  | (12 bits: 4096 bytes)  |
 +------------------+------------------+------------------------+
```
- `CR3` holds base address of **Page Directory**.
- Directory entry points to **Page Table**.
- Page Table entry points to physical 4 KB **Page Frame** in RAM.

---

## 2. MESI Cache Coherence Protocol

In symmetric multiprocessing (SMP) systems with private L1/L2 caches, every cache line exists in one of **four MESI states**:

```
M - MODIFIED  : Cache line is dirty (present only in current cache, modified, memory is stale).
E - EXCLUSIVE : Cache line is clean (present only in current cache, matches main memory).
S - SHARED    : Cache line is clean (present in multiple processor caches, matches main memory).
I - INVALID   : Cache line is invalid (contains obsolete/stale data; must fetch from bus).
```

### State Transition Summary:
- **Read Hit:** Stays in M, E, or S state.
- **Write Hit on S:** Broadcasts invalidate to bus, transitions from `S -> M`.
- **Snooping on Bus Write:** Transitions from `S -> I` or `E -> I`.

---

## 3. Quick Recall Flow
```
Logical (Selector:Offset) -> GDT/LDT -> Linear Address -> Page Dir -> Page Table -> Physical Address | MESI (Modified, Exclusive, Shared, Invalid)
```
"""
}

# Write Module 5 files
for fname, content in m5_files.items():
    with open(os.path.join(m5_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created MPCA Module 5 Files!")
