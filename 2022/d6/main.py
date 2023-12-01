# AOC - 2022 day6
lines = open(0).read()

def p1(num=4):
    x = 0
    for l in lines:
        p, y =list(set(lines[x:x+num])), list(lines[x:x+num])
        p.sort()
        y.sort()
        x += 1
        if(p==y):
            break
    return x+(num-1)

def p11(num=4):
    x = 0
    for l in lines:
        data = lines[x:(x+num)]
        x += 1
        print(data)
        print(set(data))
        if len(set(data)) == num:
            break
    return x+(num-1)

print(p1())
print(p1(14))

print(p11())
print(p11(14))
