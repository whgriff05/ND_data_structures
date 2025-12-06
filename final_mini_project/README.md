# Spelling Checker Project

## Overview

This project compares the times each data structure (trie, Python dictionary, and Python list) take to find misspellings in text files.

```bash
python3 spelling_checker.py -[t/d/l/a] <dictionary file> <text file>
```

```
Flags:
    -t: Trie mode - use a trie to store the dictionary of words
    -d: Dictionary mode - use a dict to store the dictionary of words
    -l: List mode - use a list to store the dictionary of words
    -a: All mode - use each (trie, dictionary, list) to each store and calculate misspellings and generate graphs comparing the speed of each
```

Graph images have already been generated in the `figures` directory

Unit testing can be run with the `make test` command

Graphs for `essay2.txt` can be generated with the `make demo` command

### Credits

[words_alpha.txt](https://github.com/dwyl/english-words)\
[sherlock.txt](https://norvig.com/ngrams/smaller.txt)\
`essay.txt` and `essay2.txt` were essays written by me in high school/college.\
`ulysses.txt` was taken from HW06.
