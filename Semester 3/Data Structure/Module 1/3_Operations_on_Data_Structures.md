# Topic: Operations on Data Structures

**Q. Discuss the various fundamental operations that can be performed on data structures, explaining each with a suitable example.**

---

> 📌 **Definition to Remember**
> **Operations on Data Structures** are the fundamental actions performed to manipulate, store, and retrieve data. The six core operations are: **Traversal, Insertion, Deletion, Searching, Sorting, and Merging**. The choice of data structure directly determines the efficiency (time and space complexity) of these operations.

---

### The Six Fundamental Operations

| Operation | Definition | Example |
| :--- | :--- | :--- |
| **Traversal** | Visiting every element exactly once to process it | Printing all elements of an array |
| **Insertion** | Adding a new element to the data structure | Pushing a value onto a Stack |
| **Deletion** | Removing an existing element | Popping from a Stack, dequeuing from a Queue |
| **Searching** | Finding an element by its key value | Linear search, Binary search on an array |
| **Sorting** | Arranging elements in a specific order (asc/desc) | Bubble Sort, Quick Sort on an array |
| **Merging** | Combining two or more structures into one | Merging two sorted arrays into one sorted array |

### Traversal Algorithm Example (Array)
```text
Algorithm Traverse(A, N):
1. Set i = 0
2. Repeat while i < N:
3.     Print A[i]
4.     i = i + 1
5. Stop
```
*For A = [10, 20, 30], output: 10 → 20 → 30*

### Trade-offs Between Data Structures

| DS | Fast Operations | Slow Operations |
| :--- | :--- | :--- |
| **Array** | Searching (index-based, O(1)) | Insertion, Deletion (shifting, O(n)) |
| **Linked List** | Insertion, Deletion (O(1) at head) | Searching (O(n)) |
| **Stack/Queue** | Insert/Delete at ends (O(1)) | Searching middle elements (O(n)) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Six fundamental operations: **Traversal, Insertion, Deletion, Searching, Sorting, Merging**.
> 2. **Traversal**: visits each element exactly once — used for printing, processing.
> 3. **Insertion**: adds a new element; location depends on the DS type.
> 4. **Deletion**: removes an element; memory management of vacated space is required.
> 5. **Searching**: finds a specific element using its key (linear or binary search).
> 6. **Sorting**: arranges elements in order — ascending or descending.
> 7. **Merging**: combines two DS into one (e.g., merging two sorted arrays).

---

> ⚡ **Quick Recall**
> `Traversal (visit all) → Insertion (add) → Deletion (remove) → Searching (find by key) → Sorting (arrange in order) → Merging (combine structures)`
