# Hashing Concepts & Hash Functions — Data Structures

> **Definition: Hashing** is a technique that transforms a search key `K` into a table index `h(K)` using a **Hash Function**, enabling average constant time **O(1)** insertion, deletion, and lookup operations in a **Hash Table**.

---

## 1. Detailed Technical Explanation

```
Search Key (e.g., 108) ---> [ Hash Function h(k) = k % 10 ] ---> Index 8 in Hash Table
```

### 1. The Load Factor (**lpha**)
The load factor represents the density of items stored in a hash table of size `m` with `n` keys:
```
Load Factor (α) = n / m  (Number of Elements / Table Size)
```
- In Open Addressing, **lpha \le 1**. In Separate Chaining, **lpha** can exceed 1.

---

## 2. Common Hash Functions

### 1. Division Method (Modulo Arithmetic)
```
h(k) = k mod m
```
- **Rule:** `m` should be a **Prime Number** not close to a power of 2 or 10 to minimize clustering.
- *Example:* For table size `m = 11` and key `k = 47`:
  ```
  h(47) = 47 mod 11 = 3
  ```

### 2. Mid-Square Method
1. Square the key: **k^2**.
2. Extract the middle **r** digits of the square as the index (where table size **m = 10^r**).
- *Example:* For key `k = 31` and **m = 100**:
  ```
  k^2 = 31^2 = 0961 -> Middle digits = 96 -> Index = 96
  ```

### 3. Folding Method
Divide the key digits into equal parts of size **r**, and sum them together (ignoring overflow carry).
- **Fold-Shift:** Directly sum parts (e.g., Key `123456` into `12 + 34 + 56 = 102 -> 02`).
- **Fold-Boundary:** Reverse boundary parts before summing.

### 4. Multiplication Method
```
h(k) = floor(m * (k * A mod 1))  where 0 < A < 1 (Knuth recommends A ≈ 0.6180339887)
```
- *Advantage:* The choice of table size `m` is not critical (can be a power of 2).

---

## 3. Properties of a Good Hash Function
1. **Uniform Distribution:** Distributes keys evenly across all table slots to minimize collisions.
2. **Deterministic:** Must always compute the same index for the same input key.
3. **Fast Computation:** Computable in **O(1)** time.

---

## 4. Quick Recall Flow
```
Key -> Hash Function h(k) -> Index [0..m-1] | Functions: Division (k%m), Mid-Square (middle of k^2), Folding (split & sum)
```
