# AOC - 2022 day7
from collections import defaultdict
from string import ascii_lowercase
from heapq import heappop, heappush

lines = [l.strip() for l in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])

def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return 0
    if s == "E":
        return 25

for i in range(n):
    for j in range(m):
        char = grid[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j

def neighbors(i,j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii, jj

visited = [[False] * m for _ in range(n)]
heap = [(0, end[0], end[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    # if (i, j) == end:
    if height(grid[i][j]) == 0:
        print(steps)
        break

    for ii, jj in neighbors(i, j):
        heappush(heap, (steps + 1, ii, jj))
