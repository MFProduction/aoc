#!usr/bin/env python
lines = open(0).read().strip().split('\n')
A = []
B = []
ans = ans1 = 0
for line in lines:
    A.append(int(line.split("  ")[0]))
    B.append(int(line.split("  ")[1]))

A.sort()
B.sort()
for x,i in enumerate(A):
    ans += abs(i - B[x])
    ans1 += i * (B.count(i))

print(ans)
print(ans1)