#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import itertools

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
    print(lst)
    # lst = list(filter(lambda x: x != "", lst))
    if len(lst) != len(ch):
        return False
    for i, l in enumerate(lst):
        if len(l) == int(ch[i]):
            valid.append(True)
        else:
            valid.append(False)
    return all(valid)

def validate(lst, chart,iofq):
    print(lst)
    for i len(iofq)*2:
        for j in ["#","."]:
            lo = lst.replace("?",j,1)
            if lst.count("?")>0:
                return validate(lst, chart)
            print(valid(lst,chart))
            if valid(lst,chart):
                return True


ans = ans1 = 0
for line in lines:
    lst,chart = line.split()
    # lst = [*lst
    chart = chart.split(',')
    iofq = find_indices(lst,"?")
    print(validate(lst,chart))
    print("+"*88)


print(ans)
print(ans1)
# Good stuff
# print("="*80)