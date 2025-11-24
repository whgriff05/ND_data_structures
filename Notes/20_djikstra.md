# Djikstra's Shortest Path Algorithm

Djikstra is __single-source:__ you start at a single node\
It finds the shortest path/distance between two nodes (concerning itself with __weighted (and typically directed) graphs__)

Uses a __Priority Queue__ to determine which path to take

## Weighted Graph Adjacency List
```
  B ----- D
 /  \     |
A     \   |
 \      \ |
  C ----- E
```

```py
{
    A: {B: 4, C: 1},
    B: {},
    C: {E: 1},
    D: {B: 1},
    E: {B: 1, D: 1}
}
```

## Pseudocode for Djikstra

```
while frontier not empty:
    pop vertex with lowest total distance
    if not already visited:
        store (vertex: distance) in visited
        for each non-visited neighbor:
            push (distance, neighbor vertex) to frontier
```

## Time Complexity

Edges dominate: for `V` nodes, max `V^2` edges

`E` edges * push/pop min-heap = `O(E log E)`

Zybooks says that the time complexity is `O(E log V)`

Same thing because we are taking the logarithm of a value squared, and time complexity order ignores the multiplier

