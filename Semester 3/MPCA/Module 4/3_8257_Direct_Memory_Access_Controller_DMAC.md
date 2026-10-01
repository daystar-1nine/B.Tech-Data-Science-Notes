# 8257 Direct Memory Access Controller (DMAC)

**Q. What is Direct Memory Access (DMA)? Draw and explain the internal architecture of the Intel 8257 DMA Controller. Explain the step-by-step sequence of a DMA transfer and describe its operating modes.**

---

> 📌 **Definition to Remember**
> **Direct Memory Access (DMA)** is a high-speed data transfer technique where dedicated hardware (the DMA Controller) takes control of system buses to transfer data blocks directly between I/O peripherals and RAM without passing through CPU registers, bypassing processor instruction fetch-decode-execute overhead.

---

### 1. The DMA Concept vs. Programmed I/O

In programmed I/O, every data byte requires CPU execution cycles (`IN AL, DX` followed by `MOV [SI], AL`), requiring 20 to 50 clock cycles per byte. DMA transfers data in **a single bus cycle (2 to 4 clocks)**.

```
PROGRAMMED I/O:
[ Peripheral ] --------> [ CPU Register (AL) ] --------> [ System RAM ]
                         (~20-50 Clock cycles per byte - CPU Busy)

DMA DATA TRANSFER:
[ Peripheral ] ========================================> [ System RAM ]
                  (2-4 Clock cycles per byte - CPU Floats Buses)
                         ^                 ^
                         |-- Bus Controls -|
                         [ 8257 DMA Controller ]
```

| Parameter | Programmed I/O | Interrupt-Driven I/O | DMA Transfer |
| :--- | :--- | :--- | :--- |
| **Bus Master** | CPU | CPU | **DMA Controller (8257)** |
| **Transfer Rate** | Very Slow (~50 KB/s) | Moderate (~100 KB/s) | **Very Fast (~2 MB/s)** |
| **CPU Involvement** | 100% occupied | Services ISR per byte | **Zero involvement during block transfer** |
| **Target Devices** | Keyboards, simple sensors | Mice, UARTS | **Hard disks, Floppy drives, NICs, Displays**|

---

### 2. Internal Architecture & Block Diagram of 8257

The 8257 provides **4 independent DMA channels** (Channel 0 to Channel 3).

```
                         8257 INTERNAL ARCHITECTURE
 +-------------------------------------------------------------------------+
 |                                                                         |
 |  [ Channel 0 ] -> 16-bit DMA Address Reg & 14-bit Terminal Count Reg    |
 |  [ Channel 1 ] -> 16-bit DMA Address Reg & 14-bit Terminal Count Reg    |
 |  [ Channel 2 ] -> 16-bit DMA Address Reg & 14-bit Terminal Count Reg    |
 |  [ Channel 3 ] -> 16-bit DMA Address Reg & 14-bit Terminal Count Reg    |
 |                                                                         |
 |  Priority Resolver Logic:                                               |
 |    - Fixed Priority Mode (Ch 0 > Ch 1 > Ch 2 > Ch 3)                    |
 |    - Rotating Priority Mode (Round-robin servicing)                     |
 |                                                                         |
 |  Control Logic & System Interface:                                      |
 |    - DRQ0 - DRQ3 (DMA Requests from I/O Peripherals)                    |
 |    - /DACK0 - /DACK3 (DMA Acknowledgements to I/O Peripherals)          |
 |    - HRQ (Hold Request output to CPU)                                   |
 |    - HLDA (Hold Acknowledge input from CPU)                             |
 |    - /MEMR, /MEMW, /IOR, /IOW (System Bus Control Strobes)              |
 |    - TC (Terminal Count output), MARK (Modulo-128 marker)               |
 +-------------------------------------------------------------------------+
```

#### Channel Registers:
* **DMA Address Register (16-bit):** Holds the memory address for the current transfer; automatically incremented after each byte.
* **Terminal Count Register (14-bit count + 2-bit mode):** Holds the number of bytes to transfer minus 1 (up to 16,384 bytes). Lower 14 bits count down; upper 2 bits specify transfer type (DMA Read, DMA Write, DMA Verify).

---

### 3. Step-by-Step DMA Transfer Sequence

```
Peripheral              8257 DMAC                     8086 CPU
    |                       |                            |
    |---- 1. DRQ ---------->|                            |
    |                       |---- 2. HRQ --------------->|
    |                       |                            | (Finishes current cycle,
    |                       |                            |  floats Address/Data/Control)
    |                       |<--- 3. HLDA ---------------|
    |<--- 4. /DACK ---------|                            |
    |                       |                            |
    |<====== 5. Direct Data Transfer to/from RAM =======>| (Simultaneous /IOR & /MEMW)
    |                       |                            |
    |                       |-- 6. TC reached ---------->| (Count = 0)
    |                       |---- 7. Lowers HRQ -------->| (Bus mastership restored)
```

1. **Request:** Peripheral asserts **DMA Request (`DRQ`)** to 8257.
2. **Hold Request:** 8257 asserts **`HRQ` (Hold Request)** to 8086 CPU.
3. **Hold Acknowledge:** 8086 finishes its current bus cycle, floats its buses into high-impedance state, and asserts **`HLDA` (Hold Acknowledge)** back to 8257.
4. **Device Acknowledge:** 8257 activates **`DACK`** line to peripheral and puts the memory address onto the Address Bus.
5. **Single-Cycle Transfer:** 8257 asserts **$\overline{\text{IOR}}$ and $\overline{\text{MEMW}}$ simultaneously** (for DMA Read) or **$\overline{\text{MEMR}}$ and $\overline{\text{IOW}}$ simultaneously** (for DMA Write). Data moves in one bus cycle without entering DMAC registers.
6. **Increment & Decrement:** Memory address register increments by 1; Terminal Count decrements by 1.
7. **Completion (TC):** When count reaches zero, 8257 asserts **Terminal Count (`TC`)** and lowers `HRQ`, releasing bus mastership back to the 8086 CPU.

---

### 4. DMA Transfer Modes

1. **Byte / Single Transfer Mode:** Transfers one byte per request, releasing buses back to CPU after each byte. Useful when CPU cannot be blocked.
2. **Burst / Block Transfer Mode:** Transfers the entire block of data continuously until Terminal Count reaches zero. Highest throughput.
3. **Demand Transfer Mode:** Continues transferring data as long as the peripheral asserts `DRQ`; pauses if peripheral buffer runs empty.
4. **Cascade Mode:** Multiple 8257 chips interconnected in master-slave hierarchy to expand channels beyond 4.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. DMA bypasses the CPU to perform high-speed memory-peripheral data transfers in a single bus cycle.
> 2. The 8257 contains **4 independent DMA channels**, each with a 16-bit Address Register and a 14-bit Terminal Count Register (up to 16 KB transfer).
> 3. Key handshaking signals: **`DRQ`** (from peripheral), **`HRQ`** (to CPU), **`HLDA`** (from CPU), and **`DACK`** (to peripheral).
> 4. During transfer, the CPU enters a hold state and tristates its address, data, and control lines.
> 5. 8257 simultaneously asserts **$\overline{\text{IOR}}$ and $\overline{\text{MEMW}}$** (or $\overline{\text{MEMR}}$ and $\overline{\text{IOW}}$) to move data directly.
> 6. Priority can be configured as **Fixed Priority** (Ch 0 highest) or **Rotating Priority** (Round-robin).
> 7. **Terminal Count (`TC`)** signal is asserted when the programmed number of bytes has been transferred.

---

> ⚡ **Quick Recall**
> `DRQ (Peripheral) → HRQ (to CPU) → HLDA (from CPU) → DACK (to Device) → Simultaneous /IOR & /MEMW → Terminal Count (TC) → Release Bus`
