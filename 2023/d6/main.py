#!usr/bin/env python
from collections import defaultdict

lines = [line.rstrip() for line in open(0).readlines()]
times = [int(x) for x in  lines[0].split(':')[-1].split()]
distances = [int(x) for x in lines[1].split(':')[-1].split()]

def calculate(time,record):
    count = 0
    start_point = time//2
    for x in range(start_point, 0,-1):
        if x*(time-x) > record:
            count +=1
        else:
            break
    for x in range(start_point+1, time):
        if x*(time-x) > record:
            count +=1
        else:
            break
    return count

ans = ans1 = 1
for i, v in enumerate(times):
    ans *= calculate(v, distances[i])
print(ans)

t = int(''.join(map(str, times)))
d = int(''.join(map(str, distances)))
ans1 *= calculate(t, d)
print(ans1)