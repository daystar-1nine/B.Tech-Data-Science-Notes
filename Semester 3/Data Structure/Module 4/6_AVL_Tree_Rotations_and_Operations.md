# AVL Tree Rotations & Operations

**Q. Define an AVL Tree and Balance Factor. Explain the four AVL tree rotations (LL, RR, LR, RL) with neat diagrams and examples. Construct an AVL tree for a given sequence of numbers.**

---

> 📌 **Definition to Remember**
> An **AVL Tree** (Adelson-Velsky and Landis) is a self-balancing Binary Search Tree in which the **Balance Factor (BF)** of every node is strictly restricted to **$-1, 0, \text{ or } +1$**. If insertion or deletion causes $|\text{BF}| \ge 2$, the tree is rebalanced using **Rotations**, strictly guaranteeing **$O(\log N)$** worst-case time complexity.

---

### 1. Balance Factor Formula & Rebalancing Rule

$$\text{Balance Factor (BF)} = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree})$$

* **Valid AVL Node:** $\text{BF} \in \{-1, 0, +1\}$.
* **Unbalanced Node:** $\text{BF} = +2$ (Left-heavy) or $\text{BF} = -2$ (Right-heavy).
* Whenever a node becomes unbalanced following an insert or delete, a rotation is performed at the **lowest unbalanced ancestor** (critical node).

---

### 2. The Four AVL Tree Rotations

#### 1. LL Rotation (Single Right Rotation)
* **Cause:** Insertion occurs in the **Left subtree of the Left child** of node $z$ (BF of $z = +2$, BF of left child $= +1$).
* **Fix:** Single **Right Rotation** at node $z$.

```
       [ z ] (+2)                      [ y ] (0)
      /                               /     \
   [ y ] (+1)      === Right ==>   [ x ]   [ z ] (0)
   /               Rotation at z
[ x ]
```

#### 2. RR Rotation (Single Left Rotation)
* **Cause:** Insertion occurs in the **Right subtree of the Right child** of node $z$ (BF of $z = -2$, BF of right child $= -1$).
* **Fix:** Single **Left Rotation** at node $z$.

```
[ z ] (-2)                             [ y ] (0)
    \                                 /     \
    [ y ] (-1)     === Left ===>    [ z ]   [ x ] (0)
        \          Rotation at z
        [ x ]
```

#### 3. LR Rotation (Double Rotation: Left then Right)
* **Cause:** Insertion occurs in the **Right subtree of the Left child** of node $z$ (BF of $z = +2$, BF of left child $= -1$).
* **Fix:** **Left Rotation** on $y$, followed by **Right Rotation** on $z$.

```
     [ z ] (+2)             [ z ] (+2)               [ x ] (0)
    /                      /                        /     \
 [ y ] (-1)    == Left => [ x ]         == Right => [ y ]   [ z ]
     \        on y       /             on z
     [ x ]             [ y ]
```

#### 4. RL Rotation (Double Rotation: Right then Left)
* **Cause:** Insertion occurs in the **Left subtree of the Right child** of node $z$ (BF of $z = -2$, BF of right child $= +1$).
* **Fix:** **Right Rotation** on $y$, followed by **Left Rotation** on $z$.

```
[ z ] (-2)             [ z ] (-2)                   [ x ] (0)
    \                      \                       /     \
    [ y ] (+1) == Right => [ x ]         == Left => [ z ]   [ y ]
    /          on y            \         on z
 [ x ]                         [ y ]
```

---

### 3. Step-by-Step AVL Tree Construction

**Insert sequence:** `[ 10, 20, 30, 40, 50, 25 ]`

1. **Insert 10, 20, 30:**
   * After inserting 30: Node 10 has $\text{BF} = -2$, child 20 has $\text{BF} = -1$ $\implies$ **RR Imbalance at 10**.
   * Apply **RR Rotation (Left Rotate 10)**: 20 becomes root, with 10 (left) and 30 (right).
2. **Insert 40:** Node 30 has $\text{BF} = -1$; Root 20 has $\text{BF} = -1$. Balanced.
3. **Insert 50:** Node 30 has $\text{BF} = -2$, child 40 has $\text{BF} = -1$ $\implies$ **RR Imbalance at 30**.
   * Apply **RR Rotation (Left Rotate 30)**: 40 becomes parent of 30 and 50.
4. **Insert 25:** Node 20 has $\text{BF} = -2$, child 40 has $\text{BF} = +1$ $\implies$ **RL Imbalance at 20**.
   * Apply **RL Rotation**: Right rotate 40, then Left rotate 20. Node 30 becomes the new balanced root!

---

### 4. AVL Tree vs. Standard BST Comparison

| Parameter | Standard BST | AVL Tree |
| :--- | :--- | :--- |
| **Balance Property** | No balancing mechanism | **Strictly balanced: $|h_L - h_R| \le 1$** |
| **Worst-Case Search Time** | **$O(N)$** (Degenerates into linked list) | **$O(\log N)$ Guaranteed** |
| **Worst-Case Insert/Delete** | $O(N)$ | **$O(\log N)$** (Including rotations) |
| **Tree Height** | Up to $N$ | At most $1.44 \log_2 N$ |
| **Implementation Complexity** | Simple | Complex (Balance factors & rotations) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. AVL tree is a self-balancing BST where **Balance Factor $\text{BF} \in \{-1, 0, +1\}$** at every node.
> 2. $\text{BF} = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree})$.
> 3. **LL Rotation:** Left-Left insertion $\implies$ Single **Right rotation**.
> 4. **RR Rotation:** Right-Right insertion $\implies$ Single **Left rotation**.
> 5. **LR Rotation:** Left-Right insertion $\implies$ **Left rotation** on child, then **Right rotation** on root.
> 6. **RL Rotation:** Right-Left insertion $\implies$ **Right rotation** on child, then **Left rotation** on root.
> 7. Guarantees **$O(\log N)$ time** for search, insertion, and deletion by capping maximum tree height at $1.44 \log_2 N$.

---

> ⚡ **Quick Recall**
> `Balance Factor = hL - hR in {-1, 0, 1} → LL (Right Rotate) → RR (Left Rotate) → LR (Left then Right) → RL (Right then Left) → O(log N) Guaranteed`
