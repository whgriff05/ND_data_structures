# AVL Trees

__AVL (Adelson-Velsky, Landis) Tree:__ self balancing tree
- used to keep trees O(log N) / keep trees from becoming glorified linked lists

## Key Idea: Rotation

You can rotate a tree around a node while maintaining BST ordering properties

```
/* Ex1 Rotate Left: */

1             
 \
  2      --->     2
   \             / \
    3           1   3


/* Ex2 Rotate Right: */

    3
   /
  2      --->     2
 /               / \
1               1   3
```

Sometimes nodes are "decoupled" and "recoupled" to new nodes:

## Detecting Imbalance

A new `Node` class:
```py
class Node:
    def __init__(self, key, left, right, height=0):
        self.key = key
        self.left = left
        self.right = right
        self.height = height   # Will be automatically calculated
```

When we add, remove, or rotate, we recursively update the heights of the nodes

__Height:__ number of edges from leaf to root
- leaf height = 0
- null height = -1

__Balance Factor:__ `self.left.height - self.right.height`
- Rebalance when the balance factor is more than 1 or less than -1

### 4 Possible Cases of Imbalance
```
/* Left-Left */
    3
   /
  2      --->     2
 /               / \
1               1   3

/* Right-Right */
1             
 \
  2      --->     2
   \             / \
    3           1   3

/* Left-Right */
  3                  3
 /                  /
1        --->      2        --->     2
 \                /                 / \
  2              1                 1   3

/* Right-Left */
1                1
 \                \
  3      --->      2        --->     2
 /                  \               / \
2                    3             1   3
```

Naming Convention: (child-causing-imbalance direction)-(grandchild-causing-imbalance direction)

__Left-Left Fix:__ rotate right\
__Right-Right Fix:__ rotate left\
__Left-Right Fix:__ rotate left on the left child, then rotate right the whole thing\
__Right-Left Fix:__ rotate right on the right child, then rotate left the whole thing

## Functions for Implementation
`_get_height(self, node)`
- gets the height of the node
- `None` returns -1 
- otherwise return the stored height `node.height`

`_update_height(self, node)`
- the height of the node is 1 + the maximum height of left and right
- `1 + max(_get_height(node.left), _get_height(node.right))`

`_balance_factor(self, node)`
- gets the balance factor of a node
- return the difference of the children's heights
- if there isn't a node, return 0

`_rotate_left(self, z)`
```
   z                    y
  / \                  / \
T1   y      --->      z   T3
    / \              / \  
  T2  T3           T1   T2
```

- get the pieces
    - `y = z.right`
    - `t2 = y.left`
- perform the rotation
    - `y.left = z`
    - `z.right = t2`
- update heights
    - `_update_height(z)`
    - `_update_height(y)`
- return the new root

`_rotate_right(self, z)`
```
     z                   y
    / \                 / \
   y  T3    --->      T1   z
  / \                     / \
T1   T2                 T2   T3
```

- get the pieces
    - `y = z.left`
    - `t2 = y.right`
- perform the rotation
    - `y.right = z`
    - `z.left = t2`
- update heights
    - `_update_height(z)`
    - `_update_height(y)`
- return the new root

`_balance(self, node)`
- left heavy: `_balance_factor(node) > 0`
    - left-left: `_balance_factor(node.left) > 0`
    - left-right: `_balance_factor(node.left) < 0`

