#!usr/bin/env python
import math

lines = [line.rstrip() for line in open(0).readlines()]
times = [int(x) for x in  lines[0].split(':')[-1].split()]
distances = [int(x) for x in lines[1].split(':')[-1].split()]

def quadratic(time,distance):
    ans = 1
    # charge_time = 0
    # D(charge_time) = time*(time-charge-time) How far the car will travel if we charge it or charge_time
    # D(charge_time) > Dr # to bet record
    # charge_time * (time-charge_time) > distance
    # charge_time * (time-charge_time) = distance
    # charge_time**2 + charge_time*time + distance = 0
    # charge_time = (time +- sqrt(time**2 - 4 distance))/2
    # (time - sqrt(time**2 -4*distance))/2 < charge_time < (time + sqrt(time**2 - 4*distance))/2
    # (time - sqrt(time**2 -4*distance))/2 < charge_time < (time + sqrt(time**2 - 4*distance))/2
    D = (math.sqrt(time**2 -4*distance))
    limit1 = math.ceil((time - D) / 2)
    limit2 = math.ceil((time + D) / 2)
    if limit1 * (time - limit1)  <= distance:
        limit1 += 1

    if limit2 * (time + limit2)  >= distance:
        limit2 -= 1

    return limit2-limit1+1

def calculate(time,record):
    count = 0
    start_point = time//2
    # # Takes 4sec
    # for r in range(time):
    #     if r*(time-r) > record:
    #         count +=1

    # Takes 3sec
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
for time, distance in zip(times, distances):
    # ans *= calculate(time, distance)
    ans *= quadratic(time, distance)
print(ans)

t = int(''.join(map(str, times)))
d = int(''.join(map(str, distances)))
# ans1 *= calculate(t, d)
ans1 *= quadratic(t, d)
print(ans1)