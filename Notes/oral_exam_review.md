# Oral Exam Review

## Review of Midterm Exam

```C
/* Consider the recursive C function to print a string in reversed */

void print_reversed(char *a) {
    if (CODE_1) {
        CODE_2
    }
}

/* My answer */
CODE_2 = {
    printf("%c", *a)
    print_reversed(a+1);
}

/* Solution */
CODE_2 = {
    print_reversed(a+1);
    printf("%c", *a)
}
```

My solution was wrong because all it would do is print the string in the correct order. The recursive call looking forward in the string must be first to print the later characters first.

```
Suppose that quicksort is used to sort an array of 2,000 elements. On average, what number is closest to number of swaps?

/* My answer */
200

/* Solution */
2,000 or 20,000
```

My solution was wrong because it incorrectly calculated using the time complexity `O(n log n)` or `2000 * ln(2000) = ~15000`

## Huffman Code Homework Review

`heap.py`
- `percolate_up()`
    - While the current node is not at the top
        - Calculate the parent node's index
        - If the current node is greater than the parent node
            - Swap the current and parent nodes
        - Set the current node index to the parent node's original index
- `percolate_down()`
    - Calculates the current node's child's index
    - While the child node exists (is within the heap array)
        - Set the maximum value to the current node and the maximum index to the end
        - Loops through each child of the current node getting the maximum value/index of the children
    - If the children are bigger than the parent
        - The bigger child swaps with the parent
        - The next current node index is passed down and its new child index is calculated
- `insert()`
    - Appends the value to the end of the heap array
    - Percolates the value up the heap array
- `remove()`
    - Pops the maximum value from the heap array
    - Gets the last value in the heap array and adds it to the top, then percolating it down

`huffman.py`
- `build_frequency_table()`
    - Initialize an empty dict
    - Count every character using the dict {letter: count}
- `huffman_build_tree()`
    - Get the frequency table of the string
    - Initialize a `MaxHeap()`
    - For every character and count, append a node of (character, frequency) to the heap
    - While there is more than one node on the heap
        - Pop two nodes
        - Calculate their frequency sum
        - Create a parent node of the two keys and the frequency sum
        - Add it to the heap
    - Return the final singular combined node
- `huffman_get_codes()`
    - If the root node is None, return an empty dictionary
    - If the chilren are None, return a dictionary of {key: prefix}
    - Return the union of the dicts returned by the recursive calls on the children of the root node with a `0` or `1` attached to the prefix respectively
- `huffman_compress()`
    - Build the tree and get the codes
    - For every character in the string
        - Append the huffman encoding to the output string
    - Return a tuple of (huffman string, huffman tree, huffman dict)
- `huffman_decompress()`
    - For every bit in the huffman string
        - Depending on the value of the bit, move the node pointer to the left or right child
        - If a leaf node is reached, add the node's key character to the output string
    - Return the output string
- `huffman_compression_ratio()`
    - Calculate the original bit length (`char * 8`)
    - Calculate the huffman bit length (`char * 1`)
    - Return the ratio of original to huffman

## Final Project Notes

### Summary

I created a program to count misspellings in text files comparing the effectiveness of certain data structures to use as word dictionaries. The program can individually use a Trie, a Python Dict, and a Python List to count and track misspellings, returning the times of dictionary initialization and misspelling counting. It can also test each data structure at once, providing comparison graphs of times of initialization and misspelling counting.

### Interesting Notices

In the initialization times using the same word file for the dictionary, the Trie took the slowest amount of time, orders of magnitude longer than both the list and the dict.\
In counting misspell times, the dict was the quickest, and the trie came second, but the list was orders of magnitude slower than both of them. 

### Challenging Notices

Finding and writing the edge cases for the unit tests.\
Writing the classes in such a way to make it so the same methods could be used to add items to the trie, dict, and list.

## Notes about each Data Structures topic

### Pointers and Regions of Memory
- Pointers
    - A pointer is a variable of the form `type *ptr`
        - `*` indicates pointer
    - A variable's address can be acquired using `&`
        - `ptr = &x`
    - To see what a pointer points at, dereference using `*`
        - `printf("%d", *ptr)`
    - Arrays are contiguous blocks of memory with the name being a pointer to the first address
    - Adding/subtracting to a pointer increments/decrements it by `sizeof(type)` bytes away
- Regions of Memory
    - The stack is automatically managed/garbaged collected, but the heap is not
    - A __segmentation fault__ is attempted access to memory without specific permissions

|Memory|Region|What's Stored There|
|-|-|-|
|0xFFF...|Stack (grows ↓)|functions, local variables|
|↓|...||
| |Heap (grows ↑)|dynamic memory: malloc, calloc, free|
|↑|Data|global variables, static variables, string constants|
|0x000...|Code|executable machine code for the program|

### Abstract Data Types
- An __ADT__ is a type defined by supported operations and internal contents
    - They have internal details hidden to the user
    - Related to the idea of object-oriented programming
- In C, ADTs are usually implemented with `structs`

### Stacks, Queues, and Sets
- Stack: LIFO/FILO data structure (item is either pushed to or popped from top of stack)
- Queue: FIFO data structure (like how a line works in real life)
- Set: unordered collection of non-repeatable items

### Basic Time Complexity Analysis
- General Big O Notation Rules
    - Ignore constants and coefficients `O(6N+5) --> O(N)`
    - Only care about the highest degree term `O(N^2 + N) --> O(N^2)`
    - Take the product of multiplied items `O(N * N) --> O(N^2)`
- O(1)
    - Arithmetic operations
    - Variable assignments
    - Loops with fixed number of iterations
    - Array indexing
    - Comparison
- O(N)
    - Loops with variable range
- O(N^2)
    - Nested loops with variable range
- O(log N)
    - Divide and conquer algorithms
    - Binary Search
- O(N log N)
    - Divide and conquer algorithms with a O(N) step
    - Merge Sort
    - Quick Sort
- O(c^N)
- O(N!)

### Recursive Functions
- __Recursive function:__ a function that calls itself
- They have a __base case__, where they can reach an end to the recursive calls, and a __recursive call__ (or multiple), where the function is called again on a smaller subset of the original input
- Offer a hidden space complexity: the __call stack__ in a recursive function will fill up with all recursive calls
- Iterative versions often use some type of tracking variable or stack/queue to keep track of the original data while still allowing subsets

### Sorting Algorithms
- Bubble Sort
    - Compare pairs, swapping to put the greater on the right/lesser on the left (bubbling them down to a sorted end)
- Insertion Sort
    - Compares each item to the entire unsorted portion of the array, inserting to its corresponding place
    - Builds a sorted portion on low end
- Selection Sort
    - Finds the lowest unsorted value, swaps with the lowest index
    - Builds a sorted portion on low end
- Merge Sort
    - Divides and conquers into pairs of numbers, then merges pairs in a sorted fashion, then merges merges in a sorted fashion...
    - Recursive
- Quick Sort
    - In Place
    - Chooses a pivot value and swaps numbers around to be lesser/greater than pivot value
    - Divides and conquers to cover each pivot value
- Heap Sort
    - Push each value to a min/max heap, pop the top until it's empty
    - OR
    - Continue percolating all non-leaf nodes of subtrees of the heap into a sorted place, building up a sorted position at the end of the heap array
- Adaptibility: takes less time/does less work on a partially sorted array
    - Bubble sort can be made adaptable (keeping track of where the sorted portion begins)
    - Insertion Sort
- Stability: if two elements have the same value, their order will not be changed
    - Bubble Sort
    - Insertion Sort
    - Merge Sort

### Linked Lists
- A recursive data structure where each node contains a pointer to its successor
- __Pointer chasing:__ to move forward, use `node = node->next`
- To insert a node in the list (assuming doubly-linked)
    - Get pointers to the current node and new node
    - Link the new node's next and previous to the current's next and current
    - Link the current's next's previous to the new node
    - Link the current's next to the new node
- To remove a node from the list (assuming doubly-linked)
    - Get pointer to the current node
    - Set the current's previous's next pointer to the previous node
    - Set the current's next's previous pointer to the next node
    - Create a temporary value for the variable
    - Free the current node

### How Hashing Works
- __General Idea:__ Converts some key into a numerical value to be used in finding an array index
    - `index = hash(k) % (size of hash table)`
- Multiply-Right Shift Hashing
    - Given a original key `k`
    - Multiply `k` by some large arbitrary (usually prime) number `A`
    - The result is naturally truncated to X amount of bits (X-bit computing; e.g. 64-bit computing)
    - The result is bit-shifted to the right `p` number of times (dividing the number by `2^(X-p)`) to get the "most significant bits" of the number (the highest degree bits) and to delete the rest of the less significant bits
    - Overall formula: `(A*k % 2^X) / (2^X-p)`
- Collision Resolution
    - __Collision:__  when two values of `k` hash to the same index
    - __Chaining__ makes the hash table an array of linked lists, so that when a duplicate index is hashed, the result is added to the tail of the linked list at that index
    - __Linear Probing__ is where all values are stored directly in the internal hash table array. If a duplicate index is hashed, the result will be added at the next available index

### Binary Trees
- Types of Traversals
    - Preorder Traversal: `operation(curr)`, `visit(curr.left)`, `visit(curr.right)`
    - Inorder Traversal: `visit(curr.left)`, `operation(curr)`, `visit(curr.right)`
    - Postorder Traversal: `visit(curr.left)`, `visit(curr.right)`, `operation(curr)`
    - Level Order Traversal: Visit the tree nodes level by level left to right
- Inversion
    - Swap each node's right and left child
    - Mirror of the tree

### Binary Search Trees
- Binary tree with the following rules
    - Every node __>__ Every node in __left__ subtree
    - Every node __<__ Every node in __right__ subtree
- Insertion 
    - Continue down the tree following the rules until a leaf node is reached
    - Insert the node with the value corresponding to the rules
- Deletion
    - Recursive function
    - When the root node is the key to be deleted
        - If the root is a leaf, return None to remove it
        - If the root has 1 child, return the child to replace it
        - If the root has 2 children, favor the right child and move it to the root
- Balanced Tree vs Unbalanced Tree
    - An unbalanced tree appears more or less a linked list, and inherits O(N) general time complexity
    - A balanced tree has O(log n) general time complexity

### Greedy Algorithms
- A __greedy algorithm__ is an algorithm that looks for the best possible solution from where it is currently at
- It makes a "locally optimal choice" in hope of a "globally optimal outcome"
- It can fail when the locally optimal choice reaches a dead end, or when the problem is better solved looking at the big picture/long term

### Heaps
- Priority Queue
    - Keeps the lowest/highest value on the top
- Heap Sort
    - Since a heap automatically keeps the lowest/highest value on top, either continue popping the top to sort or heapify the list in place
- Heapification
    - Continue percolating all non-leaf nodes of subtrees of the heap into a sorted place, building up a sorted position at the end of the heap array

### Graph Algorithms
- Depth-First Search
    - Explore as "deep" as you can (continuing down children) before moving to the next child of a given node
    - __Frontier:__ stack
    - __Visited:__ set
- Breadth-First Search
    - Explore as "broad" as you can (going through all direct children of a given node) before continuing to sub-children
    - __Frontier:__ queue
    - __Visited:__ set
- Djikstra's Shortest Path Algorithm
    - Finds the shortest path between a starting node and all nodes on the graph
    - __Frontier:__ priority queue/min heap `Heap((distance, node))`
    - __Visited:__ dict/hash table `{node: distance}`
- Prim's Minimal Spanning Tree Algorithm
    - Creates a tree that covers the least total distance between nodes on the graph
    - Same output regardless of starting node
    - __Frontier:__ priority queue/min heap `Heap((weight, current node, predecessor))`
    - __Visited:__ dict/hash table `{node: predecessor}`
- Kahn's Topological Sort Algorithm
    - 
    - __Frontier:__ 
    - __Visited:__











