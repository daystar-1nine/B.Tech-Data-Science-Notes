# 8257 Direct Memory Access Controller (DMAC) — MPCA Module 4

> **Definition:** The **Intel 8257** is a 4-channel programmable **Direct Memory Access Controller (DMAC)** that enables high-speed data transfer directly between I/O peripherals and system RAM without CPU intervention, bypassing the slow CPU fetch-execute cycle.

---

## 1. Detailed Technical Explanation

### 1. The DMA Concept & Speed Advantage
In standard programmed I/O, every byte transferred from a disk/network card to RAM requires multiple CPU instructions (`IN AL, DX` followed by `MOV [SI], AL`). DMA bypasses the CPU:

```
PROGRAMMED I/O:  Peripheral ---> CPU (AL Reg) ---> RAM   (Slow: ~20-50 Clock cycles/byte)
DMA TRANSFER:    Peripheral ======================> RAM   (Fast: 2-4 Clock cycles/byte)
```

---

## 2. 8257 Internal Block Diagram & Channels

```
                        8257 DMAC ARCHITECTURE
 +---------------------------------------------------------------+
 |  [ Channel 0 ] -> 16-bit DMA Address Reg & 14-bit Count Reg   |
 |  [ Channel 1 ] -> 16-bit DMA Address Reg & 14-bit Count Reg   |
 |  [ Channel 2 ] -> 16-bit DMA Address Reg & 14-bit Count Reg   |
 |  [ Channel 3 ] -> 16-bit DMA Address Reg & 14-bit Count Reg   |
 |                                                               |
 |  Control Logic & Priority Resolver:                           |
 |    - DRQ0 to DRQ3 (DMA Requests from Peripherals)             |
 |    - /DACK0 to /DACK3 (DMA Acknowledgements to Peripherals)   |
 |    - HRQ (Hold Request to 8086 CPU)                           |
 |    - HLDA (Hold Acknowledge from 8086 CPU)                    |
 |    - /MEMR, /MEMW, /IOR, /IOW (Bus Control Strobes)           |
 +---------------------------------------------------------------+
```

---

## 3. DMA Transfer Sequence (Step-by-Step)
1. Peripheral asserts **DMA Request (`DRQ`)** to 8257.
2. 8257 asserts **Hold Request (`HRQ`)** to the 8086 CPU.
3. 8086 finishes its current bus cycle, floats its Address, Data, and Control buses into high-impedance state, and asserts **Hold Acknowledge (`HLDA`)** to 8257.
4. 8257 takes master control of system buses, sends **`DACK`** to peripheral.
5. 8257 places memory address on address bus and issues simultaneous **\overlineIOR** and **\overlineMEMW** (or **\overlineMEMR** and **\overlineIOW**) to transfer data in **a single bus cycle**.
6. After count register reaches zero (**Terminal Count TC**), 8257 lowers `HRQ`, returning bus mastership to 8086 CPU.

---

## 4. DMA Transfer Modes
1. **Single Transfer Mode:** 8257 transfers one byte per request, releasing the bus back to CPU between transfers.
2. **Block Transfer Mode (Burst Mode):** 8257 transfers the entire block of data continuously until Terminal Count is reached.
3. **Demand Transfer Mode:** 8257 continues transferring data as long as peripheral holds `DRQ` active.
4. **Cascade Mode:** Allows multiple 8257 master-slave chips to be interconnected to expand channels.

---

## 5. Must-Write Points for Exams
- 8257 has **4 independent DMA channels** (Channel 0 to Channel 3).
- Each channel contains a **16-bit Address Register** and a **14-bit Terminal Count Register**.
- DMA transfer achieves maximum memory-to-I/O bandwidth with zero CPU software overhead.

---

## 6. Quick Recall Flow
```
DRQ -> HRQ -> CPU floats bus & asserts HLDA -> DACK -> Single Cycle MEM/IO Read/Write -> Terminal Count (TC)
```
