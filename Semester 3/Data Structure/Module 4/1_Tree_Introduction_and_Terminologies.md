# Tree Introduction & Terminologies

**Q. Define a tree as a non-linear data structure. Explain the essential tree terminologies (root, edge, leaf, internal node, degree, level, depth, height) with a neat diagram, and state the key mathematical properties of trees.**

---

> 📌 **Definition to Remember**
> A **Tree** is a non-linear, hierarchical data structure consisting of a collection of nodes connected by directed or undirected edges, such that there exists **exactly one path** between any two nodes and **no cycles** are formed. A valid tree with $N$ nodes always contains exactly **$N - 1$ edges**.

---

### 1. Hierarchical Structure & Sample Tree Diagram

Unlike linear structures (Arrays, Stacks, Queues) where elements maintain sequential relationships, trees organize data hierarchically into parent-child relationships:

```
                     [ A ]  <-- Root Node (Level 0, Depth 0, Height 3)
                    /     \
                  /         \
              [ B ]         [ C ]  <-- Internal Nodes (Level 1, Height 2)
             /     \           \
          [ D ]   [ E ]       [ F ] <-- Subtree Nodes (Level 2)
                 /     \
               [ G ]   [ H ] <-- Leaf / External Nodes (Level 3, Height 0)
```

---

### 2. Core Tree Terminologies Explained

1. **Root:** The topmost node with no incoming edges and no parent (Node `A`).
2. **Edge:** The directed link or connection between a parent node and its child node.
3. **Parent:** The immediate predecessor of a node (e.g., `A` is the parent of `B` and `C`).
4. **Child:** The immediate successor of a node (e.g., `B` and `C` are children of `A`).
5. **Siblings:** Nodes that share the exact same immediate parent (e.g., `D` and `E` are siblings).
6. **Leaf / External Node:** A node with zero children / degree zero (Nodes `D`, `G`, `H`, `F`).
7. **Internal / Non-Leaf Node:** A node with at least one child (Nodes `A`, `B`, `C`, `E`).
8. **Degree of a Node:** The total number of children connected to that node (e.g., Degree of `B` = 2, Degree of `D` = 0).
9. **Degree of a Tree:** The maximum degree among all nodes in the tree.
10. **Level of a Node:** The distance (number of edges) from the root node. The Root is at **Level 0**; its children are at Level 1, grandchildren at Level 2.
11. **Depth of a Node:** The number of edges on the unique path from the Root to that node (Depth of Root = 0).
12. **Height of a Node:** The number of edges on the longest downward path from that node to a leaf (Height of Leaf = 0).
13. **Height of a Tree:** The height of the Root node (equal to the maximum depth of any leaf in the tree).
14. **Subtree:** Any node together with all of its descendants forms an independent subtree.
15. **Path:** A sequence of consecutive edges connecting a sequence of nodes.
16. **Forest:** A collection of disjoint trees formed by removing the root node.

---

### 3. Depth vs. Height: The Crucial Distinction

| Parameter | Depth of a Node | Height of a Node |
| :--- | :--- | :--- |
| **Measurement Direction** | Measured **top-down** from the Root | Measured **bottom-up** from the Leaves |
| **Reference Point** | Distance from Root down to the node | Distance from the node down to deepest leaf |
| **Base Case** | $\text{Depth}(\text{Root}) = 0$ | $\text{Height}(\text{Leaf}) = 0$ |
| **Tree Metric** | Max depth of any node = Height of tree | Height of the root = Height of tree |

---

### 4. Key Mathematical Properties of Trees

* **Node-to-Edge Relation:** Every tree with $N$ nodes has exactly **$N - 1$ edges**.
* **Path Uniqueness:** There exists exactly one unique simple path between any pair of nodes.
* **Cycle Freedom:** A connected undirected graph with $N$ nodes and $N-1$ edges is acyclic (a tree).
* **Leaves vs. Internal Nodes:** In a strict binary tree, number of leaves $L = I + 1$ (where $I$ is internal nodes).

---

### 5. Practical Real-World Applications

* **File System Hierarchies:** Folders and subfolders in operating systems (Linux `/usr/bin/`).
* **HTML / XML DOM Trees:** Web browser Document Object Model representations.
* **Database Indexing:** B-Trees and B+ Trees in SQL engines for fast disk lookups.
* **Compiler Syntax Trees:** Abstract Syntax Trees (AST) representing program expressions.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A tree is a non-linear hierarchical data structure with **$N$ nodes and exactly $N - 1$ edges**.
> 2. The **Root** is the unique topmost node with no parent.
> 3. **Leaf nodes** have degree 0 (no children); **internal nodes** have degree $\ge 1$.
> 4. **Depth** is measured top-down from root (Depth of root = 0).
> 5. **Height** is measured bottom-up from the deepest leaf (Height of leaf = 0).
> 6. There exists **exactly one unique path** between any two nodes in a tree.
> 7. Real-world uses: File system directories, HTML DOM, compiler ASTs, and database indexing.

---

> ⚡ **Quick Recall**
> `Hierarchical Structure → Root (No Parent) → Edges = N-1 → Degree (Child Count) → Depth (Top-Down) vs Height (Bottom-Up) → Leaves (Degree 0) → Unique Path`
