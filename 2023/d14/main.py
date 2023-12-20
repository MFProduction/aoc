#!usr/bin/env python
from collections import defaultdict
import queue
import sys
import json

lines = [line.rstrip() for line in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
ans = ans1 = 0
ans = ans1 = 0

def move_up(x,y):
    if x != 0 and grid[x-1][y] == ".":
        grid[x][y] = "."
        grid[x-1][y] = "O"
        return move_up(x-1,y)
    else:
        return (x,y)

def move_right(x,y):
    if y != m-1 and grid[x][y+1] == ".":
        grid[x][y] = "."
        grid[x][y+1] = "O"
        return move_right(x,y+1)
    else:
        return (x,y)

def move_down(x,y):
    if x != n-1 and grid[x+1][y] == ".":
        grid[x][y] = "."
        grid[x+1][y] = "O"
        return move_down(x+1,y)
    else:
        return (x,y)
def move_left(x,y):
    if y != 0 and grid[x][y-1] == ".":
        grid[x][y] = "."
        grid[x][y-1] = "O"
        return move_down(x,y-1)
    else:
        return (x,y)

def get_rocks(grid):
    rocks = []
    for i in range(0, n):
        for j in range(0,m):
            if grid[i][j] == "O":
                rocks.append(tuple([i,j]))
    return tuple(rocks)

def grid_sum(grid):
    a = 0
    for x in grid:
        nn = n
        a += x.count("O") * nn
        nn -= 1
    return a

start_grid = json.dumps(grid)
cache = defaultdict(int)
tmp_rocks = get_rocks(grid)
range_start = 1000000000
c = 0
while c < range_start:
    c+=1
    if (c % 1000) == 0:
        print(c)
    if start_grid in cache:
        # print(c+cache[start_grid])
        c = c + cache[start_grid] * 100000000
        # print(grid)
        print(grid_sum(grid))
        continue
    else:
        # print("Cache miss")
        # tmp_rocks
        tmp_rocks = get_rocks(grid)
        rr = tuple(sorted(tmp_rocks , key=lambda k: [k[0], k[1]], reverse=False))
        tmp_rocks = []
        for x,y in rr:
            tmp_rocks.append(move_up(x,y))

        rr2 = tuple(sorted(tmp_rocks , key=lambda k: [k[1], k[0]], reverse=False))
        tmp_rocks = []
        for x,y in rr2:
            tmp_rocks.append(move_left(x,y))

        rr3 = tuple(sorted(tmp_rocks , key=lambda k: [k[0], k[1]], reverse=True))
        tmp_rocks = []
        for x,y in rr3:
            tmp_rocks.append(move_down(x,y,))

        rr4 = tuple(sorted(tmp_rocks , key=lambda k: [k[1], k[0]], reverse=True))
        tmp_rocks = []
        for x,y in rr4:
            tmp_rocks.append(move_right(x,y))

        cache[start_grid] = c
        start_grid = json.dumps(grid)

print(ans)
print(ans1)
# Good stuff
# print("="*80)