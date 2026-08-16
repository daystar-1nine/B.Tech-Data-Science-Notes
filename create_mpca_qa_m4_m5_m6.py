import os

MPCA_DIR = r"S:\B.Tech Data Science Notes\Semester 3\MPCA"

m4_qa = os.path.join(MPCA_DIR, "Module 4", "Module_4_QA")
m5_qa = os.path.join(MPCA_DIR, "Module 5", "Module_5_QA")
m6_qa = os.path.join(MPCA_DIR, "Module 6", "Module_6_QA")

os.makedirs(m4_qa, exist_ok=True)
os.makedirs(m5_qa, exist_ok=True)
os.makedirs(m6_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4 QA (INTERFACING & PERIPHERALS)
# --------------------------------------------------------------------------

u4_2m = """# 2-Mark Questions & Answers — MPCA Module 4: Memory & Peripherals Interfacing

---

### Q1. What is the role of 74LS138 in memory interfacing?

The **74LS138** is a 3-to-8 line decoder that translates 3 higher address bus lines into 8 active-low Chip Select (/CS) signals to uniquely enable individual RAM/EPROM memory chips.

---

### Q2. What are the three operating modes of 8255 PPI?

1. **Mode 0 (Basic I/O):** Simple input/output without handshaking.
2. **Mode 1 (Strobed I/O):** Unidirectional data transfer with Port C handshake signals.
3. **Mode 2 (Strobed Bidirectional Bus):** Port A acts as an 8-bit bidirectional bus using 5 handshake lines of Port C.

---

### Q3. Define DMA and list the 4 channels of 8257 DMAC.

**DMA (Direct Memory Access)** is a high-speed data transfer mechanism directly between I/O peripherals and RAM without CPU intervention.
- The 8257 has **4 independent DMA channels (CH0, CH1, CH2, CH3)**.

---

### Q4. Differentiate between IRR, ISR, and IMR in 8259 PIC.

- **IRR (Interrupt Request Register):** Stores pending interrupt requests.
- **ISR (In-Service Register):** Tracks the interrupt currently being serviced.
- **IMR (Interrupt Mask Register):** Stores mask bits to enable/disable specific interrupt lines.

---

### Q5. What is absolute vs partial address decoding?

- **Absolute Decoding:** All address lines are decoded; no shadow addresses exist.
- **Partial Decoding:** Some address lines are left unconnected ("don't cares"); creates shadow aliases.
"""

u4_3m = """# 3-Mark Questions & Answers — MPCA Module 4: Memory & Peripherals Interfacing

---

### Q1. Explain the Control Word Register (CWR) format of 8255 PPI in I/O mode.

- **Bit D7 = 1:** I/O Mode Set flag.
- **Bits D6-D5:** Group A Mode (00=Mode 0, 01=Mode 1, 1X=Mode 2).
- **Bit D4:** Port A (1=Input, 0=Output).
- **Bit D3:** Port C Upper (1=Input, 0=Output).
- **Bit D2:** Group B Mode (0=Mode 0, 1=Mode 1).
- **Bit D1:** Port B (1=Input, 0=Output).
- **Bit D0:** Port C Lower (1=Input, 0=Output).

---

### Q2. Explain the DMA transfer cycle between 8257 and 8086 CPU.

1. Peripheral asserts `DRQ` to 8257.
2. 8257 asserts `HRQ` to 8086 CPU.
3. 8086 floats system buses and asserts `HLDA` to 8257.
4. 8257 asserts `DACK`, puts memory address on bus, and executes single-cycle I/O to memory transfer.
5. On reaching Terminal Count (`TC`), 8257 drops `HRQ`, releasing buses to CPU.

---

### Q3. Explain 8259 cascading in Master-Slave mode.

- One **Master 8259** connects to up to **8 Slave 8259s** via the 3-line Cascade Bus (`CAS0`, `CAS1`, `CAS2`).
- Increases interrupt handling capacity from 8 to **64 priority channels**.
"""

u4_5m = """# 5-Mark Questions & Answers — MPCA Module 4: Memory & Peripherals Interfacing

---

### Q1. Explain 8255 PPI internal block diagram, operating modes, and interface with 8086.

- Block diagram (Data buffer, Read/Write logic, Group A & B controls, Ports A, B, C).
- Mode 0, Mode 1, Mode 2, and BSR bit set/reset format.
- Pin connection with 8086 Data lines $D_0-D_7$, Address lines $A_1-A_2$, and chip select logic.

---

### Q2. Explain 8257 DMAC block diagram, register set, and DMA transfer modes.

- Architecture of 4 channels, Address/Count registers, and Priority Resolver.
- Single, Block (Burst), Demand, and Cascade transfer modes.

---

### Q3. Explain 8259 PIC internal architecture, interrupt sequence, and priority modes.

- Detailed breakdown of IRR, ISR, IMR, Priority Resolver, and Control logic.
- Step-by-step two-/INTA pulse handshake and vector delivery to 8086 IVT.
"""

u4_10m = """# 10-Mark Questions & Answers — MPCA Module 4: Memory & Peripherals Interfacing

---

### Q1. Explain Memory Interfacing with 8086 (RAM/ROM decoding), 8255 PPI, 8257 DMAC, and 8259 PIC in detail with block diagrams and control words.

Comprehensive 10-mark master answer covering:
1. 8086 Memory Banking (Even/Odd banks, A0, /BHE) and 74LS138 address decoding.
2. 8255 PPI Architecture, Control Word format, and Mode 0/1/2 operations.
3. 8257 DMA Controller operation, HOLD/HLDA timing, and Burst/Single modes.
4. 8259 PIC Block Diagram, IRR/ISR/IMR registers, vector transfer, and cascading.
"""

# Write Module 4 QA
with open(os.path.join(m4_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u4_2m)
with open(os.path.join(m4_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u4_3m)
with open(os.path.join(m4_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u4_5m)
with open(os.path.join(m4_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u4_10m)

# --------------------------------------------------------------------------
# MODULE 5 QA (80386 & PENTIUM)
# --------------------------------------------------------------------------

u5_2m = """# 2-Mark Questions & Answers — MPCA Module 5: 80386DX & Pentium Processors

---

### Q1. What are the bus widths and addressable memory of 80386DX?

- **Data Bus:** 32-bit (transfers 4 bytes per cycle).
- **Address Bus:** 32-bit.
- **Physical Memory:** $2^{32} = 4\\text{ GB}$.
- **Virtual Memory:** 64 Terabytes (TB).

---

### Q2. List the 3 operating modes of 80386DX.

1. **Real Address Mode:** 16-bit 8086 clone mode (1 MB memory).
2. **Protected Virtual Address Mode:** 32-bit multitasking mode with 4-level privilege rings (0-3) and Paging.
3. **Virtual 8086 Mode:** Sub-mode running legacy 8086 apps under protected OS.

---

### Q3. What is superscalar operation in Pentium?

**Superscalar Execution** allows the processor to execute **more than one instruction per clock cycle** by using two parallel integer execution pipelines (**U-Pipe and V-Pipe**).

---

### Q4. What are the four states of the MESI cache protocol?

- **M (Modified):** Dirty line, exclusive to cache, memory is stale.
- **E (Exclusive):** Clean line, exclusive to cache, matches memory.
- **S (Shared):** Clean line, present in multiple caches, matches memory.
- **I (Invalid):** Line is invalid / stale.
"""

u5_3m = """# 3-Mark Questions & Answers — MPCA Module 5: 80386DX & Pentium Processors

---

### Q1. Explain the 4 privilege rings of 80386 Protected Mode.

- **Ring 0 (Kernel Core):** Highest privilege; executes privileged OS instructions.
- **Ring 1 (Device Drivers):** System services and drivers.
- **Ring 2 (OS Extensions):** Middleware and database engines.
- **Ring 3 (User Applications):** Lowest privilege; untrusted user applications.

---

### Q2. Explain the 5 pipeline stages of Pentium processor.

1. **Prefetch (PF):** Fetches instructions from 8 KB Code Cache.
2. **Decode-1 (D1):** Decodes opcode and determines U/V pairability.
3. **Decode-2 (D2):** Generates memory addresses for operands.
4. **Execute (EX):** ALU integer execution and Data Cache access.
5. **Writeback (WB):** Updates destination registers and flags.

---

### Q3. Explain two-level Paging in 80386 microprocessor.

Linear address (32-bit) is divided into:
- `Bits 31-22 (10 bits)`: Page Directory Index.
- `Bits 21-12 (10 bits)`: Page Table Index.
- `Bits 11-0 (12 bits)`: Offset within 4 KB Page Frame.
- `CR3` register holds the physical base address of the Page Directory.
"""

u5_5m = """# 5-Mark Questions & Answers — MPCA Module 5: 80386DX & Pentium Processors

---

### Q1. Explain the architecture and functional units of 80386DX microprocessor.

- Detailed diagram and explanation of Bus Interface Unit (BIU), Central Processing Unit (Execution Unit & Instruction Unit), and Memory Management Unit (Segmentation & Paging Units).

---

### Q2. Explain Pentium architecture, dual U and V pipelines, and Dynamic Branch Prediction (BTB).

- Dual integer pipelines, pairing conditions, 8KB split caches, and 2-bit branch target buffer state machine.
"""

u5_10m = """# 10-Mark Questions & Answers — MPCA Module 5: 80386DX & Pentium Processors

---

### Q1. Explain 80386DX architecture, register organization, operating modes, memory management (Segmentation & Paging), and Pentium superscalar pipelining in detail.

Comprehensive master answer covering:
1. 80386DX 32-bit block diagram and functional units.
2. Extended registers (EAX-ESP, EFLAGS, CR0-CR3).
3. Real Mode vs Protected Mode (Privilege rings 0-3, GDT/LDT descriptors) vs Virtual 8086 Mode.
4. Two-level 4KB Paging mechanism.
5. Pentium Superscalar U & V pipelines, Branch Target Buffer (BTB), and MESI cache protocol.
"""

# Write Module 5 QA
with open(os.path.join(m5_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u5_2m)
with open(os.path.join(m5_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u5_3m)
with open(os.path.join(m5_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u5_5m)
with open(os.path.join(m5_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u5_10m)

# --------------------------------------------------------------------------
# MODULE 6 QA (PENTIUM 4 & ARM)
# --------------------------------------------------------------------------

u6_2m = """# 2-Mark Questions & Answers — MPCA Module 6: Pentium 4 & ARM Processor

---

### Q1. What is NetBurst microarchitecture in Pentium 4?

The **NetBurst Microarchitecture** is Intel's 7th-gen x86 design featuring a **20-stage hyper-pipeline**, Execution Trace Cache, and Rapid Execution Engine to achieve high clock speeds (up to 3.8 GHz).

---

### Q2. What is Execution Trace Cache in Pentium 4?

The **Execution Trace Cache** replaces the traditional L1 instruction cache by storing up to **12,000 pre-decoded micro-operations (uops)** in their predicted execution sequence, bypassing the instruction decoder.

---

### Q3. Define Hyper-Threading Technology (HT).

**Hyper-Threading** is Simultaneous Multithreading (SMT) that allows a single physical processor core to function as **two logical processors** by duplicating architectural registers while sharing execution units.

---

### Q4. What is the Inline Barrel Shifter in ARM processors?

The **Inline Barrel Shifter** is an on-chip hardware unit in ARM that can shift or rotate one operand by arbitrary bit positions within the **same single clock cycle** as arithmetic/logical operations.
"""

u6_3m = """# 3-Mark Questions & Answers — MPCA Module 6: Pentium 4 & ARM Processor

---

### Q1. Compare 8086, 80386, Pentium 1, and Pentium 4 microprocessors.

| Feature | 8086 | 80386 | Pentium 1 | Pentium 4 |
| :--- | :--- | :--- | :--- | :--- |
| **Data Bus** | 16-bit | 32-bit | 64-bit | 64-bit |
| **Address Bus** | 20-bit (1 MB) | 32-bit (4 GB) | 32-bit (4 GB) | 36-bit (64 GB) |
| **Clock Speed** | 5 - 10 MHz | 16 - 33 MHz | 60 - 200 MHz | 1.3 - 3.8 GHz |
| **Pipeline** | 2-stage | 3-stage | 5-stage dual U/V | 20-stage NetBurst |

---

### Q2. Explain ARM vs Thumb instruction states.

- **ARM State (32-bit):** Standard high-performance 32-bit instruction set with conditional execution on all instructions.
- **Thumb State (16-bit):** Compact 16-bit subset providing 30-40% code size reduction for memory-constrained embedded systems.
"""

u6_5m = """# 5-Mark Questions & Answers — MPCA Module 6: Pentium 4 & ARM Processor

---

### Q1. Explain Pentium 4 NetBurst microarchitecture, Trace Cache, and Rapid Execution Engine.

- 20-stage Hyper-Pipeline.
- 12K micro-op Trace Cache removing decode bottlenecks.
- Rapid Execution Engine integer ALUs clocked at 2x core processor frequency.
- Quad-pumped Front Side Bus (400-800 MHz).

---

### Q2. Explain Hyper-Threading Technology (HT) architecture, benefits, and hardware implementation.

- Duplicated state (GPRs, EFLAGS, CR0-CR3) vs shared execution units (ALUs, FPUs, Caches).
- 15-30% multithreaded throughput boost with minimal silicon overhead.

---

### Q3. Explain ARM RISC Processor architecture, Load-Store design, Barrel Shifter, and CPSR/SPSR registers.

- Strict Load-Store architecture (LDR/STR).
- 37 total registers, Inline Barrel Shifter, conditional instruction execution, and low power efficiency.
"""

u6_10m = """# 10-Mark Questions & Answers — MPCA Module 6: Pentium 4 & ARM Processor

---

### Q1. Explain the evolutionary comparison of Intel processors (8086 to Pentium 4), Pentium 4 NetBurst architecture, Hyper-Threading, and ARM RISC processor architecture in detail.

Comprehensive 10-mark master answer covering:
1. Comparative analysis of 8086, 80386, Pentium, Pentium II, and Pentium 4.
2. Pentium 4 NetBurst components: 20-stage pipeline, Trace Cache, Rapid ALUs, Quad-Pumped FSB.
3. Hyper-Threading simultaneous multithreading architecture.
4. ARM Processor architecture, Load-Store paradigm, Barrel Shifter, 37 registers, ARM/Thumb modes, and mobile dominance.
"""

# Write Module 6 QA
with open(os.path.join(m6_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u6_2m)
with open(os.path.join(m6_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u6_3m)
with open(os.path.join(m6_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u6_5m)
with open(os.path.join(m6_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u6_10m)

print("Created MPCA Module 4, 5, 6 Q&A Bank Files!")
