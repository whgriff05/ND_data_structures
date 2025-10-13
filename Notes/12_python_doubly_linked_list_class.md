# Python Doubly-Linked List Class

Recall a doubly linked list:\
Head: `[dummy] <-> [items...] <-> [dummy]` :Tail

For this, we will have a `Node` class and a `List` class

## Node Class and Constructor Method

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 'None' is Python's 
        self.prev = None # null value/pointer
```

To instantiate: `x = Node(7)`\
__You don't include the `self` parameter when instantiating the variable!__

## Public and Private Methods

In Python, the convention is to start the function name with an underscore `_` to denote a "private" method

## Doubly-Linked List Class

### Outline
Constructor:
- `DoublyLinkedList()`

Private:
- `_insert_after(node, data)`
- `_pop_node(node)`

Public:
- `append(data)`
- `insert(index, data)`
- `pop(index)`
- `clear()`
- `index(data)`

Magic Methods:
- `__str()__`
- `__bool()__`
- `__contains(data)__`
- `__iter()__`
- `__next()__`

### Code
```py
class DoublyLinkedList:
    # Constructor for an empty list
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        # Used for __iter__ which supports the syntax:  for data in dll:
        self.iter_state = None
    
    # Insert a new node after the given node
    # This is a private method and should not be called directly from outside the class
    def _insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
    
    # Remove the given node and return its data
    # This is a private method and should not be called directly from outside the class
    def _pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.data
    
    # Insert after the last node
    def append(self, data):
        self._insert_after(self.tail.prev, data)
  
    # Insert before the node at the given index
    def insert(self, index, data):
        node = self.head
        for _ in range(index):
            if node == self.tail:
                raise IndexError
            node = node.next
        self._insert_after(node, data)

    # Remove and return the data of the node at the given index
    def pop(self, index):
        node = self.head.next
        for _ in range(index):
            if node == self.tail:
                raise IndexError
            node = node.next
        return self._pop_node(node)  

    # Remove all nodes except head and tail
    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Return the index of the first node with the given data
    def index(self, data):
        index = 0
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return index
            index += 1
            node = node.next
        return -1

    # Return a string representation of the list
    # Supports the following syntax to convert a list to a string:  str(dll)
    def __str__(self):
        return " ".join([str(x) for x in self])


    # Return True if the list is not empty
    # Supports the if dll: syntax to check if the list is not empty
    def __bool__(self):
        return self.head.next != self.tail
    
    # Return True if the list contains a node with the given data
    # Supports the syntax:  data in dll
    def __contains__(self, data):
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return True
            node = node.next
        return False

    # Initialize the iterator state
    # Supports the syntax:  for data in dll:
    def __iter__(self):
        self.iter_state = self.head.next
        return self
    
    # Return the next data from the iterator
    # Supports the syntax:  for data in dll:
    def __next__(self):
        if self.iter_state == self.tail:
            raise StopIteration
        data = self.iter_state.data
        self.iter_state = self.iter_state.next
        return data
```
