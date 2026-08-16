# Self-Learning: NoSQL Data Models — DBMS

> **Definition: NoSQL (Not Only SQL)** refers to non-relational database management systems designed for horizontal scalability, high-velocity big data, flexible schema-less data models, and high availability.

---

## 1. Detailed Technical Explanation

NoSQL databases trade traditional ACID strict transactional guarantees for high performance and horizontal scaling across distributed clusters (governed by the **CAP Theorem**).

### CAP Theorem:
A distributed database system can guarantee at most **two out of three** properties simultaneously:
1. **Consistency (C):** All nodes read the latest data at the same time.
2. **Availability (A):** Every non-failing request receives a non-error response.
3. **Partition Tolerance (P):** System continues to operate despite network communication failures.

---

## 2. The Four Major NoSQL Data Models

| NoSQL Category | Data Model | Key Features | Popular Industry Tools | Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Key-Value Store** | Hash Table (Key -> Value Blob) | Fast lookup by key, ultra-high performance. | Redis, Amazon DynamoDB, Riak | Caching, session management, user shopping carts. |
| **Document Store** | JSON / BSON / XML Documents | Schema-free nested documents, rich indexing. | MongoDB, CouchDB | Content management, e-commerce product catalogs. |
| **Column-Family Store**| Sparse tables indexed by Rows & Column Families | Optimized for heavy write throughput and analytical queries. | Apache Cassandra, HBase | Time-series data, IoT analytics, financial logs. |
| **Graph Database** | Nodes, Edges (Properties) | Graph traversal queries for interconnected data. | Neo4j, Amazon Neptune | Social networks, fraud detection, recommendation engines. |

---

## 3. SQL vs NoSQL Architecture Comparison

| Feature | Relational SQL Databases | NoSQL Databases |
| :--- | :--- | :--- |
| **Data Schema** | Fixed, predefined rigid schema. | Dynamic, schema-less / flexible. |
| **Scaling** | Vertical scaling (Scale-up: bigger CPU/RAM). | Horizontal scaling (Scale-out: sharding across commodity nodes). |
| **Transactions** | Strict ACID Compliance. | BASE Model (Basically Available, Soft-state, Eventual consistency). |
| **Joins** | Native SQL `JOIN` operations. | Denormalized data / Application-side joins. |

---

## 4. Quick Recall Flow
```
NoSQL -> Scale-Out Horizontal Architecture -> CAP Theorem Tradeoffs -> Key-Value | Document | Column-Family | Graph
```
