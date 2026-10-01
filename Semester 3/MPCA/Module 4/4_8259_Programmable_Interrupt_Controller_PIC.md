# 8259 Programmable Interrupt Controller (PIC)

**Q. Draw and explain the internal architecture of the 8259 Programmable Interrupt Controller (PIC). Explain the complete interrupt response sequence between 8086 and 8259 with the two INTA pulses, and describe its priority modes.**

---

> 📌 **Definition to Remember**
> The **Intel 8259A (PIC)** is an 8-channel programmable interrupt controller designed to manage, prioritize, resolve, and vector up to 8 hardware interrupt requests ($IR_0 - IR_7$) to the microprocessor CPU, expandable up to **64 vectored priority interrupts** using master-slave cascading.

---

### 1. Internal Architecture & Block Diagram of 8259

The 8259 internal architecture consists of eight primary functional blocks:

```
                           8259 INTERNAL ARCHITECTURE
 +-------------------------------------------------------------------------+
 |                                                                         |
 |  [ Interrupt Request Register (IRR) ]:                                  |
 |    Latches asynchronous interrupt request lines IR0 to IR7.             |
 |                                                                         |
 |  [ Interrupt Mask Register (IMR) ]:                                     |
 |    Stores 8 mask bits to selectively enable/disable individual IR lines.|
 |                                                                         |
 |  [ Priority Resolver (PR) ]:                                            |
 |    Determines highest priority pending unmasked interrupt request.      |
 |                                                                         |
 |  [ In-Service Register (ISR) ]:                                         |
 |    Tracks which interrupt level is currently being serviced by the CPU. |
 |                                                                         |
 |  [ Cascade Buffer / Comparator ]:                                       |
 |    Drives/compares CAS0, CAS1, CAS2 lines in Master-Slave cascade modes.|
 |                                                                         |
 |  [ Control Logic ]:                                                     |
 |    Interfaces INT to CPU, receives /INTA, /RD, /WR, /CS, A0.            |
 |                                                                         |
 |  [ Data Bus Buffer ]:                                                   |
 |    8-bit bi-directional buffer (D0 - D7) to send vector byte to CPU.    |
 +-------------------------------------------------------------------------+
```

#### Core Register Functions:
* **IRR (Interrupt Request Register):** Stores all incoming interrupt signals awaiting service.
* **IMR (Interrupt Mask Register):** Programmed via OCW1 to block individual IR inputs without affecting others.
* **ISR (In-Service Register):** Holds the bit corresponding to the interrupt routine currently executing in the CPU.
* **Priority Resolver:** Evaluates IRR, IMR, and ISR to decide if a new interrupt has higher priority than the one currently executing.

---

### 2. Step-by-Step Interrupt Response Sequence (The Two INTA Pulses)

When a peripheral requests an interrupt, the 8259 and 8086 execute the following precise handshake:

```
Peripheral            8259 PIC                       8086 CPU
    |                     |                             |
    |---- 1. IR asserted->|                             |
    |                     | (Priority resolved)         |
    |                     |---- 2. INT ---------------->|
    |                     |                             | (Checks IF flag in EFLAGS)
    |                     |<--- 3. 1st /INTA -----------|
    |                     | (Sets ISR bit, clears IRR)  |
    |                     |<--- 4. 2nd /INTA -----------|
    |                     |==== 5. Vector on D0-D7 ====>|
    |                     |                             | (Reads Type N, jumps to
    |                     |                             |  ISR in IVT: Addr = N * 4)
    |                     |<--- 6. EOI Command ---------| (At end of ISR subroutine)
```

1. **Interrupt Request:** An I/O device asserts one of the interrupt request lines ($IR_0 - IR_7$).
2. **Latch & Resolve:** The 8259 sets the corresponding bit in **IRR**. If that bit is not masked in **IMR**, the Priority Resolver signals the Control Logic.
3. **CPU Alert:** 8259 asserts the **`INT`** pin connected to the 8086 CPU `INTR` input.
4. **First $\overline{\text{INTA}}$ Pulse:** 8086 CPU acknowledges by pulsing $\overline{\text{INTA}}$ LOW.
   * Upon the first pulse, the highest priority bit is set in **ISR** and cleared from **IRR**.
   * In cascade mode, the Master 8259 outputs the 3-bit Slave ID on $CAS_0 - CAS_2$.
5. **Second $\overline{\text{INTA}}$ Pulse:** 8086 CPU issues a second $\overline{\text{INTA}}$ LOW pulse.
   * The 8259 places the programmed **8-bit Interrupt Vector Type Number ($00\text{H} - \text{FFH}$)** onto data lines $D_0 - D_7$.
6. **Vector Execution:** 8086 reads the vector byte $N$, calculates the Interrupt Vector Table address ($N \times 4$), pushes FLAGS, CS, IP, and jumps to the Interrupt Service Routine (ISR).
7. **End of Interrupt (EOI):** At the end of the ISR routine, the CPU writes an **EOI command** (via OCW2) to 8259 to clear the active bit in the ISR register.

---

### 3. Priority Modes of 8259

| Priority Mode | Working Principle | Use Case |
| :--- | :--- | :--- |
| **Fully Nested Mode (Default)** | Fixed priority: $IR_0$ (highest) down to $IR_7$ (lowest). Interrupt of higher level can interrupt an ongoing lower level ISR. | Standard PC architecture |
| **Automatic Rotation Mode** | Equal priority round-robin. Once an IR channel is serviced, it is automatically assigned the **lowest priority**. | Devices with equal service urgency |
| **Specific Rotation Mode** | Programmer manually designates which IR channel has the lowest priority via software OCW2 command. | Dynamic prioritization |
| **Special Mask Mode** | Allows lower priority interrupts to be serviced even while a higher priority ISR is running by masking the active ISR bit. | Complex OS interrupt handling |
| **Polled Mode** | Disables CPU `INT` line. CPU periodically reads 8259 status register to find pending interrupts. | Systems without hardware interrupt pins |

---

### 4. Initialization vs. Operational Command Words

* **ICWs (Initialization Command Words - ICW1 to ICW4):** Programmed once upon system boot to define single/cascade mode, call address interval, vector offset, and 8086/8085 mode.
* **OCWs (Operational Command Words - OCW1 to OCW3):** Programmed dynamically during runtime:
  * **OCW1:** Sets/clears interrupt mask bits in IMR.
  * **OCW2:** Issues EOI commands and rotation modes.
  * **OCW3:** Reads IRR/ISR status registers and sets special mask mode.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8259 manages 8 priority interrupts ($IR_0 - IR_7$); cascadable up to 64 priority channels.
> 2. **IRR** latches incoming requests; **IMR** masks unwanted interrupts; **ISR** tracks the currently executing interrupt.
> 3. The 8086 CPU issues **two $\overline{\text{INTA}}$ pulses** during interrupt acknowledgement.
> 4. **1st $\overline{\text{INTA}}$:** Freezes priority, sets ISR bit, clears IRR bit, drives cascade lines.
> 5. **2nd $\overline{\text{INTA}}$:** 8259 places the 8-bit vector number ($N$) on the data bus ($D_0 - D_7$).
> 6. CPU calculates IVT base address as **$N \times 4$** to fetch the ISR pointer (CS:IP).
> 7. An **EOI (End of Interrupt)** command must be issued at the end of the service routine to reset the ISR bit.

---

> ⚡ **Quick Recall**
> `IRR (Pending) → Priority Resolver → INT to CPU → 1st /INTA (Set ISR) → 2nd /INTA (Vector Byte N) → Vector * 4 in IVT → EOI to Clear ISR`
