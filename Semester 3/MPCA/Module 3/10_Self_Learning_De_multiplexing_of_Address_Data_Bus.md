# Topic: De-multiplexing of Address/Data Bus — Self-Learning

**Q. Why does the 8086 use a multiplexed Address/Data bus? Explain the process of de-multiplexing this bus using Address Latch Enable (ALE) and Latches.**

---

> 📌 **Definition to Remember**
> To save physical pins on the 40-pin 8086 IC, Intel used a **Multiplexed Bus** (AD0-AD15), where the same pins carry the Address during clock cycle T1, and Data during T2-T4. **De-multiplexing** is the hardware process of using external **Latches** and the **ALE** signal to extract and hold the address before the pins switch to data mode.

---

### 1. Need for Multiplexing and De-multiplexing
* **Multiplexing:** The 8086 needs 20 pins for the address and 16 pins for data. Having 36 separate pins on a 40-pin chip leaves no room for power, clock, and control signals. Hence, they are multiplexed.
* **De-multiplexing:** Memory chips require a stable, constant address for the entire read/write cycle. If the 8086 removes the address after T1 to send data, memory loses track of the location. The address must be externally locked in place (latched).

### 2. The Role of ALE (Address Latch Enable)
* The 8086 generates a positive pulse on the **ALE** pin strictly during the **T1 state** of every machine cycle.
* This pulse guarantees that the signals currently on the AD pins represent a valid memory address.

### 3. Using Latches (74LS373) for De-multiplexing
To de-multiplex, external **D-type transparent latches** (e.g., 74LS373) are used.
* **Hardware Connection:** 
  * The AD bus (from CPU) connects to the Latch Inputs.
  * The ALE pin (from CPU) connects to the **Latch Enable (LE)** pin.
* **Working Mechanism:**
  1. **During T1:** 8086 puts the Address on the bus and pulses ALE High.
  2. Because ALE is High, the latches become "transparent," passing the address through to their outputs.
  3. **End of T1:** ALE goes Low. The latches "lock" (latch) the address present at their inputs.
  4. **During T2, T3, T4:** The 8086 removes the address and uses the AD lines for Data. However, the memory safely receives a constant address from the outputs of the latches.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Multiplexing** saves pins (AD0-AD15 act as Address in T1, Data in T2-T4).
> 2. Memory requires a stable address for the entire cycle, creating the need for **De-multiplexing**.
> 3. De-multiplexing separates the Address and Data using external **Latches** (e.g., 74LS373).
> 4. The **ALE (Address Latch Enable)** signal is pulsed High by the CPU only during **T1**.
> 5. ALE connects to the Enable pin of the external latches.
> 6. When ALE is High (T1), the latches grab the address from the AD bus.
> 7. When ALE goes Low, the latches lock the address and hold it steady for the memory, while the CPU uses the AD bus for data in T2-T4.

---

> ⚡ **Quick Recall**
> `Multiplexing saves pins → Memory needs stable address → Use Latches (74LS373) + ALE signal → T1: ALE is High, Latches grab Address → T2-T4: ALE Low, Latches hold Address, Bus used for Data`
