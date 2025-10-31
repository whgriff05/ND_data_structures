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

Types of Traversals
- Preorder Traversal: `operation(curr)`, `visit(curr.left)`, `visit(curr.right)`
- Inorder Traversal: `visit(curr.left)`, `operation(curr)`, `visit(curr.right)`
- Postorder Traversal: `visit(curr.left)`, `visit(curr.right)`, `operation(curr)`
- Level Order Traversal: Visit the tree nodes level by level left to right

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

### BST Inorder Traversal (recursive)
`def inorder(root: Node)`

An inorder traversal prints all left children, the root node, and then all right children

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

/* prints 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 */
```

Base case:
- root is `None` --> return

Recursive cases:
- `inorder(root.left)` --> traverse all left children
- `print(root)` --> print the root node
- `inorder(root.right)` --> traverse all right children

### BST Height (recursive)
`def height(root: Node) -> int`

The __height__ of a BST is the number of edges traversed from root to furthest leaf
- 1 node tree has height = 0
- 1 node with 2 children has height = 1
- __empty tree has height = -1__

Base case:
- root is `None` --> return `-1`

Recursive cases:
- get the maximum value of the heights of the left children and right children --> `height_max = max(height(root.left), height(root.right))`
- return the maximum value + 1 (to account for the current node's height) --> return `height_max + 1`

### Removing a BST Node
`root = remove(root, key)`

Base case:
- root is `None` --> return `None`

Recursive cases:
- root is NOT key
  - key < root.key --> `root.left = remove(root.left, key)`
  - key > root.key --> `root.right = remove(root.right, key)`
- root is key
  - root has no children --> return `None`
  - root has 1 child --> return `root.(left/right)`
  - root has 2 children --> move the right child to the root
    - convention: favor the right child
  - root has 2 children AND the height > 1 --> move the next smallest node after the key to the root, remove that new key from the right subtree


## Depth-First (DFS) and Breadth-First (BFS) Search of Binary Trees

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

__Depth-First:__ Continuing as far down in a node's children before moving onto the next child (called a _"preorder traversal"_)
- Order: 50, 20, 10, 30, 40, 80, 60, 70, 90, 100

__Breadth-First:__ Search by level (called a _"level order traversal"_)
- Order: 50, 20, 80, 10, 30, 60, 90, 40, 70, 100

### Depth-First Search (DFS)

Recursively:
```py
def dfs(root):
  operation(root) # Perform operation/etc...
  dfs(root.left)
  dfs(root.right)
```

Iteratively:
- we need a "frontier" (usually a stack) to keep track of what nodes to visit
```py
def dfs(root):
  frontier = Stack()
  visited = []

  frontier.push(root)

  while frontier:
    curr = frontier.pop()

    operation(curr) # Perform operation/etc...
    visited.append(curr)

    frontier.push(curr.right)
    frontier.push(curr.left)
```

### Breadth-First Search (BFS)

Iteratively:
```py
def bfs(root):
  # Use a queue for correct visiting order
  frontier = Queue() 
  visited = []

  frontier.queue(root)

  while frontier:
    curr = frontier.dequeue()

    operation(curr)
    visited.append(curr)

    frontier.queue(curr.left)
    frontier.queue(curr.right)
```