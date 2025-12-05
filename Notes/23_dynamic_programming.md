# Dynamic Programming

## What is Dynamic Programming?

Dynamic Programming is an algorithmic technique that splits a problem into sub-problems and serially computes and stores results to sub-problems. It uses the sub-problem solutions to reach the final solution.

## Ex: Longest Common Substring

| |B|R|E|A|K|
|-|-|-|-|-|-|
|__B__|1|0|0|0|0|
|__E__|0|0|1|0|0|
|__A__|0|0|0|2|0|
|__K__|0|0|0|0|3|

If there is a match between letters, the matrix value is 1 + the upper left corner's matrix value

(Ex: E matches E, upper left corner = 0 --> 1)\
(Ex: A matches A, upper left corner = 1 --> 2)\
(Ex: K matches K, upper left corner = 2 --> 3)

## Ex: N-Queens

__The N-Queens Problem:__ For an NxN board, is there a way to place N queens in such a way that no queen attacks any other queen?

```
/* Ex: 4x4 */

[ |Q| | ]
[ | | |Q]
[Q| | | ]
[ | |Q| ]

```

__How would we represent the board?__ While the first thought would be a matrix, since each row can only have one queen, we can just use a list with values for each column position and each index is a row number\
`4x4: [1, 3, 0, 2]`

__What is the dynamic programming table like?__

```
/* Ex: 4x4 */

[ | | | ]   [[0], [1], [2], [3]]
[ | | | ]   [[0, 2], [0, 3], [1, 3], [2, 0], [3, 0], [3, 1]]
[ | | | ]   ...
[ | | | ]   [[1, 3, 0, 2], [2, 0, 3, 1]]
```

__How do we determine placement is safe?__

1. One queen per row (same x coordinate)
2. One queen per column (same y coordinate)
3. One queen per any diagonal
    - Up Diagonal: start from bottom left and go up toward top right
        - Pattern: sum of x and y coordinates is equal
    - Down Diagonal: start from top left and go down toward bottom right
        - Pattern: difference between x and y coordinates is equal
    - Overall: 
        - (Unsafe Down) row - r = col - c
        - (Unsafe Up) row - r = -(col - c)
        - ==> row - r = abs(col - c)

