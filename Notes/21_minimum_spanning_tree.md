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


