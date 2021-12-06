tables = []
with open("input.txt") as f:
    random_numbers = f.readline().rstrip().split(",")
    table = []
    for line in f:
        if line.strip() == "":
            if  table:
             tables.append(table)
            table = []
        else:
            table.append(line.strip().split())

def calculate_score(win_table, all_numbers):
    sums = 0
    for line in tables[win_table]:
        for item in line:
            if item not in all_numbers:
                sums = sums + int(item) 
    return(sums * int(all_numbers[-1]))

def part_one(tables, random_numbers):
    all_numbers = []
    for number in random_numbers:
        all_numbers.append(number)
        for it, table in enumerate(tables):
            for line in table:
                if all(item in all_numbers for item in line):
                    return(calculate_score(it, all_numbers))

def part_two(tables, random_numbers):
    all_numbers = []
    removed_tables = []
    for number in random_numbers:
        all_numbers.append(number)
        for it, table in enumerate(tables):
             if it not in removed_tables:
                for line in table:
                    if all(item in all_numbers for item in line):
                        if len(removed_tables) == len(tables) -2:
                            print(it)
                            print(calculate_score(it, all_numbers))
                        removed_tables.append(it)

print(part_one(tables, random_numbers))
print(part_two(tables, random_numbers))