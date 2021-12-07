import math

coordinates = []
with open("input.txt") as f:
    for line in f:
        coordinates.append(line.strip().split("->"))

rows = cols = 1000
arr = [[0 for i in range(cols)] for j in range(rows)]

for row in coordinates:
    x1,y1 = list(map(int,row[0].strip().split(",")))
    x2, y2 = list(map(int,row[1].strip().split(",")))
    if x1 == x2:
        if y1 > y2:
            for y in range(y2, y1+1):
                arr[y][x1] += 1
        else:
            for y in range(y1, y2+1):
                arr[y][x1] += 1
    elif y1 == y2:
        if x1 > x2:
            for x in range(x2, x1+1):
                arr[y1][x] += 1
        else:
            for x in range(x1, x2+1):
                arr[y1][x] += 1
    else:
        k = (y2-y1)/(x2-x1)
        for ind in range(abs(x2-x1)+1):
            if k > 0:
                    if x1 > x2:
                        arr[y1-ind][x1-ind] +=1
                    else:
                        arr[y1+ind][x1+ind] +=1
            else:
                if x1 > x2:
                    arr[y1+ind][x1-ind] +=1
                else:
                    arr[y1-ind][x1+ind] +=1
sum = 0

for r in arr:
    for i in r:
        if i > 1:
            sum += 1

print(sum)
