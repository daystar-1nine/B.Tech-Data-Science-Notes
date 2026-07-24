# Topic: Addressing Modes of 8086

**Q. What is an Addressing Mode? Explain the various addressing modes supported by the 8086 microprocessor with appropriate examples.**

---

> 📌 **Definition to Remember**
> An **Addressing Mode** is the method by which an instruction specifies the location of its operand (the data to be processed). Because data can be located in registers, embedded in instructions, or stored in memory, 8086 provides multiple addressing modes to access it efficiently.

---

### 1. Register and Immediate Modes (No Memory Access)

| Mode | Description | Example |
| :--- | :--- | :--- |
| **Immediate** | Data is provided directly inside the instruction. | `MOV AX, 1234H` (AX = 1234H) |
| **Register** | Data is in an internal CPU register. (Fastest mode). | `MOV AX, BX` (AX = BX) |

### 2. Memory Addressing Modes (Uses Data Segment - DS)

| Mode | Description | Example |
| :--- | :--- | :--- |
| **Direct** | 16-bit memory offset address is explicitly given in the instruction. | `MOV AL, [2000H]` |
| **Register Indirect** | Offset address is held in a base (`BX`) or index (`SI`, `DI`) register. | `MOV AX, [BX]` |
| **Based** | Effective Address = Base Register (`BX` / `BP`) + Displacement. | `MOV AL, [BX + 04H]` |
| **Indexed** | Effective Address = Index Register (`SI` / `DI`) + Displacement. | `MOV AX, [SI + 08H]` |
| **Based-Indexed** | Effective Address = Base Register + Index Register + Displacement. | `MOV AL, [BX + SI + 02H]` |

### 3. Usage of Memory Modes
* **Register Indirect:** Good for passing pointers.
* **Based Addressing:** Ideal for accessing data structures (base holds struct start, displacement holds field offset).
* **Indexed Addressing:** Ideal for accessing 1D arrays (index holds array counter).
* **Based-Indexed:** Ideal for 2D arrays or complex data structures (row + column indexing).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Addressing Mode** specifies the location of the operand.
> 2. **Immediate**: Operand is constant in the instruction (`MOV AX, 1234H`).
> 3. **Register**: Operand is in a register (`MOV AX, BX`) — extremely fast.
> 4. **Direct**: Memory offset is explicitly given (`MOV AL, [2000H]`).
> 5. **Register Indirect**: Address is inside a register (`MOV AX, [BX]`).
> 6. **Based/Indexed**: Adds a displacement to a Base (`BX`/`BP`) or Index (`SI`/`DI`) register.
> 7. **Based-Indexed**: Base + Index + Displacement (`[BX+SI+02H]`) — used for 2D arrays.

---

> ⚡ **Quick Recall**
> `Addressing Modes → Immediate (value) → Register (AX=BX) → Direct ([addr]) → Indirect ([BX]) → Based ([BX+disp]) → Indexed ([SI+disp]) → Based-Indexed ([BX+SI+disp])`
