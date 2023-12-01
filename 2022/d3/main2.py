# AOC - 2022 day3
from string import ascii_lowercase, ascii_uppercase
lines = [line.rstrip() for line in open(0).readlines()]
abc = ascii_lowercase + ascii_uppercase
print(abc.index('A'))

def p1():
    ss = 0
    for line in lines:
        f, s = line[:len(line)//2], line[len(line)//2:]
        for c in f:
            if c in s:
                ss += abc.index(c) + 1
                break
    return ss

# worse method always go rhrough whole abc
def p12():
    ss = 0
    for line in lines:
        f, s = line[:len(line)//2], line[len(line)//2:]
        for i, c in enumerate(abc):
            if c in s and c in f:
                ss += abc.index(c) + 1
                break
    return ss


def p2():
    x = y = ss = 0
    while x < len(lines)//3:
        l1, l2, l3 = lines[y], lines[y+1], lines[y+2]
        for char in l1:
            if char in l2 and char in l3:
                ss += abc.index(char) + 1
                break
        x += 1
        y += 3
    return ss

def p22():
    ss = 0
    for i in range(0, len(lines), 3):
        a = lines[i:(i+3)]
        for i, c in enumerate(abc):
            if all([c in li for li in a]):
                ss += abc.index(c)
    return ss


print(p1())
print(p12())
print(p2())
print(p22())