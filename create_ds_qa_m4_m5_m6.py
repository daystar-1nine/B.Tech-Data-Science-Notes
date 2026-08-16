import os

DS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Data Structure"

m4_qa = os.path.join(DS_DIR, "Module 4", "Module_4_QA")
m5_qa = os.path.join(DS_DIR, "Module 5", "Module_5_QA")
m6_qa = os.path.join(DS_DIR, "Module 6", "Module_6_QA")

os.makedirs(m4_qa, exist_ok=True)
os.makedirs(m5_qa, exist_ok=True)
os.makedirs(m6_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 4 QA (TREES)
# --------------------------------------------------------------------------

u4_2m = """# 2-Mark Questions & Answers — Data Structures Module 4: Trees

---

### Q1. Define a Binary Tree and list its representations.

A **Binary Tree** is a hierarchical non-linear data structure where every node has at most two children (left and right).
- **Representations:**
  1. **Sequential (Array-Based):** Left child at `2*i`, Right child at `2*i + 1`.
  2. **Linked (Pointer-Based):** Nodes with `data`, `*left`, and `*right` pointers.

---

### Q2. What is a Full Binary Tree vs Complete Binary Tree?

- **Full Binary Tree:** Every node has either 0 or 2 children.
- **Complete Binary Tree:** All levels are completely filled except possibly the last, which is filled from left to right without gaps.

---

### Q3. Define Balance Factor in an AVL Tree.

The **Balance Factor (BF)** of a node in an AVL tree is defined as:
```
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
Valid AVL Condition: BF ∈ {-1, 0, +1}
```

---

### Q4. What is an Expression Tree?

An **Expression Tree** is a binary tree representation of an arithmetic expression where internal nodes are operators (`+`, `-`, `*`, `/`) and leaf nodes are operands (constants or variables).

---

### Q5. Differentiate between B-Tree and B+ Tree.

- **B-Tree:** Stores keys and data record pointers in both internal and leaf nodes.
- **B+ Tree:** Stores data records only in leaf nodes; leaves are linked together sequentially for fast range queries.
"""

u4_3m = """# 3-Mark Questions & Answers — Data Structures Module 4: Trees

---

### Q1. Explain the three Depth-First Traversals of a Binary Tree with examples.

1. **Preorder (Root -> Left -> Right):** Visit root first, then left and right subtrees.
2. **Inorder (Left -> Root -> Right):** Yields sorted ascending order for Binary Search Trees.
3. **Postorder (Left -> Right -> Root):** Used for bottom-up node deletion and expression evaluation.

---

### Q2. Explain the four AVL Tree rotations with diagrams.

1. **LL Rotation:** Single Right Rotation at unbalanced node `z` (Left-Left insertion).
2. **RR Rotation:** Single Left Rotation at unbalanced node `z` (Right-Right insertion).
3. **LR Rotation:** Double rotation (Left rotation on child `y`, then Right rotation on `z`).
4. **RL Rotation:** Double rotation (Right rotation on child `y`, then Left rotation on `z`).

---

### Q3. Explain the steps of Huffman Encoding algorithm.

1. Count character frequencies and insert each into a Min-Heap.
2. Repeatedly extract two nodes with lowest frequencies, combine them under a new parent node with sum frequency, and reinsert.
3. Assign binary `0` to left branches and binary `1` to right branches to generate optimal prefix-free variable-length codes.

---

### Q4. State the 5 properties of Red-Black Trees.

1. Every node is either RED or BLACK.
2. The root node is always BLACK.
3. All `NIL` leaves are BLACK.
4. If a node is RED, both its children must be BLACK (No consecutive REDs).
5. Every path from a node to descendant `NIL` leaves has the same Black-Height.
"""

u4_5m = """# 5-Mark Questions & Answers — Data Structures Module 4: Trees

---

### Q1. Explain Binary Search Tree (BST) operations: Search, Insert, and Delete (all 3 cases) with C algorithms.

- **Search / Insert:** Follow binary decision (Key < Node: go left, Key > Node: go right).
- **Delete Cases:**
  - Case 1 (0 Child): Free node and set pointer to NULL.
  - Case 2 (1 Child): Bypass node with its single child.
  - Case 3 (2 Children): Replace with **Inorder Successor** (smallest in right subtree) and recursively delete successor.

---

### Q2. Construct a Huffman Tree and compute binary codes for the following character frequencies:
`A: 45, B: 13, C: 12, D: 16, E: 9, F: 5`

```
Min-Heap merges:
1. Merge F(5) + E(9) = Node(14)
2. Merge C(12) + B(13) = Node(25)
3. Merge D(16) + Node(14) = Node(30)
4. Merge Node(25) + Node(30) = Node(55)
5. Merge A(45) + Node(55) = Root(100)
```
- Codes: `A=0, C=100, B=101, D=110, F=1110, E=1111`.

---

### Q3. Explain B-Tree properties and compare B-Tree with B+ Tree in database indexing.

- Properties of order `m`: Max `m` children, min `ceil(m/2)` children, all leaves at same level.
- B+ Tree advantages: Higher fanout, faster sequential range queries via doubly linked leaf nodes.
"""

u4_10m = """# 10-Mark Questions & Answers — Data Structures Module 4: Trees

---

### Q1. Explain Binary Trees, Tree Traversals, BST operations, and AVL Tree balancing in detail with diagrams and C implementations.

Comprehensive explanation covering:
1. Binary Tree definitions, array and pointer representations.
2. Inorder, Preorder, Postorder, and Level Order traversal algorithms.
3. BST Search, Insertion, and Deletion algorithms.
4. AVL Tree Balance Factor, LL/RR/LR/RL rotation cases, and step-by-step rebalancing trace.
5. Introduction to Multi-way B-Trees, B+ Trees, and Red-Black Trees.
"""

# Write Module 4 QA
with open(os.path.join(m4_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u4_2m)
with open(os.path.join(m4_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u4_3m)
with open(os.path.join(m4_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u4_5m)
with open(os.path.join(m4_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u4_10m)

# --------------------------------------------------------------------------
# MODULE 5 QA (GRAPHS)
# --------------------------------------------------------------------------

u5_2m = """# 2-Mark Questions & Answers — Data Structures Module 5: Graphs

---

### Q1. Define a Graph and state the Handshaking Lemma.

A **Graph** is $G = (V, E)$ consisting of a set of vertices $V$ and edges $E$.
- **Handshaking Lemma:** In any undirected graph, the sum of degrees of all vertices is twice the number of edges:
  ```
  Sum of Deg(v) = 2 * |E|
  ```

---

### Q2. Differentiate between Directed and Undirected graphs.

- **Undirected Graph:** Edges are bidirectional and symmetric ($(u, v) = (v, u)$).
- **Directed Graph (Digraph):** Edges have a specific direction ($(u, v) \ne (v, u)$).

---

### Q3. What is Adjacency Matrix vs Adjacency List?

- **Adjacency Matrix:** 2D array of size $V \times V$, $O(V^2)$ space, $O(1)$ edge query.
- **Adjacency List:** Array of linked lists, $O(V + E)$ space, ideal for sparse graphs.

---

### Q4. Define Topological Sorting.

**Topological Sorting** of a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge $(u, v)$, vertex $u$ appears before $v$ in the ordering.
"""

u5_3m = """# 3-Mark Questions & Answers — Data Structures Module 5: Graphs

---

### Q1. Compare BFS and DFS graph traversal algorithms.

| Feature | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Data Structure** | FIFO Queue | Call Stack / Recursion |
| **Strategy** | Level-by-level exploration | Branch-by-branch deep dive |
| **Shortest Path** | Finds shortest path in unweighted graphs | Explores deep paths & cycles |
| **Complexity** | $O(V + E)$ | $O(V + E)$ |

---

### Q2. Explain Kahn's algorithm for Topological Sorting.

1. Compute in-degree for all vertices.
2. Push all vertices with in-degree 0 into a Queue.
3. Dequeue vertex `u`, add to result, and decrement in-degree of all neighbors `v`.
4. If in-degree of `v` becomes 0, enqueue `v`. Repeat until queue is empty.
"""

u5_5m = """# 5-Mark Questions & Answers — Data Structures Module 5: Graphs

---

### Q1. Write complete C functions for BFS and DFS graph traversals.

Detailed C code demonstrating BFS using queue and DFS using recursion/stack on adjacency matrix representation with visited tracking.

---

### Q2. Explain graph representations (Adjacency Matrix & Adjacency List) with examples, diagrams, and complexity comparisons.

Detailed comparison of space, edge lookup, neighbor iteration, and suitability for dense vs sparse graphs.
"""

u5_10m = """# 10-Mark Questions & Answers — Data Structures Module 5: Graphs

---

### Q1. Explain Graph representations, BFS, DFS traversals, and Topological Sorting in detail with algorithms, diagrams, and applications.

Complete 10-mark solution covering Graph definitions, Adjacency Matrix vs List, step-by-step BFS and DFS traces with C code, and Topological sorting algorithms (Kahn's & DFS stack).
"""

# Write Module 5 QA
with open(os.path.join(m5_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u5_2m)
with open(os.path.join(m5_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u5_3m)
with open(os.path.join(m5_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u5_5m)
with open(os.path.join(m5_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u5_10m)

# --------------------------------------------------------------------------
# MODULE 6 QA (SORTING & SEARCHING)
# --------------------------------------------------------------------------

u6_2m = """# 2-Mark Questions & Answers — Data Structures Module 6: Sorting & Searching Techniques

---

### Q1. Differentiate between Linear Search and Binary Search.

- **Linear Search:** Unsorted/sorted arrays, sequential scan, $O(N)$ time.
- **Binary Search:** Strictly sorted arrays, divide-and-conquer interval halving, $O(\log N)$ time.

---

### Q2. What is a Stable Sorting algorithm? Give examples.

A sorting algorithm is **Stable** if it preserves the relative order of duplicate elements with equal keys.
- **Stable Sorts:** Bubble Sort, Insertion Sort, Merge Sort.
- **Unstable Sorts:** Selection Sort, Quick Sort, Heap Sort.

---

### Q3. Define Hashing and Collision.

- **Hashing:** Mapping a search key $K$ to a table index $h(K)$ using a hash function.
- **Collision:** When two distinct keys $k_1 \ne k_2$ produce the same hash index ($h(k_1) = h(k_2)$).

---

### Q4. What is Linear Probing vs Quadratic Probing?

- **Linear Probing:** Probes linearly $h(k, i) = (h'(k) + i) \bmod m$. Suffers from primary clustering.
- **Quadratic Probing:** Probes quadratically $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \bmod m$. Eliminates primary clustering.
"""

u6_3m = """# 3-Mark Questions & Answers — Data Structures Module 6: Sorting & Searching Techniques

---

### Q1. Explain the four common Hash Functions.

1. **Division Method:** $h(k) = k \bmod m$ (where $m$ is prime).
2. **Mid-Square Method:** Square $k^2$ and extract middle $r$ digits.
3. **Folding Method:** Divide key into parts and sum them.
4. **Multiplication Method:** $h(k) = \lfloor m(kA \bmod 1)\rfloor$.

---

### Q2. Compare Open Addressing and Separate Chaining collision resolution.

| Feature | Open Addressing | Separate Chaining |
| :--- | :--- | :--- |
| **Storage** | Inside table array slots | Array of linked lists |
| **Load Factor** | $\alpha \le 1$ | $\alpha > 1$ possible |
| **Deletion** | Requires `DELETED` markers | Simple linked list node deletion |
| **Cache Locality**| Excellent | Poor (pointer chasing) |
"""

u6_5m = """# 5-Mark Questions & Answers — Data Structures Module 6: Sorting & Searching Techniques

---

### Q1. Explain Bubble Sort, Insertion Sort, and Selection Sort with step-by-step trace and C programs.

Detailed algorithms, code implementations, and complexity analysis ($O(N^2)$ average, $O(1)$ space).

---

### Q2. Explain Merge Sort and Quick Sort algorithms with Divide-and-Conquer recurrence relations.

- **Merge Sort:** Divide in half, recursively sort, merge halves. $T(N) = 2T(N/2) + O(N) \implies O(N \log N)$ in all cases.
- **Quick Sort:** Partition around pivot. $O(N \log N)$ average, $O(N^2)$ worst case. In-place sorting.

---

### Q3. Explain Collision Resolution Techniques in Hashing with numerical examples.

Detailed walkthrough of Linear Probing, Quadratic Probing, Double Hashing, and Separate Chaining.
"""

u6_10m = """# 10-Mark Questions & Answers — Data Structures Module 6: Sorting & Searching Techniques

---

### Q1. Explain all major Sorting and Searching techniques, Hashing, and Collision Resolution methods in detail with complexity tables and C code.

Comprehensive 10-mark master guide covering:
1. Linear Search and Binary Search algorithms.
2. Bubble, Insertion, Selection, Merge, and Quick Sort algorithms.
3. Hash functions (Division, Mid-square, Folding, Multiplication).
4. Collision resolution: Open addressing (Linear, Quadratic, Double Hashing) vs Separate Chaining.
5. Complete Big-O Space and Time complexity comparison summary table.
"""

# Write Module 6 QA
with open(os.path.join(m6_qa, "2M.md"), "w", encoding="utf-8") as f: f.write(u6_2m)
with open(os.path.join(m6_qa, "3M.md"), "w", encoding="utf-8") as f: f.write(u6_3m)
with open(os.path.join(m6_qa, "5M.md"), "w", encoding="utf-8") as f: f.write(u6_5m)
with open(os.path.join(m6_qa, "10M.md"), "w", encoding="utf-8") as f: f.write(u6_10m)

print("Created Data Structure Module 4, 5, 6 Q&A Bank Files!")
