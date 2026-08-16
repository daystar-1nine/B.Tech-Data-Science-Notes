# Sorting Techniques: Bubble Sort, Insertion Sort & Selection Sort — Data Structures

> **Definition: Sorting** is the algorithmic process of arranging elements of a collection into a systematic order (ascending or descending).

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
