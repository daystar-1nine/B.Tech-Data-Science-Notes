# Introduction to B-Tree & B+ Tree — Data Structures

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
                   /      |      \
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
                        /      \
               [ 10 | 20 ]    [ 40 | 50 ]  <-- Internal Index Nodes
              /     |     \   /     |     \
            [L1] <-> [L2] <-> [L3] <-> [L4] <-- Leaves (Contain Data Pointers + Linked List)
```

### Detailed Comparison Table:
| Feature | B-Tree | B+ Tree |
| :--- | :--- | :--- |
| **Data Storage** | Data stored in internal & leaf nodes. | Data stored ONLY in leaf nodes. |
| **Search Efficiency** | Search may finish early at internal nodes. | Search always goes down to leaf nodes (**O(\log N)** uniform). |
| **Range Queries** | Inefficient (requires in-order tree traversal). | **Extremely Fast** (traverse sequential linked list of leaves). |
| **Node Capacity** | Fewer keys per disk block due to data pointers. | More keys per block (higher fanout, smaller tree height). |
| **Applications** | File systems, database core storage. | Relational Database Indexing (MySQL InnoDB, Oracle, Db2). |

---

## 3. Core Concepts & Memory Keywords
- **Order m:** Maximum number of children a node can have.
- **Fanout:** Number of branch pointers per index node (high fanout reduces disk I/O).
- **Sequential Leaf Chaining:** Doubly linked leaf nodes enabling **O(K)** range queries (`WHERE age BETWEEN 20 AND 30`).

---

## 4. Must-Write Points for Exams
- B-Trees and B+ Trees reduce disk I/O by fitting large numbers of keys inside a single disk page block (e.g., 4KB or 8KB).
- B+ Trees are preferred over B-Trees for database indexes because leaf chaining enables fast range searches and higher fanout.

---

## 5. Quick Recall Flow
```
Multi-Way Search Tree -> B-Tree (Data in all nodes) vs B+ Tree (Data only in linked leaves + High Fanout for DB Indexing)
```
