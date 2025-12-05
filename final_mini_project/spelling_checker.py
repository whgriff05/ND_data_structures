import re
import sys
import time
from trie import Trie

def initialize_dictionary(dict_file, structure):
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

def get_misspells(dict_trie, text_file):
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

    if len(aarray) != 3:
        print("Error: too many arguments")
        print("Usage: \t ./spelling_checker.py -[t/d/a] <dictionary file> <text file>")
        sys.exit(1)

    if aarray[0] == "-t":
        pass
    elif aarray[0] == "-d":
        pass
    elif aarray[0] == '-a':
        pass
    else:
        print("Error: data structure does not exist")
        print("Usage: \t ./spelling_checker.py -[t/d/a] <dictionary file> <text file>")
        sys.exit(1)

    tstart = time.time()
    dict_trie = initialize_dictionary(aarray[1])
    t_initialize = round(time.time() - tstart, 5)
    print(f"Time to initialize word dictionary: {t_initialize}")

    tstart = time.time()
    misspells = get_misspells(dict_trie, aarray[2])
    t_misspells = round(time.time() - tstart, 5)
    print(f"Time to search for misspells: {t_misspells}")

    print(misspells)


if __name__ == "__main__":
    main()