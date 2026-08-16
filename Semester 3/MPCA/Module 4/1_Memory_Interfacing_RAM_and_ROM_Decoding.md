# Memory Interfacing: RAM & ROM Decoding — MPCA Module 4

> **Definition: Memory Interfacing** is the electronic hardware arrangement that connects semiconductor memory chips (RAM and EPROM/ROM) to the microprocessor's Address, Data, and Control buses using **Address Decoding Logic** to assign unique physical address ranges to each memory chip.

---

## 1. Detailed Technical Explanation

### 1. 8086 Memory Organization Review
- The 8086 microprocessor has a **20-bit Address Bus** (**A_0 - A_19**), enabling it to address up to **1 MB** (**2^20** bytes) of physical memory.
- Physical memory is organized into two 512 KB banks:
  - **Even Bank (Lower Bank):** Connected to Data Bus lines **D_0 - D_7**, selected by address line **A_0 = 0**.
  - **Odd Bank (Higher Bank):** Connected to Data Bus lines **D_8 - D_15**, selected by **\overlineBHE = 0** (Bus High Enable).

```
   Microprocessor 8086                  Memory Banks (1 MB Total)
 +----------------------+             +-----------------------------+
 |                      |  A0 = 0     | EVEN BANK (512 KB RAM/ROM)  |
 |  Data Lines D0-D7    |===========> | Data Lines D0-D7            |
 |                      |             +-----------------------------+
 |                      |  /BHE = 0   | ODD BANK (512 KB RAM/ROM)   |
 |  Data Lines D8-D15   |===========> | Data Lines D8-D15           |
 +----------------------+             +-----------------------------+
```

---

## 2. Address Decoding Logic (74LS138 3-to-8 Decoder)

The **74LS138** decoder is the industry standard IC used to generate chip select (**\overlineCS**) signals for multiple memory chips.

```
                  74LS138 3-to-8 DECODER
                +------------------------+
   A19 -------->| G1 (Active High Enable)|
   A18 -------->| /G2A (Active Low)      |
   M//IO ------>| /G2B (Active Low)      |
                |                        |
   A17 -------->| C (Select Input 2)     |-----> /Y0 (CS for Chip 0)
   A16 -------->| B (Select Input 1)     |-----> /Y1 (CS for Chip 1)
   A15 -------->| A (Select Input 0)     |-----> /Y2 (CS for Chip 2)
                +------------------------+-----> ...
```

### Memory Map Design Example:
To interface a 64 KB EPROM chip (Address lines **A_0 - A_15** used internally inside chip):
- Higher address lines **A_16 - A_19** are connected to the decoder.
- When **A_19A_18A_17A_16 = 1111_2**, decoder output **\overlineY_7** goes LOW, activating the EPROM chip in address range `F0000H - FFFFFH` (Reset address area of 8086).

---

## 3. Core Concepts & Memory Keywords
- **Address Decoding:** Translating upper address bus bits into unique **\overlineCS** chip select signals.
- \overlineBHE** & **A_0**:** Control signals used to select byte or 16-bit word memory transfers.
- **74LS138 Decoder:** 3 select inputs (**A, B, C**) to 8 active-low outputs (**\overlineY_0 - \overlineY_7**).

---

## 4. Must-Write Points for Exams
- ROM/EPROM is always placed at the top of memory (`FFFF0H`) because 8086 starts execution at `FFFF0H` upon reset.
- RAM is typically mapped starting from address `00000H` (to hold Interrupt Vector Table IVT).
- Both Even and Odd memory banks must receive appropriate **\overlineRD** / **\overlineWR** control strobes.

---

## 5. Quick Recall Flow
```
20-bit Address Bus -> Lower bits (A0-Ak) to Memory Chip -> Upper bits to 74LS138 Decoder -> Chip Select /CS Generated
```
