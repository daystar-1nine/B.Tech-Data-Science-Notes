# Transaction Concept & ACID Properties — DBMS

> **Definition:** A **Transaction** is a logical unit of database processing that includes one or more database operations (READ, WRITE). To preserve data integrity, transactions must satisfy all four **ACID Properties**.

---

## 1. Detailed Technical Explanation

### The ACID Properties:

```
A - ATOMICITY      : All operations complete successfully, or ALL are undone ("All-or-Nothing").
C - CONSISTENCY    : Transaction transforms database from one valid state to another valid state.
I - ISOLATION      : Concurrent transactions execute independently without interfering with each other.
D - DURABILITY     : Once committed, updates persist permanently in non-volatile storage even after system failure.
```

### 1. Atomicity
- Enforced by the **Recovery Manager** using Write-Ahead Logging (WAL) and Rollback mechanisms.
- Operations: `COMMIT` (permanent save) or `ROLLBACK` (undo changes).

### 2. Consistency
- Enforced by database schema constraints (Primary Key, Foreign Key, `CHECK` constraints) and application logic.

### 3. Isolation
- Enforced by the **Concurrency Control Manager** using locking or timestamping.
- Prevents anomalies: Dirty Reads, Non-Repeatable Reads, Phantom Reads.

### 4. Durability
- Enforced by **Log Recovery & Checkpointing** writing updates to non-volatile disk/SSD storage.

---

## 2. Transaction State Diagram

```
                 +--------------+
                 |    ACTIVE    | (Initial state: reading/writing)
                 +--------------+
                  /                             /                              v                v
      +------------------+     +-------------------+
      | PARTIALLY        |     |      FAILED       |
      | COMMITTED        |     +-------------------+
      +------------------+               |
                |                        v
                v              +-------------------+
      +------------------+     |     ABORTED       | (Rollback complete)
      |    COMMITTED     |     +-------------------+
      +------------------+
     (Successfully saved)
```

---

## 3. Core Concepts & Memory Keywords
- **ACID:** Atomicity, Consistency, Isolation, Durability.
- **Commit Point:** The exact moment transaction updates become permanent.
- **Rollback / Abort:** Undoing all operations of an incomplete transaction.

---

## 4. Must-Write Points for Exams
- Atomicity guarantees that partial execution of a transaction is impossible.
- Isolation ensures that concurrent execution yields the same state as serial execution.
- The transaction state transitions from Active -> Partially Committed -> Committed, or Active -> Failed -> Aborted.

---

## 5. Quick Recall Flow
```
Active -> Read/Write -> Partially Committed -> Commit Log Written -> Committed (Or Aborted on Failure)
```
