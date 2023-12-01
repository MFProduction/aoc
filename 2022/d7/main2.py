# AOC - 2022 day7
from collections import defaultdict

lines = [l.rstrip() for l in open(0).readlines()]

SZ = defaultdict(int)
path = []
for line in lines:
    words =  line.split()
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    print(path)
