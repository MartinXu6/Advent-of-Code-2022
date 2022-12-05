stacks = [["C", "S", "G", "B"],
          ["G", "V", "N", "J", "H", "W", "M", "T"],
          ["S", "Q", "M"],
          ["M", "N", "W", "T", "L", "S", "B"],
          ["P", "W", "G", "V", "T", "F", "Z", "J"],
          ["S", "H", "Q", "G", "B", "T", "C"],
          ["W","B","P","J","T"],
          ["M", "Q", "T", "F", 'Z', "C", "D", "G"],
          ["F", "p", "B", "H", "S", "N"]]

instruction = open("Input", "r")
instruction = [i.strip("\n") for i in list(instruction)]
indexes = []
double = 0
# Just collecting the data took me big effort
for i in instruction:
    for x in range(len(i)):
        if x == double:
            continue
        if i[x].isdigit():
            indexes.append((i[x]))
            try:
                indexes[-1] += i[x + 1]
                double = x+1
            except:
                pass
indexes = list(map(int,indexes))
for i in range(0,len(indexes),3):
    quantity, start, end = indexes[i], indexes[i+1]-1, indexes[i+2]-1
    # It took me an hour to figure out where the bug is in p1, and I realise that packages are moved in reversed order
    #  I accidentally solved p2 by not adding the [::-1]
    # to get p2, you delete the [::-1] part
    stacks[end] = stacks[start][:quantity][::-1] + stacks[end]
    del stacks[start][:quantity]
print("".join([i[0] for i in stacks]))

