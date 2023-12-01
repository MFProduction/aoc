# AOC - 2022 day2
lines = open(0).read().strip().split('\n')


values = { "X": 1, "Y": 2, "Z": 3,
           "A": 1, "B": 2, "C": 3
         }

score = 0
for line in lines:
    you, me = [values[i] for i in line.split()]
    if (me - you) % 3 == 1:
        score += 6
    if you == me:
        score += 3
    score += me

print(score)