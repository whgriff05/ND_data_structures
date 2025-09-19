# Stacks, Queues, Deques, and Sets

### Stacks
__LIFO: last in, first out__\
Similar to a dynamic array, except its main features are `push()` and `pop()`

`push(Array *array, int value)`: add element to the top of the stack\
`pop(Array *array)`: remove top element from the stack\
`peek(Array *array)`: get top element's value without removing it\
`is_empty(Array *array)`: true if the stack is empty, false if not

### Queues
__FIFO: first in, first out__\
Similar to a dynamic array, it works like a line in real life\
Push and pop work on separate ends

Complexities
|Function|Time|Space|
|-|-|-|
|`push()`|O(1)|O(1)|
|`pop()`|O(N)|O(1)|
|`front()`|O(1)|O(1)|
|`is_empty()`|O(1)|O(1)|

### Deques
A double-ended queue, you can push and pop from either end

### Sets
An unordered collection of __non-repeatable__ items

`add(Set *set, int value)`: add value to the set
`contains(Set *set, int value)`: true if value is in the set
`remove(Set *set, int value)`: removes value from set

Complexities
|Function|Time|Space|
|-|-|-|
|`add()`|O(1)|O(1)|
|`contains()`|O(N)|O(1)|
|`remove()`|O(N)|O(1)|


