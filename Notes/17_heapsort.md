# Heap Sort

Idea:
- start with an unordered array
- push each value onto a heap
- pop until empty
- done!

However, you don't need to push values onto a separate array, you can instead just do this by bubbling
- Bubble all non-leaf nodes into place

__Heapifying an Array__

Ex: `[5, 5, 7, 3, 9, 2, 8]`
- right subtree: `[7, 2, 8]` --> `[8, 2, 7]`
- left subtree: `[5, 3, 9]` --> `[9, 3, 5]`
- whole tree: `[5, 9, 8, 3, 5, 2, 7]` --> `[9, 5, 8, 3, 5, 2, 7]`

__Array-Based Heap Sort__

After heapifying, the maximum value will be at index `0`\
Then, swap the maximum value with the value at the last index in the array\
From there, heapify the array again from `0` to `(last index - 1)`, keeping a "sorted" portion at the end of the array\
Loop this process of heapifying and swapping until the last index is the beginning of the array\
Sorts the array __in place__ --> Spatial Complexity: O(1)
