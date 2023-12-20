#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
from heapq import heappop, heappush

lines = [l.strip() for l in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])

def neighbors(i,j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii, jj

ans = ans1 = 0
for line in lines:
    print(line)

visited = [[False] * m for _ in range(n)]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if (i, j) == end:
        print(steps)
        break

    for ii, jj in neighbors(i, j):
        heappush(heap, (steps + 1, ii, jj))

print(ans)
print(ans1)
# Good stuff
# print("="*80)