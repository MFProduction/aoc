# AOC - 2022 day5
lines = open(0).readlines()
T = [[],["P","F","M","Q","W","G","R","T"],["H","F","R"],["P","Z","R","V","G","H","S","D"],["Q","H","P","B","F","W","G"],["P","S","M","J","H"],["M","Z","T","H","S","R","P","L"],["P","T","H","N","M","L"],["F","D","Q","R"],["D","S","C","N","L","P","H"]]

def main(part=1):
    for line in lines:
        x = line.split()
        change_count = int(x[1])
        change_from = int(x[3])
        change_to = int(x[5])
        change = T[change_from][-change_count:]
        if part == 1:
            change = change[::-1]
        del T[change_from][len(T[change_from]) - change_count:]
        T[change_to][-change_count:] += change

    s = ""
    for p in T:
        s += ''.join(p[-1:])
    return s

print(main(1))
print(main(2))