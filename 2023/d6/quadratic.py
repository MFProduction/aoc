#!usr/bin/env python
from collections import defaultdict
import math

lines = [line.rstrip() for line in open(0).readlines()]
data_1 = {}
data_2 = {}
for line in lines:
    name,values = line.split(':')
    values = values.split()
    values_2 = int(''.join(values))
    data_1[name] = values
    data_2[name] = [values_2]

def quadratic(data):
    ans = 1
    for i, v in enumerate(data["Time"]):
        time = int(v)
        distance = int(data["Distance"][i])
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
        limit2 = math.floor((time + D) / 2)
        if limit1 * (time - limit1)  <= distance:
            limit1 += 1

        if limit2 * (time + limit2)  >= distance:
            limit2 -= 1

        x = limit2-limit1+1
        print(x)
        ans *= x
    return ans
        # sol2 = (-b+cmath.sqrt(d))/(2*a)




print(quadratic(data_1))
print('='*88)
print(quadratic(data_2))