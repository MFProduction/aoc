# D2 my solution
lines = [line.rstrip() for line in open(0).readlines()]
sum = sum1 = 0
for line in lines:
    r=g=b= 0
    possible = True
    game, records = line.split(':')
    game_num = int(game.split()[1])
    values = records.split(";")
    for event in values:
        cubes = event.split(',')
        for cube in cubes:
            num, color = cube.split()
            num = int(num)
            if color == "red":
                if num > 12:
                    possible = False
                if r < num:
                    r = num
            elif color == "green":
                if num > 13:
                    possible = False
                if g < num:
                    g = num
            elif color == "blue":
                if num > 14:
                    possible = False
                if b < num:
                    b = num
        power = r*g*b
    sum1 += power
    if possible:
        sum += game_num
print(sum)
print(sum1)



