# Graph Introduction & Terminologies

**Q. Define a graph as an Abstract Data Type (ADT). Explain essential graph terminologies (vertices, edges, directed/undirected, in-degree, out-degree, path, cycle, connected, complete graph) with neat diagrams and state the Handshaking Lemma.**

---

> 📌 **Definition to Remember**
> A **Graph** is a non-linear data structure denoted as **$G = (V, E)$**, consisting of a non-empty finite set of **Vertices (Nodes) $V$** and a set of **Edges (Arcs) $E$** connecting pairs of vertices, representing many-to-many relationships between objects.

---

### 1. Graph Concept & Visual Structures

```
UNDIRECTED GRAPH:                     DIRECTED GRAPH (DIGRAPH):
     ( 1 ) -------- ( 2 )                  ( 1 ) ------> ( 2 )
       |     \        |                      |    \        |
       |       \      |                      |      \      v
       |         \    |                      v        v   ( 4 )
     ( 3 ) -------- ( 4 )                  ( 3 ) <------ ( 4 )
```

---

### 2. Core Graph Terminologies Explained

1. **Vertex (Node):** An individual entity or data element in the graph ($V$).
2. **Edge (Arc):** A link or pair $(u, v)$ connecting two vertices in the graph ($E$).
3. **Undirected Graph:** A graph where edges have no direction; connections are symmetric ($(u, v) = (v, u)$).
4. **Directed Graph (Digraph):** A graph where each edge has an assigned direction; represented as an ordered pair ($(u, v) \neq (v, u)$).
5. **Weighted Graph:** A graph where each edge is assigned a numerical cost, weight, or distance $w(u, v)$.
6. **Degree of a Vertex:**
   * **In Undirected Graph:** The total number of edges incident to that vertex.
   * **In Directed Graph:**
     * **In-Degree:** Number of edges directed **into** the vertex.
     * **Out-Degree:** Number of edges directed **out of** the vertex.
7. **Adjacent Vertices (Neighbors):** Two vertices connected directly by an edge.
8. **Path:** A sequence of alternating vertices and edges connecting a source vertex to a destination vertex.
9. **Cycle:** A closed path where the start vertex and end vertex are the same, with no edge repeated.
10. **Acyclic Graph:** A graph containing zero cycles (e.g., Trees, Directed Acyclic Graphs - DAG).
11. **Connected Graph (Undirected):** A graph where there exists at least one valid path between every pair of vertices.
12. **Strongly Connected Graph (Directed):** A digraph where there is a directed path from every vertex to every other vertex.
13. **Complete Graph ($K_n$):** A graph where every single vertex is connected to every other vertex by an edge.
14. **Sub-graph:** A graph $G' = (V', E')$ where $V' \subseteq V$ and $E' \subseteq E$.

---

### 3. The Handshaking Lemma

> **Handshaking Lemma:** In any undirected graph, the sum of degrees of all vertices is equal to **twice the number of edges**:
> $$\sum_{v \in V} \text{deg}(v) = 2 \times |E|$$

* **Crucial Consequence:** In any undirected graph, the **number of vertices with an ODD degree is ALWAYS EVEN**!

---

### 4. Maximum Edges Formula Comparison Table

| Graph Type | Vertices | Max Edges Formula | Complete Graph Example ($N=4$) |
| :--- | :---: | :---: | :---: |
| **Undirected Graph** | $N$ | $\mathbf{\frac{N(N - 1)}{2}}$ | $\frac{4 \times 3}{2} = \mathbf{6 \text{ edges}}$ |
| **Directed Graph** | $N$ | $\mathbf{N(N - 1)}$ | $4 \times 3 = \mathbf{12 \text{ edges}}$ |

* **Tree Relation:** A connected undirected graph with $N$ vertices and exactly **$N - 1$ edges** is a Tree.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Graph $G = (V, E)$ consists of vertices $V$ and connecting edges $E$.
> 2. Undirected edges are unordered pairs $(u, v)$; directed edges are ordered pairs $(u, v) \neq (v, u)$.
> 3. In directed graphs, **In-Degree** is incoming edges; **Out-Degree** is outgoing edges.
> 4. **Handshaking Lemma:** $\sum \text{deg}(v) = 2|E|$; odd-degree vertices must be even in number.
> 5. Max edges in undirected graph = **$N(N-1)/2$**; in directed graph = **$N(N-1)$**.
> 6. An undirected graph is **Connected** if a path exists between all pairs; directed is **Strongly Connected**.
> 7. A connected acyclic graph with $N-1$ edges is a tree.

---

> ⚡ **Quick Recall**
> `Graph G=(V, E) → Undirected vs Directed → In/Out Degree → Handshaking Lemma (Sum deg = 2|E|) → Path & Cycle → Complete Graph (N(N-1)/2)`
