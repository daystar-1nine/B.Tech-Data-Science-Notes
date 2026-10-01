# Graph Representations (Adjacency Matrix & Adjacency List)

**Q. Explain the two primary graph representations in computer memory: Adjacency Matrix and Adjacency List. Compare both representations across time and space complexities, and provide clean C code structures for both.**

---

> 📌 **Definition to Remember**
> **Graph Representations** are memory data structures used to store the vertices and edge connections of a graph in computer memory, primarily implemented as a 2D array (**Adjacency Matrix**) or an array of linked lists (**Adjacency List**).

---

### 1. Visual Graph Example

```
Sample Undirected Graph:
        ( 0 ) ------- ( 1 )
          |   \         |
          |     \       |
        ( 3 ) ------- ( 2 )
```

---

### 2. Adjacency Matrix Representation

A 2D array `adj[V][V]` of size $V \times V$, where:
* `adj[i][j] = 1` (or edge weight $w$) if an edge exists from vertex $i$ to vertex $j$.
* `adj[i][j] = 0` if no edge exists.
* For undirected graphs, the adjacency matrix is always **symmetric** about the main diagonal (`adj[i][j] == adj[j][i]`).

#### Adjacency Matrix for Sample Graph:
```
       0   1   2   3
   +-----------------
 0 |   0   1   1   1
 1 |   1   0   1   0
 2 |   1   1   0   1
 3 |   1   0   1   0
```

#### C Implementation:
```c
#define V 4
int adjMatrix[V][V] = {0};

void addEdgeMatrix(int u, int v) {
    adjMatrix[u][v] = 1;
    adjMatrix[v][u] = 1; // For undirected graph
}
```

---

### 3. Adjacency List Representation

An array of linked lists `adj[V]`, where each element `adj[i]` points to a singly linked list containing all neighboring vertices directly connected to vertex $i$.

#### Adjacency List for Sample Graph:
```
 [ 0 ] ---> [ 1 ] ---> [ 2 ] ---> [ 3 ] ---> NULL
 [ 1 ] ---> [ 0 ] ---> [ 2 ] ---> NULL
 [ 2 ] ---> [ 0 ] ---> [ 1 ] ---> [ 3 ] ---> NULL
 [ 3 ] ---> [ 0 ] ---> [ 2 ] ---> NULL
```

#### C Implementation:
```c
#include <stdio.h>
#include <stdlib.h>

struct AdjListNode {
    int dest;
    struct AdjListNode* next;
};

struct Graph {
    int numVertices;
    struct AdjListNode** adjLists;
};

struct Graph* createGraph(int vertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;
    graph->adjLists = (struct AdjListNode**)malloc(vertices * sizeof(struct AdjListNode*));
    for (int i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;
    return graph;
}

void addEdgeList(struct Graph* graph, int src, int dest) {
    // Add edge from src to dest
    struct AdjListNode* newNode = (struct AdjListNode*)malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    // Add edge from dest to src (undirected)
    newNode = (struct AdjListNode*)malloc(sizeof(struct AdjListNode));
    newNode->dest = src;
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}
```

---

### 4. Comprehensive Comparison Table

| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space Complexity** | **$O(V^2)$** (Fixed, large memory footprint) | **$O(V + E)$** (Dynamic, compact) |
| **Check Edge Existence $(u, v)$** | **$O(1)$** (Instant index lookup `adj[u][v]`) | **$O(\text{deg}(u))$** (Traverse linked list) |
| **Find All Neighbors of $u$** | **$O(V)$** (Must scan entire row) | **$O(\text{deg}(u))$** (Only iterate active neighbors) |
| **Add a Vertex** | **$O(V^2)$** (Requires reallocating 2D array) | **$O(1)$** (Append new pointer to array) |
| **Add an Edge** | **$O(1)$** | **$O(1)$** (Insert at head of list) |
| **Remove an Edge** | **$O(1)$** | **$O(\text{deg}(u))$** |
| **Ideal Graph Type** | **Dense Graphs** ($|E| \approx |V|^2$) | **Sparse Graphs** ($|E| \ll |V|^2$) |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. **Adjacency Matrix:** 2D array of size $V \times V$; entries are 1 (edge) or 0 (no edge).
> 2. Matrix space complexity is **$O(V^2)$**, wasting memory for sparse graphs.
> 3. Edge check `hasEdge(u, v)` is instant **$O(1)$** in adjacency matrix.
> 4. **Adjacency List:** Array of $V$ linked lists; space complexity is **$O(V + E)$**.
> 5. Finding all neighbors of vertex $u$ takes **$O(\text{deg}(u))$** in adjacency list.
> 6. Adjacency list is the industry standard for real-world **sparse graphs** (road networks, social graphs).
> 7. Adjacency matrix is preferred for **dense graphs** where fast edge lookup is critical.

---

> ⚡ **Quick Recall**
> `Adjacency Matrix (V x V 2D Array, O(V^2) Space, O(1) Edge Check, Dense Graphs) vs Adjacency List (Array of Linked Lists, O(V+E) Space, O(deg) Traversal, Sparse Graphs)`
