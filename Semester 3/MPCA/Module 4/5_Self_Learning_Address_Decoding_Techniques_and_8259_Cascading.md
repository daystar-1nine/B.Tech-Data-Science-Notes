# Address Decoding Techniques & 8259 Cascading

**Q. Differentiate between Absolute and Partial Address Decoding with neat circuit diagrams. Explain the master-slave cascading configuration of the 8259 PIC to support up to 64 interrupt inputs.**

---

> 📌 **Definition to Remember**
> **Address Decoding Techniques** map processor address bus lines to memory/IO chip selects using either all lines (Absolute) or a subset (Partial), while **8259 Cascading** uses a dedicated 3-bit cascade bus ($CAS_0 - CAS_2$) in a master-slave topology to expand interrupt capability from 8 to 64 channels.

---

### 1. Absolute vs. Partial Address Decoding

When interfacing memory or peripherals to a microprocessor, the high-order address lines determine which device is selected.

```
ABSOLUTE ADDRESS DECODING:
  Address Lines A0 - A19 (ALL 20 lines connected)
        +----------------------------------------+
        | Decoders, NAND/NOR Gates, Comparators  |
        +----------------------------------------+
                           |
                           v
              Chip Select /CS (Exact 1-to-1 Mapping)

PARTIAL ADDRESS DECODING:
  Address Lines A15 - A19 (Only upper lines connected)
        +----------------------+
        | Simple 74LS138       |     (A0 - A14 "Don't Cares" X)
        +----------------------+
                   |
                   v
      Chip Select /CS (Creates Multiple Ghost/Shadow Addresses)
```

#### Detailed Comparison:
| Parameter | Absolute Address Decoding | Partial Address Decoding |
| :--- | :--- | :--- |
| **Address Lines Used** | **All address lines** ($A_0 - A_{19}$) are decoded | Only a subset of upper lines are connected |
| **Shadow / Ghost Addresses** | **None** — Every byte has exactly one unique address | **Multiple shadow addresses** point to the same physical byte |
| **Hardware Complexity** | High — requires multi-gate logic or PAL/GALs | Low — simple 3-to-8 decoder (74LS138) |
| **Memory Map Utilization** | Full 100% efficient utilization | Inefficient; fragments address space |
| **Risk of Bus Conflict** | Low | High if future expansions overlap shadow ranges |
| **Typical Use** | Personal computers, servers, large systems | Small microcontrollers, single-board prototypes |

---

### 2. Linear Address Decoding (Direct Select)

In ultra-simple systems with only 2 or 3 peripheral chips:
* Individual upper address lines (e.g., $A_{16}, A_{17}, A_{18}$) are connected **directly** to active-low chip select pins ($\overline{\text{CS}}$) without any decoder ICs.
* **Advantage:** Eliminates decoder ICs entirely, minimizing component cost.
* **Disadvantage:** Wastes huge chunks of address space and creates severe aliasing.

---

### 3. 8259 Master-Slave Cascading Architecture

To handle more than 8 vectored interrupts, the 8259 supports cascading:
* **One Master 8259** connects directly to the 8086 CPU via `INT` and $\overline{\text{INTA}}$.
* **Up to 8 Slave 8259s** connect their `INT` outputs to the Master's $IR_0 - IR_7$ inputs.
* Total interrupt capacity = $1 \text{ Master} \times 8 \text{ Slaves} = \mathbf{64 \text{ Interrupt Channels}}$.

```
                            8086 MICROPROCESSOR
                            +-----------------+
                            |  INTR     /INTA |
                            +-----------------+
                               ^          |
                               | INT      | /INTA (Broadcast to all)
                               |          v
                 +---------------------------------+
                 |          MASTER 8259            |
                 |  SP/EN = 1 (Tied to VCC)        |
                 |  CAS0, CAS1, CAS2 Outputs       |
                 +---------------------------------+
                    |       |              |
                    |       |              | (CAS0 - CAS2 Bus)
            +-------+       +------+       +-------+
            | IR0                  | IR1           | IR7
            v                      v               v
  +--------------------+ +--------------------+ +--------------------+
  |    SLAVE 8259 #0   | |    SLAVE 8259 #1   | |    SLAVE 8259 #7   |
  | SP/EN = 0 (GND)    | | SP/EN = 0 (GND)    | | SP/EN = 0 (GND)    |
  | CAS0-2 Inputs      | | CAS0-2 Inputs      | | CAS0-2 Inputs      |
  +--------------------+ +--------------------+ +--------------------+
     | | | | | | | |        | | | | | | | |        | | | | | | | |
     IR0 to IR7 Pins        IR0 to IR7 Pins        IR0 to IR7 Pins
     (8 Devices)            (8 Devices)            (8 Devices)
```

---

### 4. Cascaded Interrupt Operation & Timing

1. **Slave Interrupted:** A device connected to Slave #1 asserts an $IR$ pin.
2. **Master Alerted:** Slave #1 asserts its `INT` output, which drives $IR_1$ of Master 8259.
3. **CPU Alerted:** Master 8259 resolves priority and sends `INT` to 8086 CPU `INTR`.
4. **1st $\overline{\text{INTA}}$ Pulse:**
   * 8086 pulses $\overline{\text{INTA}}$ LOW (received by Master and all Slaves).
   * Master sets bit 1 in its ISR, determines $IR_1$ is a cascaded slave, and **broadcasts Slave ID `001` on $CAS_0 - CAS_2$**.
5. **2nd $\overline{\text{INTA}}$ Pulse:**
   * 8086 pulses second $\overline{\text{INTA}}$ LOW.
   * Slave #1 sees its matching ID (`001`) on $CAS_0 - CAS_2$ and **places its programmed 8-bit Interrupt Vector Byte on the Data Bus**.
   * Master keeps its data bus buffer in high-impedance mode during the 2nd pulse.
6. **EOI Sequencing:** An EOI command must be sent to **both the Slave and the Master** to clear both ISR registers.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Absolute Decoding:** Uses all 20 address lines; generates unique 1-to-1 mapping with zero shadow addresses.
> 2. **Partial Decoding:** Omits some address lines, saving decoder hardware but creating **shadow addresses**.
> 3. Linear decoding connects address lines directly to $\overline{\text{CS}}$, viable only in minimal systems.
> 4. 8259 cascading enables **up to 64 vectored interrupts** using 1 Master and up to 8 Slaves.
> 5. **$\overline{\text{SP}}/\overline{\text{EN}}$ Pin:** Tied to $V_{CC}$ (1) for Master; tied to $GND$ (0) for Slaves.
> 6. Cascade lines **$CAS_0, CAS_1, CAS_2$** broadcast the 3-bit active Slave ID during the 1st $\overline{\text{INTA}}$ pulse.
> 7. The addressed Slave places its vector byte onto $D_0 - D_7$ during the 2nd $\overline{\text{INTA}}$ pulse.

---

> ⚡ **Quick Recall**
> `Absolute (All lines, No shadows) vs Partial (Subset, Shadow aliases) | 8259 Cascade: 1 Master + 8 Slaves = 64 Channels → CAS0-2 Bus → Dual EOI Required`
