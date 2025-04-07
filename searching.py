import os
import json
import time

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
    vzor_size = len(vzor)
    ind = set()

    left_idx = 0
    right_idx = vzor_size
    while right_idx < len(seq):
        for idx in range(vzor_size):
            if vzor[idx] != seq[left_idx + idx]:
                break
        else:
            ind.add(left_idx + vzor_size // 2)

        left_idx +=1
        right_idx +=1
    return ind


def binary_search(seq, num):
    """

    :param seq: prohledávaný seznam čísel
    :param num: a hledané číslo
    :return: Funkce vrátí index, na kterém se hledané číslo v sekvenci nachází. Pokud není číslo
nalezeno, funkce vrátí hodnotu None.
    """
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (low + high)//2
        if seq[mid] == num:
            return mid
        elif seq[mid] < num:
            low = mid
        else:
            high = mid

    return None

def main():
    file_name = "sequential.json"

    #read data
    seq = read_data(file_name, field="unordered_numbers")
    print(seq)


    cis = linear_search(seq, 102)
    print(cis)


    seq = read_data(file_name, field="dna_sequence")
    print(seq)
    pozice = pattern_search(seq, "ATA")
    print(pozice)

    start_time = time.time()
    seq = read_data(file_name, field="ordered_numbers")
    print(seq)
    ind = binary_search(seq, 63)
    print(ind)

    total_time = time.time() - start_time
    print(total_time)

if __name__ == '__main__':
    main()