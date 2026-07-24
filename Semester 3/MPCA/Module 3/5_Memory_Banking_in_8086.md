# Topic: Memory Banking in 8086

**Q. What is Memory Banking in the 8086 microprocessor? Explain the roles of the A0 and BHE' signals in accessing Even and Odd memory banks for byte and word transfers.**

---

> 📌 **Definition to Remember**
> **Memory Banking** is the hardware organization of the 8086's 1 MB physical memory into two parallel 512 KB halves: the **Even Bank** (connected to D0-D7) and the **Odd Bank** (connected to D8-D15). This allows the CPU to efficiently read/write either 8-bit bytes or 16-bit words.

---

### 1. Concept of Memory Banking
To support a 16-bit data bus while maintaining byte-level addressing, memory is split:
* **Even Bank (Lower Bank):** Contains even addresses (`00000H`, `00002H`). Connected to the lower half of the data bus (**D0 - D7**).
* **Odd Bank (Upper Bank):** Contains odd addresses (`00001H`, `00003H`). Connected to the upper half of the data bus (**D8 - D15**).

### 2. Role of A0 and BHE' Signals
The CPU uses two specific signals to select which bank to activate during a memory cycle:
* **A0 (Address Line 0):** Selects the **Even Bank** (active when A0 = 0).
* **BHE' (Bus High Enable):** Selects the **Odd Bank** (active low, BHE' = 0).

### 3. Byte and Word Access Scenarios

| BHE' | A0 | Selection | Transfer Type |
| :---: | :---: | :--- | :--- |
| **0** | **0** | Both Banks | **Read/Write 16-bit Word from an Even Address.** Uses D0-D15. Completes in **1 Clock Cycle**. |
| **0** | **1** | Odd Bank | **Read/Write 8-bit Byte from an Odd Address.** Uses D8-D15. |
| **1** | **0** | Even Bank | **Read/Write 8-bit Byte from an Even Address.** Uses D0-D7. |
| **1** | **1** | None | No memory access. |

### 4. Accessing a Word from an Odd Address (Unaligned Access)
If the CPU tries to read a 16-bit word starting at an **odd address** (e.g., `00001H`), it cannot do it in one cycle. It requires **two clock cycles**:
* **Cycle 1 (BHE'=0, A0=1):** Reads the lower byte from the odd address (`00001H`) via D8-D15.
* **Cycle 2 (BHE'=1, A0=0):** Increments address to the next even boundary (`00002H`) and reads the upper byte via D0-D7.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Memory Banking** splits 1 MB memory into two 512 KB banks: **Even** and **Odd**.
> 2. **Even Bank**: Even addresses, connected to lower data bus (**D0-D7**).
> 3. **Odd Bank**: Odd addresses, connected to upper data bus (**D8-D15**).
> 4. **A0=0** enables the Even Bank; **BHE'=0** enables the Odd Bank.
> 5. **BHE'=0, A0=0**: Reads a 16-bit word from an Even address in **1 clock cycle**.
> 6. Reading an 8-bit byte from Even sets A0=0, BHE'=1 (and vice versa for Odd).
> 7. Reading a 16-bit word from an **Odd Address** (unaligned) takes **2 clock cycles**.

---

> ⚡ **Quick Recall**
> `Memory Banking → 2 Banks (Even/Odd) → Even Bank (D0-D7, A0=0) → Odd Bank (D8-D15, BHE'=0) → Both=0 = 16-bit transfer in 1 cycle → Unaligned Word = 2 cycles`
