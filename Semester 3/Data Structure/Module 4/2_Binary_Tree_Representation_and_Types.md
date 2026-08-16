# Binary Tree Representation & Types — Data Structures

> **Definition:** A **Binary Tree** is a hierarchical tree data structure in which every node has at most **two children**, referred to as the **left child** and the **right child**.

---

## 1. Detailed Technical Explanation

### 1. Types of Binary Trees

```
1. FULL (PROPER) BINARY TREE         2. COMPLETE BINARY TREE
         [ 1 ]                                [ 1 ]
        /     \                              /     \
     [ 2 ]   [ 3 ]                        [ 2 ]   [ 3 ]
    /     \                              /     \   /
  [ 4 ]   [ 5 ]                        [ 4 ] [ 5 ][ 6 ]
(Every node has 0 or 2 children)    (All levels full except last, filled L-to-R)

3. PERFECT BINARY TREE               4. DEGENERATE / SKEWED TREE
         [ 1 ]                                [ 1 ]
        /     \                                \
     [ 2 ]   [ 3 ]                              [ 2 ]
    /   \   /   \                                 \
  [4]   [5][6]   [7]                                [ 3 ]
(All internal nodes have 2 children,      (All nodes have only 1 child;
 all leaves at same level)                 behaves like a linked list)
```

1. **Full (Proper/Strict) Binary Tree:** Every node has either 0 or 2 children. No node has only 1 child.
2. **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from **left to right** without gaps. (Crucial for Binary Heaps).
3. **Perfect Binary Tree:** All internal nodes have 2 children and all leaf nodes are at the exact same depth. Total nodes for height `h` is `2^(h+1) - 1`.
4. **Balanced Binary Tree (AVL/Height-balanced):** The height difference between the left and right subtrees of any node is at most 1 (`|Height(Left) - Height(Right)| <= 1`).
5. **Degenerate (Skewed) Tree:** Every internal node has only one child (Left-skewed or Right-skewed). Time complexity degrades to O(N).

---

## 2. Binary Tree Representations in Memory

### 1. Sequential (Array-Based) Representation
For a complete binary tree stored in array `A` (1-indexed):
- Node at index `i`:
  - **Left Child:** `2 * i`
  - **Right Child:** `2 * i + 1`
  - **Parent:** `floor(i / 2)`

### 2. Linked (Pointer-Based) Representation in C

```c
#include <stdio.h>
#include <stdlib.h>

// Structure for a Binary Tree Node
struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};

// Function to create a new tree node
struct TreeNode* createNode(int value) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
```

---

## 3. Mathematical Properties of Binary Trees
- Maximum nodes at level `i` (root at level 0) = `2^i`.
- Maximum nodes in binary tree of height `h` = `2^(h+1) - 1`.
- Minimum height of binary tree with `N` nodes = `ceil(log2(N + 1)) - 1`.
- In any non-empty binary tree, if `n0` is leaf count and `n2` is nodes of degree 2:
  ```
  n0 = n2 + 1
  ```

---

## 4. Must-Write Points for Exams
- In a Full Binary Tree, no node has degree 1.
- In a Complete Binary Tree, array storage has zero memory gaps.
- The formula `n0 = n2 + 1` is frequently asked in university proofs and GATE MCQs.

---

## 5. Quick Recall Flow
```
Binary Tree (<= 2 Children) -> Types: Full (0/2), Complete (L-to-R), Perfect, Skewed -> Array (2i, 2i+1) vs Linked Node
```
