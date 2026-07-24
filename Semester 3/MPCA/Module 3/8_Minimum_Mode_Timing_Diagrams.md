# Topic: Minimum Mode Timing Diagrams

**Q. Draw and explain the timing diagram for a Memory Read and Memory Write operation of the 8086 microprocessor in Minimum Mode. Detail the events occurring in each T-State.**

---

> 📌 **Definition to Remember**
> A **Timing Diagram** graphically represents the signals the CPU generates over time. In 8086, a basic bus cycle consists of 4 clock periods called **T-States (T1, T2, T3, T4)**. T1 is for addressing, T2 for bus turnaround, T3 for data transfer, and T4 for cycle completion.

---

### 1. General T-State Roles
* **T1:** Address is generated and latched.
* **T2:** Multiplexed bus switches from Address to Data mode. Control signals asserted.
* **T3:** Actual data transfer occurs. (Wait states $T_W$ inserted here if memory is slow).
* **T4:** Control signals deactivated; cycle ends.

### 2. Memory Read Timing (Minimum Mode)
CPU fetches data from memory.
* **T1:** 
  * 20-bit address placed on AD and A bus.
  * `M/IO'` is **HIGH** (Memory op).
  * `ALE` (Address Latch Enable) pulses **HIGH** to latch the address.
  * `DT/R'` goes **LOW** (Configure transceivers to Receive).
* **T2:** 
  * Address is removed from AD bus (goes to high impedance).
  * `RD'` (Read) is pulled **LOW**.
  * `DEN'` (Data Enable) goes **LOW** to enable transceivers.
* **T3:** 
  * Memory places data onto the AD bus. CPU reads it.
  * *(CPU checks READY pin. If low, inserts $T_W$)*.
* **T4:** 
  * `RD'` and `DEN'` go **HIGH**. Data is locked into the CPU. Cycle ends.

### 3. Memory Write Timing (Minimum Mode)
CPU sends data to memory.
* **T1:** 
  * 20-bit address placed on AD and A bus.
  * `M/IO'` is **HIGH**. `ALE` pulses **HIGH**.
  * `DT/R'` goes **HIGH** (Configure transceivers to Transmit).
* **T2:** 
  * CPU places data to be written onto the AD bus.
  * `WR'` (Write) is pulled **LOW**.
  * `DEN'` is pulled **LOW**.
* **T3:** 
  * Data remains stable on the AD bus so memory has time to write it.
* **T4:** 
  * `WR'` and `DEN'` go **HIGH**. AD bus goes to high impedance. Cycle ends.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A basic bus cycle consists of 4 clock periods: **T1, T2, T3, T4**.
> 2. **T1**: CPU outputs address on AD bus; pulses **ALE** high to latch the address.
> 3. **T2**: AD bus switches to data. Control signals (**RD'** or **WR'**, and **DEN'**) are asserted (pulled Low).
> 4. **T3**: Data is transferred (Read from or written to memory).
> 5. **Wait States ($T_W$)**: Inserted between T3 and T4 if the **READY** pin is low (used for slow memory).
> 6. **T4**: Control signals are deactivated (pulled High) and the cycle concludes.
> 7. **DT/R'** indicates direction (Low for Read, High for Write). `M/IO'` is High for Memory.

---

> ⚡ **Quick Recall**
> `Timing Diagram → 4 T-States → T1 (Address out, ALE pulse) → T2 (RD/WR asserted, DEN asserted, Bus turnaround) → T3 (Data Transfer, Wait States if slow) → T4 (Signals deactivated)`
