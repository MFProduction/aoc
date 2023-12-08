#!usr/bin/env python
lines = open(0).read()

def floos(part=False):  
    ans = 0
    pos = 1
    for line in lines:
        if line == "(":
            ans +=1
        elif line == ")":
            ans -=1
        if part and ans == -1:
            return pos
        pos +=1
    return ans

print(floos())
print(floos(True))