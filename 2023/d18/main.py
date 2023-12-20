#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import operator

# lines = open(0).read()
# lines = open(0).readlines()
# lines = open(0).read().strip().split('\n')
lines = [line.rstrip() for line in open(0).readlines()]

def move(state,d,m):
    i,j = state
    if d == "R":
        for r in range(j,j+m+1):
            visited[i].append(r)
        state = (i,j+m)
    elif d == "L":
        for r in range(j,j-m-1, -1):
            visited[i].append(r)
        state = (i,j-m)
    elif d == "U":
        for r in range(i,i-m-1, -1):
            visited[r].append(j)
        state = (i-m,j)
    elif d == "D":
        for r in range(i,i+m+1):
            visited[r].append(j)
        state = (i+m,j)
    return state

ans = ans1 = 0
visited = defaultdict(list)
state=(0,0)
visited[0].append(0)
for line in lines:
    d,m,c = line.split()
    m = int(m)
    c = c[1:-1]
    state = move(state,d,m)

    # print(d,m,c)
visited = dict(sorted(visited.items(), key=operator.itemgetter(0)))
# print(visited)
n = len(visited)
m = -99999999999999
for i in range(list(visited.keys())[0],n):
    if i in visited:
        minn = abs(min(visited[i]))
        maxx = abs(max(visited[i]))+1
        # print(minn,maxx, minn+maxx)
        m = max(m,minn+maxx)


# shoud use shulace formula +
# for k,x in visited.items():
#     print(k,x)
# import sys
# sys.exit(1)
# for k in range(list(visited.keys())[0],n):
#     if k in visited:
#         visited[k] = list(set(visited[k]))
#         if visited[k] != []:
#             # ans += len(visited[k])
#             print(visited[k][0],visited[k][-1],abs(visited[k][0]-visited[k][-1])+1)
#             ans+=abs(visited[k][0]-visited[k][-1])+1
#                 # tmp_pair = 0
#                 # first = visited[k][tmp_pair]
#                 # second = visited[k][tmp_pair+1]
#                 # last = visited[k][-1]
#                 # tmp_pair +=1
#                 # for x in range(visited[k][0], m):
#                 #     if first < x < second:
#                 #         ans+=1
#                 #     elif x == second and second != last:
#                 #         first = visited[k][tmp_pair]
#                 #         second = visited[k][tmp_pair+1]
#                 #         tmp_pair +=1





print(ans)
print(ans1)
# Good stuff
# print("="*80)