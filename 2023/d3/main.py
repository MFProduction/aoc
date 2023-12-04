#!usr/bin/env python
from collections import defaultdict

lines = [line.rstrip() for line in open(0).readlines()]
ans = ans1 = 0
n = len(lines)
m = len(lines[0])

def has_symbol(i,j):
    valid = False
    sym = None
    # for di in [-1,0,1]:
        # for dj in [-1,0,1]:
            # if  0 <= i+di < n and 0 <= j+dj < m:
            # then do stuff
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        ii = i + di
        jj = j + dj

        if not (0 <= ii < n and 0 <= jj < m):
            continue

        if (not lines[ii][jj].isdigit()) and (not lines[ii][jj] == '.'):
            valid = True
        if lines[ii][jj] == "*":
            sym = (ii, jj)
    return valid, sym

stars = defaultdict(list)
for i,line in enumerate(lines):
    num = ""
    valid = False
    star = None
    for j, element in enumerate(line):
        if element.isnumeric():
            num += element
            is_valid, star_coordinates = has_symbol(i,j)
            if not star:
                star = star_coordinates
            if is_valid:
                valid = True
            if m == j+1:
                if valid:
                    ans += int(num)
                if star:
                    stars[star].append(num)
                num = ""
                valid = False
                star = None
        else:
            if num != "":
                if valid:
                    ans += int(num)
                if star:
                    stars[star].append(num)
            num = ""
            valid = False
            star = None

for _,v in stars.items():
    if len(v) == 2:
        ans1 += (int(v[0]) * int(v[1]))

print(ans)
print(ans1)



# Imprivments
# n = n*10+int(new_number)