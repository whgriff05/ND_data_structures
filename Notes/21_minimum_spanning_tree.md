# Prim's Minimum Spanning Tree Algorithm

## Revised Djikstra's Algorithm

We want to return info to construct the actual shortest path, not just get the total shortest distance

__Before:__
- Visited was a dict `{vertex: distance}`
- Frontier was a min heap of `(distance, vertex)`

__After:__
- Visited is a dict `{vertex: source}`
- Frontier is a min heap of `(distance, vertex, source)`

## Minimum Spanning Tree

Frontier-based algorithm\
Uses an __undirected__ graph

Similar to Djikstra's SSSP\
In choosing next vertex, choose neighbor with lowest weight edge

### What data stuctures do we use for `frontier` and `visited`?

 `visited`: dictionary of `{node: predecessor}`

 `frontier`: priority queue/min heap of `(weight, current node, predecessor)`

 ## What is the difference between Djikstra and MST?

 __MST:__ Find the total weight in the edges traveled overall
 - returns the same regardless of starting node

 __Djikstra:__ Find the shortest path (total weight) in the edges traveled from a start node to all other nodes
 - output depends on starting node

 These algorithms may end up in the same path traversal, but also may not

## Summary of Prim's Algorithm

Minimum Spanning Tree

Similar to Djikstra

__Time Complexity: O(E log E)__\
where E is the number of __edges__


