#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import math
import sys


lines = [line.rstrip() for line in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
ans = ans1 = 0

# https://www.geeksforgeeks.org/calculate-the-manhattan-distance-between-two-cells-of-given-2d-array/
def manhattanDist(X1, Y1, X2, Y2):
    dist = math.fabs(X2 - X1) + math.fabs(Y2 - Y1)
    return (int)(dist)

def find_missing(lst, rr):
    list1 = []
    for l in range(0,rr):
        if l not in lst:
            list1.append(l)
    return list1


a_c = set()
a_r = set()
for i in range(0,n):
    for j in range(0,m):
        if grid[i][j] == "#":
            a_r.add(i)
            a_c.add(j)
# 2, 5, 8
missing_c = find_missing(list(a_c), m)

for i in range(0,n):
    for j in missing_c:
        grid[i].insert(j,".")
m += len(missing_c)
missing_r = find_missing(list(a_r), n)
for i in missing_r:
        n += 1
        grid.insert(i,["."]*m)
print(grid[5])
G = []
for i in range(0,n):
    for j in range(0,m):
        if grid[i][j] == "#":
            G.append(tuple([i,j]))



for i in range(0,len(G)):
    x1,y1 = G[i]
    for j in range(i+1,len(G)):
        x2,y2 = G[j]
        # for cc in missing_c:
        #     if (x1 < cc < x2):
        #         x2+=1
        #     elif(x2 < cc < x1):
        #         print("row", rr)
        #         x1+=1
        # for rr in missing_r:
        #     if (y1 < rr < y2):
        #         y2+=1
        #     elif (y2 <= rr <= y1):
        #         y2-=1
        # print(x1,y1)
        # print(x2,y2)
        # print("="*88)
        ans +=manhattanDist(x1,y1,x2,y2)
print(ans)
print(ans1)
# Good stuff
# print("="*80)