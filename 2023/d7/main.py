#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase

lines = [line.rstrip().split() for line in open(0).readlines()]

def get_type(hand, part):
    d = defaultdict(int)
    for key in hand:
        d[key]+=1

    if part == 2:
        J = d.pop("J", 0)
        if J == 5:
            return 7
        max_value = max(d.values())
        max_value += J
    else:
        max_value = max(d.values())

    if max_value == 5:
        return 7
    elif max_value == 4:
        return 6
    elif max_value == 3:
        mmm = min(d.values())
        if mmm == 2:
            return 5
        else:
            return 4
    elif max_value == 2:
        if len(d) == 4:
            return 2
        else:
            return 3
    else:
        return 1

def get_order(hand1,hand2, part):
    if part == 1:
        order = list("23456789TJQKA")
    else:
        order = list("J23456789TQKA")
    for i, char in enumerate(hand1):
        if order.index(char) > order.index(hand2[i]):
            return hand1
        elif order.index(char) < order.index(hand2[i]):
            return hand2

def bubbleSort(arr,part):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if get_order(arr[j], arr[j+1], part) == arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


ans = ans1 = 0
type_map_1 = defaultdict(list)
type_map_2 = defaultdict(list)

bid_map = defaultdict(int)

for line , bid in lines:
    t1 = get_type(line, 1)
    t2 = get_type(line, 2)

    type_map_1[t1].append(line)
    type_map_2[t2].append(line)
    bid_map[line] = bid

rr = 1
for i in range(1,8):
    for s in bubbleSort(type_map_1[i], 1):
        ans += int(rr)*int(bid_map[s])
        rr +=1
rr = 1
for i in range(1,8):
    for s in bubbleSort(type_map_2[i], 2):
        ans1 += int(rr)*int(bid_map[s])
        rr +=1

print(ans)
print(ans1)