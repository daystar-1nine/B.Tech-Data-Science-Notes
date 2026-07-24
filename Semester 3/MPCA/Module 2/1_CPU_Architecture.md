# Topic: CPU Architecture

**Q. Explain the internal organization of a CPU. Describe the basic components including Registers, ALU, and the Control Unit.**

---

> 📌 **Definition to Remember**
> The **CPU (Central Processing Unit)** is the brain of the computer. Its internal architecture defines how it fetches, decodes, and executes instructions. It consists of three primary components interconnected by an internal bus: **Registers** (storage), **ALU** (processing), and the **Control Unit** (management).

---

### 1. Registers
High-speed, temporary storage locations situated directly on the CPU chip.
* **General Purpose Registers (GPRs):** Used by programmers to temporarily store data during arithmetic operations.
* **Special Purpose Registers (SPRs):**
  * **Program Counter (PC):** Holds the address of the *next* instruction to be fetched.
  * **Instruction Register (IR):** Holds the *current* instruction being decoded/executed.
  * **Memory Address Register (MAR):** Holds the memory address for reading/writing.
  * **Memory Buffer Register (MBR/MDR):** Holds the actual data fetched from memory.
  * **Accumulator (ACC):** Stores intermediate mathematical results.

### 2. Arithmetic and Logic Unit (ALU)
The execution core where actual data processing happens.
* **Arithmetic Operations:** Addition, Subtraction, Multiplication, Division.
* **Logical Operations:** AND, OR, NOT, XOR, Shift, Compare.
* Outputs results to the Accumulator or updates **Status Flags** (Zero flag, Carry flag).

### 3. Control Unit (CU)
The manager of the CPU. It does not process data itself.
* **Functions:** Fetches instructions, decodes them, and generates **timing and control signals** to direct the ALU, memory, and I/O devices.

### 4. Internal CPU Organization
The Registers, ALU, and CU are connected via an **Internal CPU Bus**. This localized data pathway ensures high-speed data transfer between CPU components without having to use the slower external system bus.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. CPU has 3 main components: **Registers, ALU, and Control Unit (CU)**.
> 2. **Registers**: Extremely fast, on-chip storage for temporary data and addresses.
> 3. **PC (Program Counter)** stores next instruction address; **IR** holds current instruction.
> 4. **MAR/MBR** handle memory addresses/data; **Accumulator** stores math results.
> 5. **ALU**: Performs all Arithmetic (add, sub) and Logical (AND, OR) operations.
> 6. **Control Unit (CU)**: Decodes instructions and issues control signals to direct hardware.
> 7. Components communicate over high-speed **Internal CPU Buses**.

---

> ⚡ **Quick Recall**
> `CPU Org → Registers (PC/IR/MAR/MBR/ACC) → ALU (Math + Logic) → CU (Manager/Signals) → Internal Bus connects them`
