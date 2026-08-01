# Topic: Memory Segmentation in 8086

**Q. Explain the concept of Memory Segmentation in the 8086 microprocessor. How is a 20-bit physical address calculated using a 16-bit segment register and a 16-bit offset?**

---

> 📌 **Definition to Remember**
> **Memory Segmentation** divides the 1 MB of physical memory of the 8086 into logical **64 KB blocks (segments)**. Because internal registers are only 16-bit (max 64 KB), the CPU mathematically combines a 16-bit **Segment Base** and a 16-bit **Offset** to generate the required 20-bit physical address.

---

# Memory Segmentation in 8086
The CPU manages these memory blocks using four specialized 16-bit Segment Registers:
1. **Code Segment (CS):** Points to the executing program instructions. Paired with Instruction Pointer (IP).
2. **Data Segment (DS):** Points to program variables. Paired with BX, SI, or direct addresses.
3. **Stack Segment (SS):** Points to the system stack. Paired with Stack Pointer (SP) or Base Pointer (BP).
4. **Extra Segment (ES):** Additional data segment, often used as destination in string operations (paired with DI).

### 2. Logical vs Physical Address
* **Logical Address:** Format used by programmers `(Segment : Offset)`. e.g., `1000H:0002H`.
* **Physical Address:** The actual 20-bit address sent over the bus to access memory.

### 3. Calculating the 20-bit Physical Address
The Bus Interface Unit (BIU) performs this calculation:
**Formula:** `Physical Address = (Segment Register × 10H) + Offset`
*(Multiplying by 10H in Hex shifts the segment value 4 bits to the left, making it a 20-bit base address).*

**Calculation Example:**
* `CS` (Segment) = `2000H`
* `IP` (Offset) = `1234H`

1. **Shift Segment by 10H:** `2000H × 10H` = `20000H` (20-bit Base)
2. **Add Offset:**
   ` 20000H`
   `+ 1234H`
   `-------`
   **` 21234H`** (20-bit Physical Address)

### 4. Advantages of Segmentation
* **Code Relocation:** Programs can be moved anywhere in memory by changing only the Segment Register; internal offset addresses remain unchanged.
* **Memory Protection/Separation:** Code, data, and stack are kept in separate segments, preventing accidental overwriting (e.g., data overwriting executable code).

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8086 has a 20-bit address bus (1 MB memory) but only 16-bit internal registers.
> 2. **Segmentation** divides memory into 64 KB logical blocks to solve this addressing mismatch.
> 3. Four Segment Registers: **CS (Code), DS (Data), SS (Stack), ES (Extra)**.
> 4. Physical Address is calculated by the BIU combining a Segment Base and an Offset.
> 5. **Formula**: `Physical Addr = (Segment Value × 10H) + Offset`.
> 6. Provide the calculation example (e.g., CS=2000H, IP=1234H → Base=20000H → Result=21234H).
> 7. **Advantages**: Easy program relocation and separation of code/data/stack.

---

> ⚡ **Quick Recall**
> `Segmentation → 1 MB Memory / 16-bit registers → Divides into 64KB blocks (CS, DS, SS, ES) → Physical Addr = (Segment × 10H) + Offset → Pros: Relocation, Code/Data separation`

