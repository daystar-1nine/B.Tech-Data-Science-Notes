# 8259 Programmable Interrupt Controller (PIC) — MPCA Module 4

> **Definition:** The **Intel 8259A (PIC)** is an 8-channel programmable interrupt controller designed to manage, prioritize, and translate multiple hardware interrupt requests (**IR_0 - IR_7**) into 8086 vector interrupt instructions.

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
1. Peripheral asserts an interrupt line (**IR_0 - IR_7**).
2. **IRR** stores the request; **Priority Resolver** checks IRR against **IMR** mask and current **ISR** level.
3. 8259 sends an **`INT`** signal to 8086 CPU's `INTR` pin.
4. 8086 CPU responds with the **First **\overlineINTA** Pulse** (Interrupt Acknowledge).
5. Upon 1st **\overlineINTA**, the highest priority bit is set in **ISR** and cleared from **IRR**.
6. 8086 issues the **Second **\overlineINTA** Pulse**. 8259 places the **8-bit Interrupt Vector Type Number (00H - FFH)** on the Data Bus (**D_0 - D_7**).
7. 8086 reads the vector number, multiplies by 4, and jumps to the corresponding **Interrupt Service Routine (ISR)** in the IVT table.
8. At the end of the ISR subroutine, an **End of Interrupt (EOI)** command is sent to 8259 to clear the active bit in the ISR register.

---

## 3. Priority Modes in 8259
1. **Fully Nested Mode (Default): IR_0** has the highest priority and **IR_7** has the lowest priority. Lower priority interrupts are inhibited while a higher priority ISR is running.
2. **Automatic Rotation Mode:** Equal priority round-robin; after a channel is serviced, it is assigned the lowest priority.
3. **Specific Rotation Mode:** Programmer manually sets which IR channel has the lowest priority.

---

## 4. Must-Write Points for Exams
- **IRR** stores requested interrupts, **ISR** stores currently executing interrupt, **IMR** masks unwanted interrupts.
- Two **\overlineINTA** pulses are required from 8086 to fetch the interrupt vector from 8259.
- A single 8259 supports 8 interrupt levels (**IR_0 - IR_7**); cascading in Master-Slave supports up to **64 interrupt levels**.

---

## 5. Quick Recall Flow
```
IR0-IR7 -> IRR -> Priority Resolver -> INT to 8086 -> 1st /INTA (Set ISR) -> 2nd /INTA (Send Vector Byte) -> Execute ISR -> EOI Command
```
