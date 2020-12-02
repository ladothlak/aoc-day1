with open('p1input.txt') as f:
    read_data = list(f)

for line in range(len(read_data)):
    read_data[line] = int(read_data[line].rstrip('\n'))

num_dict = dict(zip(read_data, range(len(read_data))))

for i in range(len(read_data)):
    remainder = 2020-read_data[i]

    for m in range(len(read_data)):
        if m == i:
            continue

        lookup = remainder-read_data[m]

        if num_dict.get(lookup) != None:
            print(read_data[m]+read_data[i]+lookup,
                  read_data[m]*read_data[i]*lookup)
            break
