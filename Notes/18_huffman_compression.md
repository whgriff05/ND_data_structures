# Huffman Compression

We are used to fixed-length compression codes (every key uses the same amount of bits):
- ASCII

However, there are variable-length compression codes too (different keys use different amounts of bits):
- Morse code
- Huffman code

These variable-length compression codes can be prefix codes or not
- Morse code is __NOT__ a prefix code, the only way to distinguish between letters is a delay in the signal
- Prefix codes use trees usually, and the letter continues down a code path in a tree or a graph until it reaches a leaf or a null node path

```
/* Ex: for a node with left child 0 and right child 1 */

     / \
   /     \
 / \     / \
a   b   c   d

00: a
01: b
10: c
11: d
```

## Huffman Code
Huffman Code uses letter frequencies to form an unbalanced tree with shortest paths to most frequent letters

### Ex: "ab"
- freq(a) = 1
- freq(b) = 1

```
 /\
a  b
```

a: 0\
b: 1

01\
ab

### Ex: "abbccc"
- freq(a) = 1
- freq(b) = 2
- freq(c) = 3

```
  / \
 /\  \
a  b  c
```

a: 00\
b: 01\
c: 1

000101111\
abbccc

## Huffman Encoding Algorithm

1. Get Frequencies
2. Build Tree
    - Push character nodes by frequency onto priority queue
    - Min priority queue since we will build the tree from bottom up
    - While queue has more than one node,
        - Pop
        - Combine into subtree and add frequencies
        - Push subtree
3. Get codes from the tree
