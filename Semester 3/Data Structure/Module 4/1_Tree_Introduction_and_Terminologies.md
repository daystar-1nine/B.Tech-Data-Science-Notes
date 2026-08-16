# Tree Introduction & Terminologies — Data Structures

> **Definition:** A **Tree** is a non-linear, hierarchical data structure consisting of a collection of nodes connected by directed or undirected edges, such that there exists exactly one path between any two nodes and no cycles are formed.

---

## 1. Detailed Technical Explanation

Unlike linear data structures (Arrays, Linked Lists, Stacks, Queues) where elements are stored sequentially, trees organize data hierarchically.

```
                     [ A ]  <-- Root Node (Level 0, Height 3)
                    /     \
                  /         \
              [ B ]         [ C ]  <-- Internal / Non-Leaf Nodes (Level 1)
             /     \           \
          [ D ]   [ E ]       [ F ] <-- Subtree Nodes (Level 2)
                 /     \
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
