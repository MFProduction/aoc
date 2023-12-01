# AOC - 2022 day3
lines = [line.rstrip() for line in open(0).readlines()]
abc = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1():
    ss = 0
    for line in lines:
        f, s = line[:len(line)//2], line[len(line)//2:]
        for c in f:
            if c in s:
                ss = ss + abc.rfind(c)
                break
    return ss

def p2():
    x = y = ss = 0
    while x < len(lines)//3:
        l1, l2, l3 = lines[y], lines[y+1], lines[y+2]
        for char in l1:
            if char in l2 and char in l3:
                ss += abc.rfind(char)
                break
        x += 1
        y += 3
    return ss

def main(step=1):
    x = y = ss = 0
    while x < len(lines)//step:
        l1, l2, l3 = lines[y], lines[y+1], lines[y+2]
        for char in l1:
            if char in l2 and char in l3:
                ss += abc.rfind(char)
                break
        x += 1
        y += 3
    return ss

print(p1())
print(p2())