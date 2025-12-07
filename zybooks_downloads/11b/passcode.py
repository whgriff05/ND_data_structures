#!/usr/bin/env python3

import sys

from collections import defaultdict, deque

# Types

Graph   = dict[int, set[int]]
Degrees = dict[int, int]

# Functions

def read_graph(stream) -> Graph:
    # TODO:
    pass
    """
    Reads a graph from a stream, where each line represents a dependency.
    '123' means 1->2, 1->3, 2->3.
    """
    graph = defaultdict(set)
    for line in stream:
        line = line.strip()
        if not line:
            continue
        for i, source in enumerate(line):
            for target in line[i+1:]:
                graph[int(source)].add(int(target))
    return dict(graph)

def compute_degrees(graph: Graph) -> Degrees:
    # TODO:
    pass
    """
    Computes the in-degree for each vertex in the graph.
    """
    nodes = set(graph.keys())
    for destinations in graph.values():
        nodes.update(destinations)
    
    degrees = {node: 0 for node in nodes}

    for destinations in graph.values():
        for dest in destinations:
            degrees[dest] += 1
            
    return degrees

def find_passcode(graph: Graph) -> list[int]:
    # TODO:
    pass
    """
    Performs a topological sort on the graph using Kahn's algorithm.
    """
    degrees = compute_degrees(graph)
    
    # Initialize frontier with nodes having an in-degree of 0
    frontier = deque([node for node, degree in degrees.items() if degree == 0])
    
    passcode = []
    while frontier:
        current = frontier.popleft()
        passcode.append(current)
        
        for neighbor in sorted(list(graph.get(current, set()))):
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                frontier.append(neighbor)
                
    return passcode

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    with open(args[0], 'r') as stream:
        graph = read_graph(stream)
        
    passcode = find_passcode(graph)
    print(''.join(map(str, passcode)))

if __name__ == '__main__':
    main()