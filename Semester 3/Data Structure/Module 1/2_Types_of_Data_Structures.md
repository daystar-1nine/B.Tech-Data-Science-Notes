# Types of Data Structures: Linear & Non-Linear

**Q. Classify Data Structures into Linear and Non-Linear types. Differentiate between them and provide examples of each.**

---

> 📌 **Definition to Remember**
> A **Data Structure** is a specialized format for organizing, processing, retrieving, and storing data. Based on how elements are arranged, data structures are classified into **Linear** (elements in sequential order) and **Non-Linear** (elements arranged hierarchically or in a network).

---

### 1. Linear Data Structures
* Elements are arranged in **sequential order** — each element has a unique predecessor and successor.
* Can be **traversed in a single run**.
* Memory is usually allocated in **contiguous blocks** (arrays) or nodes (linked lists).

**Examples:**

| DS | Description |
| :--- | :--- |
| **Array** | Contiguous memory block, same data type, index-based access |
| **Linked List** | Chain of nodes; each node points to the next |
| **Stack** | Follows **LIFO** (Last In, First Out) principle |
| **Queue** | Follows **FIFO** (First In, First Out) principle |

### 2. Non-Linear Data Structures
* Elements are arranged in a **hierarchical or network** structure.
* One element can be connected to **multiple other elements**.
* Traversal requires **multiple paths or recursive algorithms**.

**Examples:**

| DS | Description |
| :--- | :--- |
| **Tree** | Hierarchical structure with a root node and child nodes |
| **Graph** | Network of **vertices (nodes)** and **edges** — no strict hierarchy |

### 3. Linear vs Non-Linear Comparison

| Feature | Linear | Non-Linear |
| :--- | :--- | :--- |
| **Arrangement** | Sequential order | Hierarchical / network |
| **Traversal** | Single run | Multiple paths / recursion |
| **Memory** | Often less efficient | More efficient (dynamic allocation) |
| **Implementation** | Simpler | More complex |
| **Levels** | Single level | Multi-level |
| **Examples** | Array, Stack, Queue, Linked List | Tree, Graph |

```
  LINEAR:    [A] → [B] → [C] → [D]

  NON-LINEAR (Tree):
          [A]
         /   \
       [B]   [C]
      /   \
    [D]   [E]
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Data structures are classified into **Linear** (sequential) and **Non-Linear** (hierarchical/network).
> 2. Linear DS: elements arranged sequentially — each has one predecessor and one successor.
> 3. Linear examples: **Array, Linked List, Stack (LIFO), Queue (FIFO)**.
> 4. Non-Linear DS: elements connected to multiple others — Tree and Graph.
> 5. Linear DS can be traversed in a single run; Non-Linear requires multiple paths.
> 6. Non-Linear DS uses memory more efficiently via dynamic allocation.
> 7. Trees are used in database indexing; Graphs are used in route planning and AI.

---

> ⚡ **Quick Recall**
> `Linear (sequential, single run) → Array, Linked List, Stack (LIFO), Queue (FIFO) → Non-Linear (hierarchical/network, multi-path) → Tree, Graph → Non-Linear: efficient memory, complex traversal`
