#!/usr/bin/env python3

import sys

from collections import defaultdict
from heapq       import heappop, heappush
from typing      import Iterator
from math import inf

# Types

Graph = dict[int, dict[int, int]]
Plan  = dict[int, int]

# Functions

def read_graph(stream) -> Graph:
    graph = defaultdict(dict)
    for line in stream:
        line = line.strip().split()
        graph[int(line[0])][int(line[1])] = int(line[2])

    return dict(graph)


def find_cheapest_flight_plan(origin: int, destination: int, graph: Graph) -> tuple[int, Plan]:
    pass


      


def generate_flight_path(origin: int, destination: int, plan: Plan) -> Iterator[int]:
    # TODO:
    pass

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]
    
    origin      = int(args[0])
    destination = int(args[1])
    graph_fname = args[2]

    with open(graph_fname) as stream:
        graph = read_graph(stream)
    
    cost, plan = find_cheapest_flight_plan(origin, destination, graph)
    stops = generate_flight_path(origin, destination, plan)
    print(f'Cost: ${cost}, Plan: {" -> ".join(map(str, stops))}')

if __name__ == '__main__':
    main()