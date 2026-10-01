# 80386 Register Organization

**Q. Explain the complete register organization of the Intel 80386 microprocessor. Describe General-Purpose Registers, Segment Registers, EFLAGS register, and Control Registers (CR0 to CR3) with neat diagrams.**

---

> 📌 **Definition to Remember**
> The **80386 Register Set** contains thirty-two 32-bit and 16-bit registers categorized into **General-Purpose Registers (32-bit)**, **Segment Registers (16-bit Selectors)**, **Status and Instruction Registers (EFLAGS & EIP)**, **Control Registers (CR0–CR3)**, and **System Address Registers (GDTR, LDTR, IDTR, TR)**.

---

### 1. General-Purpose Registers (32-bit Extended)

All eight general-purpose registers of the 8086 were extended to 32 bits with the `E` (Extended) prefix, while maintaining complete backward compatibility for 16-bit and 8-bit addressing:

```
  31                 16 15        8 7          0
 +---------------------+-----------+-----------+
 |                     |    AH     |    AL     |  EAX (Accumulator / I/O)
 +---------------------+-----------+-----------+  AX (16-bit)
 |                     |    BH     |    BL     |  EBX (Base Pointer to data)
 +---------------------+-----------+-----------+  BX (16-bit)
 |                     |    CH     |    CL     |  ECX (Loop / String Counter)
 +---------------------+-----------+-----------+  CX (16-bit)
 |                     |    DH     |    DL     |  EDX (Data / I/O pointer)
 +---------------------+-----------+-----------+  DX (16-bit)
 |                     |          SI           |  ESI (Source Index)
 +---------------------+-----------------------+  SI (16-bit)
 |                     |          DI           |  EDI (Destination Index)
 +---------------------+-----------------------+  DI (16-bit)
 |                     |          BP           |  EBP (Base Pointer / Stack Frame)
 +---------------------+-----------------------+  BP (16-bit)
 |                     |          SP           |  ESP (Stack Pointer)
 +---------------------+-----------------------+  SP (16-bit)
```

---

### 2. Segment Registers (16-bit Selectors)

The 80386 contains **six 16-bit segment registers**. In protected mode, they act as **Segment Selectors**:
* `CS` (Code Segment), `SS` (Stack Segment), `DS` (Data Segment), `ES` (Extra Segment).
* **`FS` and `GS`:** Two new segment registers introduced in 80386 for additional data segment access.

#### Segment Selector Format:
```
  15                                     3   2   1   0
 +----------------------------------------+---+-------+
 |        Descriptor Index (13 bits)      | TI|  RPL  |
 +----------------------------------------+---+-------+
```
* **Index (Bits 3-15):** Selects one of 8,192 ($2^{13}$) descriptors in the descriptor table.
* **TI (Table Indicator, Bit 2):** $0 = \text{GDT}$, $1 = \text{LDT}$.
* **RPL (Requested Privilege Level, Bits 0-1):** Privilege ring ($00 = \text{Ring 0}$ to $11 = \text{Ring 3}$).

---

### 3. EFLAGS Register (32-bit Extended Flags)

The 32-bit EFLAGS register contains status, control, and system privilege flags:

```
 31             18  17  16  14 13-12  11  10  9   8   7   6   4   2   0
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
| Reserved (0) |AC |VM |RF | 0 |IOPL |OF |DF |IF |TF |SF |ZF |AF |PF |CF |
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
```

#### New 80386 System Flags:
1. **VM (Virtual 8086 Mode, Bit 17):** When $1$, switches CPU to Virtual 8086 mode to execute legacy 8086 code inside protected mode.
2. **RF (Resume Flag, Bit 16):** Used with debug registers to suppress breakpoint exceptions on instruction restart.
3. **IOPL (I/O Privilege Level, Bits 12-13):** 2-bit field indicating the minimum privilege level required to execute I/O instructions (`IN`, `OUT`, `CLI`, `STI`).
4. **NT (Nested Task, Bit 14):** Set to 1 when current task is nested inside another task via a `CALL` instruction with a Task State Segment (TSS).
5. **AC (Alignment Check, Bit 18):** Enables alignment fault traps for unaligned memory accesses (added in 80486/late 386).

---

### 4. Control Registers (CR0 to CR3)

The four 32-bit Control Registers configure machine operating states and virtual memory paging:

```
CR0: [ PG | ... | ET | TS | EM | MP | PE ]
      ^                               ^
      |                               +--- Bit 0: PE (Protection Enable: 1=Prot, 0=Real)
      +----------------------------------- Bit 31: PG (Paging Enable: 1=Enable, 0=Disable)
```

* **CR0 (Machine Status & Control):**
  * **PE (Bit 0 - Protection Enable):** $1 = \text{Protected Mode}$, $0 = \text{Real Mode}$.
  * **MP (Bit 1 - Monitor Coprocessor):** Controls coprocessor task switching.
  * **EM (Bit 2 - Emulation):** $1 = \text{Trap numeric instructions}$ (software emulation).
  * **TS (Bit 3 - Task Switched):** Set automatically on task switch to protect FPU state.
  * **ET (Bit 4 - Extension Type):** $1 = \text{80387 math coprocessor present}$.
  * **PG (Bit 31 - Paging Enable):** $1 = \text{Enables hardware Paging MMU}$, $0 = \text{Disabled}$.
* **CR1:** Reserved by Intel for future processors.
* **CR2 (Page Fault Linear Address):** Stores the 32-bit linear address that caused a page fault exception (Interrupt 14).
* **CR3 (Page Directory Base Register - PDBR):** Stores the 32-bit physical base address of the **Page Directory** table for the current task.

---

### 5. System Address Registers (Descriptor Table Registers)

* **GDTR (48-bit):** Stores 32-bit base address and 16-bit limit of the **Global Descriptor Table (GDT)**.
* **IDTR (48-bit):** Stores 32-bit base address and 16-bit limit of the **Interrupt Descriptor Table (IDT)**.
* **LDTR (16-bit Selector):** Points to the **Local Descriptor Table (LDT)** descriptor in the GDT.
* **TR (Task Register - 16-bit Selector):** Points to the **Task State Segment (TSS)** descriptor in the GDT for hardware multitasking.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Eight 32-bit General Purpose Registers: **EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP** (lower 16/8 bits accessible).
> 2. Six 16-bit Segment Registers: **CS, SS, DS, ES, FS, GS** act as Segment Selectors in protected mode.
> 3. Segment Selector contains **13-bit Index ($8192$ descriptors), 1-bit TI (GDT/LDT), and 2-bit RPL**.
> 4. **EFLAGS** extends 8086 flags with **VM (Virtual 8086), RF (Resume), IOPL (I/O Privilege), and NT (Nested Task)**.
> 5. **CR0 controls core operating modes:** `PE = 1` activates Protected Mode; `PG = 1` activates hardware Paging.
> 6. **CR2** holds the faulting linear address during a Page Fault exception.
> 7. **CR3 (PDBR)** holds the physical base address of the Page Directory.

---

> ⚡ **Quick Recall**
> `8 Extended GPRs (EAX-ESP) → 6 Segment Selectors (CS-GS) → EFLAGS (VM, IOPL, NT) → CR0 (PE, PG) → CR2 (Page Fault Addr) → CR3 (Page Dir Base) → GDTR/IDTR/TR`
