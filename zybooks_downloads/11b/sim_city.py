#!/usr/bin/env python3

''' sim_city.py - Sim City '''

import sys

from collections import defaultdict
from heapq       import heappop, heappush
from math        import dist

# Types

Points = list[tuple[int, float, float]]
Graph  = dict[int, dict[int, float]]
Edges  = dict[int, int]

# Functions

def read_points(stream) -> Points:
    # TODO:
    pass

def build_graph(points: Points) -> Graph:
    # TODO:
    pass

def construct_mst(graph) -> tuple[float, Edges]:
    """
    Constructs a Minimum Spanning Tree (MST) for a given graph using
    Prim's algorithm.

    Args:
        graph: The graph for which to construct the MST.

    Returns:
        A tuple containing the total weight of the MST and a dictionary
        representing the edges of the MST, where the key is the
        destination and the value is the source.
    """
    if not graph:
        return 0.0, {}

    start_node = next(iter(graph))
    frontier = [(0.0, start_node, start_node)]  # (weight, node, source)
    visited = {}
    total_weight = 0.0

    while frontier and len(visited) < len(graph):
        weight, node, source = heappop(frontier)
        if node in visited:
            continue
        visited[node] = source
        total_weight += weight
        for neighbor, edge_weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heappush(frontier, (edge_weight, neighbor, node))

    if start_node in visited:
        del visited[start_node]

    return total_weight, visited

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    points_fname = args[0]

    with open(points_fname) as stream:
        points = read_points(stream)
    graph = build_graph(points)
    total_length, edges = construct_mst(graph)
    print(f'Length: {total_length:.2f}', end=' ')
    print('Edges: '+', '.join(f'{p1}-{p2}' for p1, p2 in edges.items()))

if __name__ == '__main__':
    main()