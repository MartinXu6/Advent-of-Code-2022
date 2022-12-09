H_pos = [0, 0]
T_pos = [0, 0]
positions = []
for move in open("Input", "r"):
    move = [i.strip("\n") for i in move.split()]
    for step in range(int(move[1])):
        match move[0]:
            case "L":
                H_pos[0] -= 1
                if abs(H_pos[0] - T_pos[0]) == 2 and H_pos[1] != T_pos[1]:
                    T_pos[0], T_pos[1] = H_pos[0] + 1, H_pos[1]
                elif abs(H_pos[0] - T_pos[0]) == 2:
                    T_pos[0] = H_pos[0] + 1
            case "R":
                H_pos[0] += 1
                if abs(H_pos[0] - T_pos[0]) == 2 and H_pos[1] != T_pos[1]:
                    T_pos[0], T_pos[1] = H_pos[0] - 1, H_pos[1]
                elif abs(H_pos[0] - T_pos[0]) == 2:
                    T_pos[0] = H_pos[0] - 1
            case "U":
                H_pos[1] += 1
                if abs(H_pos[1] - T_pos[1]) == 2 and H_pos[0] != T_pos[0]:
                    T_pos[0], T_pos[1] = H_pos[0], T_pos[1] + 1
                elif abs(H_pos[1] - T_pos[1]) == 2:
                    T_pos[1] = H_pos[1] - 1
            case "D":
                H_pos[1] -= 1
                if abs(H_pos[1] - T_pos[1]) == 2 and H_pos[0] != T_pos[0]:
                    T_pos[0], T_pos[1] = H_pos[0], T_pos[1] - 1
                elif abs(H_pos[1] - T_pos[1]) == 2:
                    T_pos[1] = H_pos[1] + 1
        if T_pos not in positions:
            positions.append(T_pos[:])
print(len(positions))
