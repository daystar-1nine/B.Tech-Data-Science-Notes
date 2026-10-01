# NoSQL Data Models & Architecture

**Q. What is NoSQL? Compare Relational DBMS and NoSQL databases. Explain the CAP Theorem, the BASE consistency model, and describe the four major NoSQL data models with real-world use cases.**

---

> 📌 **Definition to Remember**
> **NoSQL ("Not Only SQL")** refers to non-relational, horizontally scalable database management systems designed to store, manage, and process massive volumes of unstructured, semi-structured, and rapidly changing data across distributed commodity clusters with flexible schemas.

---

### 1. Relational DBMS vs. NoSQL Databases

| Feature | Relational Databases (RDBMS) | NoSQL Databases |
| :--- | :--- | :--- |
| **Data Model** | Tables with fixed rows and columns | Key-Value, Document, Columnar, or Graph |
| **Schema** | Rigid, predefined static schema | **Dynamic, schema-less / flexible** |
| **Scaling** | **Vertical (Scale-up):** Bigger CPU, RAM, SSD | **Horizontal (Scale-out):** Distributed cluster nodes |
| **Transactions** | Strict **ACID** Compliance | **BASE** Model (Eventual consistency) |
| **Query Language** | Standardized SQL with complex joins | API calls, JSON queries, GraphQL |
| **Joins** | Native mathematical relational `JOIN` | Denormalized data / Application-side joins |
| **Primary Use** | Financial systems, ERP, structured transactions | Big data, real-time analytics, social networks, IoT |

---

### 2. The CAP Theorem in Distributed Databases

Proposed by Eric Brewer, the **CAP Theorem** states that a distributed data store can guarantee at most **two out of the three** guarantees simultaneously:

```
                         CAP THEOREM
                         /         \
                        /           \
           Consistency [C] -------- [A] Availability
                        \           /
                         \         /
                     Partition Tolerance [P]
```

1. **Consistency (C):** Every read receives the most recent write or an error (all replicas show identical data simultaneously).
2. **Availability (A):** Every non-failing node returns a successful response without guarantee that it contains the newest write.
3. **Partition Tolerance (P):** The system continues operating despite arbitrary network dropped messages or partitioned network splits.

> In physical distributed networks, **network partitions (P) are unavoidable**. Thus, distributed databases must choose between **CP (Consistency + Partition Tolerance)** or **AP (Availability + Partition Tolerance)**.

---

### 3. ACID vs. BASE Properties

* **ACID (RDBMS):** Atomicity, Consistency, Isolation, Durability. Focuses on absolute data consistency.
* **BASE (NoSQL):**
  * **Basically Available:** System remains operational during partial node failures.
  * **Soft State:** Data values may change over time even without external user interaction due to background replication.
  * **Eventual Consistency:** Given enough time without updates, all replicas converge to identical values.

---

### 4. The Four Major NoSQL Data Models

```
   1. KEY-VALUE STORE            2. DOCUMENT STORE
   [ "user:101" ] -> {Data}      { "id": 101, "name": "Rahul",
                                   "skills": ["Java", "SQL"] }

   3. COLUMN-FAMILY STORE        4. GRAPH DATABASE
   Row: 101 -> CF_Personal:     (User:Rahul)-[:FRIEND]->(User:Anita)
               CF_Financial:
```

| NoSQL Model | Architecture & Storage | Key Strengths | Popular Tools | Real-World Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Key-Value Store** | Hash table storing opaque data blobs indexed by unique keys. | Ultra-fast read/write latency ($O(1)$ lookup). | **Redis, DynamoDB, Riak** | Session management, shopping carts, caching. |
| **Document Store** | Encapsulates semi-structured data as JSON/BSON documents. | Flexible nested data, dynamic schemas, secondary indexing. | **MongoDB, Couchbase** | E-commerce product catalogs, blogging, CMS platforms. |
| **Column-Family Store**| Stores data in column families rather than rows; sparse tables. | Massive write scalability, compressed columnar scans. | **Apache Cassandra, HBase** | IoT sensor telemetry, financial logs, time-series data. |
| **Graph Database** | Nodes (entities), Edges (relationships), and Properties. | Blazing-fast complex relationship traversals. | **Neo4j, Amazon Neptune** | Social media graphs, fraud detection, recommendation engines. |

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. NoSQL provides **schema-less, horizontally scalable** data stores for modern big data.
> 2. Relational databases scale vertically (hardware upgrade); NoSQL scales horizontally (commodity nodes).
> 3. **CAP Theorem:** Distributed systems can choose only **CP (Consistency)** or **AP (Availability)** in the presence of network Partitions.
> 4. **BASE model:** Basically Available, Soft-state, Eventual consistency (replaces strict ACID).
> 5. **Key-Value stores (Redis):** Fastest performance for caching and session data.
> 6. **Document stores (MongoDB):** JSON/BSON structures ideal for polymorphic product catalogs.
> 7. **Column-Family stores (Cassandra):** High write throughput for time-series analytics; **Graph databases (Neo4j):** Interconnected network queries.

---

> ⚡ **Quick Recall**
> `Scale-Out Architecture → Dynamic Schema → CAP Theorem (CP vs AP) → BASE Model (Eventual Consistency) → Key-Value | Document | Column-Family | Graph`
