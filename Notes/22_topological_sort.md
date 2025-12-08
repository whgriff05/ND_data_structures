# Kahn's Topological Sort Algorithm

This is a __priority scheduling__ algorithm

```
/* Ex: given this direction, give a possible ordering */

A --> B -|
         |---> E
C --> D -|

/* Results:
   A B C D E
   A C B D E
   C D A B E
   ...
*/
```

## Degree of a Vertex

__degree:__ number of edges incident on a vertex (edges pointing in)

For a node with `x` edges out and `0` edges in: degree = `0`

For a node with `x` edges out and `n` edges in: degree = `n`

Construct a degree dict of `{node: degree}`

## What about `frontier` and `visited`?
`frontier`: stack (you can use a queue or a stack, but we want a data structure with O(1) for push and pop)

`visited`: list

## Kahn's Topological Sort Algorithm

Construct a table of degrees for each node

Add vertices with degree 0 to frontier

While frontier is not empty
- pop the vertex
- append vertex to visited
- for each neighbor of vertex
    - decrement degree
    - if degree is 0, append to frontier

## Detecting Cycles

```
/* Ex: Basic Cycle */

A ---> B ---> C
       ^      |
       |-------
```

For this example, after passing A, the algorithm will stop because B's starting degree will be `2` and after decrementing, it will be `1`. Since no vertices have degree `0`, the algorithm stops

To detect a cycle, see if the length of the visited list is less than the number of vertices

## Complexity of Kahn's Algorithm

`O(V + E)`

Mostly linear dependent on number of vertices/edges
