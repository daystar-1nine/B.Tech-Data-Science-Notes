# Applications of Binary Trees: Expression Tree & Huffman Coding

**Q. Explain the construction and evaluation of Expression Trees from postfix expressions. Explain Huffman Coding for lossless data compression with an algorithm and step-by-step tree construction example.**

---

> 📌 **Definition to Remember**
> Primary applications of binary trees include **Expression Trees** (binary trees where internal nodes represent operators and leaf nodes represent operands) and **Huffman Coding Trees** (optimal prefix-free variable-length binary trees used for lossless data compression).

---

### 1. Expression Trees

An **Expression Tree** represents an algebraic expression in hierarchical form:
* **Leaf Nodes:** Operands (variables or constants: `a`, `b`, `c`, `5`).
* **Internal Nodes:** Operators (`+`, `-`, `*`, `/`, `^`).

```
Expression: (a + b) * (c - d)

                     [ * ]  <-- Root Operator
                    /     \
                [ + ]     [ - ]
               /     \   /     \
             [a]     [b] [c]    [d]
```

#### Traversals of Expression Tree:
* **Inorder Traversal:** Infix Expression with parentheses: `(a + b) * (c - d)`.
* **Preorder Traversal:** Prefix (Polish) Expression: `* + a b - c d`.
* **Postorder Traversal:** Postfix (Reverse Polish) Expression: `a b + c d - *`.

---

### 2. Constructing an Expression Tree from Postfix (Using Stack)

```
Algorithm: Construct_Expression_Tree(Postfix_String)
1. Initialize an empty Stack of Tree Node pointers.
2. For each character ch in Postfix_String:
     a. If ch is an OPERAND:
        Create a new node containing ch, push its pointer onto Stack.
     b. If ch is an OPERATOR:
        Create a new node containing ch.
        Pop top node from Stack -> Assign as right child.
        Pop next node from Stack -> Assign as left child.
        Push operator node pointer onto Stack.
3. The remaining pointer on top of the Stack is the ROOT of the Expression Tree.
```

---

### 3. Huffman Coding (Lossless Data Compression)

Huffman coding is a **Greedy Algorithm** that assigns variable-length binary codes to characters based on their frequencies:
* **Frequent characters** receive **shorter bit codes**.
* **Infrequent characters** receive **longer bit codes**.
* **Prefix-Free Property:** No code is a prefix of any other code, allowing unambiguous decoding without delimiters.

---

### 4. Step-by-Step Huffman Tree Construction Example

#### Character Frequency Table:
| Character | Frequency |
| :---: | :---: |
| **A** | 45 |
| **B** | 13 |
| **C** | 12 |
| **D** | 16 |
| **E** | 9 |
| **F** | 5 |

#### Construction Steps (Greedy Min-Heap):
1. **Merge two smallest:** `F(5)` and `E(9)` $\rightarrow$ Node `(14)`.
2. **Merge next two smallest:** `C(12)` and `B(13)` $\rightarrow$ Node `(25)`.
3. **Merge smallest:** Node `(14)` and `D(16)` $\rightarrow$ Node `(30)`.
4. **Merge smallest:** Node `(25)` and Node `(30)` $\rightarrow$ Node `(55)`.
5. **Final merge:** `A(45)` and Node `(55)` $\rightarrow$ Root `(100)`.

```
                        [ 100 ]
                       /       \
                     0/         \1
                   [ A: 45 ]    [ 55 ]
                               /      \
                             0/        \1
                           [ 25 ]      [ 30 ]
                          /      \     /      \
                        0/       1\  0/       1\
                     [ C:12 ] [ B:13 ][ 14 ]   [ D:16 ]
                                      /    \
                                    0/      \1
                                  [ F:5 ]  [ E:9 ]
```

#### Resulting Huffman Prefix Codes:
* Label left branch with `0` and right branch with `1`:
  * **A:** `0` (1 bit)
  * **C:** `100` (3 bits)
  * **B:** `101` (3 bits)
  * **F:** `1100` (4 bits)
  * **E:** `1101` (4 bits)
  * **D:** `111` (3 bits)

#### Compression Analysis:
* **Fixed-length encoding:** 6 characters require 3 bits each ($100 \times 3 = \mathbf{300 \text{ bits}}$).
* **Huffman encoding:**
  $$(45 \times 1) + (12 \times 3) + (13 \times 3) + (5 \times 4) + (9 \times 4) + (16 \times 3) = 45 + 36 + 39 + 20 + 36 + 48 = \mathbf{224 \text{ bits}}$$
* **Storage Saved:** $\approx 25.3\%$ bandwidth compression!

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. Expression Trees store operators in **internal nodes** and operands in **leaf nodes**.
> 2. Inorder yields infix; Preorder yields prefix; Postorder yields postfix.
> 3. Expression tree is built from postfix using a **Stack of node pointers**.
> 4. **Huffman coding** is a greedy compression algorithm producing optimal variable-length codes.
> 5. High-frequency characters get shorter codes; low-frequency characters get longer codes.
> 6. Huffman codes are **prefix-free** (no code is a prefix of another), enabling direct stream decoding.
> 7. Time complexity of Huffman tree construction is **$O(N \log N)$** using a Min-Priority Queue.

---

> ⚡ **Quick Recall**
> `Expression Tree (Operators = Internal, Operands = Leaves) → Stack Construction from Postfix | Huffman Tree: Min-Heap → Merge 2 Lowest Frequencies → Assign 0/1 Branches → Prefix-Free Codes`
