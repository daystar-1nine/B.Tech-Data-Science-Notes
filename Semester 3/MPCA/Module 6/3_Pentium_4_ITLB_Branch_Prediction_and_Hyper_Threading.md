# Pentium 4 ITLB, Branch Prediction & Hyper-Threading — MPCA Module 6

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
  Logical Core 1: [ Thread 1 ]                                 ===> Shared Physical Execution Units (ALU, FPU, Caches)
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
