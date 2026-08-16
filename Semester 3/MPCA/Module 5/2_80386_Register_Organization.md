# 80386 Register Organization — MPCA Module 5

> **Definition:** The **80386 Register Set** consists of thirty-two 32-bit and 16-bit registers categorized into General-Purpose Registers, Segment Registers, Status and Instruction Registers (EFLAGS & EIP), Control Registers, and Debug/Test Registers.

---

## 1. Detailed Technical Explanation

### 1. General-Purpose Registers (32-bit Extended)
All 16-bit registers of 8086 were extended to 32 bits with the `E` prefix:

```
  31                 16 15        8 7          0
 +---------------------+-----------+-----------+
 |                     |    AH     |    AL     |  EAX (Accumulator)
 +---------------------+-----------+-----------+
 |                     |    BH     |    BL     |  EBX (Base Register)
 +---------------------+-----------+-----------+
 |                     |    CH     |    CL     |  ECX (Count Register)
 +---------------------+-----------+-----------+
 |                     |    DH     |    DL     |  EDX (Data Register)
 +---------------------+-----------+-----------+
 |                     |          SI           |  ESI (Source Index)
 +---------------------+-----------------------+
 |                     |          DI           |  EDI (Destination Index)
 +---------------------+-----------------------+
 |                     |          BP           |  EBP (Base Pointer)
 +---------------------+-----------------------+
 |                     |          SP           |  ESP (Stack Pointer)
 +---------------------+-----------------------+
```

---

### 2. Segment Registers (16-bit)
The 80386 has **6 Segment Selectors** (added FS and GS for additional data segment access):
- `CS` (Code Segment), `SS` (Stack Segment), `DS` (Data Segment), `ES` (Extra Segment), `FS` (General Data Segment 2), `GS` (General Data Segment 3).

---

### 3. EFLAGS Register (32-bit Extended Flags)
Extends the 8086 flags with critical operating system mode control bits:

```
 31             18  17  16  14 13-12  11  10  9   8   7   6   4   2   0
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
| Reserved (0) |AC |VM |RF | 0 |IOPL |OF |DF |IF |TF |SF |ZF |AF |PF |CF |
+--------------+---+---+---+---+-----+---+---+---+---+---+---+---+---+---+
```
- **VM (Virtual 8086 Mode, Bit 17):** When set (1), processor switches to Virtual 8086 mode.
- **RF (Resume Flag, Bit 16):** Used with debug breakpoints to disable debug exceptions on the next instruction.
- **IOPL (I/O Privilege Level, Bits 12-13):** 2-bit field (00 to 11) indicating minimum privilege required to execute I/O instructions.
- **NT (Nested Task, Bit 14):** Set when a task is invoked via a `CALL` instruction with a Task State Segment (TSS).

---

### 4. Control Registers (CR0 - CR3)
- **CR0 (Machine Status Word Extended):**
  - `PE` (Bit 0 - Protection Enable): 1 = Protected Mode, 0 = Real Mode.
  - `PG` (Bit 31 - Paging Enable): 1 = Enable Paging MMU, 0 = Disable Paging.
- **CR2 (Page Fault Linear Address):** Stores the 32-bit linear address that caused the last page fault exception.
- **CR3 (Page Directory Base Register PDBR):** Stores the 32-bit physical base address of the top-level Page Directory.

---

## 2. Quick Recall Flow
```
80386 Registers -> 8 GPRs (EAX-ESP) -> 6 Segments (CS, DS, SS, ES, FS, GS) -> EFLAGS (VM, RF, IOPL, NT) -> Control (CR0: PE/PG, CR3: Page Directory)
```
