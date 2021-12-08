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

def count_normal(input):
    res = 0
    for i in input:
        serial = i.split("|")[0].split()
        out = i.split("|")[1].split()
        for o in out:
            if len(o) == 2 or len(o) == 3 or len(o) == 7 or len(o) == 4:
                res += 1
    return(res)

print(count_unique(input))
# print(fuel(input, "high"))
