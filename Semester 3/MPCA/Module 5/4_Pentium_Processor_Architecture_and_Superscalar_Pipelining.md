# Pentium Processor Architecture & Superscalar Operation — MPCA Module 5

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
 |        /                \                                                 |
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
- Dual-issue U and V pipelines achieve execution throughput of up to 2 instructions per clock cycle (**IPC = 2**).

---

## 5. Quick Recall Flow
```
Pentium -> Superscalar -> U & V Dual Pipelines (5-stages: PF, D1, D2, EX, WB) -> 8KB Code/Data Caches -> BTB 2-bit Branch Prediction
```
