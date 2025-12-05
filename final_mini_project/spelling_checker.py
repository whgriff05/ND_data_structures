import re
import sys
import time
from trie import Trie
from dictionary import Dictionary

def initialize_dictionary(dict_file, structure):
    match structure:
        case "-t":
            dictionary = Trie()
        case "-d":
            dictionary = Dictionary()
        case "-l":
            dictionary = []
    with open(dict_file, "r") as df:
        for line in df:
            line = line.strip()
            words = re.split(r'[\W_]+', line)
            for word in words:
                if word == "":
                    continue
                word = word.lower()
                dictionary.append(word)

    return dictionary

def get_misspells(dictionary, text_file):
    misspells = []
    with open(text_file, "r") as tf:
        for line in tf:
            line = line.strip()
            words = re.split(r'[\W_]+', line)
            for word in words:
                if word == "":
                    continue
                word = word.lower()
                if word not in dictionary:
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

    if aarray[0] not in ['-t', '-d', '-l']:
        print(aarray[0])
        print("Error: data structure does not exist")
        print("Usage: \t ./spelling_checker.py -[t/d/a] <dictionary file> <text file>")
        sys.exit(1)

    tstart = time.time()
    dictionary = initialize_dictionary(aarray[1], aarray[0])
    t_initialize = round(time.time() - tstart, 5)
    print(f"Time to initialize word dictionary: {t_initialize}")

    tstart = time.time()
    misspells = get_misspells(dictionary, aarray[2])
    t_misspells = round(time.time() - tstart, 5)
    print(f"Time to search for misspells: {t_misspells}")

    print(misspells)


if __name__ == "__main__":
    main()