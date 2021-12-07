init = open("input-test.txt", "r").readline().split(",")
for i, val in enumerate(init):
    init[i] = int(val)

for i in range(256):
    for ind, x in enumerate(init):
        if x > 0:
            init[ind] = x - 1
        elif x == 0:
            init[ind] = 6
            init.append(9)
    print("Day:", i)
    
    
print(len(init))