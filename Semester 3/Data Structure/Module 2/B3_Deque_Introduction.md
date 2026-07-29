# Introduction to Double-Ended Queue (Deque)

**Q. What is a Double-Ended Queue (Deque)? Explain its types and how it differs from a standard queue and stack. Provide real-world applications.**

---

> 📌 **Definition to Remember**
> A **Double-Ended Queue (Deque)** is a generalized linear data structure where insertion and deletion of elements can be performed at **both ends** (Front and Rear). It effectively combines the capabilities of both a Stack (LIFO) and a Queue (FIFO) into a single versatile structure.

---

### 1. Operations in a Deque
Unlike standard queues (insert Rear, delete Front) or stacks (insert Top, delete Top), a Deque supports **four primary operations**:
1. Insert at Front
2. Insert at Rear
3. Delete at Front
4. Delete at Rear

**Visual Representation:**
```text
  Insert/Delete                      Insert/Delete
       <---> [ E1 | E2 | E3 | E4 ] <--->
       Front                      Rear
```

### 2. Types of Restricted Deques
To enforce specific behaviors, Deques are classified into two restricted variants:

| Type | Restriction | Allowed Operations |
| :--- | :--- | :--- |
| **Input Restricted Deque** | Insertion limited to ONE end | Insert (Rear only)<br>Delete (Front & Rear) |
| **Output Restricted Deque**| Deletion limited to ONE end | Delete (Front only)<br>Insert (Front & Rear) |

### 3. Comparison with Stack and Queue

| Data Structure | Insertion Point | Deletion Point | Principle |
| :--- | :--- | :--- | :--- |
| **Stack** | Top | Top | LIFO |
| **Standard Queue** | Rear | Front | FIFO |
| **Deque** | **Front & Rear** | **Front & Rear** | Both |

### 4. Real-World Applications
* **Web Browser History:** When navigating back and forth, URLs are added/removed from one end. If history exceeds the max limit, oldest URLs are dropped from the other end.
* **Undo/Redo Operations:** Text editors use deques to maintain action histories.
* **Multiprocessor Scheduling (Work-Stealing):** If one processor finishes its own tasks, it can "steal" work from the rear of another busy processor's deque.
* **Palindrome Checking:** Reading a string simultaneously from the front and rear is efficiently handled by a Deque.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A Deque allows insertion and deletion at **both ends** (Front and Rear).
> 2. It combines the functionality of both Stacks and Queues.
> 3. Four main operations: Insert Front, Insert Rear, Delete Front, Delete Rear.
> 4. **Input Restricted Deque**: insertion at one end only, deletion at both.
> 5. **Output Restricted Deque**: deletion at one end only, insertion at both.
> 6. A standard queue restricts insertion to rear and deletion to front.
> 7. Key applications include Web Browser History, Undo/Redo, and the Work-Stealing scheduling algorithm.

---

> ⚡ **Quick Recall**
> `Deque → Insert/Delete at BOTH ends → Input Restricted (Insert 1 end) → Output Restricted (Delete 1 end) → Apps: Browser History, Undo/Redo, Work-Stealing`
