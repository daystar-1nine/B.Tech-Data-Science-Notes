# 8086 Microprocessor in Maximum Mode

**Q. Explain the operation of the 8086 microprocessor in Maximum Mode. Discuss the role of the Bus Controller (8288) and how a multiprocessor environment is managed.**

---

> 📌 **Definition to Remember**
> The 8086 operates in **Maximum Mode** when the **MN/MX'** pin is tied to Ground (Logic Low). Designed for **multi-processor systems** (e.g., using an 8087 coprocessor), the 8086 stops generating control signals and instead sends status codes to an external **8288 Bus Controller**.

---

### 1. Maximum Mode Configuration
In this mode, pins that previously generated control signals (like `ALE`, `WR'`) take on new functions related to bus arbitration and multiprocessor coordination. 
* The 8086 relies on the **Intel 8288 Bus Controller** to generate actual memory and I/O signals, freeing the CPU to manage shared resources.

### 2. Reassigned Maximum Mode Signals
* **S2', S1', S0' (Status Lines):** The 8086 outputs its current cycle status on these 3 pins. The 8288 reads them to generate command signals.
* **RQ'/GT0' & RQ'/GT1' (Request/Grant):** Replaces HOLD/HLDA. Used by coprocessors to request control of the local bus from the 8086, and for the 8086 to grant it.
* **LOCK':** When the 8086 executes an instruction with a `LOCK` prefix, it asserts this pin. It prevents other processors from taking the bus, ensuring safe updates to shared memory.
* **QS1, QS0 (Queue Status):** Broadcasts the status of the 8086's internal instruction queue to coprocessors.

### 3. Role of the 8288 Bus Controller
The 8288 decodes the `S2'-S0'` signals to generate system controls:
* **000:** Interrupt Acknowledge (INTA')
* **001:** Read I/O Port (IORC')
* **010:** Write I/O Port (IOWC')
* **101:** Read Memory (MRDC')
* **110:** Write Memory (MWTC')
*(The 8288 also generates ALE, DEN, and DT/R' for the system).*

### 4. Managing the Multiprocessor Environment
* **Bus Arbitration:** To prevent data corruption, only one processor can use the bus at a time. A coprocessor asserts **RQ'**. The 8086 finishes its cycle, floats its buses (High-Z), and asserts **GT'** to hand over control.
* **Shared Memory:** The **LOCK'** signal is crucial. It creates an "atomic" operation, preventing other CPUs from reading a memory location while the 8086 is in the middle of updating it.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Maximum Mode** is activated by tying the **MN/MX' pin to Ground (Low)**.
> 2. Designed for **multi-processor** environments (e.g., CPU + 8087 Math Coprocessor).
> 3. The 8086 stops generating control signals; relies on the **8288 Bus Controller**.
> 4. 8086 outputs status on **S2, S1, S0**, which the 8288 decodes to generate Memory/IO Read/Write signals.
> 5. HOLD/HLDA are replaced by bidirectional **RQ'/GT' (Request/Grant)** for bus arbitration.
> 6. **LOCK' pin**: Asserts exclusive control over the bus to protect shared memory.
> 7. **QS0/QS1**: Broadcast instruction queue status to coprocessors.

---

> ⚡ **Quick Recall**
> `Maximum Mode → MN/MX' = GND → Multi-processor → 8288 Bus Controller does the work → CPU sends S0, S1, S2 → Uses RQ/GT for bus request → LOCK to protect shared memory`
