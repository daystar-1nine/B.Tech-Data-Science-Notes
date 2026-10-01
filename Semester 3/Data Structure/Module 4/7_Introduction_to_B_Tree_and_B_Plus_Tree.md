# Introduction to B-Tree & B+ Tree

**Q. What is a B-Tree of order $m$? State its structural properties. Explain the differences between a B-Tree and a B+ Tree with diagrams, and explain why B+ Trees are preferred for database indexing.**

---

> 📌 **Definition to Remember**
> A **B-Tree** is a self-balancing multi-way search tree of order $m$ where each node can contain multiple keys and more than two children, designed specifically to optimize **disk read/write block transfers** by matching tree node sizes to physical disk block sizes.

---

### 1. Structural Properties of a B-Tree of Order $m$

1. **Max Children:** Every node has at most $m$ children.
2. **Min Children (Internal Nodes):** Every internal node (except the root) has at least $\lceil m / 2 \rceil$ children.
3. **Root Property:** The root has at least 2 children (unless it is a leaf).
4. **Key-to-Child Rule:** A node with $k$ children contains exactly **$k - 1$ sorted keys**.
5. **Leaf Level Uniformity:** **All leaf nodes reside at the exact same physical depth**, ensuring perfect tree balance.

```
Sample B-Tree of Order 3:
                     [ 20 | 50 ]
                   /      |      \
        [ 10 ]        [ 30 | 40 ]     [ 60 | 70 ]
```

---

### 2. B-Tree vs. B+ Tree Structural Comparison

```
B-TREE:
- Keys AND actual record data pointers are stored in BOTH internal and leaf nodes.

B+ TREE:
- Internal nodes store ONLY routing index keys (no data pointers).
- ALL satellite data records / pointers reside EXCLUSIVELY in the leaf nodes.
- ALL leaf nodes are linked sequentially as a DOUBLY LINKED LIST for range scans!
```

```
B+ TREE ARCHITECTURE:
                         [ 30 ]  <-- Internal Index Node (Routing Key Only)
                        /      \
               [ 10 | 20 ]    [ 40 | 50 ]  <-- Internal Index Nodes
              /     |     \   /     |     \
            [L1] <-> [L2] <-> [L3] <-> [L4] <-- Leaves (Contain Data Pointers + Linked List)
             |        |        |        |
         [Data1]   [Data2]  [Data3]  [Data4]
```

---

### 3. Detailed Comparison Table: B-Tree vs. B+ Tree

| Feature | B-Tree | B+ Tree |
| :--- | :--- | :--- |
| **Data Storage Location** | Stored in **both internal and leaf nodes** | Stored **ONLY in leaf nodes** |
| **Search Performance** | Search may terminate early at internal node | Search **always descends to leaf** ($O(\log N)$ uniform) |
| **Sequential Range Queries**| **Inefficient** (requires in-order tree traversal) | **Extremely Fast** (sequential scan via leaf linked list) |
| **Node Key Capacity** | Lower (data pointers take space in every node) | **Higher fanout** (internal nodes hold only keys) |
| **Tree Height** | Taller for the same number of records | **Shorter / Flatter** (due to higher fanout) |
| **Disk Block I/O Cost** | Higher I/O per query | **Minimal Disk I/O** |
| **Leaf Interconnection** | Leaves are isolated | **Leaves linked as Doubly Linked List** |
| **Primary Application** | Operating system file systems (ext4, NTFS) | **Relational Database Indexes** (InnoDB, PostgreSQL) |

---

### 4. Why B+ Trees are Preferred for Database Indexing

1. **Higher Fanout & Shallower Tree:** Because internal nodes store only search keys (without bulky data records), a single 4 KB disk block can hold hundreds of keys. This creates a massive branch factor (fanout), reducing tree height to just 3 or 4 levels for millions of records ($3 - 4$ disk I/Os per lookup!).
2. **Superior Range Queries (`BETWEEN` Clauses):** In SQL, queries like `WHERE age BETWEEN 20 AND 30` find the first leaf node `20` in $O(\log N)$ time, and then traverse the doubly linked list of leaves directly in **$O(K)$ linear time** without returning up the tree!

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. B-Tree of order $m$: Nodes have at most $m$ children, at least $\lceil m / 2 \rceil$ children (except root).
> 2. All leaves in a B-Tree / B+ Tree appear at the **exact same physical depth**.
> 3. In B-Trees, data is stored in both internal and leaf nodes.
> 4. In B+ Trees, data is stored **exclusively in leaf nodes**; internal nodes hold only routing keys.
> 5. **B+ Tree leaves are linked sequentially as a linked list**, enabling rapid range queries.
> 6. B+ Trees have higher fanout and shallower height, drastically minimizing disk block I/O reads.
> 7. B+ Trees form the standard indexing engine for MySQL InnoDB, Oracle, and Microsoft SQL Server.

---

> ⚡ **Quick Recall**
> `B-Tree (Order m, Data in All Nodes) vs B+ Tree (Data ONLY in Leaves, Higher Fanout, Flatter Tree, Linked Leaves for Range Queries) → Preferred in Database Indexing`
