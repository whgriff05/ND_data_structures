# Abstract Data Types / Dynamic Arrays

What is an ADT?
- Defined by supported operations
- Hidden internal details
- Related to the idea of object-oriented programming

### Review of Structs
```C
// Point (x, y)
struct Point {
    int x;
    int y;
};

// OR
typedef struct {
    int x;
    int y;
} Point;
```
- Struct memory is contiguous liek arrays
- Typically, compilers pad to power of 2 size of bytes

### Dynamic Arrays
- Consist of three parts
    1. Data: the internal array
    2. Capacity: the maximum amount of items the array can hold
    3. Size: the current amount of items the array is holding
- When the internal array is full, it needs to be regrown
    - Use the `realloc()` function
    - `void *realloc(void *p, size_t size)`
        - Returns a void pointer to the new memory
        - Takes in the old pointer and the new size in bytes

Computational Complexity of a Dynamic Array
|Function|Avg Time|Worst Time|Avg Space|Worst Space|
|-|-|-|-|-|
|append()|O(1) _add to end_|O(N) _realloc_|O(1) _memory is ready_|O(N) _copy to new memory_|
|at()|O(1)|O(1)|O(1)|O(1)|
|index()|O(N)|O(N)|O(1)|O(1)|
|insert()|O(N)|O(N)|O(1)|O(N)|

