#!usr/bin/env python
lines = open(0).read()

visited = set()
position = (0,0)
visited.add(position)
for line in lines:
    x,y = position
    if line == "^":
        position = (x-1,y)
    elif line == "v":
        position = (x+1,y)
    elif line == ">":
        position = (x,y+1)
    elif line == "<":
        position = (x,y-1)
    visited.add(position)

print(len(set(visited)))

visited = set()
p1 = p2 = (0,0)
visited.add(p1)
for i in range(0,len(lines), 2):
    x,y = p1
    a,b = p2
    if lines[i] == "^":
        p1 = (x-1,y)
    elif lines[i] == "v":
        p1 = (x+1,y)
    elif lines[i] == ">":
        p1 = (x,y+1)
    elif lines[i] == "<":
        p1 = (x,y-1)
    
    if lines[i+1] == "^":
        p2 = (a-1,b)
    elif lines[i+1] == "v":
        p2 = (a+1,b)
    elif lines[i+1] == ">":
        p2 = (a,b+1)
    elif lines[i+1] == "<":
        p2 = (a,b-1)
    
    visited.add(p1)
    visited.add(p2)

print(len(set(visited)))