# AOC day1
file1 = open('input.txt', 'r')
# file1 = open('sample.txt', 'r')

def p1():
    count = 0
    lines = file1.readlines()
    max_total = 0

    total = 0
    for line in lines:
        count += 1
        if not line.strip():
            if total > max_total:
                max_total = total
            total = 0
        else:
            total = total + int(line.strip())
        print(total)
    print(max_total)

def p2():
    lines = file1.readlines()
    max_total_1 = 0
    max_total_2 = 0
    max_total_3 = 0

    total = 0
    for line in lines:
        if not line.strip():
            if total > max_total_1:
                max_total_3 = max_total_2
                max_total_2 = max_total_1
                max_total_1 = total
            elif total > max_total_2:
                max_total_3 = max_total_2
                max_total_2 = total
            elif total > max_total_3:
                max_total_3 = total
            total = 0
            # print(max_total_1)
            # print(max_total_2)
            # print(max_total_3)
        else:
            total = total + int(line.strip())
    print(max_total_1 + max_total_2 + max_total_3)
    # print(max_total_1)
    # print(max_total_2)
    # print(max_total_3)
p2()