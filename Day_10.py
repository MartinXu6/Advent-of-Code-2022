command = [i.strip("\n") for i in list(open("Input","r"))]

x_sum = 1
cycle = 0
p1 = 0


for line in command:
    if "addx" in line:
        for i in range(2):
            cycle += 1
            if cycle in range(20, 221, 40):
                p1 += cycle * x_sum
        x_sum += int(line.split()[1])
    else:
        cycle += 1
        if cycle in range(20, 221, 40):
            p1 += cycle * x_sum


x_sum = 1
cycle = 0
p2 = ""
for line in command:
    if "addx" in line:
        for i in range(2):
            if cycle % 40 in (x_sum - 1, x_sum, x_sum + 1):
                p2 += "#"
            else:
                p2 += "."
            cycle += 1
            if cycle % 40 == 0:
                p2 += "\n"
        x_sum += int(line.split()[1])
    else:
        if cycle % 40 in (x_sum - 1, x_sum, x_sum + 1):
            p2 += "#"
        else:
            p2 += "."
        cycle += 1
        if cycle % 40 == 0:
            p2 += "\n"

print(p1)
print(p2)
