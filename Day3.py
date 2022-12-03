games = open("Input", "r")
games = [i.strip("\n") for i in list(games)]
p1 = 0
p2 = 0

for l in games:
    for x in l[int(len(l)/2):]:
        if x in l[:int(len(l)/2)]:
            p1 += (ord(x) - 96) if x.islower() else ord(x) - 38
            break

for i in range(0, len(games), 3):
    for x in games[i]:
        if x in games[i + 1] and x in games[i + 2]:
            p2 += (ord(x) - 96) if x.islower() else ord(x) - 38
            break

print(p1)
print(p2)
