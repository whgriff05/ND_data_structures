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
    # TODO:
    pass

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