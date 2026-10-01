# 8255 Programmable Peripheral Interface (PPI)

**Q. Draw and explain the internal architecture and pin diagram of the 8255 Programmable Peripheral Interface (PPI). Explain its operating modes, Control Word formats for I/O mode and BSR mode with suitable examples.**

---

> 📌 **Definition to Remember**
> The **Intel 8255A (PPI)** is a general-purpose programmable parallel I/O interface IC containing **24 I/O pins** divided into three 8-bit ports (Port A, Port B, Port C) that can be configured via software control words for simple I/O, strobed handshake I/O, or bidirectional bus operations.

---

### 1. Internal Architecture & Block Diagram of 8255

The 8255 architecture consists of five core functional blocks:
1. **Data Bus Buffer:** Tri-state, bidirectional 8-bit buffer ($D_0 - D_7$) interfacing the 8255 to the system data bus.
2. **Read/Write Control Logic:** Manages internal transfers using control strobes $\overline{\text{RD}}, \overline{\text{WR}}, A_1, A_0, \overline{\text{CS}}, \text{RESET}$.
3. **Group A Control:** Controls Port A ($PA_0 - PA_7$) and Port C Upper ($PC_4 - PC_7$).
4. **Group B Control:** Controls Port B ($PB_0 - PB_7$) and Port C Lower ($PC_0 - PC_3$).
5. **Ports A, B, and C:**
   * **Port A:** 8-bit data output latch/buffer and data input latch.
   * **Port B:** 8-bit data input/output latch/buffer.
   * **Port C:** 8-bit port that can be split into two 4-bit ports or used for handshake control signals.

```
                          8255 INTERNAL ARCHITECTURE
 +-------------------------------------------------------------------------+
 |                                                                         |
 |  Data Bus Buffer (D0-D7) <=============> System Data Bus (D0-D7)       |
 |                                                                         |
 |  Read/Write & Control Logic:                                            |
 |    Inputs: /RD, /WR, A0, A1, /CS, RESET                                 |
 |                                                                         |
 |  [ GROUP A CONTROL ] -----------------> Port A (PA0 - PA7: 8 Pins)     |
 |                      -----------------> Port C Upper (PC4 - PC7: 4 Pins)|
 |                                                                         |
 |  [ GROUP B CONTROL ] -----------------> Port B (PB0 - PB7: 8 Pins)     |
 |                      -----------------> Port C Lower (PC0 - PC3: 4 Pins)|
 +-------------------------------------------------------------------------+
```

---

### 2. Port Selection Truth Table

The address lines $A_1$ and $A_0$ select the target port or the Control Word Register (CWR):

| $\overline{\text{CS}}$ | $A_1$ | $A_0$ | $\overline{\text{RD}}$ | $\overline{\text{WR}}$ | Selected Operation / Port |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | **0** | **0** | 0 | 1 | Read from **Port A** onto Data Bus |
| **0** | **0** | **0** | 1 | 0 | Write from Data Bus to **Port A** |
| **0** | **0** | **1** | 0 | 1 | Read from **Port B** onto Data Bus |
| **0** | **0** | **1** | 1 | 0 | Write from Data Bus to **Port B** |
| **0** | **1** | **0** | 0 | 1 | Read from **Port C** onto Data Bus |
| **0** | **1** | **0** | 1 | 0 | Write from Data Bus to **Port C** |
| **0** | **1** | **1** | 1 | 0 | Write to **Control Word Register (CWR)** |
| **1** | X | X | X | X | **8255 Deselected** (Data bus tri-stated) |

---

### 3. Control Word Register Formats

The 8255 contains a single 8-bit Control Register accessed when $A_1 A_0 = 11$. The MSB bit ($D_7$) determines the control word mode:
* If **$D_7 = 1$**: **I/O Mode Set Control Word**.
* If **$D_7 = 0$**: **Bit Set/Reset (BSR) Mode Control Word**.

#### 1. I/O Mode Control Word Format ($D_7 = 1$)

```
  D7    D6    D5    D4    D3    D2    D1    D0
+-----+-----+-----+-----+-----+-----+-----+-----+
|  1  |   Mode A  | PA  | PCU | MB  | PB  | PCL |
+-----+-----+-----+-----+-----+-----+-----+-----+
   |     \_____/     |     |     |     |     +---> Port C Lower: 1=Input, 0=Output
   |      Mode A     |     |     |     +---------> Port B:       1=Input, 0=Output
   |    00: Mode 0   |     |     +---------------> Mode B:       0=Mode 0, 1=Mode 1
   |    01: Mode 1   |     +---------------------> Port C Upper: 1=Input, 0=Output
   |    1X: Mode 2   +---------------------------> Port A:       1=Input, 0=Output
   +---------------------------------------------> Mode Set Flag: 1 = I/O Mode Active
```

#### 2. Bit Set/Reset (BSR) Mode Control Word Format ($D_7 = 0$)
The BSR mode is used exclusively to **set or clear individual bits of Port C** ($PC_0 - PC_7$) without altering the other bits.

```
  D7    D6    D5    D4    D3    D2    D1    D0
+-----+-----+-----+-----+-----+-----+-----+-----+
|  0  |  X  |  X  |  X  |    Bit Select   | S/R |
+-----+-----+-----+-----+-----+-----+-----+-----+
   |     \___________/     \____________/     |
   |      Don't Care        000 = PC0         +-> 1 = SET bit
   |      (Set to 0)        001 = PC1             0 = RESET bit
   |                        ...
   |                        111 = PC7
   +--------------------------------------------> BSR Mode Flag: 0 = BSR Mode
```

* **Example:** To set bit $PC_3$, Control Word = `0000 0111` ($07\text{H}$). To reset bit $PC_3$, Control Word = `0000 0110` ($06\text{H}$).

---

### 4. Operating Modes of 8255

#### Mode 0: Basic I/O (Simple I/O)
* Ports A, B, and both halves of Port C operate independently as simple input or output ports.
* Inputs are unlatched; outputs are latched.
* No handshaking signals required. Used for simple switches, LEDs, and 7-segment displays.

#### Mode 1: Strobed I/O (Handshake I/O)
* Handshake signals are exchanged between peripheral and CPU before transferring data.
* **Port A** and **Port B** act as 8-bit data ports; **Port C** pins provide handshake control signals:
  * **Input Handshake Signals:**
    * $\overline{\text{STB}}$ (Strobe Input): Peripheral asserts LOW to load data into 8255 port latch.
    * $\text{IBF}$ (Input Buffer Full): 8255 asserts HIGH to signal that data is latched.
    * $\text{INTR}$ (Interrupt Request): 8255 asserts HIGH to request CPU interrupt to read data.
  * **Output Handshake Signals:**
    * $\overline{\text{OBF}}$ (Output Buffer Full): 8255 asserts LOW indicating CPU wrote data.
    * $\overline{\text{ACK}}$ (Acknowledge Input): Peripheral pulses LOW when it accepts data.
    * $\text{INTR}$ (Interrupt Request): Signals CPU that output buffer is empty.

#### Mode 2: Strobed Bidirectional Bus I/O
* Only **Port A** can be configured in Mode 2 as an 8-bit bidirectional data bus.
* Uses **5 pins of Port C** ($PC_3 - PC_7$) for bidirectional handshake control: $\overline{\text{STBA}}, \text{IBFA}, \overline{\text{OBFA}}, \overline{\text{ACKA}}, \text{INTRA}$.
* Port B can independently operate in Mode 0 or Mode 1.

---

### 5. Mode Comparison Summary

| Parameter | Mode 0 (Basic I/O) | Mode 1 (Strobed Handshake) | Mode 2 (Bidirectional) |
| :--- | :--- | :--- | :--- |
| **Port A Capability** | Simple Input / Output | Handshake Input / Output | **Bidirectional 8-bit Bus** |
| **Port B Capability** | Simple Input / Output | Handshake Input / Output | Not applicable (Mode 0/1 only) |
| **Port C Role** | Data I/O (Two 4-bit ports) | Handshake control signals | Handshake signals ($PC_3-PC_7$) |
| **Latching** | Output latched, input unlatched | Both input & output latched | Both input & output latched |
| **Interrupts** | None | Hardware $\text{INTR}$ generated | Hardware $\text{INTR}$ generated |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8255 provides **24 programmable I/O pins** organized as Port A (8), Port B (8), and Port C (8).
> 2. Read/Write control uses $\overline{\text{RD}}, \overline{\text{WR}}, \overline{\text{CS}}$ and address pins **$A_1, A_0$** to select Port A, B, C, or CWR.
> 3. Control Word register distinguishes **I/O Mode ($D_7 = 1$)** from **BSR Mode ($D_7 = 0$)**.
> 4. **BSR mode modifies only individual bits of Port C** without disturbing other port bits.
> 5. **Mode 0** supports simple un-strobed I/O across all ports.
> 6. **Mode 1** implements strobed handshake data transfer using Port C signals ($\text{STB}, \text{IBF}, \text{OBF}, \text{ACK}, \text{INTR}$).
> 7. **Mode 2** enables Port A as a bidirectional bus using 5 handshake lines of Port C.

---

> ⚡ **Quick Recall**
> `24 I/O Pins → Ports A, B, C → A1/A0 Port Select → D7=1 (I/O Mode 0/1/2) → D7=0 (BSR Mode for Port C) → Mode 1 Handshake (STB, IBF, INTR) → Mode 2 Bidirectional Bus`
