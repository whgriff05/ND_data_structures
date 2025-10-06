# Midterm Review

## General Info
- In class, 50m
- Multiple Choice and Short Answer
- Beginning of class to linked lists (HW 5)
- Specific Tips
    - Know powers of 2 
    - Be familiar with __both__ unoptimized and optimized sort algorithms
    - Quicksort: __be familiar with the exact version in zyBooks__ (choice of pivot, revursive reassignment of upper and lower bounds)
    - zyBooks 15.1 -- C playground


## Review of Regions of Memory
```C
/* Assume 6-bit memory: 0-63 (0x00 - 0x3F) */
/* Each memory location can hold one int, char, ... address (don't have to worry about endian/ints having more than one address) */

double p = 3;

int main() {
    int i = 25;
    char a[] = "wx";
    char *s = "yz";
    int *m = malloc(10*sizeof(int));
    static int t = 2;

    *m = 100;
    *(m + 1) = 101;
    m[2] = 103;

    return 0;
}
```

| Stack | Heap | Data | Code |
|-|-|-|-|
|0x3F: `i = 25`| | | |
|0x3E: `a[2] = '\0'`| | | |
|0x3D: `a[1] = 'x'`| | | |
|0x3C: `a[0] = 'w'`| | | |
|0x3B: `s = 0x11`| | | |
|0x3A: `m = 0x20`| | | |
| |0x29: | | |
| |0x28: | | |
| |0x27: | | |
| |0x26: | | |
| |0x25: | | |
| |0x24: |0x14: `t = 2`| |
| |0x23: |0x13: `'\0'`| |
| |0x22: `103`|0x12: `'z'`| |
| |0x21: `101`|0x11: `'y'`| |
| |0x20: `100`|0x10: `p = 3`|0x00: `main`|

