# Binary Tree Traversals (Inorder, Preorder, Postorder, Level Order)

**Q. Explain binary tree traversals in detail. Write recursive C algorithms for Preorder, Inorder, and Postorder traversals, and demonstrate how a binary tree is uniquely constructed from given Inorder and Preorder traversals.**

---

> 📌 **Definition to Remember**
> **Tree Traversal** is the algorithmic process of visiting (reading, processing, or displaying) every node in a binary tree **exactly once**. Traversals are classified into **Depth-First Traversals** (Preorder, Inorder, Postorder) and **Breadth-First Traversal** (Level Order).

---

### 1. The Four Traversal Techniques

```
                [ 1 ]
               /     \
            [ 2 ]   [ 3 ]
           /     \
        [ 4 ]   [ 5 ]
```

1. **Preorder Traversal (Root $\rightarrow$ Left $\rightarrow$ Right):**
   * Visit Root node first, recursively traverse Left subtree, recursively traverse Right subtree.
   * *Output:* `1 -> 2 -> 4 -> 5 -> 3`
   * *Use:* Creating a copy of the tree, prefix expression generation.
2. **Inorder Traversal (Left $\rightarrow$ Root $\rightarrow$ Right):**
   * Recursively traverse Left subtree, visit Root node, recursively traverse Right subtree.
   * *Output:* `4 -> 2 -> 5 -> 1 -> 3`
   * *Key Property:* Inorder traversal of a **Binary Search Tree (BST)** always outputs elements in **sorted ascending order**!
3. **Postorder Traversal (Left $\rightarrow$ Right $\rightarrow$ Root):**
   * Recursively traverse Left subtree, recursively traverse Right subtree, visit Root node last.
   * *Output:* `4 -> 5 -> 2 -> 3 -> 1`
   * *Use:* Deleting a tree bottom-up (freeing memory), postfix expression evaluation.
4. **Level Order Traversal (Breadth-First / BFS):**
   * Visits nodes level-by-level from top to bottom, and left-to-right within each level using a **FIFO Queue**.
   * *Output:* `1 -> 2 -> 3 -> 4 -> 5`

---

### 2. Recursive C Implementation of DFS Traversals

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// 1. Preorder Traversal: Root -> Left -> Right
void preorder(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);   // Visit Root
    preorder(root->left);        // Traverse Left
    preorder(root->right);       // Traverse Right
}

// 2. Inorder Traversal: Left -> Root -> Right
void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);         // Traverse Left
    printf("%d ", root->data);   // Visit Root
    inorder(root->right);        // Traverse Right
}

// 3. Postorder Traversal: Left -> Right -> Root
void postorder(struct Node* root) {
    if (root == NULL) return;
    postorder(root->left);       // Traverse Left
    postorder(root->right);      // Traverse Right
    printf("%d ", root->data);   // Visit Root
}
```

* **Time Complexity:** $O(N)$ for all traversals (each node visited once).
* **Space Complexity:** $O(h)$ auxiliary stack memory (where $h$ is tree height; $O(\log N)$ for balanced, $O(N)$ for skewed).

---

### 3. Tree Reconstruction from Inorder & Preorder Sequences

> **Fundamental Rule:** A unique binary tree can be constructed if and only if **Inorder** is provided along with either **Preorder** or **Postorder**. (Preorder + Postorder cannot uniquely construct a tree if nodes have 1 child).

#### Worked Reconstruction Example:
* **Preorder:** `[ A, B, D, E, C, F ]`
* **Inorder:**  `[ D, B, E, A, F, C ]`

**Step-by-Step Procedure:**
1. The **first element in Preorder is always the Root**: Root = `A`.
2. Find `A` in the Inorder sequence:
   * Left of `A` in Inorder: `[ D, B, E ]` $\implies$ Left Subtree.
   * Right of `A` in Inorder: `[ F, C ]` $\implies$ Right Subtree.
3. Next element in Preorder is `B`: Root of left subtree = `B`.
   * In Inorder `[ D, B, E ]`: `D` is left child of `B`, `E` is right child of `B`.
4. Next element in Preorder for right subtree is `C`: Root of right subtree = `C`.
   * In Inorder `[ F, C ]`: `F` is left of `C`, so `F` is left child of `C`.

```
RECONSTRUCTED BINARY TREE:
            [ A ]
           /     \
        [ B ]   [ C ]
       /     \   /
     [ D ]  [ E ][ F ]
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Tree traversal visits every node in the tree exactly once with **$O(N)$ time complexity**.
> 2. **Preorder (Root, Left, Right):** Visits root first; used for tree cloning.
> 3. **Inorder (Left, Root, Right):** On a BST, outputs keys in **sorted ascending order**.
> 4. **Postorder (Left, Right, Root):** Visits root last; used for bottom-up node deletion.
> 5. **Level Order:** Breadth-first traversal implemented using an auxiliary **FIFO Queue**.
> 6. Auxiliary recursion stack memory is $O(h)$ where $h$ is the tree height.
> 7. A unique tree requires **Inorder + Preorder** (or Inorder + Postorder) to resolve left/right child assignments.

---

> ⚡ **Quick Recall**
> `Preorder (Root-L-R) | Inorder (L-Root-R: Sorted BST) | Postorder (L-R-Root: Deletion) | Level Order (BFS Queue) | Unique Tree: Inorder + Preorder`
