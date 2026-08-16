# Self-Learning: 80386 Memory Management & MESI Cache Protocol — MPCA Module 5

> **Definition:** The 80386 Memory Management Unit (MMU) provides two-stage address translation (**Segmentation & Paging**), while multiprocessor systems maintain cache consistency using the **MESI (Illinois) Protocol**.

---

## 1. 80386 Protected Mode Memory Translation

```
Logical Address (Selector:Offset)
        |
        v
[ SEGMENTATION UNIT ]  ---> Checks Descriptor in GDT/LDT -> Produces 32-bit Linear Address
        |
        v
[ PAGING UNIT (PG=1)]  ---> Uses CR3, Page Directory & Page Table -> Produces 32-bit Physical Address
```

### 1. Descriptor Tables (GDT, LDT, IDT):
- **GDT (Global Descriptor Table):** Holds segment descriptors accessible by all system tasks.
- **LDT (Local Descriptor Table):** Holds segment descriptors private to an individual application task.
- **IDT (Interrupt Descriptor Table):** Holds Gate Descriptors for 256 interrupt vectors.

### 2. Two-Level Paging Scheme (4 KB Pages):
A 32-bit Linear Address is split into:
```
  31              22 21              12 11                     0
 +------------------+------------------+------------------------+
 | Directory Index  |    Table Index   |     Offset in Page     |
 | (10 bits: 1024)  | (10 bits: 1024)  | (12 bits: 4096 bytes)  |
 +------------------+------------------+------------------------+
```
- `CR3` holds base address of **Page Directory**.
- Directory entry points to **Page Table**.
- Page Table entry points to physical 4 KB **Page Frame** in RAM.

---

## 2. MESI Cache Coherence Protocol

In symmetric multiprocessing (SMP) systems with private L1/L2 caches, every cache line exists in one of **four MESI states**:

```
M - MODIFIED  : Cache line is dirty (present only in current cache, modified, memory is stale).
E - EXCLUSIVE : Cache line is clean (present only in current cache, matches main memory).
S - SHARED    : Cache line is clean (present in multiple processor caches, matches main memory).
I - INVALID   : Cache line is invalid (contains obsolete/stale data; must fetch from bus).
```

### State Transition Summary:
- **Read Hit:** Stays in M, E, or S state.
- **Write Hit on S:** Broadcasts invalidate to bus, transitions from `S -> M`.
- **Snooping on Bus Write:** Transitions from `S -> I` or `E -> I`.

---

## 3. Quick Recall Flow
```
Logical (Selector:Offset) -> GDT/LDT -> Linear Address -> Page Dir -> Page Table -> Physical Address | MESI (Modified, Exclusive, Shared, Invalid)
```
