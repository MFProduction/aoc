#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import sys 
sys.setrecursionlimit(1000000)

lines = [l.strip() for l in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])


def linearSearch (arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == target):
                return i, j
    return -1, -1

 
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
ways = {
    (-1, 0): "up",
    (0, 1): "right",
    (1, 0): "down",
    (0, -1): "left"

}
visited = [[False] * m for _ in range(n)]
# result = []
def find_loop(i,j,result=[]):
    pipe_type = grid[i][j]
    visited[i][j] = True       
    
    for di, dj in [[-1, 0],[0, 1],[1, 0],[0, -1]]:
        ii = i + di
        jj = j + dj
        
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        
        way = ways[tuple([di,dj])]
        new_pipe_type=grid[ii][jj]
        match = False
        
        if new_pipe_type == ".":
            continue
        
        if pipe_type == "|":
            if way == "up" and new_pipe_type in "7F|":
                match = True
            if way == "down" and new_pipe_type in "LJ|":
                match = True
        elif pipe_type == "-":
            if way == "left" and new_pipe_type in "LF-":
                match = True
            if way == "right" and new_pipe_type in "7J-":
                match = True
        elif pipe_type == "L":
            if way == "right" and new_pipe_type in "J7-":
                match = True
            if way == "up" and new_pipe_type in "7F|":
                match = True
        elif pipe_type == "F":
            if way == "right" and new_pipe_type in "J7-":
                match = True
            if way == "down" and new_pipe_type in "JL|":
                match = True
        elif pipe_type == "J":
            if way == "left" and new_pipe_type in "FL-":
                match = True
            if way == "up" and new_pipe_type in "7F|":
                match = True
        elif pipe_type == "7":
            if way == "left" and new_pipe_type in "FL-":
                match = True
            if way == "down" and new_pipe_type in "JL|":
                match = True
        
        if pipe_type == "S":
            match = True

        if match and not visited[ii][jj]:
            result.append(grid[i][j])
            print(grid[ii][jj], result)
            return find_loop(ii,jj,result)
             
    if result:
        result.pop()
            


    # print(x,y)


i,j = linearSearch(grid,"S")
ans = ans1 = 0

# visited = []
x = find_loop(i,j)
print(x)

print(ans)
print(ans1)
# Good stuff
# print("="*80)