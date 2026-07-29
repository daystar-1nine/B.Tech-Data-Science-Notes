# 8086 CPU Architecture

**Q. Explain the internal architecture of the 8086 microprocessor. Describe the functions of the Bus Interface Unit (BIU) and the Execution Unit (EU).**

---

> 📌 **Definition to Remember**
> The **Intel 8086** is a 16-bit microprocessor with a 20-bit address bus (1 MB memory). Its architecture is divided into two asynchronously operating units: the **Bus Interface Unit (BIU)** (handles memory/bus fetches) and the **Execution Unit (EU)** (decodes and executes instructions), enabling early instruction pipelining.

---

### 1. Bus Interface Unit (BIU)
The BIU handles all data and address transfers on the system buses.
* **Functions:** Calculates physical addresses, fetches instructions from memory, reads/writes data.
* **Components:**
  * **Segment Registers:** `CS`, `DS`, `SS`, `ES` (for memory segmentation).
  * **Instruction Pointer (IP):** Holds the offset of the next instruction.
  * **Address Generation Circuit:** Calculates `Physical Address = (Segment * 10H) + Offset`.
  * **Instruction Queue:** A 6-byte FIFO queue. Prefetches up to 6 bytes of instructions to keep the EU busy (Pipelining).

### 2. Execution Unit (EU)
The EU is responsible for decoding and executing the fetched instructions.
* **Functions:** Pulls instructions from the BIU's queue, decodes them, performs operations, and requests BIU to store results.
* **Components:**
  * **ALU:** 16-bit Arithmetic Logic Unit.
  * **General Purpose Registers:** `AX`, `BX`, `CX`, `DX`.
  * **Pointer/Index Registers:** `SP`, `BP`, `SI`, `DI`.
  * **Flag Register:** 16-bit register showing ALU status.
  * **Control Circuitry:** Decodes and generates control signals.

### 3. Parallel Operation
Because the BIU and EU operate independently, the BIU continuously fills the 6-byte queue from memory while the EU executes the previously fetched instructions. This prevents the EU from sitting idle waiting for memory fetches, drastically reducing execution time.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8086 architecture is divided into the **BIU (Bus Interface Unit)** and **EU (Execution Unit)**.
> 2. **BIU** handles memory/bus operations and calculates the 20-bit physical address.
> 3. BIU contains Segment Registers (CS, DS, SS, ES) and a **6-byte Instruction Queue** for pipelining.
> 4. **EU** decodes and executes instructions from the queue.
> 5. EU contains the ALU, General Purpose Registers (AX, BX, CX, DX), Pointers, and Flags.
> 6. The independent operation allows the BIU to prefetch instructions while the EU executes them.
> 7. This parallel operation minimizes CPU idle time.

---

> ⚡ **Quick Recall**
> `8086 Arch → BIU + EU → BIU (Bus transfers, Address Calc, 6-byte Queue, Seg Registers) → EU (Execute, ALU, Gen Registers, Flags) → Parallel operation (Pipelining)`
