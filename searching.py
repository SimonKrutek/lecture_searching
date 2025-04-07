import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)

    return seq[field]

def linear_search(seq, number):
    """

    :param seq: prohledávana sekvenci
    :param number: hledane cislo
    :return: Funkce vrátí slovník se dvěma klíči. Pod prvním klíčem positions bude uložen
seznam pozic (indexů). Pod druhým klíčem count bude uložen počet výskytů
hledaného čísla.
    """
    ind=[]
    count = 0

    idx = 0
    while idx < len(seq):
        if seq[idx] == number:
            ind.append(idx)
            count += 1
        idx += 1

    return {
        "position": ind,
        "count": count,
    }

def pattern_search(seq, vzor):
    """

    :param seq: prohledávanou sekvenci
    :param vzor: hledany vzor
    :return: Funkce vrátí množinu, ve které budou uloženy pozice (indexy) výskytu vzoru v
sekvenci.

    """


def main():
    file_name = "sequential.json"

    #read data
    seq = read_data(file_name, field="unordered_numbers")
    print(seq)

    cis = linear_search(seq, 102)
    print(cis)

if __name__ == '__main__':
    main()