camp = open("Input", "r")
camp = [i.strip().replace(",","-") for i in list(camp)]
p1 = 0
p2 = 0
for i in range(len(camp)):
    splited = list(map(int, camp[i].split("-")))
    for l in range(0,4,2):
        if splited[l] == min(splited) and splited[l+1] == max(splited):
            p1 += 1
            break
    keep_going = True
    for x in range(splited[0], splited[1]+1):
        if keep_going:
            for f in range(splited[2], splited[3]+1):
                if x == f:
                    p2 += 1
                    keep_going = False
                    break
        else:
            break
print(p1)
print(p2)
