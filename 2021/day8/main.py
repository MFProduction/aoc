NUMBERS = {
    0: [0,1,4,5,6],
    1: [2,5],         
    2: [0,2,3,4,6],
    3: [0,2,3,5,6],
    4: [1,2,3,5],
    5: [0,1,3,5,6],
    6: [0,1,3,4,5,6],
    7: [0,2,5],
    8: [0,1,2,3,4,5,6],
    9: [0,1,2,3,5,6]
}

input = []
with open("input.txt") as f:
    for line in f:
        input.append(line.strip())


def count_unique(input):
    res = 0
    for i in input:
        inn = i.split("|")[0]
        out = i.split("|")[1].split()
        for o in out:
            if len(o) == 2 or len(o) == 3 or len(o) == 7 or len(o) == 4:
                res += 1
    return(res)

def splitw(word):
    return [char for char in word]

def count_normal(input):
    summ_org =0
    for i in input:
        serials = i.split("|")[0].split()
        out = i.split("|")[1].split()
        all = splitw(sorted(serials, key=len))
        strings = {
            1: all[0],
            4: all[2],
            7: all[1],
            8: all[9] 
        }

        for x in all[3:6]:
            xxx = strings[4].replace(strings[1][0], "").replace(strings[1][1], "")
            if strings[1][0] in x and strings[1][1] in x:
                strings[3] = x
            elif xxx[0] in x and xxx[1] in x:
                strings[5] = x
            else:
                strings[2] = x
        for x in all[6:9]:
            if strings[4][0] in x and strings[4][1] in x and strings[4][2] in x and strings[4][3] in x:
                strings[9] = x
            elif strings[1][0] in x and strings[1][1] in x:
                strings[0] = x
            else:
                strings[6] = x
        xxxxxxxxx = ""
        for o in out:
            for key, val in strings.items():
                x = splitw(o)
                y = splitw(val)
                x.sort()
                y.sort()
                if x == y:
                    xxxxxxxxx += str(key)
        summ_org += int(xxxxxxxxx)
    return(summ_org)

# print(count_unique(input))
print(count_normal(input))
