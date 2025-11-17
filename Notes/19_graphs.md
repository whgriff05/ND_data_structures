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

