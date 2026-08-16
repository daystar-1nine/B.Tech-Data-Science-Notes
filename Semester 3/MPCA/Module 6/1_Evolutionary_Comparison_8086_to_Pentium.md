# Comparative Study: 8086 to Pentium 4 — MPCA Module 6

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
