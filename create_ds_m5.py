import os

DS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Data Structure"

m5_dir = os.path.join(DS_DIR, "Module 5")
m5_qa = os.path.join(m5_dir, "Module_5_QA")

os.makedirs(m5_dir, exist_ok=True)
os.makedirs(m5_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 5: GRAPHS
# --------------------------------------------------------------------------

m5_files = {
    "1_Graph_Introduction_and_Terminologies.md": """# Graph Introduction & Terminologies — Data Structures

> **Definition:** A **Graph** is a non-linear data structure denoted as $G = (V, E)$, consisting of a non-empty finite set of **Vertices (Nodes)** $V$ and a set of **Edges (Arcs)** $E$ connecting pairs of vertices.

---

## 1. Detailed Technical Explanation

```
UNDIRECTED GRAPH:                     DIRECTED GRAPH (DIGRAPH):
     ( 1 ) -------- ( 2 )                  ( 1 ) ------> ( 2 )
       |     \\        |                      |    \\        |
       |       \\      |                      |      \\      v
       |         \\    |                      v        v   ( 4 )
     ( 3 ) -------- ( 4 )                  ( 3 ) <------ ( 4 )
```

### Core Graph Terminologies:
1. **Vertex (Node):** An individual data point or entity in the graph.
2. **Edge (Arc):** A link or line connecting two vertices $(u, v)$.
3. **Directed Graph (Digraph):** A graph where edges have a defined direction (ordered pair $(u, v) \ne (v, u)$).
4. **Undirected Graph:** A graph where edges are bidirectional and symmetric ($(u, v) = (v, u)$).
5. **Weighted Graph:** A graph where each edge is assigned a numerical cost, distance, or weight $w(u, v)$.
6. **Degree of a Vertex:**
   - **In Undirected Graphs:** The total number of edges connected to that vertex.
   - **In Directed Graphs:**
     - **In-Degree:** Number of edges directed *into* the vertex.
     - **Out-Degree:** Number of edges directed *out of* the vertex.
7. **Handshaking Lemma:** In any undirected graph, the sum of degrees of all vertices equals twice the number of edges:
   ```
   Sum of Deg(v) = 2 * |E|
   ```
8. **Adjacent Vertices (Neighbors):** Two vertices connected directly by an edge.
9. **Path:** A sequence of alternating vertices and edges connecting a source vertex to a destination vertex.
10. **Cycle:** A closed path where the start vertex and end vertex are the same, with no edge repeated.
11. **Acyclic Graph:** A graph containing zero cycles (e.g., Trees, Directed Acyclic Graphs - DAG).
12. **Connected Graph (Undirected):** A graph where there exists at least one path between every pair of vertices.
13. **Strongly Connected Graph (Directed):** A digraph where there is a directed path from every vertex to every other vertex.
14. **Complete Graph (Kn):** A graph where every vertex is connected to every other vertex. Number of edges in $K_n$:
    ```
    |E| = n * (n - 1) / 2
    ```

---

## 2. Memory Keywords & Properties
- **Vertices & Edges:** $G = (V, E)$.
- **Handshaking Lemma:** $\sum \text{deg}(v) = 2|E|$ (Total odd degree vertices is always EVEN).
- **Dense vs Sparse Graph:** Dense when $|E| \approx |V|^2$; Sparse when $|E| \approx |V|$.

---

## 3. Must-Write Points for Exams
- In an undirected complete graph with $N$ vertices, the maximum number of edges is $N(N - 1) / 2$.
- In a directed complete graph with $N$ vertices, the maximum number of edges is $N(N - 1)$.
- Trees are a special type of connected, acyclic undirected graph with $N - 1$ edges.

---

## 4. Quick Recall Flow
```
G = (V, E) -> Directed vs Undirected -> In/Out Degree -> Handshaking Lemma (Sum Deg = 2E) -> Complete Graph E = N(N-1)/2
```
""",

    "2_Graph_Representations.md": """# Graph Representations (Adjacency Matrix & Adjacency List) — Data Structures

> **Definition:** Graph representations are memory data structures used to store the vertices and edge relationships of a graph in computer memory. The two primary methods are **Adjacency Matrix** and **Adjacency List**.

---

## 1. Detailed Technical Explanation

```
Sample Graph:
        (0) ---- (1)
         |  \\     |
         |    \\   |
        (3) ---- (2)
```

### 1. Adjacency Matrix Representation
A 2D array `adj[V][V]` of size $V \times V$, where `adj[i][j] = 1` if an edge exists from vertex `i` to vertex `j`, and `0` otherwise.

#### Adjacency Matrix for Sample Graph:
```
       0   1   2   3
   +-----------------
 0 |   0   1   1   1
 1 |   1   0   1   0
 2 |   1   1   0   1
 3 |   1   0   1   0
```
- **Pros:** Fast edge existence query in $O(1)$ time (`adj[u][v] == 1`).
- **Cons:** High memory footprint $O(V^2)$, inefficient for sparse graphs.

---

### 2. Adjacency List Representation
An array of linked lists `adj[V]`, where each element `adj[i]` points to a linked list of neighboring vertices connected to vertex `i`.

#### Adjacency List for Sample Graph:
```
[0] -> [1] -> [2] -> [3] -> NULL
[1] -> [0] -> [2] -> NULL
[2] -> [0] -> [1] -> [3] -> NULL
[3] -> [0] -> [2] -> NULL
```
- **Pros:** Memory efficient $O(V + E)$ for sparse graphs; iterates over neighbors in $O(\text{deg}(u))$ time.
- **Cons:** Checking edge existence between $u$ and $v$ takes $O(\text{deg}(u))$ time.

---

## 2. Complete Comparison Table

| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space Complexity** | $O(V^2)$ (Fixed) | $O(V + E)$ (Dynamic) |
| **Check Edge $(u, v)$** | **$O(1)$** (Instant index lookup) | $O(\text{deg}(u))$ (List traversal) |
| **Find All Neighbors** | $O(V)$ (Scan row) | **$O(\text{deg}(u))$** (Traverse list) |
| **Add / Delete Vertex** | $O(V^2)$ (Resize matrix) | $O(1)$ (Append list head) |
| **Best Suited For** | **Dense Graphs** ($|E| \approx |V|^2$) | **Sparse Graphs** ($|E| \ll |V|^2$) |

---

## 3. C Implementation of Adjacency List

```c
#include <stdio.h>
#include <stdlib.h>

struct AdjListNode {
    int dest;
    struct AdjListNode* next;
};

struct Graph {
    int V;
    struct AdjListNode** array;
};

struct Graph* createGraph(int V) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->V = V;
    graph->array = (struct AdjListNode**)malloc(V * sizeof(struct AdjListNode*));
    for (int i = 0; i < V; ++i)
        graph->array[i] = NULL;
    return graph;
}

void addEdge(struct Graph* graph, int src, int dest) {
    // Add edge from src to dest
    struct AdjListNode* newNode = (struct AdjListNode*)malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->next = graph->array[src];
    graph->array[src] = newNode;

    // For undirected graph, add dest to src
    newNode = (struct AdjListNode*)malloc(sizeof(struct AdjListNode));
    newNode->dest = src;
    newNode->next = graph->array[dest];
    graph->array[dest] = newNode;
}
```

---

## 4. Must-Write Points for Exams
- In an undirected graph's adjacency matrix, the matrix is always **symmetric** about the main diagonal (`adj[i][j] == adj[j][i]`).
- Adjacency list saves significant memory when representing real-world sparse networks (road maps, web pages, social graphs).

---

## 5. Quick Recall Flow
```
Adj Matrix: 2D Array V x V, O(V^2) Space, O(1) Edge Lookup | Adj List: Array of Linked Lists, O(V+E) Space, Best for Sparse Graphs
```
""",

    "3_Graph_Traversals_BFS_and_DFS.md": """# Graph Traversals (BFS & DFS) — Data Structures

> **Definition:** **Graph Traversal** is the process of visiting all vertices reachable from a starting vertex in a graph. The two fundamental search algorithms are **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

---

## 1. Detailed Technical Explanation

```
Sample Graph:
         ( 0 )
        /     \\
     ( 1 )   ( 2 )
     /   \\     |
   ( 3 ) ( 4 ) ( 5 )
```

### 1. Breadth-First Search (BFS)
- **Strategy:** Explores neighbor vertices level-by-level using a **FIFO Queue**.
- **Algorithm:**
  1. Initialize a `visited[]` boolean array to `false`.
  2. Enqueue the starting vertex `S` and mark `visited[S] = true`.
  3. While Queue is not empty:
     - Dequeue front vertex `u` and process/print it.
     - For each unvisited neighbor `v` of `u`: Mark `visited[v] = true` and enqueue `v`.
- **Traversal Order from 0:** `0 -> 1 -> 2 -> 3 -> 4 -> 5`
- **Applications:** Shortest path in unweighted graphs, Web crawlers, Peer-to-peer networks.

---

### 2. Depth-First Search (DFS)
- **Strategy:** Explores as deep as possible along each branch before **backtracking**, using **Recursion or a Stack**.
- **Algorithm:**
  1. Mark starting vertex `u` as `visited[u] = true` and print `u`.
  2. For each neighbor `v` of `u`:
     - If `v` is not visited, recursively call `DFS(v)`.
- **Traversal Order from 0:** `0 -> 1 -> 3 -> 4 -> 2 -> 5`
- **Applications:** Topological sorting, Cycle detection, Finding connected components, Maze solving.

---

## 2. Complete Executable C Program for BFS & DFS

```c
#include <stdio.h>
#include <stdlib.h>
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

    printf("BFS Traversal: ");
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
    printf("\\n");
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

int main() {
    // Construct edges for sample graph
    adj[0][1] = adj[1][0] = 1;
    adj[0][2] = adj[2][0] = 1;
    adj[1][3] = adj[3][1] = 1;
    adj[1][4] = adj[4][1] = 1;
    adj[2][5] = adj[5][2] = 1;

    BFS(0);

    for (int i = 0; i < V; i++) visited[i] = false;
    printf("DFS Traversal: ");
    DFS(0);
    printf("\\n");

    return 0;
}
```

---

## 3. Comparison of BFS and DFS

| Feature | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Data Structure** | **FIFO Queue** | **Call Stack / Recursion** |
| **Search Pattern** | Level-by-level exploration | Branch-by-branch deep dive |
| **Time Complexity** | $O(V + E)$ (using Adj List) | $O(V + E)$ (using Adj List) |
| **Space Complexity** | $O(V)$ (queue size) | $O(V)$ (recursion stack height) |
| **Shortest Path** | Guarantees shortest path in unweighted graph | Does not guarantee shortest path |

---

## 4. Quick Recall Flow
```
BFS -> Queue FIFO (Level-by-Level) -> Shortest Path | DFS -> Stack / Recursion (Deep Dive + Backtrack) -> Cycle Detection
```
""",

    "4_Self_Learning_Graph_Application_Topological_Sorting.md": """# Self-Learning: Topological Sorting — Data Structures

> **Definition:** **Topological Sorting** of a **Directed Acyclic Graph (DAG)** is a linear ordering of vertices such that for every directed edge $(u, v)$, vertex $u$ comes strictly **before** vertex $v$ in the ordering.

---

## 1. Detailed Technical Explanation

```
Sample DAG (Task Dependencies):
        ( 5 ) ----> ( 0 ) <---- ( 4 )
          |                       |
          v                       v
        ( 2 ) ----> ( 3 ) ----> ( 1 )

Valid Topological Orders:
- 5 -> 4 -> 2 -> 3 -> 1 -> 0
- 4 -> 5 -> 2 -> 3 -> 1 -> 0
- 5 -> 2 -> 3 -> 4 -> 1 -> 0
```

### Key Conditions:
1. Topological sorting is defined **ONLY for DAGs** (Directed Acyclic Graphs).
2. If a graph contains a **cycle**, topological sorting is **IMPOSSIBLE** because circular dependencies cannot be resolved linearly.

---

## 2. Algorithms for Topological Sorting

### 1. Kahn's Algorithm (BFS In-Degree Approach)
1. Compute the **In-Degree** of every vertex in the graph.
2. Push all vertices with **In-Degree = 0** into a Queue.
3. While Queue is not empty:
   - Dequeue front vertex `u`, append `u` to topological order.
   - For each neighbor `v` of `u`: Decrement `in_degree[v]--`.
   - If `in_degree[v] == 0`: Enqueue `v`.
4. If output order length $< |V|$, the graph contains a **Cycle**!

### 2. DFS with Stack Approach
1. Initialize a `visited[]` boolean array.
2. For every unvisited vertex `u`, call recursive `topoDFS(u)`.
3. In `topoDFS(u)`:
   - Mark `u` as visited.
   - Recursively call `topoDFS(v)` for all unvisited neighbors `v`.
   - After visiting all children, **push `u` onto a Stack**.
4. Pop elements from the Stack to obtain the topological ordering.

---

## 3. Real-World Applications
- **Build Systems (Make, Gradle, Webpack):** Resolving source code compilation dependencies.
- **Task Scheduling:** Determining valid execution order for tasks with prerequisites.
- **Package Managers (apt, pip, npm):** Installing package dependency chains.
- **Course Prerequisite Planning:** Academic curriculum scheduling.

---

## 4. Quick Recall Flow
```
DAG Only -> In-Degree = 0 Enqueue -> Decrement Neighbors -> Repeat -> Linear Dependency Order (Kahn's Algorithm)
```
"""
}

# Write Module 5 files
for fname, content in m5_files.items():
    with open(os.path.join(m5_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Data Structure Module 5 Files!")
