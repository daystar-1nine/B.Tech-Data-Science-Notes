# Topic: Programmer's Model of 8086

**Q. Describe the programmer's model of the 8086 microprocessor. Detail the General Purpose Registers, Segment Registers, Pointer/Index Registers, and the Flag Register.**

---

> 📌 **Definition to Remember**
> The **Programmer's Model** refers to the fourteen 16-bit internal registers accessible to an assembly programmer. They are divided into four groups: **General Purpose**, **Segment**, **Pointer/Index**, and the **Flag Register**.

---

### 1. General Purpose Registers (16-bit / 8-bit split)
Can be used as one 16-bit register or two 8-bit registers (High/Low).
* **AX (Accumulator):** `AH`, `AL`. Heavily used in math (multiplication/division) and I/O.
* **BX (Base):** `BH`, `BL`. Used to hold base offset addresses for memory access.
* **CX (Count):** `CH`, `CL`. Used as a loop counter.
* **DX (Data):** `DH`, `DL`. Used in 32-bit math and holds I/O port addresses.

### 2. Segment Registers (16-bit)
Hold the base addresses of 64 KB memory segments to help address 1 MB of physical memory.
* **CS (Code Segment):** Points to program instructions.
* **DS (Data Segment):** Points to variables/data.
* **SS (Stack Segment):** Points to the system stack.
* **ES (Extra Segment):** Additional data segment (used for string destinations).

### 3. Pointer and Index Registers (16-bit)
Hold offset addresses relative to the segment registers.
* **SP (Stack Pointer):** Offset of the top of the stack (pairs with SS).
* **BP (Base Pointer):** Used to pass data via stack (pairs with SS).
* **SI (Source Index):** Points to source data in string ops (pairs with DS).
* **DI (Destination Index):** Points to destination data in string ops (pairs with ES).
* **IP (Instruction Pointer):** Offset of the next instruction (pairs with CS). Not directly modifiable.

### 4. Flag Register (16-bit)
Contains 9 active flags (6 Status, 3 Control).
* **Status Flags:** 
  * **Carry (CF):** Set if carry out of MSB.
  * **Parity (PF):** Set if lower 8 bits have even number of 1s.
  * **Auxiliary (AF):** Carry from bit 3 to 4 (BCD math).
  * **Zero (ZF):** Set if result is zero.
  * **Sign (SF):** Set if result is negative (MSB=1).
  * **Overflow (OF):** Set if signed overflow occurs.
* **Control Flags:** 
  * **Trap (TF):** Single-step debugging.
  * **Interrupt (IF):** Enables maskable interrupts.
  * **Direction (DF):** Auto-increment/decrement in string ops.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Contains **fourteen 16-bit registers**.
> 2. **General Purpose**: AX (Math/IO), BX (Base address), CX (Loop counter), DX (Data/IO). Can split to 8-bit.
> 3. **Segment Registers**: CS (Code), DS (Data), SS (Stack), ES (Extra). Base addresses for 64KB segments.
> 4. **Pointers/Index**: SP & BP (Stack offsets), SI & DI (String offsets), IP (Next instruction offset).
> 5. **Flag Register**: 16-bit with 9 active flags.
> 6. **Status Flags**: Carry, Parity, Aux Carry, Zero, Sign, Overflow.
> 7. **Control Flags**: Trap, Interrupt, Direction.

---

> ⚡ **Quick Recall**
> `Model → General (AX/BX/CX/DX) → Segment (CS/DS/SS/ES) → Pointers (SP/BP/SI/DI/IP) → Flags (6 Status: CF/PF/AF/ZF/SF/OF, 3 Control: TF/IF/DF)`
