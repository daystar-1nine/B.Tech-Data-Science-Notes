import os

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

m6_dir = os.path.join(MPCA_DIR, "Module 6")
m6_qa = os.path.join(m6_dir, "Module_6_QA")

os.makedirs(m6_dir, exist_ok=True)
os.makedirs(m6_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 6: PENTIUM 4 AND ARM PROCESSOR
# --------------------------------------------------------------------------

m6_files = {
    "1_Evolutionary_Comparison_8086_to_Pentium.md": """# Comparative Study: 8086 to Pentium 4 — MPCA Module 6

> **Definition:** The evolution of the **Intel x86 Microprocessor Architecture** from the 16-bit 8086 to the 7th-generation 32/64-bit Pentium 4 demonstrates radical advancements in bus widths, pipeline depths, caching hierarchies, and parallel instruction execution.

---

## 1. Comprehensive Master Comparison Table

| Feature / Processor | Intel 8086 | Intel 80386DX | Intel Pentium (P5) | Intel Pentium II | Intel Pentium 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Year Introduced** | 1978 | 1985 | 1993 | 1997 | 2000 |
| **Data Bus Width** | 16-bit | 32-bit | 64-bit | 64-bit | 64-bit |
| **Address Bus Width** | 20-bit | 32-bit | 32-bit | 36-bit (PAE) | 36-bit (64 GB) |
| **Physical Memory** | 1 MB | 4 GB | 4 GB | 64 GB | 64 GB |
| **Virtual Memory** | None | 64 TB | 64 TB | 64 TB | 64 TB |
| **Clock Frequency** | 5 - 10 MHz | 16 - 33 MHz | 60 - 200 MHz | 233 - 450 MHz | 1.3 - 3.8 GHz |
| **Pipeline Depth** | 2-stage (BIU/EU)| 3-stage | 5-stage (Superscalar)| 14-stage (Dynamic)| **20 to 31 stages** (Hyper-Pipelined)|
| **Integer Execution**| 1 inst / ~4 clocks| 1 inst / 2 clocks | **2 inst / clock (U/V)**| 3 micro-ops / clock| Out-of-Order Engine |
| **L1 Cache** | None | None | 16 KB (8K I + 8K D) | 32 KB (16K I + 16K D)| 8 KB D-Cache + 12K micro-op Trace Cache |
| **L2 Cache** | None | External | External | 512 KB (Cartridge) | **256 KB - 2 MB On-die** |
| **Key Innovations** | Segmented memory | 32-bit MMU, Paging | Superscalar, Dual U/V, BTB | Dual Independent Bus (DIB), MMX | NetBurst, Hyper-Threading, Trace Cache |

---

## 2. Key Architectural Milestones
1. **8086:** Introduced 16-bit computing and segmented memory architecture.
2. **80386:** Introduced 32-bit processing, flat memory model, Protected mode with 4-level privilege rings, and 2-level Paging MMU.
3. **Pentium:** Introduced superscalar dual integer pipelines (U and V pipes) and dynamic branch prediction.
4. **Pentium 4:** NetBurst hyper-pipelined microarchitecture, Execution Trace Cache, and Hyper-Threading Technology.

---

## 3. Quick Recall Flow
```
8086 (16-bit, 1MB) -> 80386 (32-bit, 4GB, Paging) -> Pentium (Superscalar U/V, 64-bit bus) -> Pentium 4 (NetBurst, Hyper-Threading)
```
""",

    "2_Pentium_4_NetBurst_Microarchitecture.md": """# Pentium 4 NetBurst Microarchitecture — MPCA Module 6

> **Definition:** The **Intel NetBurst Microarchitecture** is a 7th-generation x86 processor design engineered to achieve ultra-high clock speeds (up to 3.8 GHz) and maximum throughput using a deep **20-stage (later 31-stage Prescott) Hyper-Pipelined Technology**.

---

## 1. Detailed Technical Explanation

### Functional Components of NetBurst Microarchitecture

```
                        NETBURST MICROARCHITECTURE
 +------------------------------------------------------------------------+
 |  [ Advanced Dynamic Execution Engine ]                                 |
 |    - Out-of-Order Execution Logic                                      |
 |    - 126 In-Flight Instructions Window                                 |
 |                                                                        |
 |  [ Execution Trace Cache ]                                             |
 |    - Stores 12,000 decoded micro-ops (uops)                            |
 |    - Bypasses traditional instruction decoder on loops & branch hits   |
 |                                                                        |
 |  [ Rapid Execution Engine (ALUs) ]                                     |
 |    - Integer ALUs clocked at TWICE (2x) the core processor frequency   |
 |    - Executes simple arithmetic (ADD, SUB) in 0.5 clock cycles!        |
 |                                                                        |
 |  [ High-Performance System Bus ]                                       |
 |    - Quad-Pumped Front Side Bus (FSB) at 400 / 533 / 800 MHz (6.4 GB/s)|
 +------------------------------------------------------------------------+
```

---

## 2. Deep Dive into NetBurst Innovations

### 1. Execution Trace Cache (L1 I-Cache Replacement)
- Traditional architectures store raw x86 instructions in L1 instruction cache, requiring repeated decode cycles.
- **Trace Cache** stores **pre-decoded micro-operations (uops)** in their predicted execution path order.
- Decodes instructions *before* caching, removing the x86 instruction decoder bottleneck during execution loops.

### 2. Hyper-Pipelined Technology (20 to 31 Stages)
- Decomposes instruction processing into 20 distinct pipelined clock stages.
- Enables very high operating frequencies (over 3.0 GHz) by reducing the amount of logic executed per stage.

### 3. Rapid Execution Engine (2x Clock ALUs)
- Integer Arithmetic Logic Units (ALUs) run at **double the core processor frequency**.
- Basic integer operations like `ADD`, `SUB`, and bitwise logic complete in **half a clock cycle**.

### 4. Quad-Pumped System Bus
- Transfers data 4 times per clock cycle over a 64-bit bus, delivering up to **6.4 GB/s memory bandwidth** at 800 MHz FSB.

---

## 3. Core Concepts & Memory Keywords
- **NetBurst:** 7th-gen x86 design focused on high clock frequencies.
- **Trace Cache:** Caches 12K decoded micro-ops instead of raw x86 bytes.
- **Rapid Execution Engine:** 2x core clock rate ALUs executing in 0.5 cycles.
- **Hyper-Pipeline:** 20-stage pipeline depth.

---

## 4. Quick Recall Flow
```
NetBurst -> 20-Stage Hyper-Pipeline -> Execution Trace Cache (12K uops) -> Rapid Engine (2x ALUs) -> Quad-Pumped FSB (800MHz)
```
""",

    "3_Pentium_4_ITLB_Branch_Prediction_and_Hyper_Threading.md": """# Pentium 4 ITLB, Branch Prediction & Hyper-Threading — MPCA Module 6

> **Definition:** Pentium 4 integrates an **Instruction Translation Lookaside Buffer (ITLB)**, advanced **Dynamic Branch Prediction**, and **Hyper-Threading (HT) Technology** (Simultaneous Multithreading) to maximize execution unit utilization.

---

## 1. Detailed Technical Explanation

### 1. Instruction Translation Lookaside Buffer (ITLB)
- A high-speed associative hardware cache that caches virtual-to-physical page address translations for instruction fetch.
- Eliminates memory access latency to Page Tables in RAM during code prefetch.

---

## 2. Advanced Dynamic Branch Prediction
- Because the NetBurst pipeline is **20 stages deep**, a branch misprediction penalty results in flushing 20 stages of instructions (a massive performance penalty).
- NetBurst utilizes a **4 KB Branch Target Buffer (BTB)** combining:
  - **Static Branch Predictor:** Assumes backward branches (loops) are TAKEN, forward conditional branches are NOT TAKEN.
  - **Dynamic 2-Level Adaptive Branch Predictor:** Tracks global execution history patterns, achieving **>94% prediction accuracy**.

---

## 3. Hyper-Threading Technology (HT Technology)

**Hyper-Threading** is Intel's hardware implementation of **Simultaneous Multithreading (SMT)** that allows a single physical processor core to appear as **two logical processors** to the operating system.

```
WITHOUT HYPER-THREADING:
  Physical Core: [ Thread 1 ] ===> Idle Execution Units (Wasted Silicon)

WITH HYPER-THREADING (Simultaneous Multithreading):
  Logical Core 1: [ Thread 1 ] \
                                ===> Shared Physical Execution Units (ALU, FPU, Caches)
  Logical Core 2: [ Thread 2 ] /     (Zero Idle Slots, 15-30% Throughput Boost!)
```

### Architecture of Hyper-Threading:
1. **Duplicated Architectural State:**
   - Registers (`EAX`, `EBX`, etc.), `EFLAGS`, Segment Selectors, Control Registers (`CR0-CR3`), and APIC interrupt controllers are **duplicated** for each logical thread.
2. **Shared Execution Resources:**
   - Execution Units (ALUs, FPUs), Trace Cache, L2 Cache, and Memory Subsystems are **shared dynamically** between the two threads.
3. **Performance Benefit:** Improves CPU execution pipeline utilization by up to **30%** with only a ~5% increase in physical silicon chip area.

---

## 4. Must-Write Points for Exams
- Hyper-Threading presents one physical core as two logical cores to the OS scheduler.
- Architectural state (GPRs, Flags, Program Counter) is duplicated; physical ALUs/FPUs/Caches are shared.
- Dynamic branch prediction accuracy (>94%) is vital to prevent severe 20-stage pipeline flush penalties.

---

## 5. Quick Recall Flow
```
ITLB Page Caching -> Advanced BTB (>94% Branch Accuracy) -> Hyper-Threading: 1 Physical Core = 2 Logical Processors (Duplicated State, Shared ALUs)
```
""",

    "4_Self_Learning_ARM_Processor_Architecture_and_Features.md": """# Self-Learning: ARM Processor Architecture & Features — MPCA Module 6

> **Definition:** The **ARM (Advanced RISC Machines)** processor is a 32/64-bit **Reduced Instruction Set Computer (RISC)** architecture engineered for high energy efficiency, low power consumption, and high performance in mobile, IoT, and embedded devices.

---

## 1. Detailed Technical Explanation

### 1. Key Architectural Features of ARM:
1. **Load-Store Architecture:** Data processing instructions (ADD, SUB, AND) operate **only on registers**; memory is accessed exclusively via explicit `LDR` (Load) and `STR` (Store) instructions.
2. **Inline Barrel Shifter:** One operand in any arithmetic/logic instruction can be shifted/rotated by arbitrary bits in **hardware in the same clock cycle** without extra instructions.
   - *Example:* `ADD R0, R1, R2, LSL #2` ($R0 = R1 + R2 \times 4$).
3. **Conditional Execution of All Instructions:** Every ARM instruction contains a 4-bit condition code field (`EQ`, `NE`, `GT`, `LT`, `AL`), eliminating unnecessary jump/branch instructions in small `if-else` blocks.
4. **Dual Instruction Sets (ARM vs Thumb):**
   - **ARM State (32-bit):** Full 32-bit high-performance instruction set.
   - **Thumb State (16-bit):** Compact 16-bit instruction set offering up to **30-40% code density reduction** for memory-constrained microcontrollers.

---

## 2. Register Organization of ARM (ARM7 / Cortex-A)
- Total of **37 registers** (31 General-Purpose 32-bit registers and 6 Status registers), organized into banked registers across operating modes:
  - `R0 - R12`: General-purpose data registers.
  - `R13 (SP)`: Stack Pointer.
  - `R14 (LR)`: Link Register (stores return address upon function call).
  - `R15 (PC)`: Program Counter.
  - `CPSR`: Current Program Status Register.
  - `SPSR`: Saved Program Status Register (used during interrupt/exception modes).

---

## 3. CISC (x86/Pentium) vs RISC (ARM) Comparison

| Feature | Intel x86 / Pentium (CISC) | ARM Processor (RISC) |
| :--- | :--- | :--- |
| **Instruction Size** | Variable (1 to 15 bytes) | **Fixed (32-bit ARM / 16-bit Thumb)** |
| **Memory Access** | Allowed directly in arithmetic ops | **Strict Load-Store Only (LDR/STR)** |
| **Power Consumption**| Higher (Desktop / Server oriented) | **Ultra Low Power (Battery / Mobile)** |
| **Pipelining** | Complex hyper-pipelines (20-31 stages)| Simple, highly efficient (3-8 stages) |
| **Industry Dominance**| PC, Laptops, Cloud Servers | **Smartphones (99% iOS/Android), IoT, Apple Silicon (M1/M2/M3)** |

---

## 4. Quick Recall Flow
```
ARM RISC -> Load-Store Architecture -> Inline Barrel Shifter -> Conditional Execution -> ARM (32-bit) / Thumb (16-bit) -> Mobile & Embedded Dominance
```
"""
}

# Write Module 6 files
for fname, content in m6_files.items():
    with open(os.path.join(m6_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created MPCA Module 6 Files!")
