# Linked Lists

Overall, there are two "classes" of data structures we will concern ourselves with
1. Array-based
2. Linked

Linked Data Structures we will use:
1. Linked Lists
2. Trees
3. Graphs

Linked Data Structures are generally recursive in nature
- Ex: a child of a Tree is a Tree
- Ex: the rest of a Linked List is a Linked List


## The Linked List

```C
typedef struct {
    int value;
    Node *next;
} Node;
```
The head of a list (`Node *head`) is statically allocated in the stack, but all the `Node`'s in the list itself are in the heap.

### Insert node at head of list

To insert new `Node n` at the head of the list,
1. Have `n->next` point to `head->next`
2. Have `head` point to `n`

### Remove node at head of list

To delete the first node at the head of the list,
1. Have a temporary variable `Node n` point to the head of the list
2. Set `head` to `head->next`
3. Free `n`

### Pointer Chasing

Move a pointer forward continuously until the null pointer at the end of the list is reached to traverse through the entire list\
Use `node = node->next` to move forward, `node += 1` might not work as `malloc()` doesn't allocate continuously\
__Linked Lists are not continuous!!__

### Stack using a Linked List

We want to implement operations (push, pop) at the head
- Doing so at the tail would require lots of traversal (loss of efficiency)

### Queue using a Linked List

Things will be made computationally easier if you maintain a tail pointer throughout the structure\
`push()` should be changing the __tail__ of the list\
`pop()` should be changing the __head__ of the list (don't have to re-traverse to reset the next pointer of next-to-last)\
If we wanted to use a queue with `push()` at the head and `pop()` at the tail, we should use a __doubly-linked list__ because you cannot look backward in a singly-linked list


## Doubly-Linked Lists


```C
typedef struct {
    int value;
    Node *next;
    Node *prev;
} Node;
```
These lists can be traversed both backwards and forwards

### Deque using a Doubly-Linked List

Now that we can traverse both backwards and forwards, it is equally easy to `push()` and `pop` at either the head or the tail of the list

### Doubly-Linked List with Dummy Elements

This allows us to not have to worry about moving too far in the list by having "bookends" to the list

Set __head__ and __tail__ to dummy elements, then have them point to the actual list values\
__head = [dummy] <-> vals... <-> [dummy] = tail__

### Is Empty

See if `head->next == tail` or `tail->prev == head`

### Insert after current node

Given a `current` node in the list and `new_node` to insert
1. `new_node->next = current->next`
2. `new_node->prev = current`
3. `current->next->prev = new_node`
4. `current->next = new_node`

### Popping the current node

Given a `current` node in the list to pop
1. `current->prev->next = current->next`
2. `current->next->prev = current->prev`
3. Create a temporary variable for `current->val`, `int val = current->val`
4. `free(current)`
5. `return val`



