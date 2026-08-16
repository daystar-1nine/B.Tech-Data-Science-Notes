import os

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

m4_dir = os.path.join(MPCA_DIR, "Module 4")
m4_qa = os.path.join(m4_dir, "Module_4_QA")

os.makedirs(m4_dir, exist_ok=True)
os.makedirs(m4_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4: MEMORY AND PERIPHERALS INTERFACING
# --------------------------------------------------------------------------

m4_files = {
    "1_Memory_Interfacing_RAM_and_ROM_Decoding.md": """# Memory Interfacing: RAM & ROM Decoding — MPCA Module 4

> **Definition:** **Memory Interfacing** is the electronic hardware arrangement that connects semiconductor memory chips (RAM and EPROM/ROM) to the microprocessor's Address, Data, and Control buses using **Address Decoding Logic** to assign unique physical address ranges to each memory chip.

---

## 1. Detailed Technical Explanation

### 1. 8086 Memory Organization Review
- The 8086 microprocessor has a **20-bit Address Bus** ($A_0 - A_{19}$), enabling it to address up to **1 MB** ($2^{20}$ bytes) of physical memory.
- Physical memory is organized into two 512 KB banks:
  - **Even Bank (Lower Bank):** Connected to Data Bus lines $D_0 - D_7$, selected by address line $A_0 = 0$.
  - **Odd Bank (Higher Bank):** Connected to Data Bus lines $D_8 - D_{15}$, selected by $\\overline{BHE} = 0$ (Bus High Enable).

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

The **74LS138** decoder is the industry standard IC used to generate chip select ($\\overline{CS}$) signals for multiple memory chips.

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
To interface a 64 KB EPROM chip (Address lines $A_0 - A_{15}$ used internally inside chip):
- Higher address lines $A_{16} - A_{19}$ are connected to the decoder.
- When $A_{19}A_{18}A_{17}A_{16} = 1111_2$, decoder output $\\overline{Y}_7$ goes LOW, activating the EPROM chip in address range `F0000H - FFFFFH` (Reset address area of 8086).

---

## 3. Core Concepts & Memory Keywords
- **Address Decoding:** Translating upper address bus bits into unique $\\overline{CS}$ chip select signals.
- **$\\overline{BHE}$ & $A_0$:** Control signals used to select byte or 16-bit word memory transfers.
- **74LS138 Decoder:** 3 select inputs ($A, B, C$) to 8 active-low outputs ($\\overline{Y}_0 - \\overline{Y}_7$).

---

## 4. Must-Write Points for Exams
- ROM/EPROM is always placed at the top of memory (`FFFF0H`) because 8086 starts execution at `FFFF0H` upon reset.
- RAM is typically mapped starting from address `00000H` (to hold Interrupt Vector Table IVT).
- Both Even and Odd memory banks must receive appropriate $\\overline{RD}$ / $\\overline{WR}$ control strobes.

---

## 5. Quick Recall Flow
```
20-bit Address Bus -> Lower bits (A0-Ak) to Memory Chip -> Upper bits to 74LS138 Decoder -> Chip Select /CS Generated
```
""",

    "2_8255_Programmable_Peripheral_Interface_PPI.md": """# 8255 Programmable Peripheral Interface (PPI) — MPCA Module 4

> **Definition:** The **Intel 8255A (PPI)** is a general-purpose programmable I/O device designed to interface parallel peripheral devices (keyboards, displays, ADCs, printers) to the 8086 microprocessor.

---

## 1. Detailed Technical Explanation

### 1. Internal Block Diagram of 8255
The 8255 features **24 programmable I/O pins** divided into three 8-bit ports:
- **Port A (8 pins - PA0 to PA7):** Can be programmed as 8-bit Input, Output, or Bidirectional port.
- **Port B (8 pins - PB0 to PB7):** Can be programmed as 8-bit Input or Output port.
- **Port C (8 pins - PC0 to PC7):** Can be split into two 4-bit ports: **Port C Upper (PC4-PC7)** and **Port C Lower (PC0-PC3)** for handshake signals or simple I/O.

```
                    8255 INTERNAL ARCHITECTURE
 +---------------------------------------------------------------+
 |  Data Bus Buffer (D0-D7) <====> Microprocessor Data Bus       |
 |                                                               |
 |  Read/Write Control Logic:                                    |
 |    /RD, /WR, A0, A1, /CS, RESET                               |
 |                                                               |
 |  [ Group A Control ] -----> Port A (PA0-PA7)                  |
 |                      -----> Port C Upper (PC4-PC7)            |
 |                                                               |
 |  [ Group B Control ] -----> Port B (PB0-PB7)                  |
 |                      -----> Port C Lower (PC0-PC3)            |
 +---------------------------------------------------------------+
```

---

## 2. 8255 Port Selection Truth Table

| $\\overline{CS}$ | $A_1$ | $A_0$ | Selected Register / Port |
| :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | **Port A** |
| 0 | 0 | 1 | **Port B** |
| 0 | 1 | 0 | **Port C** |
| 0 | 1 | 1 | **Control Word Register (CWR)** |
| 1 | X | X | 8255 Deselected (High Impedance) |

---

## 3. Control Word Register (CWR) Formats

### 1. I/O Mode Set Control Word ($D_7 = 1$)
```
  D7   D6   D5   D4   D3   D2   D1   D0
+----+----+----+----+----+----+----+----+
| 1  | Mode A  | PA | PCU| MB | PB | PCL|
+----+----+----+----+----+----+----+----+
  |    \______/   |    |   |    |    |
  |     Mode A    |    |   |    |    +--> Port C Lower (1=Input, 0=Output)
  |   00: Mode 0  |    |   |    +-------> Port B (1=Input, 0=Output)
  |   01: Mode 1  |    |   +------------> Mode B (0=Mode 0, 1=Mode 1)
  |   1X: Mode 2  |    +----------------> Port C Upper (1=Input, 0=Output)
  |               +---------------------> Port A (1=Input, 0=Output)
  +-------------------------------------> Mode Set Flag (1 = Active)
```

### 2. Operating Modes of 8255:
1. **Mode 0 (Basic I/O):** Simple input or output without handshake signals. All ports (A, B, C) operate independently.
2. **Mode 1 (Strobed I/O):** Handshake data transfer. Ports A and B transfer data using Port C pins for handshake control signals (STB, IBF, INTR).
3. **Mode 2 (Strobed Bidirectional Bus):** Port A acts as an 8-bit bidirectional bus using 5 pins of Port C for handshaking.
4. **BSR Mode (Bit Set/Reset Mode, $D_7 = 0$):** Used to set or reset individual bits of **Port C only** without affecting other bits.

---

## 4. Must-Write Points for Exams
- 8255 has 24 I/O pins configured into Port A, Port B, and Port C (Upper & Lower).
- $D_7 = 1$ in Control Word indicates **I/O Mode**; $D_7 = 0$ indicates **BSR Mode**.
- Port C provides handshake status lines for Mode 1 and Mode 2 transfers.

---

## 5. Quick Recall Flow
```
8255 PPI -> 24 Pins (Ports A, B, C) -> Port Selection (A1, A0) -> Modes: Mode 0 (Basic), Mode 1 (Strobe), Mode 2 (Bi-dir), BSR Mode
```
""",

    "3_8257_Direct_Memory_Access_Controller_DMAC.md": """# 8257 Direct Memory Access Controller (DMAC) — MPCA Module 4

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
5. 8257 places memory address on address bus and issues simultaneous $\\overline{IOR}$ and $\\overline{MEMW}$ (or $\\overline{MEMR}$ and $\\overline{IOW}$) to transfer data in **a single bus cycle**.
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
""",

    "4_8259_Programmable_Interrupt_Controller_PIC.md": """# 8259 Programmable Interrupt Controller (PIC) — MPCA Module 4

> **Definition:** The **Intel 8259A (PIC)** is an 8-channel programmable interrupt controller designed to manage, prioritize, and translate multiple hardware interrupt requests ($IR_0 - IR_7$) into 8086 vector interrupt instructions.

---

## 1. Detailed Technical Explanation

### Internal Architecture & Block Diagram of 8259

```
                      8259 INTERNAL ARCHITECTURE
 +------------------------------------------------------------------+
 |  Interrupt Request Register (IRR):                               |
 |    Latches incoming interrupt requests on pins IR0 - IR7.        |
 |                                                                  |
 |  Interrupt Mask Register (IMR):                                  |
 |    Stores mask bits (OCW1) to selectively enable/disable IR lines|
 |                                                                  |
 |  Priority Resolver (PR):                                         |
 |    Determines the highest priority unmasked pending interrupt.   |
 |                                                                  |
 |  In-Service Register (ISR):                                      |
 |    Tracks which interrupt level is currently being serviced.     |
 |                                                                  |
 |  Control Logic & Cascade Buffer:                                 |
 |    - INT (Interrupt output to 8086 INTR pin)                     |
 |    - /INTA (Interrupt Acknowledge input from 8086)               |
 |    - CAS0, CAS1, CAS2 (Master-Slave cascading lines)             |
 |    - /SP//EN (Slave Program / Enable Buffer)                     |
 +------------------------------------------------------------------+
```

---

## 2. 8259 Interrupt Processing Sequence
1. Peripheral asserts an interrupt line ($IR_0 - IR_7$).
2. **IRR** stores the request; **Priority Resolver** checks IRR against **IMR** mask and current **ISR** level.
3. 8259 sends an **`INT`** signal to 8086 CPU's `INTR` pin.
4. 8086 CPU responds with the **First $\\overline{INTA}$ Pulse** (Interrupt Acknowledge).
5. Upon 1st $\\overline{INTA}$, the highest priority bit is set in **ISR** and cleared from **IRR**.
6. 8086 issues the **Second $\\overline{INTA}$ Pulse**. 8259 places the **8-bit Interrupt Vector Type Number (00H - FFH)** on the Data Bus ($D_0 - D_7$).
7. 8086 reads the vector number, multiplies by 4, and jumps to the corresponding **Interrupt Service Routine (ISR)** in the IVT table.
8. At the end of the ISR subroutine, an **End of Interrupt (EOI)** command is sent to 8259 to clear the active bit in the ISR register.

---

## 3. Priority Modes in 8259
1. **Fully Nested Mode (Default):** $IR_0$ has the highest priority and $IR_7$ has the lowest priority. Lower priority interrupts are inhibited while a higher priority ISR is running.
2. **Automatic Rotation Mode:** Equal priority round-robin; after a channel is serviced, it is assigned the lowest priority.
3. **Specific Rotation Mode:** Programmer manually sets which IR channel has the lowest priority.

---

## 4. Must-Write Points for Exams
- **IRR** stores requested interrupts, **ISR** stores currently executing interrupt, **IMR** masks unwanted interrupts.
- Two $\\overline{INTA}$ pulses are required from 8086 to fetch the interrupt vector from 8259.
- A single 8259 supports 8 interrupt levels ($IR_0 - IR_7$); cascading in Master-Slave supports up to **64 interrupt levels**.

---

## 5. Quick Recall Flow
```
IR0-IR7 -> IRR -> Priority Resolver -> INT to 8086 -> 1st /INTA (Set ISR) -> 2nd /INTA (Send Vector Byte) -> Execute ISR -> EOI Command
```
""",

    "5_Self_Learning_Address_Decoding_Techniques_and_8259_Cascading.md": """# Self-Learning: Address Decoding Techniques & 8259 Cascading — MPCA Module 4

> **Definition:** **Address Decoding Techniques** define how system address lines are mapped to peripheral chip selects (Absolute vs Partial), while **8259 Cascading** expands interrupt handling capacity from 8 to 64 priority channels.

---

## 1. Absolute vs Partial Address Decoding

```
ABSOLUTE ADDRESS DECODING:
- ALL address lines (A0 - A19) are fully connected to decoders and chip logic.
- Each memory/IO location has exactly ONE unique physical address.
- Eliminates "Shadow Addresses" (ghost aliases).

PARTIAL ADDRESS DECODING:
- Only some upper address lines are decoded; unused "don't care" lines (X) are left unconnected.
- Simpler and cheaper hardware (fewer logic gates).
- Causes "Shadow Addresses" (same physical hardware responds to multiple address ranges).
```

### Comparison Table:
| Feature | Absolute Decoding | Partial Decoding |
| :--- | :--- | :--- |
| **Address Line Usage** | All address lines ($A_0 - A_{19}$) fully decoded. | Only subset of lines decoded ($A_{15}-A_{19}$). |
| **Shadow Addresses** | **Zero Shadow Addresses** (Strict 1-to-1 mapping). | Multiple shadow aliases exist. |
| **Hardware Complexity**| High (requires multi-input logic gates/decoders). | **Low** (simple 74LS138 decoder). |
| **Best Suited For** | Large systems, 1 MB full memory maps. | Small microcontroller/embedded systems. |

---

## 2. 8259 Cascaded Mode (Master-Slave Configuration)

To handle more than 8 interrupts, one **Master 8259** is connected to up to **8 Slave 8259s** via the 3-bit Cascade Bus ($CAS_0, CAS_1, CAS_2$).

```
                  MASTER 8259 (INT to 8086 CPU)
                       |
        +--------------+--------------+
        | (CAS0, CAS1, CAS2 Bus)     |
        v                             v
  [ SLAVE 8259 #1 ]             [ SLAVE 8259 #2 ]
   IR0 to IR7 (8 Levels)         IR0 to IR7 (8 Levels)
```

### Cascading Operation Flow:
1. Slave 8259 receives interrupt on its IR line and signals Master 8259 via Master's IR pin.
2. Master sends `INT` to 8086 CPU.
3. 8086 issues 1st $\\overline{INTA}$. Master broadcasts the 3-bit Slave ID on $CAS_0 - CAS_2$.
4. The matching Slave recognizes its ID, and on the 2nd $\\overline{INTA}$, the **Slave 8259 puts the interrupt vector byte** onto the Data Bus.
5. Max Capacity = 1 Master $\\times$ 8 Slaves = **64 Interrupt Inputs**.

---

## 3. Quick Recall Flow
```
Absolute (All Lines, No Shadows) vs Partial (Don't Cares, Shadow Addresses) | 8259 Cascading: Master-Slave via CAS0-2 -> Up to 64 Interrupts
```
"""
}

# Write Module 4 files
for fname, content in m4_files.items():
    with open(os.path.join(m4_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created MPCA Module 4 Files!")
