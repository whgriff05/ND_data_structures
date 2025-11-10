# Heaps

__Binary Trees__, not Binary Search Trees
- complete (filled left to right)
- operations: push and pop
- usage: priority queue

__Max Heap:__ every node's key is greater or equal than that of its children

```
/* Max Heap */
    8
   / \
  6   3
 / \
2   2
```

__Min Heap:__ every node's key is less or equal than that of its children

```
/* Min Heap */
    3
   /  \
  6     4
 / \   /
8   7 8
```

## Push Operation
```
/* Max Heap */
    6
   / \
  5   2
 / \
2   3
```

Ex: We want to push `8`

To keep a full tree, we need to push it to the left child of 2
```
/* Max Heap */
    6
   /  \
  5     2
 / \   /
2   3 8
```

But, now the 8 is in the wrong position; it needs to be __percolated/bubbled__ up (swap parent and child)
```
/* Max Heap */
    8
   /  \
  5     6
 / \   /
2   3 2
```

__Computational Complexity:__ O(log N)

## Pop Operation
```
/* Max Heap */
    6
   / \
  5   2
 / \
2   3
```
Ex: We want to remove `6`

Copy the deepest, furthest right node to `6` and __percolate/bubble__ `3` downward to make the tree a max heap again
```
/* Max Heap */
    3
   / \
  5   2
 / 
2   
```

After percolation:
```
/* Max Heap */
    5
   / \
  3   2
 / 
2   
```

## Implementation in Python
Since we need to keep track of both parent and child, we're __NOT__ representing this as a linked data structure\
Instead, we are using an array for this:

```
/* Heap */
    A
   /  \
  B     C
 / \   /
D   E F
```

The tree above becomes: `[A, B, C, D, E, F]`

If you know the index of a parent (i):
- left child's index: `2i + 1`
- right child's index: `2i + 2`

If you know the index of a child (j):
- parent's index: `(j-1) // 2` (floor division)

Since we can calculate the parent from a child and the children from a parent, we do not need a linked data structure to represent this heap

