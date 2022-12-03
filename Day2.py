file = open("Input", "r")
cal_list = [i.strip("\n") for i in file]
points = {"X":1, "Y":2, "Z":3}
def p1():
    score = sum([points[i[2]] for i in cal_list])
    for i in cal_list:
        if i[0] == "A":
            if i[2] == "X":
                score += 3
            elif i[2] == "Y":
                score += 6
        elif i[0] == "B":
            if i[2] == "Y":
                score += 3
            elif i[2] == "Z":
                score += 6
        elif i[0] == "C":
            if i[2] == "X":
                score += 6
            elif i[2] == "Z":
                score += 3
    print(score)


def p2():
    score = 0
    for i in cal_list:
        if i[0] == "A":
            if i[2] == "X":
                score += 3
            elif i[2] == "Y":
                score += 4
            elif i[2] == "Z":
                score += 8
        elif i[0] == "B":
            if i[2] == "X":
                score += 1
            elif i[2] == "Y":
                score += 5
            elif i[2] == "Z":
                score += 9
        elif i[0] == "C":
            if i[2] == "X":
                score += 2
            elif i[2] == "Y":
                score += 6
            elif i[2] == "Z":
                score += 7
    print(score)


p1()
p2()