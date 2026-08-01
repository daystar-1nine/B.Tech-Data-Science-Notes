# Register Transfer & Micro-Operations

**Q. What are Micro-Operations? Discuss the four main types: Register Transfer, Arithmetic, Logic, and Shift Micro-Operations with examples.**

---

> 📌 **Definition to Remember**
> A **Micro-Operation** is the most basic, fundamental, atomic operation performed on data stored in CPU registers during one clock pulse. Every high-level machine instruction is broken down into a sequence of these elementary micro-operations.

---

### 1. Types of Micro-Operations
There are four primary categories of micro-operations based on their function.

#### A. Register Transfer Micro-Operations
Transfers data from one register to another without modifying the actual data.
* **Notation:** `<-` indicates transfer.
* **Example:** `R2 <- R1` (Copies data from R1 into R2. R1 is unchanged).
* **Control:** Usually triggered by a control condition: `If (P=1) then R2 <- R1`.

#### B. Arithmetic Micro-Operations
Performs basic math on numeric data in registers.
* **Operations:** Add, Subtract, Increment, Decrement, 2's Complement (Negation).
* **Examples:**
  * `R3 <- R1 + R2` (Addition)
  * `R1 <- R1 + 1` (Increment)
  * `R2 <- R1' + 1` (2's Complement/Negate R1, store in R2).

#### C. Logic Micro-Operations
Performs bit-by-bit manipulation on non-numeric binary data.
* **Operations:** AND, OR, XOR, NOT.
* **Uses:** Masking bits, clearing registers, inserting bits.
* **Examples:**
  * `R1 <- R1 ^ R2` (Bitwise XOR).
  * `R1 <- R1 & R2` (Bitwise AND).
  * `R1 <- 0` (Can be done by XORing a register with itself: `R1 <- R1 ^ R1`).

#### D. Shift Micro-Operations
Moves the binary bits of a register left or right. Used for data alignment and fast multiplication/division.
* **Logical Shift:** Shifts bits, filling the newly empty space with `0`. (`R1 <- shl R1`).
* **Circular Shift (Rotate):** Bits shifted out of one end are fed directly back into the other end.
* **Arithmetic Shift:** Shifts right but preserves the Most Significant Bit (MSB/Sign bit), essential for signed negative numbers.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Micro-Operation**: The smallest atomic operation executed in one clock pulse.
> 2. Four types: **Register Transfer, Arithmetic, Logic, Shift**.
> 3. **Register Transfer**: Moves data without changing it. Example: `R2 <- R1`.
> 4. **Arithmetic**: Basic math (Add, Sub, Inc). Example: `R3 <- R1 + R2`.
> 5. **Logic**: Bitwise operations (AND, OR, XOR) used for masking. Example: `R1 <- R1 ^ R2`.
> 6. **Shift**: Moves bits left/right for alignment or fast math.
> 7. Shift types: Logical (fills with 0), Circular (rotates bits), Arithmetic (preserves sign bit).

---

> ⚡ **Quick Recall**
> `Micro-Ops (1 clock pulse) → 4 Types: Transfer (R2<-R1) → Arithmetic (R1+R2, +1) → Logic (AND/XOR, bit masking) → Shift (Logical, Circular, Arithmetic for signed math)`
