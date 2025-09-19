# Time Complexities

__Constant Time Operation__: something that takes the same amount of time regardless of data value
- arithmetic operations
- variable assignments
- loops with fixed number of iterations
- array indexing
- comparison

In Big O Notation, 
- Ignore constants and coefficients `O(6N + 5) -> O(N)`
- Only care about the highest term `O(N^2 + N) -> O(N^2)`
- Take the product of multiplied terms `O(N * N) -> O(N^2)`

### Classic Complexities
- O(1)
- O(N)
    - for loops with variable range
- O(N^2)/further polynomials
    - nested for loops with variable range
- O(log N)
    - divide and conquer (ex: binary search)
- O(N log N)
    - divide and conquer with a O(N) operation
- O(c^N)
- O(N!)


### Complexity Practice
__Ex 1:__ Calculating the dot product between 2 n-long vectors
- __Answer:__ O(N)
- __Explanation:__ A single loop from x_1 to x_n 

__Ex 2:__ Multiplying 2 NxN matricies
- __Answer:__ O(N^3)
- __Explanation:__ Three loops: Loop through each row, and each row is looped against every column, and each value in the row is multiplied by each value in the column

__Ex 3:__ Finding the greatest common divisor between a and b - N is the number of bits in A/B
- __Answer:__ O(N)
- __Explanation:__ The magnitude of the number is cut in half each time, losing a single bit until the answer is found
- __Note:__ This could be O(log n) if N was about the magnitude of numbers, not the number of bits. N being the number of bits already factors in the logarithm in the complexity so it is just linear in the example

