# 8255 Programmable Peripheral Interface (PPI) — MPCA Module 4

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

| **\overlineCS** | **A_1** | **A_0** | Selected Register / Port |
| :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | **Port A** |
| 0 | 0 | 1 | **Port B** |
| 0 | 1 | 0 | **Port C** |
| 0 | 1 | 1 | **Control Word Register (CWR)** |
| 1 | X | X | 8255 Deselected (High Impedance) |

---

## 3. Control Word Register (CWR) Formats

### 1. I/O Mode Set Control Word (**D_7 = 1**)
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
4. **BSR Mode (Bit Set/Reset Mode, **D_7 = 0**):** Used to set or reset individual bits of **Port C only** without affecting other bits.

---

## 4. Must-Write Points for Exams
- 8255 has 24 I/O pins configured into Port A, Port B, and Port C (Upper & Lower).
- **D_7 = 1** in Control Word indicates **I/O Mode**; **D_7 = 0** indicates **BSR Mode**.
- Port C provides handshake status lines for Mode 1 and Mode 2 transfers.

---

## 5. Quick Recall Flow
```
8255 PPI -> 24 Pins (Ports A, B, C) -> Port Selection (A1, A0) -> Modes: Mode 0 (Basic), Mode 1 (Strobe), Mode 2 (Bi-dir), BSR Mode
```
