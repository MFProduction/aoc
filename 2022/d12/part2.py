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

start = []
for i in range(n):
    for j in range(m):
        char = grid[i][j]
        if char == "S" or char == "a":
            start.append((i, j))
        if char == "E":
            end = i, j

# print(start)
def neighbors(i,j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii, jj

stepss = []
pp = len(start)
x = 0
for ss,dd in start:
    print(f"{x}/{pp}")
    visited = [[False] * m for _ in range(n)]
    heap = [(0, ss, dd)]
    while True:
        # print(ss,dd)
        # print(heap)
        try:
            steps, i, j = heappop(heap)
        except IndexError:
            break
        if visited[i][j]:
            continue
        visited[i][j] = True

        if (i, j) == end:
            stepss.append(steps)
            break

        for ii, jj in neighbors(i, j):
            heappush(heap, (steps + 1, ii, jj))
    x += 1

print(min(stepss))