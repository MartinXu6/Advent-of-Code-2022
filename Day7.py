from collections import deque,defaultdict

path = []
directories = defaultdict(int)
for line in open("Input", "r"):
    line = line.split()
    if line[0] == "$":
        # cd xx or cd..
        if line[1] == 'cd':
            if line[2] == '..':
                path.pop()
            else:
                dir = line[2]
                path.append(dir)
                directories[dir] = directories.get(dir, 0)
    else:
        # all files in the directory
        if line[0] != "dir":
            a, b = line
            for directory in ["".join(path[:i+1]) for i in range(len(path))]:
                # concretes all the directory so repetition of same folder won't be added twice
                directories[directory] += int(a)
print(f" p1 :{sum(filter(lambda x: x <= 100000, directories.values()))}")
print(f" p2 :{min(filter(lambda x: x >= directories['/']-40000000, directories.values()))}")
