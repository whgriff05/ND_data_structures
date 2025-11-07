# Generators and Iterators

## Problem we want to solve
- We want to iterate through objects in a data structure (ex: tree)
- We want to get them one at a time
- We want to use the `for ... in ...` protocol

## Two Approaches
Old Way
- `__iter__()` and `__next__()`

New Way
- Uses a generator
- Only needs `__iter__()`

## Example: Linked List (Old Way)
```py
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        self.current = self.head
        return self # IMPORTANT
    
    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration # Exception to stop the iterator
```

## Why use a generator?
- Simplifies the process
- Don't need `__next__()`
- New keywords: `yield` and `yield from`
    - `yield` returns a value BUT does not exit the function. The state of the function is saved and does not continue running until the next function call. `yield` also turns a function into a __generator__ object
    - `yield from` is the same thing as `yield` but applies to a function



