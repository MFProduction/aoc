# AOC - 2022 day7
from string import ascii_lowercase
from heapq import heappop, heappush

lines = [l.strip() for l in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])

def valid(s):
    if s == "#":
        return False
    if s == "S":
        return True
    if s == ".":
        return True

for i in range(n):
    for j in range(m):
        char = grid[i][j]
        if char == "S":
            start = i, j

def neighbors(i,j,mmap):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if valid(grid[ii][jj]):
            mmap.append(True)
            yield ii, jj, mmap

visited = [[False] * m for _ in range(n)]
heap = [(0, start[0], start[1])]
count = 0
while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True
    count+=1 
    mmap = []
    for ii, jj, mmap in neighbors(i, j, mmap):
        heappush(heap, (steps + 1, ii, jj))

    if steps == 6:
        print(steps)
        ssss = 0
        print(sum(mmap))
        break
    
