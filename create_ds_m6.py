import os

DS_DIR = r"S:\B.Tech Data Science Notes\Semester 3\Data Structure"

m6_dir = os.path.join(DS_DIR, "Module 6")
m6_qa = os.path.join(m6_dir, "Module_6_QA")

os.makedirs(m6_dir, exist_ok=True)
os.makedirs(m6_qa, exist_ok=True)

# --------------------------------------------------------------------------
# MODULE 6: SORTING AND SEARCHING TECHNIQUES
# --------------------------------------------------------------------------

m6_files = {
    "1_Searching_Techniques_Linear_and_Binary_Search.md": """# Searching Techniques: Linear Search & Binary Search — Data Structures

> **Definition:** **Searching** is the algorithmic process of locating the position of a target key element `K` within a collection of items (such as an array). The two primary searching techniques are **Linear Search** and **Binary Search**.

---

## 1. Detailed Technical Explanation

### 1. Linear Search (Sequential Search)
- **Concept:** Sequentially inspects every element in the array from index `0` to `N - 1` until the target element is found or the end of array is reached.
- **Requirement:** Works on both **sorted and unsorted** arrays.
- **Time Complexity:** Best: `O(1)`, Average: `O(N)`, Worst: `O(N)`.

```c
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i; // Element found at index i
    }
    return -1; // Not found
}
```

---

### 2. Binary Search (Divide and Conquer)
- **Concept:** Repeatedly divides the search interval in half by comparing the target key with the middle element `arr[mid]`:
  - If `arr[mid] == key`: Target found!
  - If `key < arr[mid]`: Search in left half (`high = mid - 1`).
  - If `key > arr[mid]`: Search in right half (`low = mid + 1`).
- **Strict Prerequisite:** The array **MUST be sorted**.
- **Time Complexity:** Best: `O(1)`, Average: `O(log N)`, Worst: `O(log N)`.

```c
// Iterative Binary Search Implementation
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2; // Prevents integer overflow
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; // Not found
}
```

---

## 2. Comparison: Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Array Prerequisite** | Any array (Unsorted or Sorted). | **Strictly Sorted Array Required**. |
| **Worst-Case Time** | `O(N)` (Linear) | **`O(log N)` (Logarithmic)** |
| **Access Paradigm** | Sequential access (Works on Linked Lists). | Random access (Requires direct indexing `arr[mid]`). |
| **Comparisons for N=1000** | Up to 1000 comparisons. | At most **10 comparisons** ($2^{10} = 1024$). |

---

## 3. Quick Recall Flow
```
Linear Search: Unsorted Arrays -> O(N) | Binary Search: Sorted Array -> Halve Interval mid = (low+high)/2 -> O(log N)
```
""",

    "2_Sorting_Techniques_Bubble_Insertion_Selection_Sort.md": """# Sorting Techniques: Bubble Sort, Insertion Sort & Selection Sort — Data Structures

> **Definition:** **Sorting** is the algorithmic process of arranging elements of a collection into a systematic order (ascending or descending).

---

## 1. Detailed Technical Explanation

### 1. Bubble Sort (Comparison & Swap)
- **Mechanism:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest element "bubbles up" to its correct position at the end of each pass.
- **Optimized Flag:** Stop early if no swaps occurred during a pass (`O(N)` best case).

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }
        if (!swapped) break; // Array is already sorted
    }
}
```

---

### 2. Selection Sort (Minimum Element Selection)
- **Mechanism:** Divides array into sorted and unsorted subarrays. Repeatedly finds the **minimum element** from the unsorted subarray and places it at the beginning of the unsorted part.
- **Key Trait:** Makes the minimum number of swaps (at most `N - 1` swaps).

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
```

---

### 3. Insertion Sort (Card Player's Sorting)
- **Mechanism:** Builds the sorted array one item at a time by picking the next element and inserting it into its correct relative position within the already-sorted left subarray.
- **Key Trait:** Highly efficient for small or nearly sorted datasets.

```c
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

---

## 2. Comprehensive Comparison Table

| Algorithm | Best Time | Average Time | Worst Time | Space | Stable? | In-Place? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | `O(N)` | `O(N^2)` | `O(N^2)` | `O(1)` | **Yes** | **Yes** |
| **Selection Sort** | `O(N^2)` | `O(N^2)` | `O(N^2)` | `O(1)` | **No** | **Yes** |
| **Insertion Sort** | `O(N)` | `O(N^2)` | `O(N^2)` | `O(1)` | **Yes** | **Yes** |

---

## 3. Quick Recall Flow
```
Bubble: Swap adjacent (Bubble largest to right) | Selection: Find min and swap to front | Insertion: Shift and insert into sorted subarray
```
""",

    "3_Hashing_Concepts_and_Hash_Functions.md": """# Hashing Concepts & Hash Functions — Data Structures

> **Definition:** **Hashing** is a technique that transforms a search key `K` into a table index `h(K)` using a **Hash Function**, enabling average constant time **O(1)** insertion, deletion, and lookup operations in a **Hash Table**.

---

## 1. Detailed Technical Explanation

```
Search Key (e.g., 108) ---> [ Hash Function h(k) = k % 10 ] ---> Index 8 in Hash Table
```

### 1. The Load Factor ($\alpha$)
The load factor represents the density of items stored in a hash table of size `m` with `n` keys:
```
Load Factor (α) = n / m  (Number of Elements / Table Size)
```
- In Open Addressing, $\alpha \le 1$. In Separate Chaining, $\alpha$ can exceed 1.

---

## 2. Common Hash Functions

### 1. Division Method (Modulo Arithmetic)
```
h(k) = k mod m
```
- **Rule:** `m` should be a **Prime Number** not close to a power of 2 or 10 to minimize clustering.
- *Example:* For table size `m = 11` and key `k = 47`:
  ```
  h(47) = 47 mod 11 = 3
  ```

### 2. Mid-Square Method
1. Square the key: $k^2$.
2. Extract the middle $r$ digits of the square as the index (where table size $m = 10^r$).
- *Example:* For key `k = 31` and $m = 100$:
  ```
  k^2 = 31^2 = 0961 -> Middle digits = 96 -> Index = 96
  ```

### 3. Folding Method
Divide the key digits into equal parts of size $r$, and sum them together (ignoring overflow carry).
- **Fold-Shift:** Directly sum parts (e.g., Key `123456` into `12 + 34 + 56 = 102 -> 02`).
- **Fold-Boundary:** Reverse boundary parts before summing.

### 4. Multiplication Method
```
h(k) = floor(m * (k * A mod 1))  where 0 < A < 1 (Knuth recommends A ≈ 0.6180339887)
```
- *Advantage:* The choice of table size `m` is not critical (can be a power of 2).

---

## 3. Properties of a Good Hash Function
1. **Uniform Distribution:** Distributes keys evenly across all table slots to minimize collisions.
2. **Deterministic:** Must always compute the same index for the same input key.
3. **Fast Computation:** Computable in $O(1)$ time.

---

## 4. Quick Recall Flow
```
Key -> Hash Function h(k) -> Index [0..m-1] | Functions: Division (k%m), Mid-Square (middle of k^2), Folding (split & sum)
```
""",

    "4_Collision_Resolution_Techniques.md": """# Collision Resolution Techniques (Open Addressing & Chaining) — Data Structures

> **Definition:** A **Collision** occurs in hashing when a hash function maps two distinct keys $k_1 \ne k_2$ to the **exact same table index** ($h(k_1) = h(k_2)$). Collision resolution techniques resolve this conflict.

---

## 1. Detailed Technical Explanation

```
COLLISION RESOLUTION STRATEGIES
             |
   +---------+----------------------------+
   |                                      |
1. OPEN ADDRESSING (Closed Hashing)    2. SEPARATE CHAINING (Open Hashing)
   - Linear Probing                       - Array of Linked Lists
   - Quadratic Probing
   - Double Hashing
```

---

## 2. Technique 1: Open Addressing

All keys are stored directly inside the hash table array. If slot $h(k)$ is occupied, systematic probing finds the next vacant slot.

### 1. Linear Probing
Probes slots sequentially with an offset of 1:
```
h(k, i) = (h'(k) + i) mod m   for i = 0, 1, 2, ..., m-1
```
- *Drawback:* Suffers from **Primary Clustering** (long contiguous blocks of occupied slots build up, degrading search time).

### 2. Quadratic Probing
Probes slots using a quadratic polynomial:
```
h(k, i) = (h'(k) + c1 * i + c2 * i^2) mod m
```
- *Advantage:* Eliminates primary clustering; but can cause **Secondary Clustering** (keys with same initial hash follow identical probe sequences).

### 3. Double Hashing (Best Open Addressing Technique)
Uses two independent hash functions $h_1(k)$ and $h_2(k)$:
```
h(k, i) = (h1(k) + i * h2(k)) mod m
```
- *Rule:* $h_2(k)$ must never evaluate to 0 and must be relatively prime to `m`.
- *Example:* $h_1(k) = k \bmod 11$ and $h_2(k) = 7 - (k \bmod 7)$.

---

## 3. Technique 2: Separate Chaining

Each slot in the hash table points to the head of a **Linked List** storing all colliding keys mapped to that index.

```
Hash Table Array
  Index 0: NULL
  Index 1: [ 12 ] -> [ 23 ] -> [ 34 ] -> NULL  (Collisions at index 1 chained)
  Index 2: [ 13 ] -> NULL
  Index 3: NULL
```

### Separate Chaining vs Open Addressing Comparison:
| Feature | Separate Chaining | Open Addressing |
| :--- | :--- | :--- |
| **Storage Structure** | Array of Linked Lists. | Single Array (Keys stored in slots). |
| **Table Capacity** | Can store $> m$ elements ($\alpha > 1$). | Limited to table size $m$ ($\alpha \le 1$). |
| **Deletion** | Simple node removal from linked list. | Complex (requires `DELETED` dummy markers). |
| **Cache Performance** | Poor cache locality due to linked list pointers. | **Excellent cache locality** (contiguous array). |

---

## 4. Quick Recall Flow
```
Collision (h(k1) == h(k2)) -> Open Addressing: Linear (i), Quadratic (i^2), Double Hashing (i*h2) | Separate Chaining: Linked List buckets
```
""",

    "5_Self_Learning_Merge_Sort_and_Quick_Sort.md": """# Self-Learning: Merge Sort & Quick Sort — Data Structures

> **Definition:** **Merge Sort** and **Quick Sort** are high-performance $O(N \log N)$ sorting algorithms based on the **Divide and Conquer** paradigm.

---

## 1. Detailed Technical Explanation

### 1. Merge Sort
- **Concept:** Divides array into two halves, recursively sorts both halves, and merges the two sorted halves into a single sorted array.
- **Recurrence Relation:** $T(N) = 2T(N/2) + \Theta(N) \implies O(N \log N)$ in all cases.
- **Key Trait:** **Stable** sort with guaranteed $O(N \log N)$ time, but requires $O(N)$ auxiliary memory.

```c
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
```

---

### 2. Quick Sort
- **Concept:** Selects a **Pivot** element, partitions the array such that all elements smaller than the pivot are on the left and all larger elements are on the right, then recursively sorts the left and right partitions.
- **Key Trait:** **In-Place** sort with fast practical performance ($O(N \log N)$ average), but worst-case time is $O(N^2)$ (when already sorted and choosing boundary pivot).

```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Lomuto Partition scheme
    int i = (low - 1);
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int t = arr[i]; arr[i] = arr[j]; arr[j] = t;
        }
    }
    int t = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = t;
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

---

## 2. Comparison: Merge Sort vs Quick Sort

| Feature | Merge Sort | Quick Sort |
| :--- | :--- | :--- |
| **Best-Case Time** | $O(N \log N)$ | $O(N \log N)$ |
| **Average-Case Time**| $O(N \log N)$ | $O(N \log N)$ |
| **Worst-Case Time** | **$O(N \log N)$** (Guaranteed) | $O(N^2)$ (Mitigated via Randomized Pivot) |
| **Auxiliary Space** | $O(N)$ (Temporary arrays) | **$O(\log N)$** (In-Place stack space) |
| **Stability** | **Stable** | **Unstable** |

---

## 3. Quick Recall Flow
```
Merge Sort: Divide in half -> Recursively Sort -> Merge sorted halves (O(N log N) Stable, O(N) space)
Quick Sort: Choose Pivot -> Partition Left < Pivot < Right -> Recursively Sort (O(N log N) In-Place)
```
"""
}

# Write Module 6 files
for fname, content in m6_files.items():
    with open(os.path.join(m6_dir, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Created Data Structure Module 6 Files!")
