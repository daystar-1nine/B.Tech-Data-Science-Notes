# Pentium 4 NetBurst Microarchitecture — MPCA Module 6

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
