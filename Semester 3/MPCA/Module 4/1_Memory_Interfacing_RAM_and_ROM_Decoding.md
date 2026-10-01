# Memory Interfacing: RAM & ROM Decoding

**Q. Explain memory interfacing with the 8086 microprocessor. Design an address decoding scheme using the 74LS138 decoder to interface 64 KB RAM (using two 32 KB chips) and 64 KB EPROM (using two 32 KB chips) to the 8086 CPU. Draw the complete memory map and interfacing diagram.**

---

> 📌 **Definition to Remember**
> **Memory Interfacing** is the electronic hardware design connecting semiconductor RAM and EPROM/ROM chips to the microprocessor's Address, Data, and Control buses using **Address Decoding Logic** so that each memory chip is mapped to a unique physical address range without bus contention.

---

### 1. 8086 Memory Organization & Banking Review

The 8086 CPU features a **20-bit Address Bus** ($A_0 - A_{19}$), enabling it to directly address **1 MB ($2^{20}$ bytes)** of physical memory spanning from `00000H` to `FFFFFH`.

To allow byte (8-bit) as well as word (16-bit) operations in a single bus cycle, physical memory is partitioned into **two 512 KB banks**:
1. **Even Bank (Lower Bank):** Connected to Data Bus lines **$D_0 - D_7$**. Activated when Address bit **$A_0 = 0$**.
2. **Odd Bank (Higher Bank):** Connected to Data Bus lines **$D_8 - D_{15}$**. Activated when Bus High Enable **$\overline{\text{BHE}} = 0$**.

```
       8086 Microprocessor                       Memory Subsystem (1 MB)
  +---------------------------+              +------------------------------+
  |                           |   A0 = 0     |  EVEN BANK (512 KB)          |
  |   Data Bus D0 - D7        |============> |  Data lines D0 - D7          |
  |                           |              +------------------------------+
  |                           |  /BHE = 0    |  ODD BANK (512 KB)           |
  |   Data Bus D8 - D15       |============> |  Data lines D8 - D15         |
  +---------------------------+              +------------------------------+
```

#### Memory Bank Selection Truth Table:
| $\overline{\text{BHE}}$ | $A_0$ | Type of Bus Cycle / Data Transfer | Data Bus Used |
| :---: | :---: | :--- | :---: |
| **0** | **0** | **16-bit Word transfer** at Even address | $D_0 - D_{15}$ (Both Banks) |
| **0** | **1** | **8-bit Byte transfer** from/to Odd Bank | $D_8 - D_{15}$ (Odd Bank only) |
| **1** | **0** | **8-bit Byte transfer** from/to Even Bank | $D_0 - D_7$ (Even Bank only) |
| **1** | **1** | **No Operation** (Bus Inactive / Idle) | None |

---

### 2. Address Decoding Logic (74LS138 3-to-8 Decoder)

The **74LS138 IC** is an active-low 3-to-8 line decoder commonly used to generate Chip Select ($\overline{\text{CS}}$) signals.

```
                     74LS138 3-to-8 DECODER
                   +------------------------+
      A19 -------->| G1   (Active-HIGH En)  |
      A18 -------->| /G2A (Active-LOW En)   |
    M//IO -------->| /G2B (Active-LOW En)   |
                   |                        |
      A17 -------->| C (Select Input 2)     |-----> /Y0 (CS for RAM Bank 0)
      A16 -------->| B (Select Input 1)     |-----> /Y1 (CS for RAM Bank 1)
      A15 -------->| A (Select Input 0)     |-----> /Y2
                   +------------------------+-----> ...
                                            +-----> /Y7 (CS for ROM Banks)
```

* **Enable Conditions:** Decoder is active only when $G_1 = 1$, $\overline{G_{2A}} = 0$, and $\overline{G_{2B}} = 0$.
* Connecting $M/\overline{IO}$ to an active-low enable input ensures the decoder asserts chip selects **only during memory cycles**, never during I/O cycles.

---

### 3. Absolute vs. Partial Address Decoding

| Parameter | Absolute Address Decoding | Partial Address Decoding |
| :--- | :--- | :--- |
| **Address Line Usage** | **All 20 address lines** ($A_0 - A_{19}$) are decoded | Only a subset of upper lines are decoded |
| **Shadow Addresses** | **Zero shadow addresses**; 1-to-1 memory mapping | **Shadow (alias) addresses exist** |
| **Hardware Complexity**| High (requires multiple decoders / gates) | Low (requires a single decoder) |
| **Cost & Board Space** | Higher | Minimal |
| **Application** | Large multi-chip systems, commercial PCs | Small embedded controllers, test circuits |

---

### 4. Memory Interfacing Design Problem (64 KB RAM & 64 KB ROM)

#### Step 1: Memory Allocation Requirements
* Total RAM required = **64 KB** $\rightarrow$ Two 32 KB SRAM chips (Even Bank & Odd Bank).
* Total EPROM required = **64 KB** $\rightarrow$ Two 32 KB EPROM chips (Even Bank & Odd Bank).
* For each 32 KB chip: $32\text{ KB} = 2^{15}\text{ bytes} \implies$ requires **15 address lines** ($A_1$ to $A_{15}$).
* $A_0$ is used with $\overline{\text{BHE}}$ to select the appropriate bank.
* Remaining upper lines for decoding = **$A_{16}, A_{17}, A_{18}, A_{19}$**.

#### Step 2: Location Rules in 8086 Physical Memory
1. **EPROM / ROM Location:** Must reside at the **top of physical memory** containing address `FFFF0H`, because upon hardware Reset, 8086 initializes `CS:IP = FFFF:0000H` (Physical Address `FFFF0H`).
   * 64 KB ROM range: **`F0000H` to `FFFFFH`**.
2. **RAM Location:** Placed at the **bottom of memory** starting at `00000H` to hold the **Interrupt Vector Table (IVT)** (`00000H - 003FFH`).
   * 64 KB RAM range: **`00000H` to `0FFFFH`**.

#### Step 3: Complete Memory Map Table
| Memory Block | Capacity | Address Range (Hex) | $A_{19}$ | $A_{18}$ | $A_{17}$ | $A_{16}$ | $A_{15}-A_1$ | $A_0$ | Decoder Output |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **RAM (Even & Odd)** | 64 KB | `00000H - 0FFFFH` | 0 | 0 | 0 | 0 | Internal to Chip | Bank Select | $\overline{Y_0}$ |
| **Unmapped** | 64 KB | `10000H - 1FFFFH` | 0 | 0 | 0 | 1 | - | - | $\overline{Y_1}$ |
| ... | ... | ... | ... | ... | ... | ... | - | - | ... |
| **ROM (Even & Odd)** | 64 KB | `F0000H - FFFFFH` | 1 | 1 | 1 | 1 | Internal to Chip | Bank Select | $\overline{Y_7}$ |

#### Step 4: Control Bus Signal Generation
* **Memory Read ($\overline{\text{MEMR}}$):** Connected to $\overline{\text{OE}}$ (Output Enable) of RAM and EPROM.
* **Memory Write ($\overline{\text{MEMW}}$):** Connected to $\overline{\text{WE}}$ (Write Enable) of RAM only (ROM has no write line).

---

### 5. Hardware Interfacing Diagram

```
         +-------------------------------------------------------------+
         |                       8086 MICROPROCESSOR                   |
         +-------------------------------------------------------------+
               | A1-A15       | A16-A19        | M//IO     | D0-D7 | D8-D15
               |              |                |           |       |
               |              v                v           |       |
               |       +--------------+     +----+         |       |
               |       | 74LS138      |     |INV |         |       |
               |       | Decoder      |     +----+         |       |
               |       |              |        |           |       |
               |       | G1 <- A19    |        |           |       |
               |       | /G2A <- /A18 |        |           |       |
               |       | /G2B <-------+--------+           |       |
               |       | C,B,A <- A17,A16,A15              |       |
               |       +--------------+                    |       |
               |         |          |                      |       |
               |      /Y0|          |/Y7                   |       |
               |         v          v                      |       |
               |      +------+   +------+                  |       |
               +=====>|32KB  |   |32KB  |                  |       |
               |      |RAM-L |   |ROM-L |==================+       |
               |      |(Even)|   |(Even)|  Data D0 - D7            |
               |      +------+   +------+                          |
               |         |          |                              |
               |      +------+   +------+                          |
               +=====>|32KB  |   |32KB  |                          |
                      |RAM-H |   |ROM-H |==========================+
                      |(Odd) |   |(Odd) |  Data D8 - D15
                      +------+   +------+
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8086 has a **20-bit address bus** (1 MB memory) split into **Even Bank ($A_0=0$, $D_0-D_7$)** and **Odd Bank ($\overline{\text{BHE}}=0$, $D_8-D_{15}$)**.
> 2. Both banks are accessed simultaneously during 16-bit aligned word access.
> 3. Address lines **$A_1 - A_{15}$** connect directly to the memory chips for intra-chip word addressing.
> 4. Upper address lines **$A_{16} - A_{19}$** and control line **$M/\overline{\text{IO}}$** connect to the 74LS138 decoder to generate $\overline{\text{CS}}$ signals.
> 5. **EPROM must be located at `F0000H - FFFFFH`** to cover the processor reset address `FFFF0H`.
> 6. **RAM is mapped to `00000H - 0FFFFH`** to accommodate the 1 KB Interrupt Vector Table (IVT).
> 7. Absolute decoding prevents ghost/shadow addresses; partial decoding saves decoder hardware at the cost of duplicate address aliasing.

---

> ⚡ **Quick Recall**
> `20-bit Address (1 MB) → Even/Odd Banks (A0 & /BHE) → Upper Bits to 74LS138 Decoder → ROM at F0000H (Reset) → RAM at 00000H (IVT) → /MEMR & /MEMW Strobes`
