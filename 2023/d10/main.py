#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import queue

lines = [l.strip() for l in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])


def linearSearch (arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == target):
                return [i,j]
    return [-1,-1]


start = linearSearch(grid,"S")
start.append("start")
ans = ans1 = 0
ll = []
D = defaultdict(list)
q = queue.Queue(maxsize=0)
q.put(start)
while q.empty() == False:
    point = q.get()
    x,y,way= point
    pipe_type = grid[x][y]
    ll.append([x,y])
    D[x].append(y)
    if pipe_type == "S" and way=="start":
        # q.put([x-1,y,"up"])
        q.put([x,y+1,"right"])
    elif pipe_type == "F" and way == "up":
        q.put([x,y+1,"right"])
    elif pipe_type == "F" and way == "left":
        q.put([x+1,y,"down"])
    elif pipe_type == "-" and way == "right":
        q.put([x,y+1,"right"])
    elif pipe_type == "-" and way == "left":
        q.put([x,y-1,"left"])
    elif pipe_type == "|" and way == "up":
        q.put([x-1,y,"up"])
    elif pipe_type == "|" and way == "down":
        q.put([x+1,y,"down"])
    elif pipe_type == "J" and way == "down":
        q.put([x,y-1,"left"])
    elif pipe_type == "J" and way == "right":
        q.put([x-1,y,"up"])
    elif pipe_type == "7" and way == "right":
        q.put([x+1,y,"down"])
    elif pipe_type == "7" and way == "up":
        q.put([x,y-1,"left"])
    elif pipe_type == "L" and way == "left":
        q.put([x-1,y,"up"])
    elif pipe_type == "L" and way == "down":
        q.put([x,y+1,"right"])
    elif pipe_type == "S" and way != "start":
        print(D)
        print(round(len(ll)/2))

for i in range(0, n):
    inside = False
    points = set(D[i])
    print(points)
    for j in range(0,m):
        if j in points:
            continue
        l = r = 0
        for x in points:
            if j < x:
                r+=1
            else:
                l+=1
        print(l,r,j)
        if (l % 2) != 0 and r > 0:
            ans+=1
            print("add",i,j)
    print("="*88)

print(ans)
print(ans1)
# Good stuff
# print("="*80)