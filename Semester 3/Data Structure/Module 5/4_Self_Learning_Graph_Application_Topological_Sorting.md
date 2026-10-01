# Topological Sorting & Applications

**Q. What is Topological Sorting? Explain why it is applicable only to Directed Acyclic Graphs (DAGs). Explain Kahn's Algorithm (BFS based) and the DFS-based algorithm for topological sorting with step-by-step examples.**

---

> 📌 **Definition to Remember**
> **Topological Sorting** of a **Directed Acyclic Graph (DAG)** is a linear ordering of its vertices such that for every directed edge $(u, v)$, vertex $u$ appears strictly **before** vertex $v$ in the ordering. It models precedence constraints where task $u$ must be finished before task $v$ can begin.

---

### 1. The DAG Requirement: Why Cycles Make It Impossible

```
VALID DAG (Topological Sort Possible):       CYCLIC GRAPH (Topological Sort IMPOSSIBLE!):
       ( 1 ) --------> ( 2 )                        ( 1 ) --------> ( 2 )
         |               |                            ^               |
         v               v                            |               v
       ( 3 ) --------> ( 4 )                        ( 4 ) <-------- ( 3 )
    Valid Order: 1 -> 3 -> 2 -> 4                   (Circular dependency deadlock!)
```

* **Why DAG Only?**
  * If a graph contains a cycle ($A \rightarrow B \rightarrow C \rightarrow A$), $A$ must precede $B$, $B$ must precede $C$, and $C$ must precede $A$—creating a logical contradiction that cannot be linearized!
  * Every valid DAG has **at least one vertex with in-degree = 0** and **at least one vertex with out-degree = 0**.

---

### 2. Kahn's Algorithm (BFS In-Degree Approach)

Kahn's algorithm repeatedly removes vertices that have no prerequisites (in-degree = 0):

```
Algorithm: Kahn_Topological_Sort(Graph)
1. Compute the In-Degree of every vertex in the graph.
2. Initialize an empty Queue.
3. Enqueue all vertices with In-Degree = 0.
4. Initialize count = 0.
5. While Queue is not empty:
     a. Dequeue front vertex u, add u to topological order list, count++.
     b. For each outgoing neighbor v of u:
        - Decrement in_degree[v]--
        - If in_degree[v] == 0:
            Enqueue v.
6. Cycle Check:
   If count != |V|:
     Output: "Graph contains a CYCLE! Topological sort impossible."
   Else:
     Output: Topological order list.
```

---

### 3. DFS with Stack Approach

```
Algorithm: DFS_Topological_Sort(Graph)
1. Initialize visited[] = false for all vertices.
2. Initialize an empty Stack.
3. For each vertex u from 0 to V - 1:
     If visited[u] == false:
       topoDFS(u, visited, Stack)
4. Pop and print all elements from the Stack to get the topological order.

Function topoDFS(u, visited, Stack):
1. Mark visited[u] = true.
2. For each neighbor v of u:
     If visited[v] == false:
       topoDFS(v, visited, Stack)
3. Push u onto Stack (Pushed AFTER all its descendants are processed!).
```

---

### 4. Step-by-Step Worked Example (Kahn's Algorithm)

```
Sample DAG:
       ( 5 ) ----> ( 0 ) <---- ( 4 )
         |                       |
         v                       v
       ( 2 ) ----> ( 3 ) ----> ( 1 )
```

#### In-Degree Table:
* $V_0: 2$, $V_1: 2$, $V_2: 1$, $V_3: 1$, $V_4: 0$, $V_5: 0$

#### Step-by-Step Execution:
1. Vertices with in-degree 0: **Enqueue 4 and 5**.
2. **Dequeue 4:** Output `4`. Decrement $V_0$ ($2 \rightarrow 1$) and $V_1$ ($2 \rightarrow 1$).
3. **Dequeue 5:** Output `5`. Decrement $V_0$ ($1 \rightarrow 0$) and $V_2$ ($1 \rightarrow 0$).
   * $V_0$ and $V_2$ now have in-degree 0 $\implies$ **Enqueue 0 and 2**.
4. **Dequeue 0:** Output `0`. (No outgoing edges).
5. **Dequeue 2:** Output `2`. Decrement $V_3$ ($1 \rightarrow 0$) $\implies$ **Enqueue 3**.
6. **Dequeue 3:** Output `3`. Decrement $V_1$ ($1 \rightarrow 0$) $\implies$ **Enqueue 1**.
7. **Dequeue 1:** Output `1`.
* **Final Valid Topological Order:** `4 -> 5 -> 0 -> 2 -> 3 -> 1`

---

### 5. Real-World Applications

* **Build Automation Systems (Make, Gradle, Maven):** Resolves compilation order of source code modules based on dependencies.
* **Package Managers (`npm`, `pip`, `apt`):** Determines installation order for libraries with dependencies.
* **Course Prerequisite Scheduling:** University academic curriculum planning.
* **Task Scheduling in Project Management:** PERT / CPM project networks.

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Topological sorting is a linear ordering where directed edge $(u, v)$ means **$u$ appears before $v$**.
> 2. Defined **ONLY for Directed Acyclic Graphs (DAGs)**.
> 3. If a graph contains a cycle, topological sorting is impossible.
> 4. **Kahn's algorithm** uses a queue of **in-degree = 0** vertices; decrements neighbor in-degrees.
> 5. Cycle detection in Kahn's: If output count $< |V|$, the graph contains a cycle.
> 6. **DFS approach** pushes each vertex onto a Stack after visiting all its descendants; popping gives topological order.
> 7. Time complexity is **$O(V + E)$**; applied in build systems (Make), package managers (`pip`), and task scheduling.

---

> ⚡ **Quick Recall**
> `DAG Only → Edge (u,v) means u before v → Kahn's Algorithm (In-Degree=0 Queue) vs DFS Stack → Cycle Detection (Count < |V|) → Build Systems & Task Scheduling`
