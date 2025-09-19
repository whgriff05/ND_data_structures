# Recursion and Recursive Algorithms

__Recursion:__ An algorithm that breaks up problems into smaller sub-problems and applies itself continuously
- Needs a __base case__ when the problem cannot be subdivided further

__Why do we use recursion?__
- Useful for structures that are also recursive (like trees)
- Usually, recursion does __not__ save time and space, but they can be logically simple to understand


### Basic Recursive Function
```
function recursive(data)
    if (base case)
        perform base action
        return

    recursive(reduced data)
```
__Variants:__
- A data value may or may not be returned
- Any number of base cases
- Any number of recursive calls

__Examples:__
- Factorial
- Cumulative Sum
- Print a list in reverse order
- Linear Search
- Binary Search
- Has Duplicates
- Reverse List
- Fibonacci






