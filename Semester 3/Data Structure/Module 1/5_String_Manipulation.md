# String Manipulation Operations

**Q. What is a String in Data Structures? Explain the common string manipulation operations with examples.**

---

> 📌 **Definition to Remember**
> In C, a **String** is a one-dimensional array of characters terminated by a special **null character (`'\0'`)**. String manipulation refers to the set of operations used to modify, analyze, or compare strings. The `<string.h>` library in C provides built-in functions for all major string operations.

---

### 1. String Representation in Memory

```
  char str[] = "HELLO";
  Memory:  H | E | L | L | O | \0
  Index:   0   1   2   3   4   5
```
* The **null character `'\0'`** marks the end of the string.
* String size in memory = length + 1 (for `'\0'`).

### 2. Common String Manipulation Operations

| Function | Operation | Description |
| :--- | :--- | :--- |
| **`strlen(s)`** | Length | Returns number of characters (excluding `'\0'`) |
| **`strcpy(dest, src)`** | Copy | Copies `src` string into `dest` |
| **`strcat(dest, src)`** | Concatenation | Appends `src` to the end of `dest` |
| **`strcmp(s1, s2)`** | Comparison | Returns 0 if equal; negative if s1 < s2; positive if s1 > s2 |
| **`strrev(s)`** | Reverse | Reverses the string in place |
| **`strupr(s)`** | Uppercase | Converts all characters to uppercase |

### 3. Code Example

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello";
    char str2[20] = "World";
    char dest[40];

    // 1. Length
    printf("Length: %lu\n", strlen(str1));       // Output: 5

    // 2. Copy
    strcpy(dest, str1);
    printf("Copy: %s\n", dest);                  // Output: Hello

    // 3. Concatenation
    strcat(dest, " ");
    strcat(dest, str2);
    printf("Concat: %s\n", dest);                // Output: Hello World

    // 4. Comparison
    if (strcmp(str1, str2) == 0)
        printf("Equal\n");
    else
        printf("Not Equal\n");                   // Output: Not Equal

    return 0;
}
```

---

> ⭐ **Must-Write Points (for 10 marks)**
> 1. A string in C is a character array terminated by **null character `'\0'`**.
> 2. String manipulation uses the `<string.h>` library in C.
> 3. `strlen(s)` → counts characters excluding `'\0'`.
> 4. `strcpy(dest, src)` → copies one string to another.
> 5. `strcat(dest, src)` → appends src to the end of dest.
> 6. `strcmp(s1, s2)` → returns 0 if equal; lexicographic comparison.
> 7. Strings are used in text processing, data validation, and pattern matching (KMP, Rabin-Karp).

---

> ⚡ **Quick Recall**
> `String → char array + '\0' → strlen (length) → strcpy (copy) → strcat (join) → strcmp (compare, 0=equal) → strrev (reverse) → <string.h>`
