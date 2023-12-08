#!usr/bin/env python
from collections import Counter

lines = [line.rstrip() for line in open(0).readlines()]

ans = ans1 = 0
wovles = "aeiou"
n = ["ab", "cd", "pq", "xy"]
def nice(line):
    wc = 0
    twice = False
    if any(x in line for x in n):
         return False
    for i, char in enumerate(line):
        if char in wovles:
            wc +=1
        if i < len(line)-1:
            if char == line[i+1]:
                twice = True
    if wc >= 3 and twice:
        return True
    return False

def nice2(line):
    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    for i, char in enumerate(line):
        twice = False
        count = Counter(line)
        print(count)
        if i < len(line)-2:
            if char == line[i+2]:
                # print(line, char,line[i+2])
                twice = True


for line in lines:
    # if nice(line):
    #     ans+=1
    if nice2(line):
        ans1+=1


print(ans)
print(ans1)
# Good stuff
# print("="*80)