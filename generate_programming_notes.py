import os
import re
import glob

SOURCE_C = r"S:\Programming\C Programming"
SOURCE_CPP = r"S:\Programming\C++ Programming"

DEST_C = r"S:\B.Tech Data Science Notes\Semester 3\Programming Skills\C Programming"
DEST_CPP = r"S:\B.Tech Data Science Notes\Semester 3\Programming Skills\C++ Programming"

os.makedirs(DEST_C, exist_ok=True)
os.makedirs(DEST_CPP, exist_ok=True)

TOPICS_CONFIG = [
    {
        "folder": "Variables, Data Types & InputOutput",
        "file_c": "C_01_Variables_Data_Types_IO.md",
        "file_cpp": "CPP_01_Variables_Data_Types_IO.md",
        "title_c": "Variables, Data Types and Input/Output in C",
        "title_cpp": "Variables, Data Types and Input/Output in C++",
        "def_c": "Variables are named memory locations holding data of specific types. In C, basic types include int, float, double, and char, interacted with via standard I/O streams using printf() and scanf() with formatted specifiers.",
        "def_cpp": "Variables in C++ are strongly-typed memory locations representing primitive and user-defined data. C++ standard I/O utilizes type-safe streams std::cin and std::cout with insertion/extraction operators alongside std::getline.",
        "must_write_c": [
            "Variable declaration allocates memory on the Stack based on sizeof(type).",
            "Format specifiers: %d for int, %f for float, %lf for double, %c for char, %s for strings.",
            "scanf() requires memory address references (&var) for scalar variables.",
            "Always initialize variables to prevent undefined behavior from garbage memory values.",
            "Constants are declared using the const keyword or #define preprocessor directives."
        ],
        "must_write_cpp": [
            "Type-safe stream I/O using std::cin >> and std::cout << eliminates format specifier mismatch errors.",
            "std::endl outputs a newline character and forces a stream buffer flush.",
            "std::getline(std::cin, str) captures full text lines including whitespaces.",
            "Use const and constexpr for compile-time constant immutability and optimization.",
            "Memory sizes: int (4 bytes), float (4 bytes), double (8 bytes), char (1 byte), bool (1 byte)."
        ],
        "recall_c": "Declare Type -> Allocate Memory -> scanf(&addr) -> Execute Logic -> printf(format, val)",
        "recall_cpp": "std::cin >> input -> Type Checking -> Stream Extraction -> Logic Execution -> std::cout << result"
    },
    {
        "folder": "Instructions, Expressions & Operators",
        "file_c": "C_02_Instructions_Expressions_Operators.md",
        "file_cpp": "CPP_02_Instructions_Expressions_Operators.md",
        "title_c": "Instructions, Expressions and Operators in C",
        "title_cpp": "Instructions, Expressions and Operators in C++",
        "def_c": "Operators are special symbols instructing the compiler to perform mathematical, logical, or bitwise operations on operands, forming expressions that evaluate to concrete values.",
        "def_cpp": "Operators in C++ define computations on fundamental types and can be overloaded for user-defined classes. Expressions evaluate according to operator precedence and associativity.",
        "must_write_c": [
            "Arithmetic operators: +, -, *, /, % (modulo only works with integers).",
            "Relational & Logical: <, >, <=, >=, ==, !=, && (AND), || (OR), ! (NOT).",
            "Bitwise operators (&, |, ^, ~, <<, >>) manipulate individual bits at the hardware register level.",
            "Operator precedence dictates execution order; parentheses () guarantee highest priority.",
            "Type casting: Implicit coercion vs explicit casting ((type)expression)."
        ],
        "must_write_cpp": [
            "Short-circuit evaluation: In A && B, B is not evaluated if A is false; in A || B, B is not evaluated if A is true.",
            "Prefix vs Postfix increment: ++x increments before evaluation; x++ increments after evaluation.",
            "Bitwise shifts: x << k multiplies by 2^k; x >> k divides by 2^k for positive integers.",
            "Ternary conditional operator: condition ? expr1 : expr2 enables concise inline branch evaluations.",
            "Explicit casting in modern C++: static_cast<type>(expr) ensures compile-time type safety."
        ],
        "recall_c": "Precedence Hierarchy -> Bitwise Registers -> Type Conversion -> Expression Evaluation -> Assignment",
        "recall_cpp": "Operator Precedence -> Short-Circuit Logic -> static_cast -> Bitwise Manipulation -> Value Return"
    },
    {
        "folder": "Data Types and Storage Classes",
        "file_c": "C_03_Data_Types_and_Storage_Classes.md",
        "file_cpp": "CPP_03_Data_Types_and_Storage_Classes.md",
        "title_c": "Data Types, Modifiers and Storage Classes in C",
        "title_cpp": "Data Types, Modifiers and Storage Classes in C++",
        "def_c": "Storage classes in C (auto, register, static, extern) determine the scope, visibility, initial default value, and lifetime of variables across translation units.",
        "def_cpp": "Storage classes and type modifiers in C++ govern variable lifetime, linkage across compilation units, and storage duration (automatic, static, thread, or dynamic).",
        "must_write_c": [
            "auto: Default local scope, allocated on Stack, lifetime ends at block exit.",
            "register: Requests CPU register storage for fast access; cannot take address (&).",
            "static: Retains value across function calls, initialized once in Data Segment (default 0).",
            "extern: Global linkage, declares variables defined in another source file.",
            "Type modifiers: signed, unsigned, short, long, long long expand numerical range."
        ],
        "must_write_cpp": [
            "static local variables are initialized exactly once upon first execution.",
            "unsigned integer overflow wraps around predictably via modulo 2^N arithmetic.",
            "long long guarantees at least 64 bits of precision for large factorial and combinatorial computations.",
            "const and mutable keywords control read-only state and exception handling in classes.",
            "Storage durations: Automatic (stack), Static (data segment), Dynamic (heap), Thread-local."
        ],
        "recall_c": "auto (Stack) -> register (CPU) -> static (Data Segment) -> extern (Global Cross-File)",
        "recall_cpp": "auto (Block Lifetime) -> static (Single Init/Persist) -> extern (External Linkage) -> Type Range"
    },
    {
        "folder": "Decision Control Structure (if-else, switch, goto, ternary)",
        "file_c": "C_04_Decision_Control_Structures.md",
        "file_cpp": "CPP_04_Decision_Control_Structures.md",
        "title_c": "Decision Control Structures in C (if-else, switch, ternary)",
        "title_cpp": "Decision Control Structures in C++ (if-else, switch, ternary)",
        "def_c": "Decision control structures direct program execution along different execution paths based on the boolean evaluation of conditional expressions.",
        "def_cpp": "Decision control structures in C++ enable conditional branching using if-else ladders, switch statements with jump tables, and ternary conditional operators.",
        "must_write_c": [
            "if-else statements evaluate non-zero as true and zero as false in C.",
            "switch statement evaluates integral/char expressions; each case requires break to prevent fall-through.",
            "default case in switch handles unmatched values.",
            "Ternary operator (?:) provides an inline 3-operand conditional expression.",
            "Avoid goto statements to prevent spaghetti code and maintain structured control flow."
        ],
        "must_write_cpp": [
            "switch statements utilize compiler jump tables for O(1) multi-way branch efficiency.",
            "Nested if-else handles complex multi-condition interval checks (e.g. Grade calculations, Leap years).",
            "Modern C++ supports if statements with initializer: if (int x = getVal(); x > 0) { ... }.",
            "break statement terminates switch block immediately; default handles fallback cases.",
            "Logical operators (&&, ||) combine relational conditions with short-circuit efficiency."
        ],
        "recall_c": "Boolean Test -> if / else if / else -> switch(integral) + break -> Fallback default",
        "recall_cpp": "Branch Evaluation -> Jump Table Switch -> Ternary Inline -> Scope Bound Initializer"
    },
    {
        "folder": "Iteration & Loop Control Structure",
        "file_c": "C_05_Iteration_and_Loop_Control.md",
        "file_cpp": "CPP_05_Iteration_and_Loop_Control.md",
        "title_c": "Iteration and Loop Control Structures in C",
        "title_cpp": "Iteration and Loop Control Structures in C++",
        "def_c": "Loops are control structures that repeatedly execute a block of code as long as a specified condition remains true. C supports entry-controlled (for, while) and exit-controlled (do-while) loops.",
        "def_cpp": "Iteration structures in C++ automate repetitive algorithms through for, while, do-while, and range-based for loops, optimized by compiler branch prediction.",
        "must_write_c": [
            "for loop: Combines initialization, condition test, and update in a single compact header.",
            "while loop: Entry-controlled loop; checks condition before executing body (0 to N iterations).",
            "do-while loop: Exit-controlled loop; guarantees at least one execution (1 to N iterations).",
            "break: Immediately exits the loop; continue: Skips remaining statements in current iteration.",
            "Nested loops: Used for multidimensional arrays, matrix arithmetic, and 2D pattern printing."
        ],
        "must_write_cpp": [
            "Loop bounds and off-by-one errors: Always verify boundary conditions (i < N vs i <= N).",
            "Fibonacci, Prime checks, and GCD/LCM utilize loop state accumulation.",
            "Range-based for loop: for (const auto& elem : container) provides safe iteration.",
            "Time complexity of single loops is O(N); nested double loops evaluate to O(N^2).",
            "Loop invariant maintenance ensures correctness of iterative algorithms."
        ],
        "recall_c": "Init -> Condition Check -> Loop Body -> Step Update -> Break/Continue Control",
        "recall_cpp": "Entry Test (for/while) -> Iteration Block -> Exit Test (do-while) -> Range Loop -> O(N) Bounds"
    },
    {
        "folder": "Function and Recursion",
        "file_c": "C_06_Functions_and_Recursion.md",
        "file_cpp": "CPP_06_Functions_and_Recursion.md",
        "title_c": "Functions and Recursion in C",
        "title_cpp": "Functions and Recursion in C++",
        "def_c": "A function is a self-contained, modular block of code performing a specific task. Recursion occurs when a function calls itself directly or indirectly until reaching a base termination condition.",
        "def_cpp": "Functions in C++ provide code modularity, parameter passing (by value, reference, or pointer), function overloading, default arguments, and recursive call stack execution.",
        "must_write_c": [
            "Function structure: Return type, function name, parameter list, and function body.",
            "Pass-by-value copies data to local parameters; changes do not affect caller arguments.",
            "Pass-by-reference in C is simulated by passing pointer addresses (&var).",
            "Recursion requirements: Base case (termination condition) and Recursive step (approaching base).",
            "Call Stack mechanics: Each recursive call pushes an Activation Record / Stack Frame."
        ],
        "must_write_cpp": [
            "Call-by-reference (type& ref) allows direct modification of caller variables without pointer syntax.",
            "Function overloading enables multiple functions with the same name but distinct signatures.",
            "Inline functions (inline keyword) suggest compiler copy-pasting function bodies to eliminate call overhead.",
            "Recursion Stack Overflow: Occurs when base case is missing or recursion depth exceeds stack limit.",
            "Divide and conquer algorithms (Merge Sort, Binary Search) rely heavily on recursive tree partitioning."
        ],
        "recall_c": "Prototype Declaration -> Call Stack Push -> Parameter Binding -> Base Case Test -> Return Unwind",
        "recall_cpp": "Signature Overload -> Reference Passing -> Base Case Guard -> Recursive Call -> Stack Pop"
    },
    {
        "folder": "Pointers",
        "file_c": "C_07_Pointers_and_Memory_Addresses.md",
        "file_cpp": "CPP_07_Pointers_and_References.md",
        "title_c": "Pointers and Direct Memory Manipulation in C",
        "title_cpp": "Pointers, References and Memory Management in C++",
        "def_c": "A pointer is a variable that stores the direct physical memory address of another variable. Pointers enable dynamic memory allocation, efficient array operations, and pass-by-reference in C.",
        "def_cpp": "Pointers and references in C++ provide direct access to memory addresses. Pointers store addresses and can be reassigned, while references act as constant aliases to existing objects.",
        "must_write_c": [
            "Address-of operator (&): Returns the hexadecimal memory address of a variable.",
            "Dereference operator (*): Accesses or modifies the value stored at the pointed address.",
            "Pointer arithmetic: ptr + 1 advances address by sizeof(data_type) bytes.",
            "NULL pointer: Points to memory address 0x0; dereferencing results in a Segmentation Fault.",
            "Pointers and arrays: The array name acts as a constant pointer to its first element (arr == &arr[0])."
        ],
        "must_write_cpp": [
            "References (int& ref = var) must be initialized upon declaration and cannot be null or reseated.",
            "Pointers vs References: Pointers can be null and re-pointed; references are safe, non-null aliases.",
            "Pass-by-const-reference (const Type&) prevents expensive object copying while guaranteeing read-only safety.",
            "nullptr keyword in modern C++ replaces NULL for strong type-safe pointer validation.",
            "Double pointers (int** ptr) store addresses of pointer variables, used in dynamic 2D matrices."
        ],
        "recall_c": "& (Address) -> * (Dereference) -> Pointer Arithmetic (+sizeof) -> NULL Guard -> Free",
        "recall_cpp": "Address-of (&) -> Pointer (*) -> Reference (& alias) -> nullptr Safety -> Pass-by-Const-Ref"
    },
    {
        "folder": "Arrays",
        "file_c": "C_08_Arrays_and_Matrix_Operations.md",
        "file_cpp": "CPP_08_Arrays_and_Vectors.md",
        "title_c": "Arrays, Multidimensional Matrices and Memory Layout in C",
        "title_cpp": "Arrays, Multidimensional Matrices and Vectors in C++",
        "def_c": "An array is a collection of elements of identical data types stored in contiguous memory locations, offering O(1) random access via index arithmetic.",
        "def_cpp": "Arrays in C++ store contiguous collections of elements. Modern C++ provides std::vector for dynamic contiguous arrays with automated memory management and O(1) random access.",
        "must_write_c": [
            "Contiguous memory calculation: Address of arr[i] = Base Address + i * sizeof(type).",
            "Array indexing starts at 0 and ends at N-1. Accessing arr[N] causes undefined behavior / memory corruption.",
            "2D Arrays: Stored in Row-Major order in memory (Row 0 elements followed by Row 1).",
            "Passing arrays to functions decays them into pointers to the first element (int* arr).",
            "Standard operations: Traversal O(N), Search O(N), Reversal O(N), Merge O(N+M)."
        ],
        "must_write_cpp": [
            "std::vector<T> automatically manages heap buffer reallocation as elements are appended.",
            "std::vector::push_back() has amortized O(1) time complexity.",
            "Two-pointer technique optimizes array reversal, palindrome verification, and sorted array merging.",
            "Matrix operations: 2D vector representation (vector<vector<int>>) simplifies dynamic grid processing.",
            "Spatial locality: Contiguous layout maximizes CPU cache hit ratios for sequential traversals."
        ],
        "recall_c": "Base Address + (i * size) -> Contiguous Stack -> Row-Major 2D -> Pointer Decay -> Bounds Check",
        "recall_cpp": "Contiguous Buffer -> O(1) Random Access -> std::vector Dynamic Growth -> Two-Pointer -> Cache Friendly"
    },
    {
        "folder": "Strings",
        "file_c": "C_09_Strings_and_Character_Arrays.md",
        "file_cpp": "CPP_09_Strings_and_STL_String.md",
        "title_c": "Strings and Character Array Manipulation in C",
        "title_cpp": "Strings, Character Arrays and std::string in C++",
        "def_c": "In C, a string is a 1D array of characters terminated by a special null character ('\\0' with ASCII value 0), manipulated via <string.h> library functions.",
        "def_cpp": "Strings in C++ can be represented as null-terminated C-style character arrays or dynamic std::string objects from the STL offering rich string manipulation methods and automatic memory management.",
        "must_write_c": [
            "Null-terminator ('\\0'): Marks the end of string buffer; array size must be at least length + 1.",
            "Standard functions in <string.h>: strlen(), strcpy(), strcat(), strcmp(), strrev().",
            "Reading strings with spaces: Use fgets(str, size, stdin) instead of unsafe gets().",
            "String comparison: strcmp(s1, s2) returns 0 if identical, <0 if s1 < s2, >0 if s1 > s2.",
            "Character classification functions in <ctype.h>: isalpha(), isdigit(), toupper(), tolower()."
        ],
        "must_write_cpp": [
            "std::string manages its own dynamic buffer, eliminating buffer overflow risks.",
            "String operators: + for concatenation, == and < for lexicographical comparisons.",
            "Useful member functions: length(), substr(), find(), append(), replace(), c_str().",
            "Two-pointer string reversal and palindrome checks operate in O(N) time and O(1) space.",
            "Converting C++ string to C-style string: str.c_str() returns const char* pointer."
        ],
        "recall_c": "char array[] -> '\\0' Null Terminator -> fgets(stdin) -> <string.h> Ops -> Bounds Safety",
        "recall_cpp": "std::string -> Dynamic Heap Buffer -> + Concatenation -> substr/find -> Two-Pointer Palindrome"
    },
    {
        "folder": "Structures",
        "file_c": "C_10_Structures_and_Unions.md",
        "file_cpp": "CPP_10_Structures_and_Classes.md",
        "title_c": "Structures, Unions and Typedef in C",
        "title_cpp": "Structures, Classes and Object-Oriented Foundations in C++",
        "def_c": "A structure (struct) is a user-defined composite data type in C that groups logically related variables of different data types under a single unified name.",
        "def_cpp": "A struct in C++ is a user-defined type identical to a class except that its members and base classes are public by default. Structures encapsulate data attributes and member functions.",
        "must_write_c": [
            "struct definition: Groups heterogeneous data fields; accessed via dot operator (obj.field).",
            "Pointer to struct: Access members using arrow operator (ptr->field == (*ptr).field).",
            "Structure Padding & Memory Alignment: Compiler inserts padding bytes to align data on word boundaries.",
            "typedef keyword creates intuitive aliases (e.g. typedef struct Student Student;).",
            "Union vs Structure: struct allocates sum of member sizes (plus padding); union shares single memory location equal to largest member."
        ],
        "must_write_cpp": [
            "struct vs class in C++: struct defaults to public access; class defaults to private access.",
            "Structures in C++ can have constructors, destructors, and member methods.",
            "Array of structures: Efficiently stores and processes database records (e.g. Students, Employees).",
            "Passing structs: Prefer pass-by-const-reference (const StructType&) to avoid full object copying.",
            "Memory layout: Total size = sum of member sizes + alignment padding bytes."
        ],
        "recall_c": "Heterogeneous Grouping -> struct definition -> dot (.) / arrow (->) -> Alignment Padding -> Union Share",
        "recall_cpp": "Encapsulated Attributes -> Member Functions -> Constructors -> public default -> const Ref Passing"
    },
    {
        "folder": "Dynamic Memory Allocation",
        "file_c": "C_11_Dynamic_Memory_Allocation.md",
        "file_cpp": "CPP_11_Dynamic_Memory_Allocation.md",
        "title_c": "Dynamic Memory Allocation in C (malloc, calloc, realloc, free)",
        "title_cpp": "Dynamic Memory Allocation in C++ (new, delete, Heap Mechanics)",
        "def_c": "Dynamic Memory Allocation (DMA) allows programs to request, resize, and release memory from the Heap segment at runtime using library functions from <stdlib.h>.",
        "def_cpp": "Dynamic memory allocation in C++ allocates heap memory at runtime using new and new[] operators, and releases memory using delete and delete[] operators to prevent memory leaks.",
        "must_write_c": [
            "malloc(size): Allocates raw uninitialized memory bytes; returns void* (or NULL on failure).",
            "calloc(n, size): Allocates and zero-initializes contiguous memory blocks.",
            "realloc(ptr, new_size): Resizes previously allocated heap block, preserving data.",
            "free(ptr): Deallocates heap memory back to the operating system.",
            "Memory Leak: Failing to call free() causes memory exhaustion; Dangling Pointer: Accessing memory after free()."
        ],
        "must_write_cpp": [
            "new operator allocates heap memory and calls the object constructor; delete calls destructor and frees heap.",
            "Array allocation: Type* arr = new Type[size]; must be paired with delete[] arr.",
            "Always set pointers to nullptr after deletion to avoid dangling pointer references.",
            "Memory leak prevention: Every new must have exactly one corresponding delete.",
            "Modern C++ RAII: Smart pointers (std::unique_ptr, std::shared_ptr) automate dynamic memory lifecycle."
        ],
        "recall_c": "malloc / calloc (Heap) -> NULL Check -> Use Buffer -> realloc -> free(ptr) -> ptr = NULL",
        "recall_cpp": "new (Allocate + Construct) -> nullptr Check -> Use Object -> delete[] (Destruct + Free) -> nullptr"
    },
    {
        "folder": "File InputOutput",
        "file_c": "C_12_File_Input_Output.md",
        "file_cpp": "CPP_12_File_Input_Output.md",
        "title_c": "File Handling and Stream I/O in C",
        "title_cpp": "File Stream Handling in C++ (ifstream, ofstream, fstream)",
        "def_c": "File Input/Output in C provides persistent data storage by transferring data between primary memory and secondary storage devices using FILE pointers and buffer streams.",
        "def_cpp": "File handling in C++ is managed via stream classes (<fstream>: ifstream for reading, ofstream for writing, fstream for both), providing object-oriented persistent storage.",
        "must_write_c": [
            "FILE pointer: FILE* fp tracks the stream state, buffer, and current read/write offset.",
            "File modes: 'r' (read), 'w' (overwrite/create), 'a' (append), 'r+' (read/write), 'b' (binary mode).",
            "Always verify fp != NULL after fopen(); missing checks cause crash on non-existent files.",
            "Standard file I/O: fgetc/fputc, fgets/fputs, fprintf/fscanf, fread/fwrite.",
            "Always close files with fclose(fp) to flush output buffers and release OS file descriptors."
        ],
        "must_write_cpp": [
            "std::ifstream reads files; std::ofstream writes files; std::fstream handles dual-mode I/O.",
            "File opening: Open via constructor or file.open(\"path\", ios::mode).",
            "Stream state validation: file.is_open() and while(file >> data) safely detect EOF.",
            "Closing files: RAII destructors automatically close streams, but explicit file.close() is best practice.",
            "Binary vs Text: ios::binary flag prevents OS-specific newline translations in binary mode."
        ],
        "recall_c": "fopen(mode) -> Check NULL -> fprintf / fscanf / fgets -> fflush -> fclose(fp)",
        "recall_cpp": "ifstream / ofstream -> is_open() Check -> Stream << / >> -> getline Loop -> file.close()"
    }
]

def parse_code_files(folder_path, ext):
    code_files = []
    if not os.path.exists(folder_path):
        return code_files
    for f in sorted(os.listdir(folder_path)):
        if f.endswith(ext):
            fpath = os.path.join(folder_path, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                code_content = fp.read()
            
            lines = code_content.split('\n')
            title = f.replace(ext, '').replace('_', ' ')
            desc = ""
            for line in lines[:5]:
                if line.startswith('//'):
                    desc = line.replace('//', '').strip()
                    break
                elif line.startswith('/*'):
                    desc = line.replace('/*', '').replace('*/', '').strip()
                    break
            
            code_files.append({
                "filename": f,
                "title": title,
                "desc": desc if desc else f"Implementation of {title}",
                "code": code_content.strip()
            })
    return code_files

def generate_notes():
    for cfg in TOPICS_CONFIG:
        folder_name = cfg["folder"]
        
        # --- Process C Programming ---
        src_c_dir = os.path.join(SOURCE_C, folder_name)
        out_c_file = os.path.join(DEST_C, cfg["file_c"])
        c_code_files = parse_code_files(src_c_dir, '.c')
        
        content_c = f"""# {cfg['title_c']}

> 📌 **Definition to Remember**
> {cfg['def_c']}

---

## 1. Concept Overview & Fundamentals 🧠

{cfg['title_c']} forms a core cornerstone of computer systems programming, hardware-level software engineering, and competitive problem solving.

In the C execution model:
- Code is compiled directly into native machine instructions without virtual machine overhead.
- Memory is strictly partitioned into **Code/Text Segment**, **Data Segment (Initialized/BSS)**, **Stack**, and **Heap**.
- Direct pointer and register manipulation provides deterministic performance critical for operating systems, embedded hardware, and database kernels.

---

## 2. Technical Architecture & Memory Mechanics ⚙️

### Memory Layout & Storage Organization

```text
+-------------------------------------------------------------+
|                      STACK SEGMENT                          |
|  - Local variables, function call stack frames, parameters  |
|  - High memory growing downwards towards Heap               |
+-------------------------------------------------------------+
                              |
                              v
                              ^
                              |
+-------------------------------------------------------------+
|                       HEAP SEGMENT                          |
|  - Dynamic memory allocations via malloc(), calloc()        |
|  - Low memory growing upwards towards Stack                 |
+-------------------------------------------------------------+
|                   INITIALIZED DATA SEGMENT                  |
|  - Global and static variables with non-zero initial values |
+-------------------------------------------------------------+
|                    BSS SEGMENT (UNINITIALIZED)              |
|  - Global and static variables initialized to zero          |
+-------------------------------------------------------------+
|                     CODE / TEXT SEGMENT                     |
|  - Read-only executable binary instructions                 |
+-------------------------------------------------------------+
```

### Core Architecture Breakdown

| Component / Concept | Technical Specification | Operational Characteristics | Performance / Complexity |
| :--- | :--- | :--- | :--- |
| **Storage Allocation** | Stack vs Heap vs Data Segment | Stack is ultra-fast LIFO; Heap offers dynamic scalability | Stack: $O(1)$ push/pop; Heap: $O(1)$ alloc |
| **Type Checking** | Static Typing | Compiler verifies types during compilation | Zero runtime type penalty |
| **Addressing Model** | Byte-addressable physical RAM | Pointer stores hexadecimal byte memory address | Direct memory dereference ($O(1)$) |
| **Execution Flow** | Procedural / Sequential | Controlled via jumps, branches, loops, and call stacks | Deterministic instruction cycles |

---

## 3. Core Syntax & Implementation Patterns 📐

### Essential Idioms & Header Declarations

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Core standard implementation pattern
int main(void) {{
    // Explicit initialization
    int status = 0;
    
    // Core logic execution
    printf("Executing C Module: {cfg['folder']}\\n");
    
    return status;
}}
```

---

## 4. Real-World Applications & System Engineering 🌍

- **Operating System Kernels:** Linux, UNIX, and Windows NT kernels utilize C for drivers, process scheduling, and memory paging.
- **Embedded & IoT Devices:** Microcontrollers with constrained RAM (8KB-64KB) require C's predictable footprint.
- **Database Engine Kernels:** High-throughput storage engines (PostgreSQL, SQLite, MySQL InnoDB) rely on low-level buffer pool managers written in C.
- **Game Engine Foundations:** Graphics rasterization, physics engines, and GPU interfaces utilize C/C++ memory arrays for zero-overhead computation.

---

## 5. Comprehensive Solved Problems & Code Walkthroughs 📝
"""
        for idx, item in enumerate(c_code_files, 1):
            content_c += f"""
### Problem {idx}: {item['title']}

**Problem Description & Objective:**
{item['desc']}

**C Code Implementation:**
```c
{item['code']}
```

---
"""

        content_c += f"""
## 6. Exam Scoring Points & Memory Revision 🎯

> ⭐ **Must-Write Points**
"""
        for pt_idx, pt in enumerate(cfg['must_write_c'], 1):
            content_c += f"> {pt_idx}. {pt}\n"

        content_c += f"""
> ⚡ **Quick Recall**
> `{cfg['recall_c']}`
"""

        with open(out_c_file, 'w', encoding='utf-8') as fp:
            fp.write(content_c.strip() + "\n")
        print(f"Generated C Note: {cfg['file_c']} with {len(c_code_files)} solved problems.")

        # --- Process C++ Programming ---
        src_cpp_dir = os.path.join(SOURCE_CPP, folder_name)
        out_cpp_file = os.path.join(DEST_CPP, cfg["file_cpp"])
        cpp_code_files = parse_code_files(src_cpp_dir, '.cpp')

        content_cpp = f"""# {cfg['title_cpp']}

> 📌 **Definition to Remember**
> {cfg['def_cpp']}

---

## 1. Concept Overview & Fundamentals 🧠

{cfg['title_cpp']} provides modern high-performance capabilities combining low-level hardware control with high-level abstractions, object-oriented paradigms, and Standard Template Library (STL) utilities.

In modern C++ (C++11 through C++20):
- **Zero-Overhead Principle:** What you don't use, you don't pay for; what you do use, you couldn't hand code any better.
- **Type Safety & Streams:** Type-safe stream I/O (`std::cin`, `std::cout`) prevents runtime format mismatch vulnerabilities.
- **Resource Acquisition Is Initialization (RAII):** Automatic resource management via constructors, destructors, and smart pointers.

---

## 2. Technical Architecture & Memory Mechanics ⚙️

### C++ Runtime Execution Architecture

```text
+-------------------------------------------------------------+
|                      STACK SEGMENT                          |
|  - Local scope objects, references, RAII stack frames       |
|  - Deterministic automatic destruction upon scope exit      |
+-------------------------------------------------------------+
                              |
                              v
                              ^
                              |
+-------------------------------------------------------------+
|                       HEAP / FREE STORE                     |
|  - Dynamic objects allocated via new, std::vector, etc.     |
|  - Managed via delete / smart pointers                      |
+-------------------------------------------------------------+
|                   STATIC & GLOBAL MEMORY                    |
|  - Global objects, static class variables, string literals  |
+-------------------------------------------------------------+
|                     CODE / TEXT SEGMENT                     |
|  - Executable machine code, inlined functions, templates    |
+-------------------------------------------------------------+
```

### Modern C++ Feature Comparison

| Modern C++ Paradigm | Legacy Equivalent | Engineering Advantage | Performance Impact |
| :--- | :--- | :--- | :--- |
| **`std::cin` / `std::cout`** | `scanf` / `printf` | Type-safe, extensible for custom classes | Buffered I/O (optimizable via `ios::sync_with_stdio(0)`) |
| **References (`Type&`)** | Pointers (`Type*`) | Non-nullable, clean syntax without dereferencing | Direct alias; zero runtime overhead |
| **`std::vector<T>`** | Raw Dynamic Array (`malloc`) | Automatic resizing, bounds safety, memory management | Amortized $O(1)$ push_back, contiguous cache |
| **`nullptr`** | `NULL` / `0` | Strongly typed pointer literal preventing integer overload bugs | Zero overhead |

---

## 3. Core Syntax & Implementation Patterns 📐

### Modern C++ Template Structure

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Fast I/O and standard namespace configuration
int main() {{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cout << "Executing C++ Module: {cfg['folder']}" << "\\n";

    return 0;
}}
```

---

## 4. Real-World Applications & System Engineering 🌍

- **Quantitative Finance & HFT:** High-frequency trading platforms use modern C++ for microsecond-level execution.
- **Game Engine Architecture:** Unreal Engine, Unity Core, and AAA game engines utilize C++ for real-time 3D rendering.
- **Deep Learning Frameworks:** Core tensor compute backends (PyTorch, TensorFlow, ONNX Runtime) are written in C++ and CUDA.
- **Web Browsers & Compilers:** Google Chrome (V8 engine), LLVM/Clang, and GCC are implemented in C++.

---

## 5. Comprehensive Solved Problems & Code Walkthroughs 📝
"""
        for idx, item in enumerate(cpp_code_files, 1):
            content_cpp += f"""
### Problem {idx}: {item['title']}

**Problem Description & Objective:**
{item['desc']}

**C++ Code Implementation:**
```cpp
{item['code']}
```

---
"""

        content_cpp += f"""
## 6. Exam Scoring Points & Memory Revision 🎯

> ⭐ **Must-Write Points**
"""
        for pt_idx, pt in enumerate(cfg['must_write_cpp'], 1):
            content_cpp += f"> {pt_idx}. {pt}\n"

        content_cpp += f"""
> ⚡ **Quick Recall**
> `{cfg['recall_cpp']}`
"""

        with open(out_cpp_file, 'w', encoding='utf-8') as fp:
            fp.write(content_cpp.strip() + "\n")
        print(f"Generated C++ Note: {cfg['file_cpp']} with {len(cpp_code_files)} solved problems.")

if __name__ == '__main__':
    generate_notes()
