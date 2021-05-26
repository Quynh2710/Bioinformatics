path = "C:\\Users\\datlu\\Downloads\\dataset_200_8.txt"
file = open(path)
dictionary = {}
line = file.readline()
while line:
    if len(line) > 0:
        sequence = line.rstrip('\n')
        # print(sequence)
        tmp = sequence[0:-1]
        if tmp in dictionary:
            dictionary[tmp].append(sequence[1:])
        else:
            dictionary[tmp] = [sequence[1:]]
    line = file.readline()
def print_list (dictionary):
    for key,value in dictionary.items():
        str = key + ' -> ' + ','.join(value)
        print(str)
print_list(dictionary)

