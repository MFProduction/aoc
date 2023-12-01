#parse the input and create a list of integers representing the Calories
input_data = open(0).read()
#parse the input and create a list of integers representing the Calories
calories = [int(line) for line in input_data.strip().split('\n') if line.strip()]

#initialize the current Elf's total Calories to 0
total = 0
#initialize the maximum total Calories to 0
max_total = 0

#iterate over the items in the list
for c in calories:
    #if the current item is a blank line, move on to the next Elf
    #and reset their total Calories to 0
    if not c:
        total = 0
        continue
    #add the current item to the current Elf's total Calories
    total += c
    #if the current Elf's total Calories is larger than the maximum,
    #update the maximum total Calories
    if total > max_total:
        max_total = total

#return the maximum total Calories
print(max_total)
