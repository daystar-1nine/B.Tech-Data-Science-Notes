# Self-Learning: Red-Black Trees — Data Structures

> **Definition:** A **Red-Black Tree** is a self-balancing Binary Search Tree where each node stores an extra bit representing **color (Red or Black)**, satisfying specific balance constraints that ensure the tree height remains bounded by **2 \log_2(N + 1)**.

---

## 1. Detailed Technical Explanation

### The 5 Red-Black Tree Properties:
1. **Node Color:** Every node is either **RED** or **BLACK**.
2. **Root Property:** The root node is always **BLACK**.
3. **Leaf Property:** Every leaf (`NIL` / `NULL` sentinel node) is **BLACK**.
4. **Red Property:** If a node is **RED**, both of its children must be **BLACK** (No two consecutive RED nodes on any path).
5. **Black-Height Property:** For every node, every simple path from that node to any of its descendant `NIL` leaves contains the **exact same number of black nodes** (Black-Height).

```
Sample Red-Black Tree:
                     [ 20 (Black) ]
                    /              \
             [ 10 (Red) ]        [ 30 (Red) ]
             /          \        /          \
         [ 5 (B) ]   [ 15 (B) ][ 25 (B) ]  [ 35 (B) ]
```

---

## 2. AVL Tree vs Red-Black Tree Comparison

| Feature | AVL Tree | Red-Black Tree |
| :--- | :--- | :--- |
| **Balance Strictness** | **Strictly Balanced** (**|BF| \le 1**). Height **pprox 1.44 \log_2 N**. | **Loosely Balanced**. Longest path at most twice shortest path. |
| **Search Speed** | Faster lookups due to strictly smaller height. | Slightly slower search than AVL. |
| **Insertion / Deletion Speed** | Slower (frequent rebalancing rotations). | **Faster insertions/deletions** (at most 2-3 rotations). |
| **Use Cases** | Search-intensive workloads (Lookups > Writes). | Standard library maps (C++ `std::map`, Java `TreeMap`). |

---

## 3. Insertion in Red-Black Tree
When inserting a new key:
1. Insert as standard BST leaf and color it **RED**.
2. If root: Color **BLACK**.
3. If parent is **RED** (Double-Red Violation):
   - **Case 1: Uncle is RED:** Perform **Color Flip** (Parent & Uncle -> Black, Grandparent -> Red) and propagate up.
   - **Case 2: Uncle is BLACK (Triangle - LR/RL):** Perform single rotation on parent to convert into Line.
   - **Case 3: Uncle is BLACK (Line - LL/RR):** Perform rotation on Grandparent and swap colors of Parent and Grandparent.

---

## 4. Quick Recall Flow
```
RB-Tree -> 5 Rules: Root Black, Leaves Black, No Consecutive Reds, Uniform Black-Height -> Color Flips & Rotations
```
