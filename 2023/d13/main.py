#!usr/bin/env python
from collections import defaultdict
import sys

sets = open(0).read().strip().split('\n\n')
lines = [s.split() for s in sets]

def check_(i,j,k,m):
    if j == m-1 or k == 0:
        if grid[i][k] == grid[i][j]:
            return True
        else:
            return False

    if grid[i][k] == grid[i][j]:
        return check_(i,j+1,k-1,m)
    else:
        return False

def text(grid):
    n = len(grid)
    m = len(grid[0])
    match = []
    for i in range(0,n):
        tmp_list = []
        for j in range(0,m):
            if j == m-1:
                continue
            if check_(i,j,j+1,m):
                tmp_list.append(j)
        if tmp_list != []:
            match.append(tmp_list)

    return set(match[0]).intersection(*match)

ans = ans1 = 0
for line in lines:
    grid = [list(l) for l in line]
    common_elements = list(text(line))
    if not common_elements:
        grid = list(map(list, zip(*grid)))
        common_elements = list(text(grid))
        if common_elements:
            x = 100
    else:
        x = 1

    print(common_elements)
    if len(common_elements) == 1:
        ans += (common_elements[0]+1) *x
    else:
        ans += (1) *x
        for xx in grid:
            print(xx)

print(ans)
print(ans1)
# Good stuff
# print("="*80)