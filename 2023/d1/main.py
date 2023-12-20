# D1
import re
# file1 = open('input-test.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()
numeric_strings = ["one", "two", "three", "four","five","six","seven","eight", "nine"]

map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def p1():
    sum = 0
    for line in lines:
        num = ""
        for c in line.strip():
            if c.isnumeric():
                num += c
        if len(num) == 0:
            x = 0
        elif len(num) == 1:
            x = int(f"{num}{num}")
        else:
            x = int(f"{num[0]}{num[-1]}")
        sum += x
    return sum

def p2():
    sum = 0
    for line in lines:
        num = ""
        str = ""
        x = []
        for c in line:
            print(str)
            for i, n in enumerate(numeric_strings):
                if n in str:
                    if map[n] not in x:
                    # if map[n] != x[-1:]:
                        num += map[n]
                        x.append(map[n])
                    # str = ""
            print(x)
            if not c.isnumeric():
                str += c
            if c.isnumeric():
                num += c
                str = ""
        print(num)
        if len(num) == 0:
            x = 0
        elif len(num) == 1:
            x = int(f"{num}{num}")
        else:
            x = int(f"{num[0]}{num[-1]}")
        sum += x
        print(x)
    return sum


def p3():
    sum = 0
    for line in lines:
        f = 0
        l = 0
        split = list(filter(None, re.split(r'(\d+)', line.strip())))
        for s in split:
            if s.isnumeric():
                if len(s) == 1:
                    if f == 0:
                        f = int(s)
                    l = int(s)
                else:
                    if f == 0:
                        f = int(s[0])
                    l = int(s[-1])

            else:
                tmp = ''
                x = []
                for char in s:
                    tmp += char
                    for  ns in numeric_strings:
                        # print(tmp)
                        if ns in tmp:
                            if len(x) > 0:
                                if f == 0:
                                    f = x[0]
                                l = x[-1]
        ss = f"{f}{l}"
        print(line, ss)
        # time.sleep(3)
        sum += int(ss)
    return sum
        # print(int(ss))
        # print()
        # print(f,l)


def p4():
    sum = 0
    for line in lines:
        p = []
        for i, c in enumerate(line):
            if c.isdigit():
                p.append(c)
            for d, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(val):
                    p.append(str(d+1))
        score = int(p[0]+p[-1])
        sum += score
    return sum






# print(p1())
print(p3())
print(p4())