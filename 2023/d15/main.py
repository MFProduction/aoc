#!usr/bin/env python
from collections import defaultdict

lines = open(0).readlines()[0].split(',')
ans = ans1 = 0

def hash_algo(line):
    value = 0
    for l in line:
        value += ord(l)
        value *= 17
        value = value % 256
    return value

for l in lines:
    ans += hash_algo(l)
print(ans)


hashmap = defaultdict(list)
for line in lines:
    if "=" in line:
        label,focal_length = line.split('=')
    else:
        label = line[:-1]
    hash_value = hash_algo(label)
    if "=" in line:
        ind = None
        for i, val in enumerate(hashmap[hash_value]):
            if val[0] == label:
                ind = i

        if ind != None:
            hashmap[hash_value][ind] = [label,focal_length]
        else:
            hashmap[hash_value].append([label,focal_length])
    else:
        for i, h in enumerate(hashmap[hash_value]):
            if h[0] == label:
                hashmap[hash_value].pop(i)

for key, values in hashmap.items():
    for i, l in enumerate(values):
        ans1+= (1+int(key)) * (i+1) * int(l[1])
print(ans1)
