#!usr/bin/env python
import time

directions = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 0

def part_one(sp):
    visited = set()
    dir = 0
    while True:
        visited.add(sp)
        xi = sp[0]+directions[dir][0]
        yi = sp[1]+directions[dir][1]
        if not (0 <= xi < n and 0 <= yi < m):
            print(len(visited))
            return 
        if grid[xi][yi] == "#":
            dir += 1
            if dir == 4: dir = 0       
        else:
            sp = (xi,yi)

def part_two(sp):
    visited = set()
    dir = 0
    while True:
        visited.add(sp)
        xi = sp[0]+directions[dir][0]
        yi = sp[1]+directions[dir][1]
        if not (0 <= xi < n and 0 <= yi < m):
            return 0
        if grid[xi][yi] == "#" or (xi == ll and yi == gg):
            dir += 1
            if dir == 4:dir = 0  
            tmp_sp = list(sp)
            tmp_sp[2] = dir
            sp = tuple(tmp_sp) 
        else:
            sp = (xi,yi, dir)
        if sp in visited:
            return 1
         
            

lines = [line.rstrip() for line in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
sp = ()
for x in range(n):
    for y in range(m):
        if lines[x][y] in '^':
            sp = (x,y,0)

part_one(sp)

for ll in range(n):
    for gg in range(m):
        if grid[ll][gg] == ".":
            ans += part_two(sp)

print(ans)