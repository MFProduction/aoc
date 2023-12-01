# AOC - 2022 day2
file1 = open('input.txt', 'r')
# file1 = open('sample.txt', 'r')
lines = file1.readlines()
values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}

def p1():
    score = 0
    for line in lines:
        i1 = values[line.strip()[0]]
        i2 = values[line.strip()[2]]
        if i1 == i2:
            i2 = i2 + 3
        elif (i2 == 1 and i1 == 3) or (i2 == 3 and i1 == 2) or (i2 == 2 and i1 == 1):
            i2 = i2 + 6
        score = score + i2
    return score

def p2():
    score = 0
    for line in lines:
        i1 = values[line.strip()[0]]
        i2 = values[line.strip()[2]]
        if i2 == 1:
            if i1 == 3:
                s = 2
            elif i1 == 1:
                s = 3
            elif i1 == 2:
                s = 1
        elif i2 == 2:
            s = 3 + i1
        elif i2 == 3:
            if i1 == 1:
                s = 2 + 6
            elif i1 == 2:
                s = 3 + 6
            elif i1 == 3:
                s = 1 + 6
        score = score + s
    return score

print(p1())
print(p2())