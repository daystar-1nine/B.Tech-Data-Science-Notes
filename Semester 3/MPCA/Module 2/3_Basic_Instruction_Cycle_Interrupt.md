# Topic: Basic Instruction Cycle with Interrupt Processing

**Q. Describe the phases of a Basic Instruction Cycle. Explain how the CPU handles interrupts by modifying the standard instruction cycle.**

---

> 📌 **Definition to Remember**
> The **Instruction Cycle** is the fundamental operational process of a CPU, consisting of three phases: **Fetch, Decode, Execute**. When an external event demands immediate attention, the CPU modifies this cycle by appending an **Interrupt Cycle** to save state and run an Interrupt Service Routine (ISR).

---

# Basic Instruction Cycle & Interrupt Servicing
1. **Fetch Cycle:**
   * CPU fetches the instruction from memory using the address in the Program Counter (PC).
   * Instruction is placed in the Instruction Register (IR).
   * PC is incremented to point to the next instruction.
2. **Decode Cycle:**
   * Control Unit decodes the Opcode in the IR to determine the operation.
3. **Execute Cycle:**
   * ALU performs the requested operation. Result is stored in a register/memory.
*(Loops back to Fetch).*

### 2. Handling Interrupts
An **Interrupt** breaks the normal sequential flow. To handle it, the CPU adds an **Interrupt Cycle** immediately after the Execute cycle.

**Interrupt Processing Steps:**
1. **Check:** At the end of every Execute cycle, CPU checks if any interrupt flag is set. If no, fetch next instruction.
2. **Suspend & Save State:** If interrupt is pending, CPU suspends the current program and pushes the **Program Counter (PC)** and Status Flags onto the **Stack** (saves context).
3. **Load ISR:** CPU loads the PC with the starting address of the **Interrupt Service Routine (ISR)**.
4. **Execute ISR:** CPU fetches and executes the ISR to handle the event (e.g., reading a key press).
5. **Return:** The ISR ends with `IRET` (Interrupt Return). CPU pops the original PC and Flags from the stack and seamlessly resumes the main program.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Standard cycle: **Fetch → Decode → Execute**.
> 2. **Fetch**: Gets instruction via PC, stores in IR, increments PC.
> 3. **Decode**: Control unit translates the Opcode.
> 4. **Execute**: ALU performs the task.
> 5. **Interrupt Cycle** occurs at the end of the Execute phase.
> 6. CPU suspends program and saves the **Program Counter (PC) and Flags to the Stack**.
> 7. CPU executes the **Interrupt Service Routine (ISR)**, then uses `IRET` to pop the PC and resume the original program.

---

> ⚡ **Quick Recall**
> `Cycle: Fetch (PC to IR) → Decode (CU) → Execute (ALU) → Check Interrupt → Save PC to Stack → Run ISR → IRET (Pop PC) → Resume`

