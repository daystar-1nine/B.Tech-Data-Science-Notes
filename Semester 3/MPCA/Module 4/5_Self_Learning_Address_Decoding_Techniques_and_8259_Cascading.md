# Self-Learning: Address Decoding Techniques & 8259 Cascading — MPCA Module 4

> **Definition: Address Decoding Techniques** define how system address lines are mapped to peripheral chip selects (Absolute vs Partial), while **8259 Cascading** expands interrupt handling capacity from 8 to 64 priority channels.

---

## 1. Absolute vs Partial Address Decoding

```
ABSOLUTE ADDRESS DECODING:
- ALL address lines (A0 - A19) are fully connected to decoders and chip logic.
- Each memory/IO location has exactly ONE unique physical address.
- Eliminates "Shadow Addresses" (ghost aliases).

PARTIAL ADDRESS DECODING:
- Only some upper address lines are decoded; unused "don't care" lines (X) are left unconnected.
- Simpler and cheaper hardware (fewer logic gates).
- Causes "Shadow Addresses" (same physical hardware responds to multiple address ranges).
```

### Comparison Table:
| Feature | Absolute Decoding | Partial Decoding |
| :--- | :--- | :--- |
| **Address Line Usage** | All address lines (**A_0 - A_19**) fully decoded. | Only subset of lines decoded (**A_15-A_19**). |
| **Shadow Addresses** | **Zero Shadow Addresses** (Strict 1-to-1 mapping). | Multiple shadow aliases exist. |
| **Hardware Complexity**| High (requires multi-input logic gates/decoders). | **Low** (simple 74LS138 decoder). |
| **Best Suited For** | Large systems, 1 MB full memory maps. | Small microcontroller/embedded systems. |

---

## 2. 8259 Cascaded Mode (Master-Slave Configuration)

To handle more than 8 interrupts, one **Master 8259** is connected to up to **8 Slave 8259s** via the 3-bit Cascade Bus (**CAS_0, CAS_1, CAS_2**).

```
                  MASTER 8259 (INT to 8086 CPU)
                       |
        +--------------+--------------+
        | (CAS0, CAS1, CAS2 Bus)     |
        v                             v
  [ SLAVE 8259 #1 ]             [ SLAVE 8259 #2 ]
   IR0 to IR7 (8 Levels)         IR0 to IR7 (8 Levels)
```

### Cascading Operation Flow:
1. Slave 8259 receives interrupt on its IR line and signals Master 8259 via Master's IR pin.
2. Master sends `INT` to 8086 CPU.
3. 8086 issues 1st **\overlineINTA**. Master broadcasts the 3-bit Slave ID on **CAS_0 - CAS_2**.
4. The matching Slave recognizes its ID, and on the 2nd **\overlineINTA**, the **Slave 8259 puts the interrupt vector byte** onto the Data Bus.
5. Max Capacity = 1 Master **×** 8 Slaves = **64 Interrupt Inputs**.

---

## 3. Quick Recall Flow
```
Absolute (All Lines, No Shadows) vs Partial (Don't Cares, Shadow Addresses) | 8259 Cascading: Master-Slave via CAS0-2 -> Up to 64 Interrupts
```
