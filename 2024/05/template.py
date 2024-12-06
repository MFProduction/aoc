#!usr/bin/env python
from collections import defaultdict


ans = ans1 = 0
rules, lines = (part.split('\n') for part in open(0).read().strip().split('\n\n'))
ordered_rules = defaultdict(list)
for r in rules:
    x,y= map(int,r.split('|'))
    ordered_rules[x].append(y)

for line in lines:
    valid = True
    line = list(map(int,line.split(',')))
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[j] not in ordered_rules[line[i]]:
                valid = False
    if valid:
        ans+=line[len(line)//2]
    else:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[j] not in ordered_rules[line[i]]:
                    tmp = line[i]
                    line[i] = line[j]
                    line[j] = tmp
        ans1+=line[len(line)//2]

print(ans)
print(ans1)