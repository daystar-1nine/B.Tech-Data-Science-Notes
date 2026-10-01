# Binary Tree Representation & Types

**Q. Define a Binary Tree. Explain the different types of binary trees (Full, Complete, Perfect, Balanced, Degenerate) with neat diagrams. Compare array-based and linked-list representations in C.**

---

> 📌 **Definition to Remember**
> A **Binary Tree** is a hierarchical tree data structure in which every node has **at most two children**, referred to as the **left child** and the **right child**. A node can have 0, 1, or 2 children.

---

### 1. Types of Binary Trees

```
1. FULL (STRICT) BINARY TREE         2. COMPLETE BINARY TREE
         [ 1 ]                                [ 1 ]
        /     \                              /     \
     [ 2 ]   [ 3 ]                        [ 2 ]   [ 3 ]
    /     \                              /     \   /
  [ 4 ]   [ 5 ]                        [ 4 ] [ 5 ][ 6 ]
(Every node has 0 or 2 children)    (Filled level-by-level, left-to-right)

3. PERFECT BINARY TREE               4. DEGENERATE (SKEWED) TREE
         [ 1 ]                                [ 1 ]
        /     \                                \
     [ 2 ]   [ 3 ]                              [ 2 ]
    /   \   /   \                                 \
  [4]   [5][6]   [7]                                [ 3 ]
(All internals have 2 children;      (All nodes have only 1 child;
 all leaves at the same depth)        degrades to O(N) linked list)
```

1. **Full (Proper / Strict) Binary Tree:** Every node has either **0 or 2 children**. No node has only 1 child.
2. **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from **left to right** without any gaps. (Forms the structural foundation for **Binary Heaps**).
3. **Perfect Binary Tree:** All internal nodes have exactly 2 children, and **all leaf nodes reside at the exact same level**.
4. **Balanced Binary Tree (Height-Balanced / AVL):** The height difference between the left and right subtrees of any node is at most 1:
   $$|\text{Height}(\text{Left}) - \text{Height}(\text{Right})| \le 1$$
5. **Degenerate (Skewed) Binary Tree:** Every internal node has exactly one child (Left-skewed or Right-skewed). Height equals $N-1$; search time degrades from $O(\log N)$ to $O(N)$.

---

### 2. Mathematical Properties of Binary Trees

* **Max Nodes at Level $i$:** $2^i$ nodes (assuming root is at Level 0).
* **Max Nodes in Tree of Height $h$:** $2^{h+1} - 1$ nodes.
* **Min Height for $N$ Nodes:** $h_{\min} = \lceil \log_2(N + 1) \rceil - 1$.
* **Max Height for $N$ Nodes:** $h_{\max} = N - 1$ (in a degenerate skewed tree).
* **Leaf vs. Internal Nodes Relation:** In any full binary tree, the number of leaf nodes $L$ is always:
  $$L = I + 1 \quad (\text{where } I = \text{number of internal nodes with 2 children})$$

---

### 3. Binary Tree Representations in Memory

#### 1. Sequential (Array-Based) Representation
Used primarily for **Complete Binary Trees** (such as Binary Heaps). For a tree stored in an array indexed starting at $i = 1$:
* Root is stored at: `A[1]`
* Left Child of node $i$: `A[2 * i]`
* Right Child of node $i$: `A[2 * i + 1]`
* Parent of node $i$: `A[floor(i / 2)]`

#### 2. Linked (Pointer-Based) Representation in C
Used for general and dynamic binary trees:

```c
#include <stdio.h>
#include <stdlib.h>

// Definition of a Binary Tree Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Helper function to allocate a new node
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
```

---

### 4. Comparison: Array vs. Linked Representation

| Parameter | Array Representation | Linked List Representation |
| :--- | :--- | :--- |
| **Memory Allocation** | Static / Contiguous memory | **Dynamic memory** (`malloc`) |
| **Wasted Space** | High for skewed/sparse trees | Minimal (extra pointer overhead per node) |
| **Child/Parent Access** | **$O(1)$ fast arithmetic** ($2i, 2i+1$) | Pointer dereferencing (`node->left`) |
| **Insertion / Deletion** | Expensive (shifting elements) | **Fast $O(1)$ pointer rewiring** |
| **Best Used For** | Complete binary trees, Heaps | General trees, BST, AVL trees |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A binary tree restricts every node to **at most two children (left and right)**.
> 2. **Full Binary Tree:** Every node has 0 or 2 children; $L = I + 1$.
> 3. **Complete Binary Tree:** Filled level by level, left to right; ideal for array storage.
> 4. **Perfect Binary Tree:** All leaves at same level; total nodes = $2^{h+1} - 1$.
> 5. **Balanced Tree:** $|h_L - h_R| \le 1$ at every node, guaranteeing $O(\log N)$ search time.
> 6. Array formula for node $i$: **Left = $2i$, Right = $2i+1$, Parent = $\lfloor i/2 \rfloor$**.
> 7. Linked representation uses `struct Node { int data; struct Node *left, *right; }`.

---

> ⚡ **Quick Recall**
> `Binary Tree (<=2 Children) → Full (0 or 2) → Complete (Left-to-Right) → Perfect (2^(h+1)-1) → Balanced (|hL - hR| <= 1) → Array (2i, 2i+1) vs Linked Pointers`
