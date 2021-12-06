coordinates = []
with open("input-test.txt") as f:
    for line in f:
        coordinates.append(line.strip().split("->"))

rows = cols = 10
arr = [[0 for i in range(cols)] for j in range(rows)]

for row in coordinates:
    x1,y1 = row[0].strip().split(",")
    x2, y2 = row[1].strip().split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x2 > x1:
        x1, x2 = x2, x1
    if y2 > y1:
        y1, y2 = y2, y1
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
        ii = 0
        while True:
            if k > 0:                
                arr[y1-ii][x1-ii] +=1
            else:
                
                arr[y1-ii][x1+ii] +=1
            if  x1-ii == x2:
                break
            ii += 1
sum = 0

for r in arr:
    print(r)

for r in arr:
    for i in r:
        if i > 1:
            sum += 1

print(sum)