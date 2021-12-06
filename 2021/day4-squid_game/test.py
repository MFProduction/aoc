list_A = [1, 2, 3, 4,5,6,7]
list_B = [2, 3, 5]

check = all(item in list_A for item in list_B)

print(check)