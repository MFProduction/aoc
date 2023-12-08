def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def find_smallest_one(start_value, i, j):
    options = {}
    if i != 0:
        options.update({input[i-1][j]:[i-1,j]})
    if j != 0:
        options.update({input[i][j-1]:[i,j-1]})
    if i != len(input)-1:
        options.update({input[i+1][j]:[i+1,j]})
    if j != len(input[i])-1:
        options.update({input[i][j+1]:[i,j+1]})
    option_list = sorted(options)
    smallest = option_list[0]
    if smallest < start_value:
        find_smallest_one(smallest, options[smallest][0], options[smallest][1])
    else:
        if start_value != 9:
            return start_value
        else:
            return None

def find_basins(input, location , visited):
    locations = []
    i,j = location
    basin_size = 1
    if i != 0:
        locations.append([i-1,j])
    if j != 0:
        locations.append([i,j-1])
    if i != len(input)-1:
        locations.append([i+1,j])
    if j != len(input[i])-1:
        locations.append([i,j+1])

    for loc in locations:
        xi, xj = loc 
        if loc not in visited and input[xi][xj] !=9:
            visited.append(loc)
            basin_size += find_basins(input, loc , visited)
    return(basin_size)



def first_one(input):
    res = 0
    basins = []
    visited = []
    for i, i_val in enumerate(input):
        for j, j_val in enumerate(i_val):
            smallest = find_smallest_one(j_val, i,j)
            if smallest != None:
                basin_size = 0
                visited.append([i,j])
                basin_size += find_basins(input,[i,j], visited)
                res += (smallest+1)
                basins.append(basin_size)
    x = sorted(basins,reverse=True)
    b = x[0] * x[1] * x[2]
    return(res, b)

input = [Convert(line.strip("\n")) for line in open("input.txt", 'r') if line != "\n"]
input = [list(map(int, i)) for i in input]

print(first_one(input))
