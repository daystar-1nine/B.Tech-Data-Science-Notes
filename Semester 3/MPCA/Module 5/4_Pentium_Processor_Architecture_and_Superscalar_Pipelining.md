# Pentium Processor Architecture & Superscalar Pipelining

**Q. Draw and explain the internal architecture of the Intel Pentium Processor. Explain superscalar pipelining with U and V pipelines, instruction pairing rules, and Dynamic Branch Prediction using the Branch Target Buffer (BTB).**

---

> 📌 **Definition to Remember**
> The **Intel Pentium Processor** is a 32-bit superscalar CISC microprocessor featuring dual integer execution pipelines (**U-Pipeline** and **V-Pipeline**) capable of executing **two instructions per clock cycle (IPC = 2)**, split on-chip 8 KB Code and Data caches, an integrated 80-bit pipelined Floating-Point Unit (FPU), and **Dynamic Branch Prediction** using a Branch Target Buffer (BTB).

---

### 1. Internal Architecture of the Pentium Processor

```
                           PENTIUM INTERNAL ARCHITECTURE
 +----------------------------------------------------------------------------+
 |  64-bit External Data Bus   <=======>   32-bit Address Bus (4 GB RAM Space)|
 |                                                                            |
 |  [ 8 KB Code Cache (I-Cache) ]         [ 8 KB Data Cache (D-Cache) ]       |
 |  (2-way set associative, 32B line)     (2-way set assoc, MESI coherent)    |
 |                                                                            |
 |  [ Branch Target Buffer (BTB) ] -----> 2-bit Dynamic Branch Prediction    |
 |  (512 entries, branch history bits)                                        |
 |                                                                            |
 |  [ Dual Instruction Prefetch & Decode Unit ]                               |
 |        /                                  \                                |
 |  [ U-Pipeline (5-Stage) ]            [ V-Pipeline (5-Stage) ]              |
 |  Executes any x86 instruction        Executes simple pairable instructions |
 |                                                                            |
 |  [ 80-bit Pipelined Floating-Point Unit (FPU) ] (8-stage arithmetic unit)   |
 +----------------------------------------------------------------------------+
```

#### Major Architectural Highlights:
* **64-bit External Data Bus:** Transfers 8 bytes per bus cycle, doubling memory bandwidth over the 80386/80486.
* **Harvard Architecture Caches:** Separate **8 KB Code Cache** and **8 KB Data Cache** on-chip, preventing bus contention between instruction prefetching and operand read/writes.
* **Data Cache MESI Protocol:** Hardware support for Write-Back and Write-Through caching with cache coherence.
* **On-Chip 80-bit Pipelined FPU:** Executes common floating-point operations in a single clock cycle.

---

### 2. Superscalar Pipelining & The 5 Pipeline Stages

Superscalar architecture allows the CPU to issue and execute multiple instructions per clock cycle. The Pentium features **two parallel 5-stage integer pipelines**:
1. **U-Pipeline:** The primary pipeline; can execute any instruction from the x86 instruction set.
2. **V-Pipeline:** The secondary pipeline; executes simple integer instructions that can be safely paired with the instruction in the U-pipe.

```
Stage 1: Prefetch (PF)     Fetches instruction stream from 8 KB Code Cache.
           |
Stage 2: Decode-1 (D1)     Decodes opcodes; checks Instruction Pairing Rules between U & V.
           |
Stage 3: Decode-2 (D2)     Computes Effective Address (Base + Index * Scale + Displacement).
           |
Stage 4: Execute (EX)      ALU executes integer operations; accesses Data Cache.
           |
Stage 5: Writeback (WB)    Updates destination register and EFLAGS status bits.
```

---

### 3. Instruction Pairing Rules

Two consecutive instructions ($I_1$ and $I_2$) can execute simultaneously in the U and V pipes if and only if they satisfy the following rules:
1. **Both instructions must be simple integer instructions:**
   * Examples: `MOV`, `ALU reg, reg` (`ADD`, `SUB`, `AND`, `OR`, `XOR`, `CMP`), `INC`, `DEC`, `NOP`, `PUSH`, `POP`, near `JMP`, `CALL`, conditional `Jcc`.
2. **No Read-After-Write (RAW) / Data Dependency:** $I_2$ must not read a register written by $I_1$.
   * *Example of Hazard:* `ADD EAX, EBX` followed by `MOV ECX, EAX` $\rightarrow$ **Cannot pair** ($I_2$ must wait for $I_1$ to finish in EX stage).
3. **No Write-After-Write (WAW) Dependency:** Both instructions must not write to the same destination register.
4. **Neither instruction can contain both a Displacement AND an Immediate value.**
5. **Instruction length:** Neither instruction can exceed 15 bytes.

---

### 4. Dynamic Branch Prediction & Branch Target Buffer (BTB)

Pipelined processors suffer branch penalty stalls (3 to 4 wasted clock cycles) if a conditional jump branches to a new target.

To solve this, the Pentium implements **Dynamic Branch Prediction**:
* **Branch Target Buffer (BTB):** An on-chip 512-entry cache storing branch instruction addresses, target destination addresses, and branch history bits.
* When an instruction is fetched, the BTB is checked:
  * **BTB Hit & Predicted Taken:** Prefetch immediately switches to the target address stored in the BTB without waiting for execution.
  * **BTB Miss / Predicted Not-Taken:** Execution continues sequentially.

#### 2-bit Dynamic Branch History State Machine:

```
                  Taken
        +-----------------------+
        v                       |
     [ 11 ] ----------------> [ 10 ]
 Strongly Taken  Not-Taken  Weakly Taken
     ^   |                      |   ^
Taken|   |Not-Taken        Taken|   |Not-Taken
     |   v                      v   |
     [ 01 ] ----------------> [ 00 ]
 Weakly Not-Taken  Taken   Strongly Not-Taken
        |                       ^
        +-----------------------+
                Not-Taken
```

* **Accuracy:** Reaches over **90% branch prediction accuracy**, virtually eliminating pipeline stalls.

---

### 5. Architectural Comparison: 8086 vs. 80386 vs. Pentium

| Parameter | 8086 | 80386DX | Intel Pentium |
| :--- | :--- | :--- | :--- |
| **Data Bus** | 16-bit | 32-bit | **64-bit** |
| **Address Bus** | 20-bit (1 MB) | 32-bit (4 GB) | **32-bit (4 GB)** |
| **Pipelining** | 2 stages (BIU/EU) | 6 stages (Sequential) | **Dual 5-stage Superscalar (U & V)** |
| **Instructions per Clock**| $\ll 1$ | Up to 1 | **Up to 2 (IPC = 2)** |
| **On-Chip Cache** | None | None | **16 KB (8 KB Code + 8 KB Data)** |
| **FPU** | External 8087 | External 80387 | **Integrated 80-bit Pipelined FPU** |
| **Branch Prediction** | None | None | **Dynamic Branch Prediction (BTB)** |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Pentium is a **32-bit superscalar processor** capable of executing **two instructions per clock (IPC = 2)**.
> 2. Features a **64-bit external data bus** and 32-bit address bus (4 GB address space).
> 3. Dual integer pipelines: **U-Pipeline** (all x86 instructions) and **V-Pipeline** (simple pairable instructions).
> 4. Integer pipeline stages: **PF (Prefetch), D1 (Decode-1), D2 (Decode-2), EX (Execute), WB (Writeback)**.
> 5. Pairing requires simple instructions without **RAW / WAW data dependencies**.
> 6. Separate on-chip Harvard caches: **8 KB Code Cache** and **8 KB Data Cache** (MESI compliant).
> 7. **Branch Target Buffer (BTB)** uses a **2-bit dynamic history state machine** achieving >90% prediction accuracy.

---

> ⚡ **Quick Recall**
> `Superscalar (IPC=2) → 64-bit Data Bus → Dual U & V 5-Stage Pipes → Split 8KB Caches → Instruction Pairing (No RAW) → 2-bit BTB Branch Prediction`
