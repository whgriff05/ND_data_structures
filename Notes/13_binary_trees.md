# Introduction to Binary Trees

```
           A
         /   \
       B       C
     /   \       \
    D     E       G
   / \   /       / \
  H   I J       L   M
 / \
N   O
```

Trees consist of __nodes/verticies__ and __edges__
- Top of the tree is the __root__
- Bottom nodes with no children are called __leaves__
- A node that has children is called a __parent__, and its descendents are called __children__

__Binary Trees__ are trees with nodes with strictly _0, 1, or 2_ children --> nodes have a left and/or right child

```py
class Node:
    def __init__(self, val: int, left: Node, right: Node):
        self.val = val
        self.left = left
        self.right = right
```

What are trees used for? __anything with hierarchical structure__
- family trees
- filesystem
- client/server
- the DOM of a website
- OOP inheritance hierarchy
- abstract syntax tree in a compiler

Binary trees have characteristics
- `perfect`: every internal node has two children, all leaf nodes are at the same level/depth
- `full`: every node has either 0 or 2 children
- `complete`: filled level by level, left to right

## Binary Search Trees
Assume no duplicates\
Used for looking things up\
Can be used as a set

The rules for a binary search tree:
- __every node > every node in left subtree__
- __every node < every node in right subtree__

```
/* 1, 2, 3 */
           2
         /   \
       1       3

           3
          /   
         2
        /
       1      

           1
             \
              2
               \
                3   
```

```
/* Values 10-100 by tens */
                                  50
                               /     \
                            /         \
                         20             80
                       /    \         /    \
                     /        \     /        \
                    10        30    60        90
                               \       \         \
                                40      70        100
```

### BST Search (recursive)
`def search(node: Node, key: int) -> bool`

Base cases:
- node is `None` --> return `False`
- node is the key --> return `True`

Recursive cases:
- key is less than the node --> return `search(node.left, key)`
- key is greater than the node --> return `search(node.right, key)`

### BST Insert (recursive)
`def insert(root: Node, key: int) -> Node`

Base cases:
- root is `None` --> return `Node(key, None, None)`
- root's value is the key --> return `root`

Recursive Cases:
- key is less than root --> `root.left = insert(root.left, key)`
- key is greater than root --> `root.right = insert(root.right, key)`