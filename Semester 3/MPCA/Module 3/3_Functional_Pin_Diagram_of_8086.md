# Topic: Functional Pin Diagram of 8086

**Q. Discuss the functional pin diagram of the 8086 microprocessor. Explain the significance of the multiplexed Address/Data bus and the pins specific to Minimum and Maximum modes.**

---

> 📌 **Definition to Remember**
> The **Intel 8086** is a 40-pin IC. To save pin count, it uses **multiplexed buses** (pins share dual roles based on the clock cycle). A unique feature is the `MN/MX'` pin, which toggles the processor between **Minimum Mode** (single-processor) and **Maximum Mode** (multi-processor).

---

### 1. Multiplexed Address/Data and Status Buses
* **AD0 - AD15 (Pins 16-2, 39):** Multiplexed Address/Data. During clock cycle T1, they carry the lower 16 bits of the memory address. During T2-T4, they carry 16-bit data.
* **A16/S3 - A19/S6 (Pins 38-35):** Multiplexed Address/Status. During T1, they carry the upper 4 bits of the 20-bit address. During T2-T4, they carry status signals.

### 2. Common Control & Interrupt Pins
* **ALE (Address Latch Enable):** Signals external latches to capture the address from the AD bus during T1.
* **BHE'/S7 (Bus High Enable):** Enables data transfer over the upper half of the data bus (D8-D15).
* **RD':** Read signal (Active Low).
* **READY:** Used by slow memory/peripherals to insert Wait states.
* **INTR & NMI:** Hardware interrupt requests (Maskable and Non-Maskable).
* **RESET:** Clears CPU, sets CS to `FFFFH` and IP to `0000H`.

### 3. Minimum Mode Pins (MN/MX' tied to +5V)
Operates as a standalone processor generating its own control signals.
* **M/IO':** Memory (High) or I/O (Low) access.
* **WR':** Write signal.
* **INTA':** Interrupt Acknowledge.
* **DT/R' & DEN':** Controls data flow direction and enables external transceivers.
* **HOLD & HLDA:** Used for DMA requests/acknowledgments.

### 4. Maximum Mode Pins (MN/MX' tied to GND)
Used in multi-processor systems (e.g., with 8087 Math Coprocessor). Control signal generation is handed to an external 8288 Bus Controller.
* **S0', S1', S2':** Status signals sent to the 8288 to generate memory/IO read and write signals.
* **RQ'/GT0' & RQ'/GT1':** Request/Grant pins for coprocessors to request bus control (replaces HOLD/HLDA).
* **LOCK':** Prevents other processors from taking the bus during critical instructions.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. The 8086 is a 40-pin IC utilizing **multiplexed buses** to save pins.
> 2. **AD0-AD15**: Act as Address during T1, and Data during T2-T4.
> 3. **ALE (Address Latch Enable)**: Tells external latches to grab the address during T1.
> 4. Can operate in **Minimum Mode** (standalone) or **Maximum Mode** (multi-processor) using the `MN/MX'` pin.
> 5. **Minimum Mode**: CPU generates its own signals (`M/IO'`, `WR'`, `HOLD`/`HLDA`).
> 6. **Maximum Mode**: Control is handed to an 8288 Bus Controller. Uses `S0, S1, S2` to tell 8288 what to do.
> 7. Coprocessors use `RQ'/GT'` (Request/Grant) to take the bus in Maximum mode.

---

> ⚡ **Quick Recall**
> `40-Pin IC → Multiplexed (AD0-AD15: Addr T1, Data T2-T4) → ALE (Latches Addr) → Min Mode (Standalone, Generates WR, M/IO, HOLD) → Max Mode (Multi-processor, Uses 8288 Controller, S0-S2, RQ/GT)`
