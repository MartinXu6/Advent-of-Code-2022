signal = "".join(list(open("Input", "r")))
#p1
for i in range(len(signal) - 3):
    if len(set([signal[i], signal[i + 1], signal[i + 2], signal[i + 3]])) == 4:
        print(i + 4)
        break
#p2
for x in range(len(signal)-13):
    marker = []
    for l in range(14):
        marker.append(signal[x+l])
    if len(set(marker)) == 14:
        print(x+14)
        break
