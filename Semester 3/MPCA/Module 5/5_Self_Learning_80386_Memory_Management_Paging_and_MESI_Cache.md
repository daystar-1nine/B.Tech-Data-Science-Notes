# 80386 Memory Management & MESI Cache Protocol

**Q. Explain the two-stage memory management unit (MMU) of the Intel 80386 microprocessor including Segmentation and two-level Paging. Explain the four states of the MESI cache coherence protocol used in multiprocessor systems.**

---

> 📌 **Definition to Remember**
> The **80386 MMU** provides a two-stage hardware memory translation mechanism that converts **Logical Addresses to Linear Addresses via Segmentation** (using GDT/LDT descriptors) and **Linear Addresses to Physical Addresses via two-level Paging**, while multiprocessor cache systems ensure cache coherence using the **MESI (Illinois) 4-state protocol**.

---

### 1. Two-Stage Memory Translation Architecture

```
Logical Address (16-bit Selector : 32-bit Offset)
       |
       v
+-------------------------+
|   SEGMENTATION UNIT     | ---> Checks Descriptor in GDT/LDT (Base + Offset)
+-------------------------+
       |
       v 32-bit Linear Address (4 GB space)
+-------------------------+
|      PAGING UNIT        | ---> Uses CR3, Page Directory & Page Table (if PG=1)
+-------------------------+
       |
       v 32-bit Physical Address
+-------------------------+
|   PHYSICAL MEMORY RAM   |
+-------------------------+
```

---

### 2. Segmentation Mechanism

* **16-bit Segment Selector:** Stored in segment registers (`CS`, `DS`, etc.).
  * Bits 3–15: Index into descriptor table ($8192$ possible descriptors).
  * Bit 2: Table Indicator ($0 = \text{GDT}$, $1 = \text{LDT}$).
  * Bits 0–1: Requested Privilege Level (RPL: Rings 0 to 3).
* **8-byte Segment Descriptor:** Stored in GDT or LDT in memory:
  * **32-bit Base Address:** Starting physical/linear location of the segment in 4 GB memory.
  * **20-bit Segment Limit:** Size of segment ($1\text{ B}$ to $1\text{ MB}$, or $4\text{ KB}$ to $4\text{ GB}$ if Granularity bit $G = 1$).
  * **Access Rights Byte:** Contains Present bit ($P$), Descriptor Privilege Level ($DPL$), Segment Type (Code/Data/Stack), and Read/Write permissions.
* **Descriptor Tables:**
  * **GDT (Global Descriptor Table):** Shared by all programs; managed via `GDTR` register.
  * **LDT (Local Descriptor Table):** Private to each task for process isolation; managed via `LDTR`.

---

### 3. Two-Level Paging Mechanism (4 KB Pages)

When the **`PG` bit (Bit 31) in register CR0 is set to 1**, the Paging Unit is activated. It divides the 4 GB linear address space into fixed **4 Kilobyte ($4096$ byte) pages**.

#### Linear Address Breakdown (32-bit):
```
  31                22 21                12 11                       0
 +--------------------+--------------------+--------------------------+
 |  Directory Index   |    Table Index     |      Offset in Page      |
 |  (10 bits: 0-1023) | (10 bits: 0-1023)  |  (12 bits: 0-4095 bytes) |
 +--------------------+--------------------+--------------------------+
```

```
 Linear Address
 [ DIR (10) ] ----------> Page Directory (1024 Entries * 4 Bytes = 4 KB)
                             | (Points to Page Table Base)
                             v
 [ PAGE (10) ] ---------> Page Table (1024 Entries * 4 Bytes = 4 KB)
                             | (Points to Physical Page Frame)
                             v
 [ OFFSET (12) ] --------> Physical Memory Page Frame (4096 Bytes in RAM)
```

1. **CR3 (PDBR):** Points to the physical base address of the **Page Directory** table ($1024$ entries $\times 4$ bytes = 4 KB).
2. **Directory Index (Bits 22-31):** Selects one of 1024 Page Directory Entries (PDE). The PDE points to a **Page Table**.
3. **Table Index (Bits 12-21):** Selects one of 1024 Page Table Entries (PTE). The PTE points to the base of a physical **4 KB Page Frame**.
4. **Offset (Bits 0-11):** Selects the exact byte inside the 4096-byte page frame.
5. **Translation Lookaside Buffer (TLB):** An on-chip 32-entry associative cache holding recently used linear-to-physical translations, achieving a **98% hit rate** and eliminating memory lookup cycles!

---

### 4. MESI Cache Coherence Protocol

In symmetric multiprocessing (SMP) systems with private L1/L2 caches sharing a common system bus, multiple caches may hold copies of the same memory block. The **MESI (Illinois) Protocol** maintains cache consistency using four states:

| State | Name | Meaning | Present in Other Caches? | Memory is Synced? |
| :---: | :--- | :--- | :---: | :---: |
| **M** | **Modified** | Line is dirty; valid only in current cache and has been modified. | **No** (Exclusive to this cache) | **No** (Main memory is stale) |
| **E** | **Exclusive** | Line is clean; present only in current cache and matches main memory. | **No** (Exclusive to this cache) | **Yes** (Memory is up-to-date) |
| **S** | **Shared** | Line is clean; present in multiple processor caches. | **Yes** (Shared across caches) | **Yes** (Memory is up-to-date) |
| **I** | **Invalid** | Line contains obsolete or stale data; unusable. | - | - |

#### State Transitions on Bus Events:
* **Read Hit:** Line state remains unchanged ($M$, $E$, or $S$).
* **Read Miss:** Processor broadcasts a Bus Read; line is loaded in state **$E$** (if no other cache has it) or state **$S$** (if other caches have it).
* **Write Hit on $M$ or $E$:** Processor modifies data silently; transitions state $E \rightarrow M$.
* **Write Hit on $S$:** Processor must broadcast a **Bus Invalidate** signal so all other caches transition $S \rightarrow I$, then current line transitions $S \rightarrow M$.
* **Bus Snooping:** When another processor writes to a line present in current cache as $S$, current cache snoops the bus and transitions its line to **$I$ (Invalid)**.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. 80386 MMU performs two-stage translation: **Logical $\rightarrow$ Linear (Segmentation) $\rightarrow$ Physical (Paging)**.
> 2. Segment Selector contains 13-bit Index, TI (GDT/LDT), and 2-bit RPL.
> 3. Segment Descriptors specify 32-bit Base, 20-bit Limit, and Access Rights (Privilege Ring DPL).
> 4. Two-level paging splits 32-bit linear address into: **10-bit Directory Index, 10-bit Table Index, and 12-bit Offset** ($4\text{ KB}$ page).
> 5. **CR3 (PDBR)** holds the base address of the Page Directory; **TLB** caches 32 entries for fast translation.
> 6. **MESI protocol states:** **M**odified (dirty, exclusive), **E**xclusive (clean, unique), **S**hared (clean, replicated), **I**nvalid (stale).
> 7. Cache snooping forces lines from $S \rightarrow I$ when another processor issues a bus write.

---

> ⚡ **Quick Recall**
> `Logical Address → GDT/LDT Base + Offset → Linear Address → Page Dir (10) → Page Table (10) → Offset (12) → Physical RAM | MESI: Modified, Exclusive, Shared, Invalid`
