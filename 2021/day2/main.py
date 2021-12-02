positions = []
with open("input.txt") as file:
    for line in file:
        name, var = line.partition(" ")[::2]
        position = [name.strip(), int(var.strip())]
        positions.append(position)


def move(positions):
    horizontal_position = 0
    depth = 0
    for position in positions:
        if position[0] == "up":
            depth -= position[1]
        elif position[0] == "down":
            depth += position[1]
        elif position[0] == "forward":
            horizontal_position += position[1]
        else:
            print("no match")
    return horizontal_position * depth

def move2(positions):
    horizontal_position = 0
    depth = 0
    aim = 0
    for position in positions:
        if position[0] == "up":
            aim -= position[1]
        elif position[0] == "down":
            aim += position[1]
        elif position[0] == "forward":
            horizontal_position += position[1]
            depth += aim * position[1]
        else:
            print("no match")
    return horizontal_position * depth


print(move(positions))
print(move2(positions))