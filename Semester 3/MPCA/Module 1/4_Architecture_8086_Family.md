# Architecture of 8086 Microprocessor Family

**Q. Describe the internal architecture of the 8086 Microprocessor. Explain the functions of the Bus Interface Unit (BIU), Execution Unit (EU), Registers, and Memory Segmentation.**

---

> 📌 **Definition to Remember**
> The **Intel 8086** is a 16-bit microprocessor with a 16-bit data bus and a 20-bit address bus (can address 1 MB of memory). Its internal architecture is divided into two parallel functional units: the **Bus Interface Unit (BIU)** for memory/bus operations, and the **Execution Unit (EU)** for instruction execution, enabling early pipelining.

---

### 1. Bus Interface Unit (BIU)
Handles all data and address transfers on the system buses. The EU relies entirely on the BIU to fetch data.
* **Functions:** Fetches instructions from memory, reads/writes data to memory/IO, calculates physical addresses.
* **Instruction Queue:** A 6-byte pipeline queue. BIU pre-fetches up to 6 bytes of instructions ahead of time to keep the EU busy (Instruction Pipelining).

### 2. Execution Unit (EU)
Responsible for decoding and executing instructions.
* **Functions:** Fetches instructions from the BIU's queue, decodes them, passes operands to the ALU, and executes the operation.
* It does NOT connect directly to the system buses.

### 3. Registers of 8086 (16-bit)

| Category | Registers |
| :--- | :--- |
| **General Purpose** | `AX` (Accumulator), `BX` (Base), `CX` (Count), `DX` (Data). Can split into 8-bit (`AH`, `AL`). |
| **Pointer & Index** | `SP` (Stack Pointer), `BP` (Base Pointer), `SI` (Source), `DI` (Destination). |
| **Segment Registers** | `CS` (Code Segment), `DS` (Data Segment), `SS` (Stack Segment), `ES` (Extra Segment). |
| **Special** | `IP` (Instruction Pointer), **Flag Register** (Status flags like Zero, Carry). |

### 4. Memory Segmentation
The 8086 has 16-bit registers but needs to access 20-bit addresses (1 MB). Memory is logically divided into segments of **64 KB** each.
* **Physical Address Calculation:** The 20-bit address is created by shifting a Segment Register left by 4 bits (multiplying by 16 or `10H`) and adding a 16-bit Offset.
* **Formula:** `Physical Address = (Segment Register * 10H) + Offset`
* **Example:** If `CS = 1000H` and `IP = 0002H`, Physical Address = `10000H + 0002H = 10002H`.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 8086 is a 16-bit processor; 16-bit data bus; 20-bit address bus (1 MB memory).
> 2. Divided into two units: **Bus Interface Unit (BIU)** and **Execution Unit (EU)**.
> 3. **BIU**: Handles bus operations, calculates addresses, manages a 6-byte Instruction Queue (Pipelining).
> 4. **EU**: Decodes and executes instructions fetched from the BIU queue using the ALU.
> 5. Registers: General Purpose (AX, BX, CX, DX), Segment (CS, DS, SS, ES), Pointers (SP, BP, IP), Flags.
> 6. **Memory Segmentation**: Divides 1 MB memory into 64 KB logical segments.
> 7. **Physical Address Calculation**: `(Segment * 10H) + Offset` (solves 20-bit address using 16-bit registers).

---

> ⚡ **Quick Recall**
> `8086 → 16-bit Data, 20-bit Address (1MB) → BIU (Bus/Memory, 6-byte Queue, Address Calc) + EU (Decode/Execute, ALU) → Registers (AX, BX, Segments, Pointers) → Segmentation (Physical Addr = Segment*10H + Offset)`
