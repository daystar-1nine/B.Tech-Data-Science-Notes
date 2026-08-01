# Queue ADT, Operations & Array Implementation

**Q. Define Queue as an Abstract Data Type (ADT). Explain its standard operations and demonstrate its implementation using an Array with a relevant code snippet.**

---

> 📌 **Definition to Remember**
> A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle — the first element inserted is the first to be removed. Insertions occur at the **Rear** (Tail) and deletions occur at the **Front** (Head).

---

### 1. Queue as an ADT
As an Abstract Data Type, a Queue manages a collection of elements and restricts access to two specific ends:
* **Rear:** Where elements are added (enqueued).
* **Front:** Where elements are removed (dequeued).

### 2. Standard Operations

| Operation | Description | Condition |
| :--- | :--- | :--- |
| **enqueue(element)** | Adds an element to the Rear | **Queue Overflow** if full |
| **dequeue()** | Removes and returns element from Front | **Queue Underflow** if empty |
| **peek() / front()** | Returns Front element without removing | Underflow if empty |
| **isEmpty()** | Returns True if queue has no elements | `front == -1` |
| **isFull()** | Returns True if queue is at max capacity | `rear == SIZE - 1` |

### 3. Array Implementation in C
Two pointers (`front` and `rear`) are initialized to `-1`.

```c
#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int value) {
    if (rear == SIZE - 1) {
        printf("Queue Overflow!\n");
    } else {
        if (front == -1) front = 0; // Set front on first insertion
        queue[++rear] = value;
    }
}

int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue Underflow!\n");
        return -1;
    } else {
        int val = queue[front++];
        // Reset pointers if queue becomes empty
        if (front > rear) front = rear = -1;
        return val;
    }
}
```

### 4. Advantages and Limitations
* **Advantage:** Array implementation is simple and fast (O(1) time complexity for enqueue/dequeue).
* **Applications:** OS Scheduling (FCFS), IO Buffering (keyboard/printers).
* **Disadvantage (Memory Wastage):** In a simple linear queue, if `rear` reaches the end, we cannot insert new elements — even if spaces at the front were freed by `dequeue()`. *(This is solved by Circular Queues).*

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Queue follows the **FIFO (First In, First Out)** principle.
> 2. Elements are inserted at the **Rear** and removed from the **Front**.
> 3. Core operations: **enqueue (insert)** and **dequeue (remove)**.
> 4. `Queue Overflow` occurs if enqueue is called when full (`rear == SIZE - 1`).
> 5. `Queue Underflow` occurs if dequeue is called when empty (`front == -1`).
> 6. In array implementation, two pointers are maintained: `front` and `rear`, both initialized to -1.
> 7. Linear array queues waste memory — empty front spaces cannot be reused once rear hits the end.

---

> ⚡ **Quick Recall**
> `Queue → FIFO → Insert at Rear (enqueue) → Remove from Front (dequeue) → Overflow (rear==SIZE-1) → Underflow (front==-1) → Linear array wastes freed memory`
