#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
import queue
import time
lines = [line.rstrip() for line in open(0).readlines()]
grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
ans = ans1 = 0
D = defaultdict(int)
def move(i,j,w):
    maze_type = grid[i][j]
    if w == "r":
        if maze_type in ['.','-']:
            q.put((i,j+1,"r"))
        elif maze_type == '/':
            q.put((i-1,j,"u"))
        elif maze_type == "\\":
            q.put((i+1,j,"d"))
        elif maze_type == '|':
            q.put((i-1,j,"u"))
            q.put((i+1,j,"d"))
    elif w == "l":
        if maze_type in ['.','-']:
            q.put((i,j-1,"l"))
        elif maze_type == '/':
            q.put((i+1,j,"d"))
        elif maze_type == '\\':
            q.put((i-1,j,"u"))
        elif maze_type == '|':
            q.put((i-1,j,"u"))
            q.put((i+1,j,"d"))
    elif w == "u":
        if maze_type in ['.','|']:
            q.put((i-1,j,"u"))
        elif maze_type == '/':
            q.put((i,j+1,"r"))
        elif maze_type == '\\':
            q.put((i,j-1,"l"))
        elif maze_type == '-':
            q.put((i,j-1,"l"))
            q.put((i,j+1,"r"))
    elif w == "d":
        if maze_type in ['.','|']:
            q.put((i+1,j,"d"))
        elif maze_type == '/':
            q.put((i,j-1,"l"))
        elif maze_type == '\\':
            q.put((i,j+1,"r"))
        elif maze_type == '-':
            q.put((i,j-1,"l"))
            q.put((i,j+1,"r"))

visited = [[False] * m for _ in range(n)]
q = queue.Queue(maxsize=0)
q.put((0,0,"r"))
cccc = 0
while q.empty() == False:
    i,j,way= q.get()
    if (0 <= i < n and 0 <= j < m):
        visited[i][j] = True
        # print([i,j], grid[i][j])
        cccc +=1
        # if cccc % 1000000 == 0:
        p = 0
        for x in visited:
            p+=sum(x)
        print(p)
        # time.sleep(0.2)
        move(i,j,way)

# for x in visited:
#     print(x)
#     ans+=sum(x)

print(ans)
print(ans1)
# Good stuff
# print("="*80)