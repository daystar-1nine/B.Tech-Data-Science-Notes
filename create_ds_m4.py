import os

DS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Data Structure"

m4_dir = os.path.join(DS_DIR, "Module 4")
m4_qa = os.path.join(m4_dir, "Module_4_QA")

os.makedirs(m4_dir, exist_ok=True)
os.makedirs(m4_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4: TREES
# --------------------------------------------------------------------------

m4_files = {
    "1_Tree_Introduction_and_Terminologies.md": """# Tree Introduction & Terminologies — Data Structures

> **Definition:** A **Tree** is a non-linear, hierarchical data structure consisting of a collection of nodes connected by directed or undirected edges, such that there exists exactly one path between any two nodes and no cycles are formed.

---

## 1. Detailed Technical Explanation

Unlike linear data structures (Arrays, Linked Lists, Stacks, Queues) where elements are stored sequentially, trees organize data hierarchically.

```
                     [ A ]  <-- Root Node (Level 0, Height 3)
                    /     \\
                  /         \\
              [ B ]         [ C ]  <-- Internal / Non-Leaf Nodes (Level 1)
             /     \\           \\
          [ D ]   [ E ]       [ F ] <-- Subtree Nodes (Level 2)
                 /     \\
               [ G ]   [ H ] <-- Leaf / External Nodes (Level 3)
```

### Core Tree Terminologies:
1. **Root:** The topmost node in a tree with no parent (Node `A`).
2. **Edge:** The link or connection between a parent node and its child node.
3. **Parent:** An immediate predecessor node (e.g., `A` is parent of `B` and `C`).
4. **Child:** An immediate successor node (e.g., `B` and `C` are children of `A`).
5. **Siblings:** Nodes that share the same immediate parent (e.g., `D` and `E` are siblings).
6. **Leaf / External Node:** A node with zero children (e.g., `D`, `G`, `H`, `F`).
7. **Internal / Non-Leaf Node:** A node with at least one child (e.g., `A`, `B`, `C`, `E`).
8. **Degree of a Node:** The number of subtrees / children attached to that node.
9. **Degree of a Tree:** The maximum degree of any node in the tree.
10. **Level of a Node:** The distance (number of edges) from the root node. Root is at Level 0 (or Level 1 in some conventions).
11. **Depth of a Node:** The number of edges on the path from the root to that node.
12. **Height of a Node:** The number of edges on the longest downward path from that node to a leaf.
13. **Height of a Tree:** The height of the root node (maximum depth among all nodes).
14. **Subtree:** Any node together with all its descendants forms a subtree.
15. **Path:** A sequence of consecutive edges connecting a sequence of nodes.
16. **Forest:** A set of disjoint trees formed by removing the root node.

---

## 2. Memory Keywords & Mathematical Relations
- **Non-linear Hierarchy:** Parent-child recursive relationship.
- **Node to Edge Relation:** In any valid tree with `N` nodes, there are exactly `N - 1` edges.
- **Path Uniqueness:** There is exactly one unique simple path between any pair of nodes.

---

## 3. Must-Write Points for Exams
- A tree with `N` nodes always has exactly `N - 1` edges.
- Leaf nodes have a degree of 0; internal nodes have degree >= 1.
- Depth is measured top-down from root (Depth of Root = 0); Height is measured bottom-up from leaf (Height of Leaf = 0).

---

## 4. Quick Recall Flow
```
Hierarchical Structure -> Root Node -> Edges = N - 1 -> Degree (Child Count) -> Height/Depth -> Leaves (Degree 0)
```
""",

    "2_Binary_Tree_Representation_and_Types.md": """# Binary Tree Representation & Types — Data Structures

> **Definition:** A **Binary Tree** is a hierarchical tree data structure in which every node has at most **two children**, referred to as the **left child** and the **right child**.

---

## 1. Detailed Technical Explanation

### 1. Types of Binary Trees

```
1. FULL (PROPER) BINARY TREE         2. COMPLETE BINARY TREE
         [ 1 ]                                [ 1 ]
        /     \\                              /     \\
     [ 2 ]   [ 3 ]                        [ 2 ]   [ 3 ]
    /     \\                              /     \\   /
  [ 4 ]   [ 5 ]                        [ 4 ] [ 5 ][ 6 ]
(Every node has 0 or 2 children)    (All levels full except last, filled L-to-R)

3. PERFECT BINARY TREE               4. DEGENERATE / SKEWED TREE
         [ 1 ]                                [ 1 ]
        /     \\                                \\
     [ 2 ]   [ 3 ]                              [ 2 ]
    /   \\   /   \\                                 \\
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
""",

    "3_Binary_Tree_Traversals.md": """# Binary Tree Traversals (Inorder, Preorder, Postorder, Level Order) — Data Structures

> **Definition:** **Tree Traversal** is the systematic process of visiting (reading, processing, or printing) every node in a tree data structure exactly once.

---

## 1. Detailed Technical Explanation

```
               [ 1 ]
              /     \\
           [ 2 ]   [ 3 ]
          /     \\
       [ 4 ]   [ 5 ]
```

### 1. Depth-First Traversals (DFS):

1. **Preorder Traversal (Root -> Left -> Right):**
   - Visit Root, Traverse Left Subtree, Traverse Right Subtree.
   - *Example Output:* `1 -> 2 -> 4 -> 5 -> 3`
2. **Inorder Traversal (Left -> Root -> Right):**
   - Traverse Left Subtree, Visit Root, Traverse Right Subtree.
   - *Example Output:* `4 -> 2 -> 5 -> 1 -> 3`
   - *Key Property:* Inorder traversal of a **Binary Search Tree (BST)** always produces elements in **sorted ascending order**!
3. **Postorder Traversal (Left -> Right -> Root):**
   - Traverse Left Subtree, Traverse Right Subtree, Visit Root.
   - *Example Output:* `4 -> 5 -> 2 -> 3 -> 1`
   - *Key Property:* Used in Expression Tree evaluation and deleting tree nodes from bottom-up.

### 2. Breadth-First Traversal (BFS / Level Order):
- Visits nodes level-by-level from top to bottom, and left to right at each level using a **FIFO Queue**.
- *Example Output:* `1 -> 2 -> 3 -> 4 -> 5`

---

## 2. Complete Executable C Program for Traversals

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int val) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = val;
    n->left = n->right = NULL;
    return n;
}

// 1. Inorder Traversal: Left -> Root -> Right
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// 2. Preorder Traversal: Root -> Left -> Right
void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// 3. Postorder Traversal: Left -> Right -> Root
void postorder(struct Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

int main() {
    // Construct sample binary tree
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    printf("Preorder  : "); preorder(root);  printf("\\n");
    printf("Inorder   : "); inorder(root);   printf("\\n");
    printf("Postorder : "); postorder(root); printf("\\n");
    return 0;
}
```

---

## 3. Reconstructing Unique Binary Tree from Traversals
- A unique binary tree can be constructed if and only if **INORDER** is given along with either **PREORDER** or **POSTORDER**.
- Inorder splits left and right subtrees; Preorder/Postorder identifies the root node.

---

## 4. Must-Write Points for Exams
- Inorder traversal of BST gives non-decreasing sorted order.
- Time Complexity of all traversals: `O(N)` since each node is visited once.
- Auxiliary Space: `O(H)` where `H` is tree height (for recursion call stack).

---

## 5. Quick Recall Flow
```
Preorder (V-L-R) | Inorder (L-V-R) | Postorder (L-R-V) | Level Order (Queue BFS)
```
""",

    "4_Binary_Search_Tree_and_Operations.md": """# Binary Search Tree (BST) & Operations — Data Structures

> **Definition:** A **Binary Search Tree (BST)** is a binary tree with the ordering property: for every node `X`, all keys in `X`'s left subtree are strictly **less than** `X.key`, and all keys in `X`'s right subtree are strictly **greater than** `X.key`.

---

## 1. Detailed Technical Explanation

```
                     [ 50 ]
                    /      \\
              [ 30 ]        [ 70 ]
             /      \\      /      \\
          [ 20 ]  [ 40 ] [ 60 ]  [ 80 ]
```

### 1. Search Operation in BST
- Compare search key `K` with `root->data`:
  - If `K == root->data`: Found!
  - If `K < root->data`: Recursively search `root->left`.
  - If `K > root->data`: Recursively search `root->right`.
- **Time Complexity:** Average `O(log N)`, Worst-case `O(N)` (skewed tree).

### 2. Insertion Operation
- Traverse tree following BST property until reaching a `NULL` pointer, then insert new node as a leaf.

### 3. Deletion Operation in BST (Three Cases):
1. **Case 1: Node is a Leaf (0 Children):** Simply delete the node and set parent's pointer to `NULL`.
2. **Case 2: Node has 1 Child:** Replace the node with its only child.
3. **Case 3: Node has 2 Children:**
   - Find the **Inorder Successor** (smallest value in right subtree) OR **Inorder Predecessor** (largest value in left subtree).
   - Copy the successor's data to the target node.
   - Recursively delete the Inorder Successor node from the right subtree.

---

## 2. Complete Executable C Implementation of BST

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};

struct Node* createNode(int key) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = key;
    n->left = n->right = NULL;
    return n;
}

// 1. BST Insert
struct Node* insert(struct Node* node, int key) {
    if (node == NULL) return createNode(key);
    if (key < node->data)
        node->left = insert(node->left, key);
    else if (key > node->data)
        node->right = insert(node->right, key);
    return node;
}

// Find minimum node (Inorder Successor helper)
struct Node* findMin(struct Node* node) {
    struct Node* current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

// 2. BST Delete
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
        struct Node* temp = findMin(root->right); // Inorder successor
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
```

---

## 3. Time and Space Complexities
| Operation | Average Case | Worst Case (Skewed) |
| :--- | :--- | :--- |
| **Search** | `O(log N)` | `O(N)` |
| **Insertion** | `O(log N)` | `O(N)` |
| **Deletion** | `O(log N)` | `O(N)` |
| **Space** | `O(H)` | `O(N)` |

---

## 4. Quick Recall Flow
```
BST Property: Left < Root < Right -> Search/Insert via Binary Decision -> Delete (0 child: drop, 1 child: bypass, 2 children: inorder successor)
```
""",

    "5_Applications_of_Binary_Tree_Expression_Tree_and_Huffman.md": """# Applications of Binary Tree: Expression Tree & Huffman Encoding — Data Structures

> **Definition:** **Binary Trees** are applied extensively in compilers (Expression Trees for arithmetic parsing) and data compression algorithms (**Huffman Encoding** for prefix-free lossless entropy coding).

---

## 1. Application 1: Expression Trees

An **Expression Tree** is a binary tree where **internal nodes are operators** (`+`, `-`, `*`, `/`) and **leaf nodes are operands** (`a`, `b`, `5`, `10`).

```
Expression: (a + b) * (c - d)

                     [ * ]
                    /     \\
                [ + ]     [ - ]
                /   \\     /   \\
              [ a ] [ b ][ c ] [ d ]
```

### Traversals of Expression Tree:
1. **Inorder Traversal:** Yields **Infix Expression** with parentheses -> `((a + b) * (c - d))`
2. **Preorder Traversal:** Yields **Prefix (Polish) Expression** -> `* + a b - c d`
3. **Postorder Traversal:** Yields **Postfix (Reverse Polish) Expression** -> `a b + c d - *`

### Constructing Expression Tree from Postfix Expression:
1. Read postfix string token by token.
2. If token is an **operand**: Create node and push to Stack.
3. If token is an **operator**: Pop two nodes `T1` and `T2` from stack, create a new operator node with `left = T2` and `right = T1`, then push the operator node back onto Stack.

---

## 2. Application 2: Huffman Encoding (Data Compression)

Huffman Coding is a **greedy algorithm** that assigns variable-length binary codes to characters based on their frequency of occurrence. More frequent characters get shorter codes.

### Step-by-Step Huffman Tree Construction:
1. Count frequency of each unique character in input text.
2. Insert all characters into a **Min-Priority Queue (Min-Heap)**.
3. While Priority Queue has more than 1 node:
   - Extract the two nodes with the smallest frequencies: `Left = extractMin()`, `Right = extractMin()`.
   - Create a new internal parent node with frequency = `Left.freq + Right.freq`.
   - Re-insert parent node into Min-Priority Queue.
4. The remaining single node is the **Root of Huffman Tree**.
5. Assign binary `0` to all left branches and binary `1` to all right branches.

```
Sample Character Frequencies:
A: 45, B: 13, C: 12, D: 16, E: 9, F: 5

                     [ 100 ]
                    /       \\
             (0)  /           \\  (1)
             [ A: 45 ]       [ 55 ]
                            /      \\
                    (0)   /          \\  (1)
                      [ 25 ]         [ 30 ]
                     /      \\       /      \\
                 [ C:12 ][ B:13 ] [ D:16 ][ 14 ]
                                         /      \\
                                     [ F:5 ]  [ E:9 ]
```

### Resulting Prefix-Free Codes:
- `A` -> `0` (1 bit)
- `C` -> `100` (3 bits)
- `B` -> `101` (3 bits)
- `D` -> `110` (3 bits)
- `F` -> `1110` (4 bits)
- `E` -> `1111` (4 bits)

---

## 3. Must-Write Points for Exams
- Huffman codes are **Prefix-Free Codes** (no character code is a prefix of any other code), enabling unambiguous decompression.
- In Expression Trees, leaves are operands and non-leaves are operators.
- Huffman Coding achieves optimal minimum weighted path length (lossless compression).

---

## 4. Quick Recall Flow
```
Expression Tree: Leaves=Operands, Internal=Operators | Huffman Coding: Min-Heap -> Merge 2 Lowest Frequencies -> 0 Left / 1 Right -> Variable Length Prefix Code
```
""",

    "6_AVL_Tree_Rotations_and_Operations.md": """# AVL Tree Rotations & Operations — Data Structures

> **Definition:** An **AVL Tree** (Adelson-Velsky and Landis) is a **self-balancing Binary Search Tree** in which the **Balance Factor (BF)** of every node is either **-1, 0, or +1**.

---

## 1. Detailed Technical Explanation

### Balance Factor Formula:
```
Balance Factor (BF) = Height(Left Subtree) - Height(Right Subtree)
Valid AVL Condition: BF ∈ {-1, 0, +1}
```
If after an insertion or deletion, the balance factor of any node becomes `<= -2` or `>= +2`, the tree is **unbalanced** and must be rebalanced using **Rotations**.

---

## 2. The Four AVL Tree Rotations

### 1. LL Rotation (Single Right Rotation)
- **Cause:** Insertion into the **Left subtree of the Left child** of node `z` (BF of `z` = +2, BF of left child = +1).
- **Fix:** Perform a single Right Rotation at `z`.

```
       [ z ] (+2)                      [ y ] (0)
      /                               /     \\
   [ y ] (+1)      === Right ==>   [ x ]   [ z ]
   /               Rotation at z
[ x ]
```

### 2. RR Rotation (Single Left Rotation)
- **Cause:** Insertion into the **Right subtree of the Right child** of node `z` (BF of `z` = -2, BF of right child = -1).
- **Fix:** Perform a single Left Rotation at `z`.

```
[ z ] (-2)                             [ y ] (0)
    \\                                 /     \\
    [ y ] (-1)     === Left ===>    [ z ]   [ x ]
        \\          Rotation at z
        [ x ]
```

### 3. LR Rotation (Double Rotation: Left then Right)
- **Cause:** Insertion into the **Right subtree of the Left child** of node `z` (BF of `z` = +2, BF of left child = -1).
- **Fix:** Perform **Left Rotation** at `y`, followed by **Right Rotation** at `z`.

```
    [ z ] (+2)             [ z ] (+2)               [ x ] (0)
   /                      /                        /     \\
[ y ] (-1)    == Left => [ x ]         == Right => [ y ]   [ z ]
    \\        on y       /             on z
    [ x ]             [ y ]
```

### 4. RL Rotation (Double Rotation: Right then Left)
- **Cause:** Insertion into the **Left subtree of the Right child** of node `z` (BF of `z` = -2, BF of right child = +1).
- **Fix:** Perform **Right Rotation** at `y`, followed by **Left Rotation** at `z`.

---

## 3. Time Complexity of AVL Tree Operations
| Operation | Average Case | Worst Case |
| :--- | :--- | :--- |
| **Search** | `O(log N)` | `O(log N)` |
| **Insertion** | `O(log N)` (at most 2 rotations) | `O(log N)` |
| **Deletion** | `O(log N)` (up to `O(log N)` rotations) | `O(log N)` |

---

## 4. Must-Write Points for Exams
- The height of an AVL tree with `N` nodes is strictly bounded by `1.44 * log2(N)`.
- AVL tree provides faster lookup `O(log N)` than Red-Black tree because it is more strictly balanced.
- Insertion requires at most 1 single or double rotation; deletion may require up to `O(log N)` rotations propagating up the tree.

---

## 5. Quick Recall Flow
```
Balance Factor = H(Left) - H(Right) ∈ {-1, 0, 1} -> Imbalance: LL (Right Rotate), RR (Left Rotate), LR (Left-Right), RL (Right-Left)
```
""",

    "7_Introduction_to_B_Tree_and_B_Plus_Tree.md": """# Introduction to B-Tree & B+ Tree — Data Structures

> **Definition:** A **B-Tree** is a self-balancing multi-way search tree of order `m` where each node can contain multiple keys and more than two children, designed specifically to optimize **disk read/write block accesses** in database indexing and file systems.

---

## 1. Detailed Technical Explanation

### 1. Properties of a B-Tree of Order `m`:
1. Every node has at most `m` children.
2. Every internal node (except root) has at least `ceil(m / 2)` children.
3. The root has at least 2 children if it is not a leaf node.
4. A non-leaf node with `k` children contains exactly `k - 1` sorted keys.
5. **All leaves appear on the same physical level** (perfectly balanced).

```
Sample B-Tree of Order 3:
                     [ 20 | 50 ]
                   /      |      \\
        [ 10 ]        [ 30 | 40 ]     [ 60 | 70 ]
```

---

## 2. B-Tree vs B+ Tree Comparison

```
B-TREE:
- Keys AND satellite record data pointers are stored in BOTH internal and leaf nodes.

B+ TREE:
- Internal nodes store ONLY routing search keys.
- ALL satellite data records/pointers reside ONLY in LEAF nodes.
- All leaf nodes are linked together as a SLL / DLL (Doubly Linked List) for sequential range scans!
```

```
B+ Tree Structure:
                         [ 30 ]  <-- Internal Index Node (Keys Only)
                        /      \\
               [ 10 | 20 ]    [ 40 | 50 ]  <-- Internal Index Nodes
              /     |     \\   /     |     \\
            [L1] <-> [L2] <-> [L3] <-> [L4] <-- Leaves (Contain Data Pointers + Linked List)
```

### Detailed Comparison Table:
| Feature | B-Tree | B+ Tree |
| :--- | :--- | :--- |
| **Data Storage** | Data stored in internal & leaf nodes. | Data stored ONLY in leaf nodes. |
| **Search Efficiency** | Search may finish early at internal nodes. | Search always goes down to leaf nodes ($O(\log N)$ uniform). |
| **Range Queries** | Inefficient (requires in-order tree traversal). | **Extremely Fast** (traverse sequential linked list of leaves). |
| **Node Capacity** | Fewer keys per disk block due to data pointers. | More keys per block (higher fanout, smaller tree height). |
| **Applications** | File systems, database core storage. | Relational Database Indexing (MySQL InnoDB, Oracle, Db2). |

---

## 3. Core Concepts & Memory Keywords
- **Order m:** Maximum number of children a node can have.
- **Fanout:** Number of branch pointers per index node (high fanout reduces disk I/O).
- **Sequential Leaf Chaining:** Doubly linked leaf nodes enabling $O(K)$ range queries (`WHERE age BETWEEN 20 AND 30`).

---

## 4. Must-Write Points for Exams
- B-Trees and B+ Trees reduce disk I/O by fitting large numbers of keys inside a single disk page block (e.g., 4KB or 8KB).
- B+ Trees are preferred over B-Trees for database indexes because leaf chaining enables fast range searches and higher fanout.

---

## 5. Quick Recall Flow
```
Multi-Way Search Tree -> B-Tree (Data in all nodes) vs B+ Tree (Data only in linked leaves + High Fanout for DB Indexing)
```
""",

    "8_Self_Learning_Red_Black_Trees.md": """# Self-Learning: Red-Black Trees — Data Structures

> **Definition:** A **Red-Black Tree** is a self-balancing Binary Search Tree where each node stores an extra bit representing **color (Red or Black)**, satisfying specific balance constraints that ensure the tree height remains bounded by $2 \log_2(N + 1)$.

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
                    /              \\
             [ 10 (Red) ]        [ 30 (Red) ]
             /          \\        /          \\
         [ 5 (B) ]   [ 15 (B) ][ 25 (B) ]  [ 35 (B) ]
```

---

## 2. AVL Tree vs Red-Black Tree Comparison

| Feature | AVL Tree | Red-Black Tree |
| :--- | :--- | :--- |
| **Balance Strictness** | **Strictly Balanced** ($|BF| \le 1$). Height $\approx 1.44 \log_2 N$. | **Loosely Balanced**. Longest path at most twice shortest path. |
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
"""
}

# Write Module 4 files
for fname, content in m4_files.items():
    with open(os.path.join(m4_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Data Structure Module 4 Files!")
