# Graph Traversals (BFS & DFS)

**Q. Explain the two fundamental graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). Trace both algorithms on a sample graph, analyze their time and space complexities, and provide complete C implementations.**

---

> 📌 **Definition to Remember**
> **Graph Traversal** is the systematic process of visiting every vertex reachable from a starting source vertex in a graph without processing any vertex more than once. The two primary techniques are **Breadth-First Search (BFS)** using a FIFO Queue and **Depth-First Search (DFS)** using Recursion or a LIFO Stack.

---

### 1. Visual Trace Graph

```
Sample Graph:
         ( 0 )
        /     \
     ( 1 )   ( 2 )
     /   \     |
   ( 3 ) ( 4 ) ( 5 )
```

---

### 2. Breadth-First Search (BFS)

* **Strategy:** Explores neighbor vertices **level-by-level** before moving deeper, using a **FIFO Queue**.
* **Algorithm Steps:**
  1. Initialize a `visited[]` boolean array to all `false`.
  2. Enqueue the starting vertex $S$ into a Queue and mark `visited[S] = true`.
  3. While the Queue is not empty:
     * Dequeue front vertex $u$ and print/process it.
     * For each unvisited neighbor $v$ of $u$:
       * Mark `visited[v] = true`.
       * Enqueue $v$.
* **Traversal Trace from 0:**
  * Queue: `[0]` $\rightarrow$ Visit `0`, Enqueue `1, 2`.
  * Queue: `[1, 2]` $\rightarrow$ Visit `1`, Enqueue `3, 4`.
  * Queue: `[2, 3, 4]` $\rightarrow$ Visit `2`, Enqueue `5`.
  * Visits: `0 -> 1 -> 2 -> 3 -> 4 -> 5`
* **Key Application:** Finds the **Shortest Path** in unweighted graphs.

---

### 3. Depth-First Search (DFS)

* **Strategy:** Explores as deep as possible along each branch before **backtracking**, using **Recursion (or a Stack)**.
* **Algorithm Steps:**
  1. Initialize `visited[]` boolean array to `false`.
  2. Call recursive function `DFS(u)`:
     * Mark `visited[u] = true` and print $u$.
     * For each neighbor $v$ of $u$:
       * If `visited[v] == false`, recursively call `DFS(v)`.
* **Traversal Trace from 0:**
  * Visit `0` $\rightarrow$ Move to neighbor `1`.
  * Visit `1` $\rightarrow$ Move to neighbor `3`.
  * Visit `3` $\rightarrow$ Dead end, backtrack to `1`.
  * Move to neighbor `4` $\rightarrow$ Visit `4`. Backtrack to `0`.
  * Move to neighbor `2` $\rightarrow$ Visit `2`, Move to neighbor `5` $\rightarrow$ Visit `5`.
  * Visits: `0 -> 1 -> 3 -> 4 -> 2 -> 5`
* **Key Applications:** Cycle detection, Topological sorting, Connected components, Maze solving.

---

### 4. Complete Executable C Program for BFS & DFS

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

int adj[MAX][MAX];
bool visited[MAX];
int V = 6;

// 1. Breadth-First Search (BFS)
void BFS(int start) {
    int queue[MAX], front = 0, rear = 0;
    bool visitedBFS[MAX] = {false};

    visitedBFS[start] = true;
    queue[rear++] = start;

    printf("BFS Order: ");
    while (front < rear) {
        int u = queue[front++];
        printf("%d ", u);

        for (int v = 0; v < V; v++) {
            if (adj[u][v] == 1 && !visitedBFS[v]) {
                visitedBFS[v] = true;
                queue[rear++] = v;
            }
        }
    }
    printf("
");
}

// 2. Depth-First Search (DFS)
void DFS(int u) {
    visited[u] = true;
    printf("%d ", u);

    for (int v = 0; v < V; v++) {
        if (adj[u][v] == 1 && !visited[v]) {
            DFS(v);
        }
    }
}
```

---

### 5. Comprehensive Comparison: BFS vs. DFS

| Parameter | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Data Structure** | **FIFO Queue** | **LIFO Stack / System Call Recursion** |
| **Traversal Direction** | Level-by-level horizontally | Deep into branches vertically |
| **Time Complexity** | **$O(V + E)$** (Adjacency List) / $O(V^2)$ (Matrix) | **$O(V + E)$** (Adjacency List) / $O(V^2)$ (Matrix) |
| **Space Complexity** | **$O(V)$** (Queue holds entire level width) | **$O(V)$** (Stack holds recursion path depth) |
| **Shortest Path** | **Guaranteed shortest path** in unweighted graphs | Does not guarantee shortest path |
| **Primary Use Cases** | Shortest path, GPS navigation, peer-to-peer | Cycle detection, topological sort, maze solving |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Graph traversal visits every reachable node exactly once using a **`visited[]` array** to prevent infinite loops.
> 2. **BFS** explores level-by-level using a **FIFO Queue**.
> 3. **DFS** explores deeply along each branch using **Recursion / LIFO Stack** and backtracks.
> 4. Time complexity for both algorithms is **$O(V + E)$** using Adjacency List ($O(V^2)$ with Adjacency Matrix).
> 5. Space complexity for both is **$O(V)$** for visited tracking and queue/stack storage.
> 6. BFS guarantees the **shortest path in unweighted graphs**.
> 7. DFS is the foundation for **topological sorting and cycle detection**.

---

> ⚡ **Quick Recall**
> `Graph Traversal → Visited Array → BFS (Queue, Level-by-Level, Shortest Path) vs DFS (Stack/Recursion, Depth-First, Backtracking) → O(V + E) Complexity`
