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

__Balance Factor:__ `|self.left.height - self.right.height|`
- Rebalance when the balance factor is more than 1

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