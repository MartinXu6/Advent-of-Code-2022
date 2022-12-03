file = open("Input","r")
cal_list = [i.strip("\n") for i in file ]
Sum = 0
total = []
#p1
for i in cal_list:
    if i != "":
        Sum += int(i)
    else:
        total.append(Sum)
        Sum = 0
print(max(total))
#p2
total = sorted(total)[len(total)-3:]
print(sum(total))

