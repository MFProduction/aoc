#!usr/bin/env python
lines = [line.rstrip() for line in open(0).readlines()]


def transform(list,part=False):
    new_list = []
    for i, l in enumerate(list):
        l = int(l)
        if i < (len(list)-1):
            new_list.append(list[i+1]-l)
    
    if all(v == 0 for v in new_list):
        return list[0] if part else list[-1]
    else:
        return (list[0] - transform(new_list,part)) if part else (list[-1] + transform(new_list,part))

 
ans = ans1 = 0
for line in lines:
    line = [int(x) for x in line.split()]
    ans+=transform(line)
    ans1+=transform(line,True)
    

print(ans)
print(ans1)