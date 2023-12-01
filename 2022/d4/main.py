# AOC - 2022 day4
lines = [line.rstrip() for line in open(0).readlines()]

# WRONG
def p1():
    ss = 0
    for line in lines:
        i,j = line.split(',')
        ir1,ir2 = i.split('-')
        jr1,jr2 = j.split('-')
        r1 = range(int(ir1),int(ir2))
        r2 = range(int(jr1),int(jr2))
        if set(r1).issubset(r2) or set(r2).issubset(r1):
        # if (ir1 >= jr1 and ir2 <= jr2) or (jr1 >= ir1 and jr2 <= ir2):
            ss = ss + 1
    return ss

# Right
def p12():
    ss = 0
    for line in lines:
        elfs = line.split(',')
        ranges = [list(map(int, elf.split("-"))) for elf in elfs]
        a,b = ranges[0]
        c,d = ranges[1]
        if (a <= c and b >= d) or (a >= c and b <= d):
            ss += 1
    return ss

def p2():
    pass

print(p1())
print(p12())
# print(p2())