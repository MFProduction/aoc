#!/bin/env python
file = open('input.txt', 'r')
lines = file.readlines()
 
def first_one(lines):
    count = 0
    increment = 0
    previous_depth = 0
    for line in lines:
        current_depth = int(line)
        if current_depth > previous_depth and count != 0:
            increment += 1
        count += 1
        previous_depth = current_depth
    return increment

def second_one(lines):
    increment = 0
    previous_depth = 0
    i = 0
    for line in lines:
        cd = int(line) 
        if i+1 >= len(lines):
            cd1 = 0
        else:
            cd1 = int(lines[i+1])
        if i+2 >= len(lines):
            cd2 = 0
        else:
            cd2 = int(lines[i+2])   

        sum = cd+cd1+cd2
        if sum > previous_depth and i != 0:
            increment += 1
        previous_depth = sum
        i += 1
    return increment

print (first_one(lines))
print (second_one(lines))