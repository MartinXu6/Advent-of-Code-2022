Monkeys = [i.strip() for i in list(open("Input", "r"))]
monkey_profiles = []


def los_Monos():
    monkey_num = Monkeys[line][-2]
    items = Monkeys[line + 1][16:].split(",")
    operation = Monkeys[line + 2][21:].split()
    test = Monkeys[line + 3][19:]
    True_ = Monkeys[line + 4][25:]
    False_ = Monkeys[line + 5][26:]
    monkey_profiles.append([monkey_num, items, operation, test, True_, False_, 0])


for line in range(len(Monkeys)):
    if "Monkey" in Monkeys[line]:
        los_Monos()
# p1, basically the same code as p2
for round in range(20):
    for turn in range(8):
        item_list = monkey_profiles[turn][1][:]
        for item in item_list:
            new_worry = int(item)
            match monkey_profiles[turn][2][0]:
                case "+":
                    new_worry += int(monkey_profiles[turn][2][1])
                case "*":
                    if monkey_profiles[turn][2][1] != "old":
                        new_worry *= int(monkey_profiles[turn][2][1])
                    else:
                        new_worry *= new_worry
            new_worry //= 3
            if new_worry % int(monkey_profiles[turn][3]) == 0:
                monkey_profiles[int(monkey_profiles[turn][4])][1].append(new_worry)
            else:
                monkey_profiles[int(monkey_profiles[turn][5])][1].append(new_worry)
            monkey_profiles[turn][1].pop(0)
            monkey_profiles[turn][-1] += 1
print("p1:", sorted([monkey_profiles[inspected][-1] for inspected in range(8)], reverse=True)[0] *
      sorted([monkey_profiles[inspected][-1] for inspected in range(8)], reverse=True)[1])

# p2, you might have to wait for a bit
monkey_profiles = []

for line in range(len(Monkeys)):
    if "Monkey" in Monkeys[line]:
        los_Monos()
for round in range(10000):
    for turn in range(8):
        item_list = monkey_profiles[turn][1][:]
        for item in item_list:
            new_worry = int(item)
            match monkey_profiles[turn][2][0]:
                case "+":
                    new_worry += int(monkey_profiles[turn][2][1])
                case "*":
                    if monkey_profiles[turn][2][1] != "old":
                        new_worry *= int(monkey_profiles[turn][2][1])
                    else:
                        new_worry *= new_worry
            if new_worry % int(monkey_profiles[turn][3]) == 0:
                monkey_profiles[int(monkey_profiles[turn][4])][1].append(new_worry)
            else:
                monkey_profiles[int(monkey_profiles[turn][5])][1].append(new_worry)
            monkey_profiles[turn][1].pop(0)
            monkey_profiles[turn][-1] += 1
print("p2:", sorted([monkey_profiles[inspected][-1] for inspected in range(8)], reverse=True)[0] *
      sorted([monkey_profiles[inspected][-1] for inspected in range(8)], reverse=True)[1])
