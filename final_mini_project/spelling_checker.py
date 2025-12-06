import os
import re
import sys
import time
import matplotlib.pyplot as plt
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
    misspells = set()
    with open(text_file, "r") as tf:
        for line in tf:
            line = line.strip()
            words = re.split(r'[\W_]+', line)
            for word in words:
                if word == "" or word.isnumeric() or not word.isalpha():
                    continue
                word = word.lower()
                if word not in dictionary:
                    misspells.add(word)
    return misspells


def main(args=sys.argv):
    aarray = []
    for arg in args:
        if arg == "./spelling_checker.py" or arg == "spelling_checker.py":
            continue
        aarray.append(arg)

    if len(aarray) != 3:
        print("Error: too many arguments")
        print("Usage: \t ./spelling_checker.py -[t/d/l/a] <dictionary file> <text file>")
        sys.exit(1)

    if aarray[0] not in ['-t', '-d', '-l', '-a']:
        print(aarray[0])
        print("Error: data structure does not exist")
        print("Usage: \t ./spelling_checker.py -[t/d/l/a] <dictionary file> <text file>")
        sys.exit(1)

    if aarray[0] != "-a":
        tstart = time.time()
        dictionary = initialize_dictionary(aarray[1], aarray[0])
        t_initialize = round(time.time() - tstart, 5)
        print(f"Time to initialize word dictionary: {t_initialize}")

        tstart = time.time()
        misspells = get_misspells(dictionary, aarray[2])
        t_misspells = round(time.time() - tstart, 5)
        print(f"Time to search for misspells: {t_misspells}")

        print(misspells)
    else:
        tst = time.time()
        dict_trie = initialize_dictionary(aarray[1], "-t")
        tit = time.time() - tst

        tsd = time.time()
        dict_dict = initialize_dictionary(aarray[1], "-d")
        tid = time.time() - tsd

        tsl = time.time()
        dict_list = initialize_dictionary(aarray[1], "-l")
        til = time.time() - tsl

        tst = time.time()
        mis_trie = get_misspells(dict_trie, aarray[2])
        tmt = time.time() - tst

        tsd = time.time()
        mis_dict = get_misspells(dict_dict, aarray[2])
        tmd = time.time() - tsd

        tsl = time.time()
        mis_list = get_misspells(dict_list, aarray[2])
        tml = time.time() - tsl

        categories_initialize = ["Initialize Trie", "Initalize Dict", "Initialize List"]
        values_initialize = [tit, tid, til]
        categories_misspells = ["Misspells Trie", "Misspells Dict", "Misspells List"]
        values_misspells = [tmt, tmd, tml]

        file_name = aarray[2].split(".")[0]

        if not os.path.isdir("figures"):
            os.mkdir("figures")

        figi, axi = plt.subplots()
        barsi = axi.bar(categories_initialize, values_initialize)
        axi.bar_label(barsi, padding=1)
        axi.set_ylabel("Time (s)")
        axi.set_xlabel("Functions")
        axi.set_title("Initialization/Reading Time")

        plt.savefig(f"figures/initialization_time_{file_name}.png")
        if os.path.exists(f"figures/initialization_time_{file_name}.png"):
            print(f"Successfully created figures/initialization_time_{file_name}.png")
        else:
            print("Failed to create Initialization Time graph")

        figm, axm = plt.subplots()
        barsm = axm.bar(categories_misspells, values_misspells)
        axm.bar_label(barsm, padding=1)
        axm.set_ylabel("Time (s)")
        axm.set_xlabel("Functions")
        axm.set_title("Misspell Finding Time")

        plt.savefig(f"figures/misspell_time_{file_name}.png")
        if os.path.exists(f"figures/misspell_time_{file_name}.png"):
            print(f"Successfully created figures/misspell_time_{file_name}.png")
        else:
            print("Failed to create Misspell Time graph")
    
        plt.show()





if __name__ == "__main__":
    main()