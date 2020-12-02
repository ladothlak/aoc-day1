with open('p1input.txt') as f:
    read_data = list(f)

for line in range(len(read_data)):
    read_data[line] = int(read_data[line].rstrip('\n'))

num_dict = dict(zip(read_data, range(len(read_data))))

for i in range(len(read_data)):
    lookup = 2020-read_data[i]

    if num_dict.get(lookup) != None:
        print(read_data[i]*lookup)
        break
