# 80386 Operating Modes (Real, Protected & Virtual 8086)

**Q. Explain the three operating modes of the Intel 80386 microprocessor: Real Address Mode, Protected Virtual Address Mode, and Virtual 8086 Mode. Compare them across memory addressing, privilege levels, and multitasking.**

---

> 📌 **Definition to Remember**
> The **80386 microprocessor** operates in three distinct operational modes: **Real Address Mode** (16-bit backward-compatible 8086 clone), **Protected Virtual Address Mode** (32-bit multitasking protected environment with 4 GB RAM, 64 TB virtual space, 4 privilege rings, and paging), and **Virtual 8086 Mode** (running real-mode 8086 applications as isolated tasks within protected mode).

---

### 1. Operating Modes Overview & Mode Transitions

```
                    +---------------------------+
                    |  POWER-UP / SYSTEM RESET  |
                    +---------------------------+
                                  |
                                  v
                    +---------------------------+
                    |     REAL ADDRESS MODE     |  <-- Bootloader / DOS
                    |  (PE = 0 in Control Reg0) |
                    +---------------------------+
                                  |
               Set PE = 1 in CR0  |   Clear PE = 0 in CR0
             (Initialize GDT/IDT) |   (Real Mode switch)
                                  v
                    +---------------------------+
                    |  PROTECTED VIRTUAL MODE   |  <-- 32-bit OS (Linux, Windows)
                    |  (PE = 1 in Control Reg0) |
                    +---------------------------+
                           |             ^
             Set VM = 1 in |             | Clear VM = 0
             EFLAGS via    |             | (Interrupt / Exception
             TSS / IRET    v             |  handler returns)
                    +---------------------------+
                    |    VIRTUAL 8086 MODE      |  <-- Legacy DOS apps inside OS
                    |   (Sub-mode of Protected) |
                    +---------------------------+
```

---

### 2. Deep Dive into Each Operating Mode

#### 1. Real Address Mode (Real Mode)
* **Default Boot Mode:** The 80386 boots into Real Mode upon hardware reset/power-on to maintain 100% binary compatibility with 8086/8088.
* **Memory Addressing:** Uses 20-bit physical addresses:
  $$\text{Physical Address} = \text{Segment} \times 16 + \text{Offset}$$
* **Address Space:** Maximum physical memory = **1 MB** (plus top 64 KB High Memory Area HMA with `A20` gate enabled).
* **Limitations:**
  * No memory protection; any user program can overwrite OS code or hardware interrupt vectors.
  * No hardware multitasking; cannot execute modern 32-bit operating systems.

#### 2. Protected Virtual Address Mode (Protected Mode)
* **Activation:** Enabled by setting the **`PE` (Protection Enable, Bit 0) = 1 in register CR0** after loading valid GDT and IDT tables.
* **Key Capabilities:**
  * **32-bit Addressing:** Accesses **4 GB physical RAM** and **64 TB virtual memory** per task.
  * **Four Privilege Rings (Rings 0 to 3):**
    * **Ring 0 (Kernel):** Highest privilege; executes core OS kernel code, memory management, and hardware drivers.
    * **Ring 1 (System Services):** Device drivers and OS utilities.
    * **Ring 2 (Custom Extensions):** Middleware and database management systems.
    * **Ring 3 (Applications):** Lowest privilege; executes standard user software. Cannot directly access hardware I/O or kernel tables.
  * **Hardware Multitasking:** Direct hardware context switching via **Task State Segment (TSS)** and Task Register (`TR`).
  * **Hardware Paging:** Divides physical memory into fixed **4 KB pages** for virtual memory demand paging.

#### 3. Virtual 8086 Mode (V86 Mode)
* **Purpose:** Allows a 32-bit multitasking OS (like Windows or Linux) to run legacy 16-bit Real Mode DOS software without rebooting or lowering OS protection.
* **Mechanism:**
  * Activated by setting the **`VM` (Virtual Mode, Bit 17) = 1 in the EFLAGS register** during a task switch via a Task State Segment (TSS).
  * Executes as a **Ring 3 (User Level) task**.
  * Hardware emulates an 8086 environment with a 1 MB address space, but the Paging Unit can map that 1 MB to **any physical 4 KB frames in RAM**.
  * Sensitive instructions (`CLI`, `STI`, `IN`, `OUT`, `INT`) trigger general protection faults (GPF) intercepted by the OS kernel, which emulates the hardware safely!

---

### 3. Comprehensive Comparison Table

| Parameter | Real Address Mode | Protected Virtual Mode | Virtual 8086 Mode |
| :--- | :--- | :--- | :--- |
| **Active Flags** | $\text{PE} = 0$ in CR0 | $\mathbf{\text{PE} = 1}$ in CR0 | $\mathbf{\text{PE} = 1}$ in CR0, $\mathbf{\text{VM} = 1}$ in EFLAGS |
| **Address Bus Width**| 20 bits | **32 bits** | 32 bits (mapped via paging) |
| **Physical Memory** | 1 MB | **4 GB** | 1 MB per V86 task |
| **Virtual Memory** | Not supported | **64 TB** per task | Supported via OS paging |
| **Address Calculation**| $\text{Segment} \times 16 + \text{Offset}$ | **Base from Descriptor + 32-bit Offset** | $\text{Segment} \times 16 + \text{Offset}$ (paged) |
| **Privilege Rings** | None (Single flat mode) | **4 Levels (Ring 0 to Ring 3)** | Runs exclusively at **Ring 3** |
| **Multitasking** | Not supported in hardware| **Hardware TSS context switching** | Multitasked by OS kernel |
| **Paging Support** | Disabled | **Supported (4 KB pages)** | **Supported (maps 1MB to RAM)** |
| **Crash Protection** | None (Buggy code crashes PC)| **Complete task isolation** | Crashed task cannot affect OS |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 80386 supports three operating modes: **Real Mode, Protected Mode, and Virtual 8086 Mode**.
> 2. **Real Mode** boots upon reset, emulates 8086, addresses 1 MB with no memory protection.
> 3. **Protected Mode** is activated by setting `PE = 1` in CR0; enables 4 GB RAM, 64 TB virtual space.
> 4. Protected mode enforces **4 privilege levels (Rings 0-3)**: Ring 0 (Kernel) to Ring 3 (User).
> 5. Segment registers act as **16-bit Selectors** indexing into 8-byte descriptors in GDT/LDT.
> 6. **Virtual 8086 Mode** (`VM = 1` in EFLAGS) runs legacy 8086 applications as isolated Ring 3 user tasks.
> 7. Sensitive I/O instructions in V86 mode trap to the Ring 0 kernel via GPF for safe software emulation.

---

> ⚡ **Quick Recall**
> `Boot (Real Mode: PE=0, 1MB, No Rings) → PE=1 (Protected Mode: 4GB, Rings 0-3, GDT/LDT, Paging) → VM=1 (Virtual 8086: Ring 3 DOS Task, Emulated I/O)`
