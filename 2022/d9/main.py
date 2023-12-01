# AOC - 2022 day7
lines = [line.strip().split(" ") for line in open(0).readlines()]



dd = {
    "R": [0,1],
    "L": [0,-1],
    "U": [1,0],
    "D": [-1,0],
}

def together(i,j,ti,tj):
    if i == ti and j == tj:
        return True
    if i == ti and (j + 1 == tj or j -1 == tj):
        return True
    if j == tj and (i + 1 == ti or i -1 == ti):
        return True
    if (i + 1 == ti or i - 1 == ti) and (j + 1 == tj or j -1 == tj):
        return True
    return False

def move_tail(i,j):
    pass

i = j =  0
ti = tj =  0
visited = set()
visited.add((i,j))

for line in lines:
    direction, count = line[0], int(line[1])
    x, y = dd[direction]

    for _ in range(count):
        i += x
        j += y
        # ti, tj = move_tail(i,j)
        visited.add((i,j))

print(visited)
for i in visited:
    print(i)
