# AOC day1
# file1 = open('input.txt', 'r')
file1 = open('sample.txt', 'r')
lines = file1.readlines()

values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def who_won(you,me):
    if you == me:
        return 3 + values[me] #draw
    elif me == "X" and you == "Z": # sum = 4
        return values[me] + 6 # win
    elif me == "Y" and you == "X":  # 3
        return values[me] + 6 # win
    elif me == "Z" and you == "Y":  # sum 5
        return values[me] + 6
    else:
        return  values[me]

def who_should_win(you,tt):
    if tt == "X": # LOse
        if you == "Z":
            return values["Y"]
        elif you == "X":
            return values["Z"]
        elif you == "Y":
            return values["X"]
    elif tt == "Y": # Draw
        return 3 + values[you]
    elif tt == "Z": # Win
        if you == "X":
            return values["Y"] + 6
        elif you == "Y":
            return values["Z"] + 6
        elif you == "Z":
            return values["X"] + 6

def p1():
    score = 0
    for line in lines:
        you = line.strip()[0]
        me = line.strip()[2]
        if you == "A":
            you = "X"
        elif you == "B":
            you = "Y"
        elif you == "C":
            you = "Z"
        # print(who_won(you,me))
        score = score + who_won(you,me)
    return score

def p2():
    score = 0
    for line in lines:
        you = line.strip()[0]
        me = line.strip()[2]
        if you == "A":
            you = "X"
        elif you == "B":
            you = "Y"
        elif you == "C":
            you = "Z"
        score = score + who_should_win(you,me)
    return score

print(p1())
print(p2())