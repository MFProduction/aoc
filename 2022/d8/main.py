# AOC - 2022 day7
lines = [list(line.rstrip()) for line in open(0).readlines()]

def p1():
    sum = 0
    for i, i_val in enumerate(lines):
        for j, j_val in enumerate(i_val):
            if i == 0 or j == 0 or (i == len(lines) -1) or (j == len(lines[i]) - 1):
                sum += 1
            else:
                char = lines[i][j]
                is_bigger = True
                i0 = i1 = i2 = i3 = 0
                j0 = j1 = j2 = j3 = 0
                for x in range(0,j):
                    if lines[i][x] >= char:
                        i0 += 1
                for x in range(j+1,len(lines[i])):
                    if lines[i][x] >= char:
                        i1 += 1
                for x in range(0,i):
                    if lines[x][j] >= char:
                        i2 += 1
                for x in range(i+1,len(lines)):
                    if lines[x][j] >= char:
                        i3 += 1

                if i0 == 0 or i1 == 0 or i2 == 0 or i3 == 0:
                    sum += 1
    return sum

def p2():
    score = []
    for i, i_val in enumerate(lines):
        for j, j_val in enumerate(i_val):
            if i == 0 or j == 0 or (i == len(lines) -1) or (j == len(lines[i]) - 1):
                continue
            else:
                char = lines[i][j]
                print("CHAR: ", char, i,j)
                c1 = c2 = c3= c4 = 0
                for x in range(j-1,-1, -1):
                    if lines[i][x] < char:
                        c1 += 1
                    else:
                        c1 += 1
                        break
                for x in range(j+1,len(lines[i])):
                    # print(lines[i][x])
                    if lines[i][x] < char:
                        c2 += 1
                    else:
                        c2 += 1
                        break
                for x in range(i-1,-1,-1):
                    if lines[x][j] < char:
                        c3 += 1
                    else:
                        c3 += 1
                        break
                for x in range(i+1,len(lines)):
                    if lines[x][j] < char:
                        c4 += 1
                    else:
                        c4 += 1
                        break
                score.append(c1*c2*c3*c4)
    return max(score)

print(p1())
print(p2())

