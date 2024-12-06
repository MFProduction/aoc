#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase

def xmas(i,j,char, path=[[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]):
    sym = []
    for di, dj in path:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if lines[ii][jj] == char:
            sym.append((ii, jj, [di,dj]))
    return sym


def x_mas(i,j):
    x = []
    y = []
    for di, dj in [[1, 1],[-1, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if lines[ii][jj] in ["S","M"]:
            x.append(lines[ii][jj])
    
    for di, dj in [[1, -1], [-1, 1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if lines[ii][jj] in ["S","M"]:
            y.append(lines[ii][jj])
    
    x.sort()
    y.sort()
    if ["M","S"] == x and ["M","S"] == y:
        return 1
    else:
        return 0

lines = [line.rstrip() for line in open(0).readlines()]
n = len(lines)
m = len(lines[0])
ans = ans1 = 0
start_points = []
for i, line in enumerate(lines):
    for j, l in enumerate(line):
        if l == "X":
            start_points.append((i,j))
        if l == "A":
            ans1 += x_mas(i,j)

M_valid_options = []
for X in start_points:
    M_valid_options.extend(xmas(X[0],X[1],"M"))
A_valid_options = []
for M in M_valid_options:
    A_valid_options.extend(xmas(M[0],M[1],"A",[M[2]]))

S_valid_options = []
for A in A_valid_options:
    S_valid_options.extend(xmas(A[0],A[1],"S",[A[2]]))

print(len(S_valid_options))
print(ans1)
