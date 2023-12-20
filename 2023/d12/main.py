#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import itertools

# lines = open(0).read()
# lines = open(0).readlines()
# lines = open(0).read().strip().split('\n')
lines = [line.rstrip() for line in open(0).readlines()]

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def valid(lst,ch):
    if "?" in lst:
        return False
    valid = []
    lst = list(filter(lambda x: x != "", lst.split('.')))
    if len(lst) != len(ch):
        return False
    for i, l in enumerate(lst):
        if len(l) == int(ch[i]):
            valid.append(True)
        else:
            valid.append(False)
    return all(valid)

ans = ans1 = 0
for line in lines:
    lst,chart = line.split()
    lst = [*lst]
    chart = chart.split(',')
    iofq = find_indices(lst,"?")
    print(iofq)
    D = defaultdict(list)
    for i in iofq:
        D[i] = [".","#"]
    print(D)
    print(valid(lst,chart))


print(ans)
print(ans1)
# Good stuff
# print("="*80)