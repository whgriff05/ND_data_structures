import re
import sys
import time
from trie import Trie

def initialize_dictionary_trie(dict_file):
    dict_trie = Trie()
    with open(dict_file, "r") as df:
        for line in df:
            line = line.strip()
            words = re.split(r'[\W_]+', line)
            for word in words:
                if word == "":
                    continue
                word = word.lower()
                dict_trie.add_word(word)

    return dict_trie

def get_misspells_trie(dict_trie, text_file):
    misspells = []
    with open(text_file, "r") as tf:
        for line in tf:
            line = line.strip()
            words = re.split(r'[\W_]+', line)
            for word in words:
                if word == "":
                    continue
                word = word.lower()
                if word not in dict_trie:
                    misspells.append(word)
    return misspells

def main(args=sys.argv):
    aarray = []
    for arg in args:
        if arg == "./spelling_checker.py" or arg == "spelling_checker.py":
            continue
        aarray.append(arg)

    if len(aarray) != 2:
        print("Error: too many arguments")
        print("Usage: \t ./spelling_checker.py <dictionary file> <text file>")
        sys.exit(1)

    tstart = time.time()
    dict_trie = initialize_dictionary_trie(aarray[0])
    t_initialize = round(time.time() - tstart, 5)
    print(f"Time to initialize dict_tree: {t_initialize}")

    tstart = time.time()
    misspells = get_misspells_trie(dict_trie, aarray[1])
    t_misspells = round(time.time() - tstart, 5)
    print(f"Time to search for misspells: {t_misspells}")

    print(misspells)


if __name__ == "__main__":
    main()