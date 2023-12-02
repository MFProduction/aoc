# D2 tried to fined better ways
from collections import defaultdict

lines = [line.rstrip() for line in open(0).readlines()]
sum = sum1 = 0
for line in lines:
    possible = True
    game, records = line.split(':')
    game_num = int(game.split()[1])
    values = records.split(";")
    V = defaultdict(int)
    for event in values:
        cubes = event.split(',')
        for cube in cubes:
            num, color = cube.split()
            num = int(num)
            V[color] = max(V[color], num)
            if int(num) > {'red': 12, 'blue': 14, 'green': 13}.get(color, 0):
                possible = False

    score = 1
    for v in V.values():
        score *= v
    sum1 += score
    if possible:
        sum += game_num
print(sum)
print(sum1)



