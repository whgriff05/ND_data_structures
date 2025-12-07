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
    """
    Finds the cheapest flight plan from an origin to a destination using
    Dijkstra's algorithm.

    Args:
        origin: The starting city's ID.
        destination: The destination city's ID.
        graph: The graph representing flight connections and costs.

    Returns:
        A tuple containing the total cost of the cheapest flight and a plan
        (a dictionary mapping each city in the path to its predecessor).
    """
    frontier = [(0, origin)]  # (cost, city_id)
    costs = {origin: 0}
    plan = {}

    while frontier:
        cost, current_city = heappop(frontier)

        if current_city == destination:
            return cost, plan

        for neighbor, flight_cost in graph.get(current_city, {}).items():
            new_cost = cost + flight_cost
            if new_cost < costs.get(neighbor, inf):
                costs[neighbor] = new_cost
                plan[neighbor] = current_city
                heappush(frontier, (new_cost, neighbor))

    return inf, {}


def generate_flight_path(origin: int, destination: int, plan: Plan) -> Iterator[int]:
    """
    Recursively generates the flight path from origin to destination.

    Args:
        origin: The starting city's ID.
        destination: The destination city's ID.
        plan: A dictionary mapping each city in a path to its predecessor.

    Yields:
        The next city ID in the flight path.
    """
    if origin == destination:
        yield origin
    elif destination in plan:
        yield from generate_flight_path(origin, plan[destination], plan)
        yield destination

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