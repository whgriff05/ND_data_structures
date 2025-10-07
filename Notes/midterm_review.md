# Midterm Review

## General Info
- In class, 50m
- Multiple Choice and Short Answer
- Beginning of class to linked lists (HW 5)
- Specific Tips
    - Know powers of 2 
    - Be familiar with __both__ unoptimized and optimized sort algorithms
    - Quicksort: __be familiar with the exact version in zyBooks__ (choice of pivot, revursive reassignment of upper and lower bounds)
    - zyBooks 15.1 -- C playground


## Review of Regions of Memory
```C
/* Assume 6-bit memory: 0-63 (0x00 - 0x3F) */
/* Each memory location can hold one int, char, ... address (don't have to worry about endian/ints having more than one address) */

double p = 3;

int main() {
    int i = 25;
    char a[] = "wx";
    char *s = "yz";
    int *m = malloc(10*sizeof(int));
    static int t = 2;

    *m = 100;
    *(m + 1) = 101;
    m[2] = 103;

    return 0;
}
```

| Stack | Heap | Data | Code |
|-|-|-|-|
|0x3F: `i = 25`|0x2F:|0x1F:|0x0F:|
|0x3E: `a[2] = '\0'`|0x2E:|0x1E:|0x0E:|
|0x3D: `a[1] = 'x'`|0x2D:|0x1D:|0x0D:|
|0x3C: `a[0] = 'w'`|0x2C:|0x1C:|0x0C:|
|0x3B: `s = 0x11`|0x2B:|0x1B:|0x0B:|
|0x3A: `m = 0x20`|0x2A:|0x1A:|0x0A:|
|0x39:|0x29: |0x19:|0x09:|
|0x38:|0x28: |0x18:|0x08:|
|0x37:|0x27: |0x17:|0x07:|
|0x36:|0x26: |0x16:|0x06:|
|0x35:|0x25: |0x15:|0x05:|
|0x34:|0x24: |0x14: `t = 2`|0x04:|
|0x33:|0x23: |0x13: `'\0'`|0x03:|
|0x32:|0x22: `103`|0x12: `'z'`|0x02:|
|0x31:|0x21: `101`|0x11: `'y'`|0x01:|
|0x30:|0x20: `100`|0x10: `p = 3`|0x00: `main`|

## Review of Abstract Data Types

__Dynamic Array:__ automatically resizing array
```C
typedef struct {
    int data[];
    int capacity;
    int size;
} Array;
```
- `data[]`: the internal array for storing data
- `capacity`: the maximum amount of elements the array can store
- `size`: the current amount of elements the array is storing
- resized when capacity > size using `realloc()`

__Stack:__ list of values following the _last in, first out (LIFO)_ order
- `push()`: adds a new element to the top of the stack
- `pop()`: removes the stack's top element

__Queue:__ list of values following the _first in, first out (FIFO)_ order
- similar to a line of people in real life
- `push()`: adds a new element to the end of the queue
- `pop()`: removes the queue's first element

__Deque:__ short for "double-ended queue", is a queue that can be pushed to and popped from both ends

__Set:__ an unordered collection of _non-repeatable_ values
- `add()`: adds an item to the set (if it is not already present)
- `contains()`: returns whether an item is in the set
- `remove()`: removes an item from the set (if the set contains it)

__Linked List:__ a collection of nodes pointing to each other in sequence
```C
typedef struct {
    int val;
    Node *next;
} Node;
```
- `val`: the value stored in the node
- `next`: a pointer to the next node in the sequence
- linked list operations are generally recursive in nature
- linked list forward traversal happens by moving a node forward as such: `curr = curr->next` -- linked lists are _not_ continuous!
- the last node in a linked list has `next` point to `NULL`

__Doubly-Linked List:__ a collection of nodes pointing to one another in sequence
```C
typedef struct {
    int val;
    Node *prev;
    Node *next;
} Node;
```
- `val`: the value stored in the node
- `prev`: a pointer to the previous node in the sequence
- `next`: a pointer to the next node in the sequence
- forward traversal: `curr = curr->next`
- backward traversal: `curr = curr->prev`
- bookended by `NULL` pointers

## Search Algorithms
__Linear Search:__ compares each value in a list to the search key one by one
- Time complexity: O(N)
- Works on both unsorted and sorted lists
- Has to traverse through the entire list if the key is not present in the list

__Binary Search:__ continuously divides a list into subsections and searches for a key by comparing it to the midpoint of the subsection
- Time complexity; O(log N)
- Only works on sorted lists
- Can be performed iteratively or recursively
- If the key is greater than the midpoint, next subsection is right of the midpoint
- If the key is less than the midpoint, next subsection is left of the midpoint
- If the key is the midpoint, return the key/true/index

## Sorting Algorithms
__Bubble Sort:__ Compares pairs down the list, swapping to put the greater element last, "bubbling" them forward to the end of the list
- O(N^2)
