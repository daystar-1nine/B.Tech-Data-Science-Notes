# Binary Search Tree (BST) & Operations

**Q. Define a Binary Search Tree (BST). Explain search, insertion, and deletion operations with suitable diagrams and C code. Discuss the three deletion cases in detail and analyze their time complexities.**

---

> 📌 **Definition to Remember**
> A **Binary Search Tree (BST)** is a binary tree with the ordering property: for every node $X$, all keys in $X$'s left subtree are strictly **less than** $X.\text{key}$, and all keys in $X$'s right subtree are strictly **greater than** $X.\text{key}$. Duplicate keys are typically not allowed.

---

### 1. BST Property & Visual Structure

$$\text{Left Subtree Keys} < \mathbf{\text{Node Key}} < \text{Right Subtree Keys}$$

```
                     [ 50 ]
                    /      \
              [ 30 ]        [ 70 ]
             /      \      /      \
          [ 20 ]  [ 40 ] [ 60 ]  [ 80 ]
```

* **Inorder Traversal:** `20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80` (Strictly Sorted Ascending!).

---

### 2. Search & Insertion Operations

#### 1. Search Operation
* Compare search key $K$ with current node:
  * If $K == \text{node.data}$: Search Successful!
  * If $K < \text{node.data}$: Recursively search left subtree.
  * If $K > \text{node.data}$: Recursively search right subtree.
* If `NULL` reached: Key does not exist in BST.

#### 2. Insertion Operation
* Traverse down the tree following search logic until reaching a `NULL` pointer.
* Attach the new node as a leaf at that exact location.

---

### 3. Deletion in BST: The Three Cases Explained

Deleting a node is the most complex BST operation because the BST ordering invariant must be preserved:

```
Case 1: Delete Leaf (20)      Case 2: Delete Node with 1 Child (30)   Case 3: Delete Node with 2 Children (50)
      [ 30 ]                               [ 50 ]                                    [ 50 ]  <-- Replace with
     /      \                            /      \                                 /      \     Inorder Successor (60)
  [ 20 ]   [ 40 ]                      [ 30 ]   [ 70 ]                          [ 30 ]   [ 70 ]
  (Remove pointer)                     /                                                 /      \
                                    [ 20 ]                                            [ 60 ]  [ 80 ]
                                (Bypass: link 50 directly to 20)
```

1. **Case 1: Node is a Leaf (0 Children):**
   * Simply free the node and set its parent's left/right pointer to `NULL`.
2. **Case 2: Node has Exactly 1 Child:**
   * Bypass the target node by connecting its parent directly to its only child, then free the target node.
3. **Case 3: Node has 2 Children:**
   * Find the **Inorder Successor** (smallest key in the right subtree: leftmost node of right child) OR **Inorder Predecessor** (largest key in the left subtree).
   * Copy the successor's data value into the target node.
   * Recursively delete the Inorder Successor node from the right subtree (which will fall into Case 1 or Case 2).

---

### 4. Complete C Implementation of BST Operations

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};

// Create a new BST node
struct Node* createNode(int key) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = key;
    n->left = n->right = NULL;
    return n;
}

// 1. Insert Operation
struct Node* insert(struct Node* node, int key) {
    if (node == NULL) return createNode(key);
    if (key < node->data)
        node->left = insert(node->left, key);
    else if (key > node->data)
        node->right = insert(node->right, key);
    return node;
}

// Helper: Find minimum node (Inorder Successor)
struct Node* minValueNode(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

// 2. Delete Operation (Covering all 3 Cases)
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) return root;

    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Case 1 & 2: 0 or 1 child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        // Case 3: 2 children
        struct Node* temp = minValueNode(root->right); // Inorder Successor
        root->data = temp->data;                       // Copy value
        root->right = deleteNode(root->right, temp->data); // Delete successor
    }
    return root;
}
```

---

### 5. Time Complexity Analysis

| Operation | Average Case (Balanced) | Worst Case (Skewed) | Reason for Degradation |
| :--- | :---: | :---: | :--- |
| **Search** | $\mathbf{O(\log N)}$ | $\mathbf{O(N)}$ | Tree degenerates into a singly linked list if keys inserted in sorted order |
| **Insert** | $\mathbf{O(\log N)}$ | $\mathbf{O(N)}$ | Traverses down the full height $h = N$ |
| **Delete** | $\mathbf{O(\log N)}$ | $\mathbf{O(N)}$ | Successor lookup takes $O(h)$ |

* **Solution to Worst Case:** Self-balancing trees like **AVL Trees** and **Red-Black Trees** strictly guarantee $O(\log N)$ worst-case time.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. BST rule: **Left Subtree Keys < Root Key < Right Subtree Keys** at every node.
> 2. **Inorder traversal of a BST always yields sorted ascending output**.
> 3. Search and insertion take **$O(\log N)$ on average**, but degrade to **$O(N)$** in skewed trees.
> 4. **Deletion Case 1 (Leaf):** Free node, set parent pointer to `NULL`.
> 5. **Deletion Case 2 (1 Child):** Replace target node with its only child.
> 6. **Deletion Case 3 (2 Children):** Replace target value with **Inorder Successor** (min in right subtree), then delete successor.
> 7. Worst-case $O(N)$ occurs when keys are inserted in strictly sorted order, creating a degenerate tree.

---

> ⚡ **Quick Recall**
> `Left < Root < Right → Inorder = Sorted → Search/Insert: O(log N) → Delete: Leaf (NULL) | 1 Child (Bypass) | 2 Children (Inorder Successor) → Skewed: O(N)`
