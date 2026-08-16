# Graph Introduction & Terminologies — Data Structures

> **Definition:** A **Graph** is a non-linear data structure denoted as **G = (V, E)**, consisting of a non-empty finite set of **Vertices (Nodes) V** and a set of **Edges (Arcs) E** connecting pairs of vertices.

---

## 1. Detailed Technical Explanation

```
UNDIRECTED GRAPH:                     DIRECTED GRAPH (DIGRAPH):
     ( 1 ) -------- ( 2 )                  ( 1 ) ------> ( 2 )
       |     \        |                      |    \        |
       |       \      |                      |      \      v
       |         \    |                      v        v   ( 4 )
     ( 3 ) -------- ( 4 )                  ( 3 ) <------ ( 4 )
```

### Core Graph Terminologies:
1. **Vertex (Node):** An individual data point or entity in the graph.
2. **Edge (Arc):** A link or line connecting two vertices **(u, v)**.
3. **Directed Graph (Digraph):** A graph where edges have a defined direction (ordered pair $(u, v) 
e (v, u)$).
4. **Undirected Graph:** A graph where edges are bidirectional and symmetric (**(u, v) = (v, u)**).
5. **Weighted Graph:** A graph where each edge is assigned a numerical cost, distance, or weight **w(u, v)**.
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
14. **Complete Graph (Kn):** A graph where every vertex is connected to every other vertex. Number of edges in **K_n**:
    ```
    |E| = n * (n - 1) / 2
    ```

---

## 2. Memory Keywords & Properties
- **Vertices & Edges: G = (V, E)**.
- **Handshaking Lemma: Sum deg(v) = 2|E|** (Total odd degree vertices is always EVEN).
- **Dense vs Sparse Graph:** Dense when **|E| pprox |V|^2**; Sparse when **|E| pprox |V|**.

---

## 3. Must-Write Points for Exams
- In an undirected complete graph with **N** vertices, the maximum number of edges is **N(N - 1) / 2**.
- In a directed complete graph with **N** vertices, the maximum number of edges is **N(N - 1)**.
- Trees are a special type of connected, acyclic undirected graph with **N - 1** edges.

---

## 4. Quick Recall Flow
```
G = (V, E) -> Directed vs Undirected -> In/Out Degree -> Handshaking Lemma (Sum Deg = 2E) -> Complete Graph E = N(N-1)/2
```
