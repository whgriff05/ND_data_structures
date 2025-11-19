# Graphs

Defined by sets of __vertices__ and __edges__\
G = (V, E)

```
/* G = (6, 7) */

1 -- 2 -- 5
|    |     \
|    |      6 
3 -- 4 ---/
```

### Applications of Graphs
- Knowledge graphs
- Maps/GPS
- Social Networks
- Internet/Web
- Road Planning
- Scheduling/Dependency Graphs

### Graph Properties
- Undirected vs Directed (Arrows on edges show one way traversal)
- Unweighted vs Weighted (Numbers on edges showing "distance"/cost between edges)
- Cyclic vs Acyclic (Only on directed graphs, whether a cycle forms)
- Connected vs Disconnected (Can be split into two separate graphs)
- Simple vs Nonsimple (Nonsimple: Self-directed edges; edge that points back at itself)

### Adjacency List Representation
```
0 --- 1
|   / | \
|  /  |  2
| /   | /
4 --- 3
```

```py
graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}
```

### Edge List File Format
```
0 --- 1
|   / | \
|  /  |  2
| /   | /
4 --- 3
```
```
5 7  /* (number of nodes, number of edges) */
0 1  /* starting node, ending node */
1 2   .
2 3   . 
3 4   .
4 0
1 4
1 3
```

### Adjacency Matrix
```
0 --- 1
|   / | \
|  /  |  2
| /   | /
4 --- 3
```

```
--         --
| 0 1 0 0 1 |
| 1 0 1 1 1 |
| 0 1 0 1 0 |
| 0 1 1 0 1 |
| 1 1 0 1 0 |
--         --
```
0 = no connection from row to column\
1 = connection from row to column


## Graph Breadth-First Search

From any given node, we will explore all edges coming out of that node before visiting any edges from a child of that node

Use a FIFO data structure to hold the "frontier" of next nodes to visit (FIFO = __queue__)

```
/* BFS: 1, 2, 3, 4, 5, 6, 7 */

   1
  /|\
 / | \
2  3  4
|  |  |
5  6  7
```

## Graph Depth-First Search

From any given node, explore as far "deep" as you can (continuing down child and subchildren) before moving to the node's next child

Use a LIFO data structure to hold the "frontier" of next nodes to visit (LIFO = __stack__)

```
/* DFS: 1, 2, 5, 3, 6, 4, 7 */

   1
  /|\
 / | \
2  3  4
|  |  |
5  6  7
```

## Dealing with Cycles

When encountering a node with a cycle as a neighbor, if the node has been visited, don't push it to the frontier

If the neighbor is already in the frontier, don't push it again to the frontier (nodes should only appear in the frontier __once__)

## Implementing this in Python

We're going to use a __deque__ to push or pop from either end of the array in __O(1)__ time

A deque in Python strings together small dynamic arrays in a linked list format
