# Opening a file
from typing import List, Any, Dict


#filepath = "C:\\Users\\datlu\\Downloads\\dataset_198_10(1).txt"

# Read file containing one sequence


def one_sequence(path):
    file = open(path)
    sequence = file.readline()
    while True:
        line = file.readline()
        sequence = sequence + line
        if not line:
            break
    return sequence


# Read file containing multiple sequences


def many_sequences(path):
    file = open(path)
    sequences = []
    while True:
        line = file.readline().rstrip('\n')
        if line == "":
            break
        sequences.append(line)
    return sequences


# Overlap graph problem


def print_edges(sequence1_list):
    for key, value in sequence1_list.items():
        print(key + " - > ", end=' '),
        print(str(value[0]), end=''),
        if len(value) > 1:
            print(", " + str(value[1]))
        print()

# loop through the list of sequence and find the prefix and check if the prefix is in the post fix


def check_nodes(sequence1, sequence2, k):
    if sequence1[0:k] == sequence2[-k:]:
        return True
    else:
        return False


path = "C:\\Users\\datlu\\Downloads\\dataset_198_10 (3).txt"
sequences = many_sequences(path)
#print(sequences)
k = len(sequences[1])-1
print(k)
dictionary = {}
# sequence4 = 'AGCACCCGTGAGATAATCTCCGCTA'
# sequence3 = 'GCACCCGTGAGATAATCTCCGCTAA'
# print(sequence4[-24:])
# print(sequence3[0:24])
# print(check_nodes(sequence3, sequence4, len(sequence3) - 1))

# print(check_nodes(sequences[1753], sequences[0], k))
# dictionary2 = {}
# dictionary2[1] = []
# dictionary2[1].append('a')
# dictionary2[1].append('b')
# print(dictionary2)
for sequence1 in sequences:
    # print(sequence1)
    dictionary[sequence1] = []
    # print(sequence1)
    for sequence2 in sequences:
        if check_nodes(sequence1, sequence2, k) == True:
            # print(sequence2)
            dictionary[sequence1].append(sequence2)
    if len(dictionary[sequence1]) == 0:
        del(dictionary[sequence1])

    # print(dictionary[sequence1])
    # print()
# print(dictionary)

tmp = {}
for key, value in dictionary.items():
    if value[0] in tmp:
        tmp[value[0]].append(key)
    else:
        tmp[value[0]] = [key]
# print(tmp)
print_edges(tmp)

# dictionary[sequence1].append(list_of_prenodes)
# print(dictionary)









