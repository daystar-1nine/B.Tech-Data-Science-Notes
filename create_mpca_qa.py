import os

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

unit1_dir = os.path.join(MPCA_DIR, "Module 1", "Module_1_QA")
unit2_dir = os.path.join(MPCA_DIR, "Module 2", "Module_2_QA")
unit3_dir = os.path.join(MPCA_DIR, "Module 3", "Module_3_QA")

os.makedirs(unit1_dir, exist_ok=True)
os.makedirs(unit2_dir, exist_ok=True)
os.makedirs(unit3_dir, exist_ok=True)

# --------------------------------------------------------------------------
# UNIT 1 FILES
# --------------------------------------------------------------------------

u1_2m = """# 2-Mark Questions & Answers — MPCA Unit 1: Overview of Computer Architecture & Organization

---

### Q1. Differentiate between Computer Architecture and Computer Organization.

| Feature | Computer Architecture | Computer Organization |
| :--- | :--- | :--- |
| **Focus** | High-level logical aspects visible to the programmer (ISA). | Hardware transparent operational units and their interconnections. |
| **Examples** | Instruction set, addressing modes, data types, registers. | Control signals, memory technology, bus interfaces, clock frequency. |

---

### Q2. What is the Von Neumann bottleneck?

The **Von Neumann Bottleneck** refers to the throughput limitation caused by the shared single system bus between the CPU and memory for both instruction fetches and data transfers. Because instructions and data cannot be accessed simultaneously over the same bus, the CPU is forced to wait (CPU stall), constraining overall processing speed.

---

### Q3. List any four performance measures of a computer system.

1. **Clock Cycle Time / Frequency (GHz)**
2. **Instruction Execution Rate (MIPS - Million Instructions Per Second)**
3. **Floating-Point Speed (FLOPS - Floating Point Operations Per Second)**
4. **Execution Time / CPU Response Time**

---

### Q4. Define MIPS and FLOPS.

- **MIPS (Million Instructions Per Second):** A measure of CPU processing speed defined as:
  $$\text{MIPS} = \frac{\text{Instruction Count}}{\text{Execution Time} \times 10^6}$$
- **FLOPS (Floating-Point Operations Per Second):** A metric measuring hardware performance in numerical, scientific, and AI floating-point calculations (GFLOPS, TFLOPS, PFLOPS).

---

### Q5. What is meant by instruction set architecture (ISA)?

**Instruction Set Architecture (ISA)** is the abstract boundary/interface between computer hardware and software. It defines everything a programmer or compiler needs to know to execute code on a CPU, including supported instructions, data types, register sets, memory addressing modes, and interrupt handling models.
"""

u1_3m = """# 3-Mark Questions & Answers — MPCA Unit 1: Overview of Computer Architecture & Organization

---

### Q1. Explain the Von Neumann model with a neat diagram.

The **Von Neumann Model** describes a computer system based on stored-program concepts, where instructions and data reside in a single shared memory.

```
+--------------------------------------------------------+
|                      CENTRAL PROCESSING UNIT           |
|  +------------------------+  +----------------------+  |
|  |  CONTROL UNIT (CU)     |  |  ALU                 |  |
|  |  (PC, IR, Control logic)|  |  (Accumulator, Flags)|  |
|  +------------------------+  +----------------------+  |
+---------------------------+----------------------------+
                            | System Bus
+---------------------------+----------------------------+
|  MAIN MEMORY (RAM)        |  INPUT / OUTPUT UNITS      |
|  (Stores Program & Data)  |  (Keyboard, Display, Disks)|
+---------------------------+----------------------------+
```
- **Control Unit (CU):** Fetches instructions and directs operations.
- **ALU:** Performs arithmetic and logic computations.
- **Memory Unit:** Holds both program instructions and working data sequentially.

---

### Q2. Explain any three addressing modes with examples.

1. **Immediate Addressing Mode:** The operand is specified directly within the instruction itself.
   - *Example:* `MOV AX, 0005H` (Loads value `0005H` directly into register `AX`).
2. **Register Addressing Mode:** The operand is stored inside a CPU register.
   - *Example:* `MOV AX, BX` (Copies 16-bit contents of `BX` into `AX`).
3. **Direct Addressing Mode:** The 16-bit offset address of the operand in memory is specified directly.
   - *Example:* `MOV AX, [2000H]` (Loads contents of memory location `DS:2000H` into `AX`).

---

### Q3. Differentiate between CISC and RISC architecture.

| Feature | CISC (Complex Instruction Set) | RISC (Reduced Instruction Set) |
| :--- | :--- | :--- |
| **Instruction Count** | Large set (300+ complex instructions). | Small set of simple, uniform instructions. |
| **Execution Time** | Variable (multiple clock cycles per instruction). | Fixed (single clock cycle per instruction). |
| **Memory Access** | Operations allowed directly on memory operands. | Load/Store architecture only (operands must be in registers). |
| **Examples** | Intel x86 (8086, Core i9), AMD Ryzen. | ARM, MIPS, RISC-V. |

---

### Q4. Explain the evolution of computers (generations) briefly.

1. **1st Gen (1940-1956):** Vacuum tubes; massive physical size; machine language; magnetic drums.
2. **2nd Gen (1956-1963):** Transistors; assembly & high-level languages (FORTRAN); magnetic core memory.
3. **3rd Gen (1964-1971):** Integrated Circuits (ICs); keyboards & monitors; operating systems introduced.
4. **4th Gen (1971-Present):** Microprocessors (VLSI/ULSI); personal computers (PCs); high-speed memory.
5. **5th Gen (Present & Future):** Artificial Intelligence, parallel processing, quantum computing, neural hardware.

---

### Q5. What are the different types of instruction formats based on operand count?

1. **Three-Address Instructions:** Specify 2 source operands and 1 destination operand.
   - *Syntax:* `ADD R1, A, B` (Meaning: `R1 = A + B`)
2. **Two-Address Instructions:** Specify 1 destination/source operand and 1 source operand.
   - *Syntax:* `ADD A, B` (Meaning: `A = A + B`)
3. **One-Address Instructions:** Use an implicit **Accumulator (AC)** register.
   - *Syntax:* `ADD B` (Meaning: `AC = AC + B`)
4. **Zero-Address Instructions:** Operate implicitly on a **Stack** data structure.
   - *Syntax:* `ADD` (Pops top two stack items, adds them, and pushes result back onto stack).
"""

u1_5m = """# 5-Mark Questions & Answers — MPCA Unit 1: Overview of Computer Architecture & Organization

---

### Q1. Explain the Von Neumann architecture in detail with its advantages and limitations.

#### 1. Detailed Concept
The **Von Neumann Architecture** is based on three fundamental principles:
- **Stored-Program Concept:** Instructions and data share the same unified primary memory space.
- **Sequential Execution:** Instructions are fetched and executed one after another, controlled by a Program Counter (`PC`).
- **Functional Components:** Central Processing Unit (ALU + CU), Main Memory, Input/Output interface.

#### 2. Key Advantages
- **Flexibility:** Program code can be dynamically loaded, modified, and re-executed without altering hardware wiring.
- **Simplified Hardware Design:** Uses a single memory controller and single system bus structure.

#### 3. Limitations (Von Neumann Bottleneck)
- **Shared Bus Contention:** The CPU cannot fetch an instruction and read/write data simultaneously over the same bus system.
- **Speed Mismatch:** CPU processing speed scales much faster than RAM access latency, creating CPU stall cycles (idle wait states).

---

### Q2. Explain all addressing modes of the 8086 microprocessor with examples.

1. **Immediate Mode:** Operand is a constant value inside instruction.
   - `MOV CX, 1234H`
2. **Register Direct Mode:** Operand resides in CPU register.
   - `MOV AX, BX`
3. **Direct Memory Mode:** Operand memory offset specified directly.
   - `MOV AX, [1000H]`
4. **Register Indirect Mode:** Address stored inside pointer register (`BX`, `BP`, `SI`, `DI`).
   - `MOV AX, [BX]`
5. **Based Addressing Mode:** Effective Address = Base Register (`BX` or `BP`) + Displacement.
   - `MOV AX, [BX + 08H]`
6. **Indexed Addressing Mode:** Effective Address = Index Register (`SI` or `DI`) + Displacement.
   - `MOV AX, [SI + 10H]`
7. **Based-Indexed Mode:** Effective Address = Base Register + Index Register.
   - `MOV AX, [BX + SI]`
8. **Based-Indexed with Displacement Mode:** Effective Address = Base Register + Index Register + Displacement.
   - `MOV AX, [BX + SI + 04H]`

---

### Q3. Discuss the performance measures of computer architecture (CPU time, clock cycles, MIPS, benchmarks) in detail.

#### 1. CPU Execution Time Formula
$$\text{CPU Time} = \text{Instruction Count (IC)} \times \text{CPI (Cycles Per Instruction)} \times \text{Clock Cycle Time (T)}$$
$$\text{CPU Time} = \frac{\text{Instruction Count} \times \text{CPI}}{\text{Clock Rate (f)}}$$

#### 2. Clock Cycles & CPI
- **Clock Rate ($f$):** CPU clock frequency measured in GHz.
- **CPI (Cycles Per Instruction):** Average number of clock cycles required to execute one instruction.

#### 3. MIPS (Million Instructions Per Second)
$$\text{MIPS} = \frac{\text{Instruction Count}}{\text{Execution Time} \times 10^6} = \frac{\text{Clock Rate}}{\text{CPI} \times 10^6}$$

#### 4. Benchmarks
Standardized suite of test programs (e.g., **SPEC CPU2017**, **Geekbench**, **Linpack**) used to evaluate real-world hardware performance across arithmetic, memory bandwidth, and multitasking workloads.

---

### Q4. Explain the basic organization and block-level description of the functional units of a computer.

```
                     +--------------------------+
                     |  PRIMARY MEMORY (RAM)    |
                     +--------------------------+
                               ^  |
                Address/Data   |  | Instructions/Data
                               v  v
+------------------+  +--------------------------+  +-------------------+
|  INPUT DEVICES   |->|  CPU                     |->|  OUTPUT DEVICES   |
| (Keyboard, Mouse)|  |  - Control Unit (CU)     |  | (Monitor, Printer)|
+------------------+  |  - ALU & Registers       |  +-------------------+
                      +--------------------------+
```

1. **Input Unit:** Accepts external user data/programs and converts them into binary code.
2. **Central Processing Unit (CPU):**
   - **Control Unit (CU):** Decoding instructions, generating synchronization clock pulses.
   - **Arithmetic Logic Unit (ALU):** Performs operations (`+`, `-`, `AND`, `OR`, shift operations).
   - **Registers:** High-speed internal storage locations (`PC`, `IR`, `MAR`, `MDR`).
3. **Memory Unit:** Primary RAM storing active programs and working variables.
4. **Output Unit:** Translates processed binary results into human-readable media.

---

### Q5. Compare Harvard architecture with Von Neumann architecture.

| Parameter | Von Neumann Architecture | Harvard Architecture |
| :--- | :--- | :--- |
| **Memory System** | Shared single memory for instructions and data. | Separate physical memory blocks for instructions and data. |
| **Bus System** | Shared single bus for instruction fetch & data access. | Separate instruction bus and data bus. |
| **Pipelining Efficiency** | Lower efficiency due to bus conflict bottlenecks. | Higher efficiency (simultaneous instruction & data access). |
| **Complexity & Cost** | Simple structure, lower hardware cost. | Complex memory controller, higher cost. |
| **Applications** | General-purpose desktop computers, servers. | DSP processors, Microcontrollers (ARM Cortex, PIC, AVR). |
"""

u1_10m = """# 10-Mark Questions & Answers — MPCA Unit 1: Overview of Computer Architecture & Organization

---

### Q1. Explain in detail the Von Neumann model of computer architecture. Also discuss the block-level description of functional units (CU, ALU, Memory, I/O) with a diagram.

#### 1. Introduction to Von Neumann Architecture
Proposed by John von Neumann in 1945, the **Von Neumann Model** laid the foundation for modern general-purpose computing based on the **Stored-Program Concept**.

```
+-----------------------------------------------------------------------+
|                       CENTRAL PROCESSING UNIT (CPU)                   |
|                                                                       |
|   +-------------------------------+   +---------------------------+   |
|   |  CONTROL UNIT (CU)            |   |  ARITHMETIC LOGIC UNIT    |   |
|   |  - Program Counter (PC)       |   |  (ALU)                    |   |
|   |  - Instruction Register (IR)  |   |  - Accumulator (AC)       |   |
|   |  - Control Logic Generator    |   |  - Status Flags           |   |
|   +-------------------------------+   +---------------------------+   |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |  INTERNAL REGISTERS (MAR, MDR, General Purpose Registers)     |   |
|   +---------------------------------------------------------------+   |
+-----------------------------------------------------------------------+
                                    | System Bus (Address, Data, Control)
+-----------------------------------+-----------------------------------+
|  MAIN MEMORY UNIT (RAM)           |  INPUT / OUTPUT INTERFACE         |
|  (Stores Program Code + Data)     |  (Keyboard, Mouse, Disk, Monitor) |
+-----------------------------------+-----------------------------------+
```

#### 2. Detailed Functional Units
1. **Control Unit (CU):**
   - **Program Counter (PC):** Holds the memory address of the next instruction to fetch.
   - **Instruction Register (IR):** Holds the current instruction fetched from memory during decoding.
   - **Instruction Decoder & Timing Logic:** Translates opcodes into control signals triggering functional execution.
2. **Arithmetic Logic Unit (ALU):**
   - Executes arithmetic operations (`ADD`, `SUB`, `MUL`) and logical operations (`AND`, `OR`, `XOR`, shifts).
   - Contains temporary registers such as the **Accumulator (AC)** and **Status Flags** (Zero, Carry, Sign, Overflow).
3. **Main Memory Unit:**
   - Linear array of addressable storage locations containing both program code and working variables.
   - Interfaced via **Memory Address Register (MAR)** and **Memory Data Register (MDR)**.
4. **Input/Output (I/O) Interface:**
   - Manages communication between external peripheral devices and internal system registers using polling, interrupts, or Direct Memory Access (DMA).

---

### Q2. Describe all the addressing modes used in the 8086 family with suitable examples for each. Explain how each mode calculates the effective address.

#### 1. Effective Address (EA) Calculation Formula
In 8086, the **Physical Address (20-bit)** is calculated as:
$$\text{Physical Address} = (\text{Segment Register} \times 16) + \text{Effective Address (EA)}$$
where $\text{EA} = \text{Base Register} + \text{Index Register} + \text{Displacement}$.

#### 2. Detailed 8086 Addressing Modes

| Addressing Mode | Effective Address Formula | Example Instruction | EA & Physical Address Explanation |
| :--- | :--- | :--- | :--- |
| **Immediate** | No EA (Operand in code). | `MOV AX, 5000H` | Data `5000H` is encoded directly inside instruction bytes. |
| **Register Direct** | No EA (Operand in register). | `MOV AX, BX` | Data taken directly from CPU register `BX`. |
| **Direct Memory** | $\text{EA} = \text{Displacement}$ | `MOV AX, [2000H]` | $\text{EA} = 2000\text{H}$. $\text{PA} = (\text{DS} \times 16) + 2000\text{H}$. |
| **Register Indirect**| $\text{EA} = [\text{BX}/\text{BP}/\text{SI}/\text{DI}]$ | `MOV AX, [BX]` | If `BX = 1500H`, $\text{EA} = 1500\text{H}$. |
| **Based** | $\text{EA} = \text{Base} + \text{Disp}$ | `MOV AX, [BX + 08H]` | If `BX = 1000H`, $\text{EA} = 1000\text{H} + 08\text{H} = 1008\text{H}$. |
| **Indexed** | $\text{EA} = \text{Index} + \text{Disp}$ | `MOV AX, [SI + 10H]` | If `SI = 2000H`, $\text{EA} = 2000\text{H} + 10\text{H} = 2010\text{H}$. |
| **Based-Indexed** | $\text{EA} = \text{Base} + \text{Index}$ | `MOV AX, [BX + SI]` | If `BX = 1000H, SI = 0050H`, $\text{EA} = 1050\text{H}$. |
| **Based-Indexed with Disp** | $\text{EA} = \text{Base} + \text{Index} + \text{Disp}$ | `MOV AX, [BX + SI + 04H]` | If `BX = 1000H, SI = 0050H`, $\text{EA} = 1054\text{H}$. |

---

### Q3. Explain the evolution of computers from the first to the fifth generation, highlighting key technological changes and performance improvements at each stage.

```
+---------------------------------------------------------------------------+
|                          COMPUTER GENERATIONS EVOLUTION                    |
|                                                                           |
| 1st Gen (1940-56)  : Vacuum Tubes ----> 1000s of Operations/sec           |
| 2nd Gen (1956-63)  : Transistors -------> 100,000s Operations/sec          |
| 3rd Gen (1964-71)  : Integrated Circuits (SSI/MSI) -> Millions Ops/sec    |
| 4th Gen (1971-Pres) : Microprocessors (VLSI/ULSI) -> Billions Ops/sec     |
| 5th Gen (Future)   : Artificial Intelligence & Quantum Computing          |
+---------------------------------------------------------------------------+
```

1. **1st Generation (1940-1956): Vacuum Tubes**
   - Technology: Thermionic vacuum tubes for logic; magnetic drums for memory.
   - Features: Enormous physical size, high heat generation, machine language programming.
   - Example: ENIAC, UNIVAC-I, EDVAC.
2. **2nd Generation (1956-1963): Transistors**
   - Technology: Bipolar junction transistors replaced bulky vacuum tubes.
   - Features: Smaller footprint, lower power consumption, Assembly & High-Level languages (FORTRAN, COBOL).
   - Example: IBM 7094, CDC 1604.
3. **3rd Generation (1964-1971): Integrated Circuits (ICs)**
   - Technology: Small/Medium Scale Integration (SSI/MSI ICs) combining dozens of transistors on silicon chips.
   - Features: Keyboards, monitors, Operating System software layer, timeshare processing.
   - Example: IBM System/360, PDP-8.
4. **4th Generation (1971-Present): Very Large Scale Integration (VLSI/ULSI)**
   - Technology: Single-chip Microprocessors containing millions/billions of transistors.
   - Features: Personal Computers (PCs), laptops, high-speed RAM, graphical user interfaces (GUI), Internet.
   - Example: Intel 8086, Pentium, Core i9, Apple M3.
5. **5th Generation (Present & Future): AI & Parallel Supercomputing**
   - Technology: Ultra Large Scale Integration (ULSI), Quantum computing, Neural processing units (NPUs).
   - Features: Parallel Processing (MIMD), natural language processing, autonomous AI decision systems.

---

### Q4. Discuss various performance metrics used to evaluate computer architecture with formulas, and explain Amdahl's Law with a numerical example.

#### 1. Performance Metrics & Formulas

1. **CPU Execution Time ($T_{\text{CPU}}$):**
   $$T_{\text{CPU}} = \text{Instruction Count (IC)} \times \text{CPI} \times \text{Clock Cycle Time } (T) = \frac{\text{IC} \times \text{CPI}}{f}$$
2. **Cycles Per Instruction (CPI):**
   $$\text{CPI} = \frac{\text{Total CPU Clock Cycles}}{\text{Instruction Count}}$$
3. **Millions of Instructions Per Second (MIPS):**
   $$\text{MIPS} = \frac{\text{Instruction Count}}{T_{\text{CPU}} \times 10^6} = \frac{f}{\text{CPI} \times 10^6}$$
4. **Floating-Point Operations Per Second (FLOPS):**
   $$\text{FLOPS} = \frac{\text{Total Floating-Point Operations}}{\text{Execution Time in Seconds}}$$

#### 2. Amdahl's Law
Amdahl's Law quantifies the maximum expected overall system speedup when only a fraction $f$ of a task is enhanced by a factor $s$:

$$\text{Speedup}_{\text{Overall}} = \frac{1}{(1 - f) + \frac{f}{s}}$$

#### 3. Numerical Example
- **Problem Statement:** A program spends **80%** of its total execution time on vector matrix multiplication. An engineer adds a hardware matrix accelerator that speeds up vector matrix operations by **5 times** ($s = 5$). Calculate the overall speedup achieved.
- **Given Data:**
  - Fraction enhanced ($f$) = $0.80$
  - Un-enhanced fraction ($1 - f$) = $0.20$
  - Enhancement speedup ($s$) = $5$
- **Calculation:**
  $$\text{Speedup}_{\text{Overall}} = \frac{1}{(1 - 0.80) + \frac{0.80}{5}} = \frac{1}{0.20 + 0.16} = \frac{1}{0.36} \approx \mathbf{2.78}$$
- **Result:** The overall system execution speed increases by **2.78 times** (or a 178% speedup).
"""

# Write Unit 1 files
with open(os.path.join(unit1_dir, "2M.md"), "w", encoding="utf-8") as f: f.write(u1_2m)
with open(os.path.join(unit1_dir, "3M.md"), "w", encoding="utf-8") as f: f.write(u1_3m)
with open(os.path.join(unit1_dir, "5M.md"), "w", encoding="utf-8") as f: f.write(u1_5m)
with open(os.path.join(unit1_dir, "10M.md"), "w", encoding="utf-8") as f: f.write(u1_10m)

print("Created Unit 1 QA Files!")
