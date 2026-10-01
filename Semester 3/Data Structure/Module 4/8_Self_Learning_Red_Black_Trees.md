# Red-Black Trees: Properties & Operations

**Q. Define a Red-Black Tree. State the five essential properties of a Red-Black Tree. Explain how insertion rebalancing is performed using color flips and rotations, and compare Red-Black Trees with AVL Trees.**

---

> 📌 **Definition to Remember**
> A **Red-Black Tree** is a self-balancing Binary Search Tree where each node stores an extra color bit (**Red or Black**) and satisfies five strict structural invariants, ensuring that no path from the root to any leaf is more than **twice as long** as any other path, strictly guaranteeing **$O(\log N)$** search, insertion, and deletion.

---

### 1. The Five Essential Properties of Red-Black Trees

1. **Node Color:** Every node is either **RED** or **BLACK**.
2. **Root Property:** The **Root node is always BLACK**.
3. **Leaf Property:** Every leaf node (`NIL` / `NULL`) is considered **BLACK**.
4. **Red Invariant (No Double-Red):** If a node is **RED**, both of its children must be **BLACK** (i.e., no two consecutive red nodes on any path).
5. **Black-Height Invariant:** For every node, all simple paths from that node to descendant `NIL` leaves contain the **exact same number of BLACK nodes**.

```
                         [ 20 (B) ]  <-- Root is BLACK
                        /          \
                 [ 10 (R) ]      [ 30 (B) ]
                /          \
            [ 5 (B) ]   [ 15 (B) ]
```

* **Maximum Tree Height:** A Red-Black tree with $N$ internal nodes has height:
  $$h \le 2 \log_2(N + 1)$$

---

### 2. Insertion Rebalancing in Red-Black Trees

New nodes are always inserted as **RED** nodes (to preserve Black-Height property 5). If the parent is also RED, a Double-Red violation occurs. The fix depends on the **Uncle node's color**:

```
Let x be the newly inserted RED node, p be parent (RED), and u be uncle:

CASE 1: Uncle (u) is RED
        Action: RECOLORING / COLOR FLIP
        - Set parent (p) = BLACK
        - Set uncle (u) = BLACK
        - Set grandparent (g) = RED
        - Repeat check on grandparent (g)

CASE 2: Uncle (u) is BLACK (Triangle: x is right child, p is left child)
        Action: ROTATE
        - Perform Left Rotation on p to transform into Line configuration (Case 3).

CASE 3: Uncle (u) is BLACK (Line: x is left child, p is left child)
        Action: ROTATE & RECOLOR
        - Perform Right Rotation on grandparent g.
        - Recolor p = BLACK, g = RED.
        Tree is now fully balanced!
```

---

### 3. Red-Black Tree vs. AVL Tree Comparison

| Feature | Red-Black Tree | AVL Tree |
| :--- | :--- | :--- |
| **Balancing Strictness** | **Roughly balanced** (path ratio $\le 2:1$) | **Strictly balanced** ($|h_L - h_R| \le 1$) |
| **Lookup / Search Speed** | Fast ($O(\log N)$) | **Faster** (due to strictly smaller height) |
| **Insert / Delete Speed** | **Faster** (at most 2-3 rotations per operation) | Slower (frequent multi-level rotations) |
| **Storage Overhead** | 1 bit per node (Color: Red/Black) | 2 bits per node (Balance Factor: -1, 0, +1) |
| **Industry Standard Use** | Standard library maps (`std::map` in C++, `TreeMap` in Java, Linux kernel process scheduler) | Look-up intensive databases, in-memory caches |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Red-Black Tree is a self-balancing BST storing a **Red/Black color bit** per node.
> 2. **Property 1 & 2:** Every node is Red or Black; **Root is always Black**.
> 3. **Property 3:** Every `NIL` leaf is Black.
> 4. **Property 4:** **No two consecutive Red nodes** (Red parent must have Black children).
> 5. **Property 5:** Every simple path from root to leaf has the **same Black-Height**.
> 6. Insertion with **Red Uncle** requires **Color Flip**; **Black Uncle** requires **Rotations + Recoloring**.
> 7. Compared to AVL trees, Red-Black trees require fewer rotations during updates, making them the standard choice for language libraries (`std::map`, Java `TreeMap`).

---

> ⚡ **Quick Recall**
> `Root is Black → Red Node has Black Children → Same Black-Height on all paths → New node inserted RED → Uncle RED (Recolor) vs Uncle BLACK (Rotate & Recolor) → O(log N)`
