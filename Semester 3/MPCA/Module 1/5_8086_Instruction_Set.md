# Topic: 8086 Instruction Set

**Q. Classify the Instruction Set of the 8086 microprocessor. Briefly explain Data Transfer, Arithmetic, Logical, Branch, String, and Processor Control instructions with one example each.**

---

> 📌 **Definition to Remember**
> An **Instruction Set** is the complete collection of commands a microprocessor can understand and execute. The 8086 Instruction Set tells the CPU how to manipulate data in registers/memory, perform math, and control the flow of execution.

---

### 1. Classification of Instructions

#### A. Data Transfer Instructions
Moves data between registers or between memory and registers. (Does NOT affect flags).
* **Example:** `MOV AX, BX` (Copies the 16-bit content of BX into AX).
* **Others:** `PUSH`, `POP`, `IN`, `OUT`, `XCHG`.

#### B. Arithmetic Instructions
Performs mathematical operations. (Updates the Flag register).
* **Example:** `ADD AL, 05H` (Adds 05H to AL and stores the result in AL).
* **Others:** `SUB`, `MUL`, `DIV`, `INC` (Increment), `DEC` (Decrement).

#### C. Logical Instructions
Performs bitwise boolean operations and bit shifting.
* **Example:** `AND CX, DX` (Performs bitwise AND on CX and DX; stores result in CX).
* **Others:** `OR`, `NOT`, `XOR`, `SHL` (Shift Left), `ROR` (Rotate Right).

#### D. Branch / Control Transfer Instructions
Changes the normal sequential flow of execution by altering the Instruction Pointer (IP).
* **Unconditional Example:** `JMP 1200H` (Jumps directly to memory address 1200H).
* **Conditional Example:** `JZ LABEL` (Jump to LABEL if the Zero Flag is set).
* **Others:** `CALL`, `RET`, `LOOP`.

#### E. String Instructions
Optimized to manipulate blocks of data (strings/arrays) in memory.
* **Example:** `MOVSB` (Moves a string byte from Source Index (SI) to Destination Index (DI)).
* **Others:** `CMPSB` (Compare string), `SCASB` (Scan string).

#### F. Processor Control Instructions
Controls processor state or hardware synchronization.
* **Example:** `STC` (Sets the Carry Flag to 1).
* **Others:** `CLC` (Clear Carry), `CLI` (Disable interrupts), `HLT` (Halt).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. An **Instruction Set** defines all commands the 8086 CPU can execute.
> 2. **Data Transfer**: Moves data (e.g., `MOV AX, BX`). Does not alter flags.
> 3. **Arithmetic**: Math operations (e.g., `ADD AL, 05H`). Updates flags.
> 4. **Logical**: Bitwise operations (e.g., `AND CX, DX`, `SHL`).
> 5. **Branch/Control**: Alters execution flow (e.g., `JMP`, `JZ`). Changes the IP register.
> 6. **String**: Operates on blocks of memory using SI and DI (e.g., `MOVSB`).
> 7. **Processor Control**: Manages hardware state/flags (e.g., `STC`, `HLT`).

---

> ⚡ **Quick Recall**
> `8086 Instructions → Data (MOV) → Arithmetic (ADD/INC) → Logical (AND/SHL) → Branch (JMP/JZ) → String (MOVSB) → Control (STC/HLT)`
