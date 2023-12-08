#!usr/bin/env python
lines = [line.rstrip() for line in open(0).readlines()]

ans = ans1 = 0
for line in lines:
    dim = [int(x) for x in line.split("x")]
    l,h,w = dim
    dim.sort()
    ans += 2*l*w + 2*w*h + 2*h*l  + min(l*w, w*h, h*l)
    ans1 += 2*dim[0] + 2*dim[1] + l*w*h

print(ans)
print(ans1)
