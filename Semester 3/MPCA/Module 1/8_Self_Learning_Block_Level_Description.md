# Topic: Block-Level Description of Functional Units — Self-Learning

**Q. Draw a block-level diagram of a computer system. Describe how the functional units are interconnected and how data and control signals flow between them.**

---

> 📌 **Definition to Remember**
> A **Block-Level Description** illustrates the physical grouping of a computer's functional units (Input, Output, Memory, CPU) and how they communicate. They do not operate in isolation; they are interconnected via a **Bus System** that transports data, memory addresses, and control signals.

---

### 1. Block Diagram of Functional Units

```text
                           +------------------------+
                           |  CENTRAL PROCESSING    |
                           |       UNIT (CPU)       |
                           |                        |
                           |    +--------------+    |
   +----------------+      |    | Control Unit |    |      +----------------+
   |                |=====>|    +------+-------+    |=====>|                |
   |  INPUT UNIT    |      |           |            |      |  OUTPUT UNIT   |
   | (e.g. Keyboard)|      |    +------+-------+    |      | (e.g. Monitor) |
   |                |<=====|    |     ALU      |    |<=====|                |
   +----------------+      |    +--------------+    |      +----------------+
            ||             |                        |              ^
            ||             +------------------------+              ||
            ||                      ||    ||                       ||
            \/                      \/    \/                       ||
   +--------------------------------------------------------------------+
   |                                                                    |
   |                           MEMORY UNIT                              |
   |                                                                    |
   +--------------------------------------------------------------------+

   Key: ====> Control Signals    ---> Data Flow
```

### 2. The Bus System (Interconnection)
Units communicate over a **Bus System**:
1. **Data Bus:** Bidirectional. Carries actual data between CPU, Memory, and I/O.
2. **Address Bus:** Unidirectional. Carries memory addresses from CPU to Memory/IO, indicating where to read/write.
3. **Control Bus:** Carries control signals (Read, Write, Interrupt) from the Control Unit to synchronize operations.

### 3. System Flow
1. **Input:** Control Unit sends a *Read* signal; Input data travels over the *Data Bus* to Memory.
2. **Processing:** Control Unit fetches data via *Data Bus*, ALU processes it, result returns to Memory.
3. **Output:** Control Unit sends a *Write* signal; Memory data travels via *Data Bus* to the Output Unit.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Functional units are interconnected using a **Bus System**.
> 2. **Block Diagram** shows CPU (CU + ALU) connected to Memory, Input, and Output units.
> 3. **Data Bus**: Bidirectional; carries actual data.
> 4. **Address Bus**: Unidirectional; carries addresses from CPU to Memory/IO.
> 5. **Control Bus**: Carries synchronization signals (Read/Write) from the Control Unit.
> 6. Control Unit directs traffic via control signals (====>).
> 7. Data (--->) always flows through the Memory Unit before going to the CPU or Output.

---

> ⚡ **Quick Recall**
> `Block Diagram → CPU, Memory, I/O → Interconnected via Buses → Data Bus (2-way, data) → Address Bus (1-way, location) → Control Bus (Signals: Read/Write)`
