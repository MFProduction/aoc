#!usr/bin/env python
import re

def find_it(lines):
    ans = 0
    for x in re.findall(r"mul\(\d+,\d+\)", lines):
        a,b = re.findall(r'\d+', x)
        ans += int(a)*int(b)
    return ans


lines = open(0).read()
ans1 = 0
for s in lines.split("do()"):
    dd = s.split("don't()")
    ans1 += find_it(dd[0])

print(find_it(lines))
print(ans1)