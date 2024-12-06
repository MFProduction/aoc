#!usr/bin/env python
def check_safety(line):
    order = 'ASC' if int(line[0]) > int(line[1]) else "DSC"
    safe = True
    for x,i in enumerate(line):
        if x == len(line) -1:
            break

        if (order == "ASC" and i > line[x+1] and not i >  line[x+1] +3) or (order == "DSC" and i < line[x+1] and not i < line[x+1]-3):
            continue
        safe = False
    return safe

lines = [list(map(int,line.rstrip().split(" "))) for line in open(0).readlines()]
ans = ans1 = 0
for line in lines:
    if check_safety(line):
        ans += 1
        ans1 += 1
    else:
        for x in range(len(line)):
            new_line = []
            new_line.extend(line)
            new_line.pop(x)
            if check_safety(new_line):
                ans1 += 1
                break
         
print(ans)
print(ans1)
