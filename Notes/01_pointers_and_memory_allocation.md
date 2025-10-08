# Pointers and Memory Allocation

### C is a low-level language - written for working with hardware
Why is memory management important?
- Utilization
- Security
- Ease of programming


C exposes and makes you deal with memory details


### C Data Types and Sizes
- `bool` -> 1 byte
- `char` -> 1 byte
- `short` -> 2 bytes
- `int` -> 4 bytes
- `float` -> 4 bytes
- `double` -> 8 bytes
- `char*` -> 8 bytes
- `int*` -> 8 bytes

### Binary and Hexidecimal
Hexidecimal uses 0-9 and A-F to go from 0000 to 1111

Memory stores values at specific locations, but some variables are stored at more than one memory location (each memory location has 8 bits)
- int: 32 bit, needs 4 bytes of memory
    - least significant bit first (smallest numerical value) -> little endian
    - most significant bit first (largest numerical value) -> big endian
- Use the & operator to get the variable's address

### Pointer and Address Variables
- `type *var`
    - `*` indicates pointer in variable declaration
- Set what a pointer points to using `&`
    - `var = &x`
- To use what the variable points at, dereference it with `*`
    - `*var = 6`
- Arrays are contiguous blocks of memory -> the variable acts as a pointer to the first address of that block
- Adding to a pointer increments it by `sizeof(type)` bytes away
- You can subtract pointers to see how many bytes are between pointers/addresses

### Strings
- A __null-terminated__ `\0` array of chars
- Since strings are arrays, the string variable is a pointer to the first char's address





