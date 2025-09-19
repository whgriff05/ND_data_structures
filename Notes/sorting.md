# Sorting


### Common Algorithms O(N^2)
[Visualization - Sorting Cards](https://anim.ide.sk/sortingcards.php)
- Bubble Sort
    - Compare pairs, swapping to put the greater one on the right, "bubbling" them up to the sorted end at the right end
    - Builds up a sorted portion on the high end
- Insertion Sort
    - Compares each item to the entire unsorted portion of the array, inserting it in its particular place
    - Builds up a sorted portion on the low end
- Selection Sort
    - Find the lowest value, swap with the lowest index, then continue until the entire list is sorted
    - Builds up a sorted portion on the low end

General Information
- Build up a sorted region and an unsorted region through multiple passes
- Generally, for a random unsorted array, Insertion Sort is the best choice/fastest

### Common Algorithms O(N log N)
- Merge Sort
    - Divides and conquers into pairs, then merges pairs, then merges merges, etc until sorted
    - Each merge is O(N)
- Quick Sort
    - In place
    - Partitions array via swaps into regions above or below a pivot value
    - If your pivots are always bad (i.e. the lowest value), it begins to look like a selection sort problem and the complexity jumps to O(N^2)

### Adaptiveness and Stability
__Adaptiveness:__ takes advantage of a partially sorted array (does less work than a full O(N^2) algorthm)
- Bubble Sort isn't adaptive unless you keep track of where in the array you make swaps
- Insertion Sort is already adaptive
- Selection Sort is not adaptive

__Stability:__ if two elements have same value, order will not be changed
- Bubble Sort is stable
- Insertion Sort is stable
- Selection Sort is unstable [2a, 2b, 1] would swap 2a and 2b
