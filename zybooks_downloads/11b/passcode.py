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

def compute_degrees(graph: Graph) -> Degrees:
    # TODO:
    pass

def find_passcode(graph: Graph) -> list[int]:
    # TODO:
    pass

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