def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def find_smallest_one(start_value, i, j):
    options = {}
    if i != 0:
        options.update({input[i-1][j]:[i,j]})
    if j != 0:
        options.update({input[i][j-1]:[i,j]})
    if i != len(input)-1:
        options.update({input[i+1][j]:[i,j]})
    if j != len(input[i])-1:
        options.update({input[i][j+1]:[i,j]})
    option_list = sorted(options)
    smallest = option_list[0]
    if smallest < start_value:
        find_smallest_one(smallest, options[smallest][0], options[smallest][1])
    else:
        if start_value != 9:
            return start_value
        else:
            return None

input = [Convert(line.strip("\n")) for line in open("input-test.txt", 'r') if line != "\n"]
input = [list(map(int, i)) for i in input]

def first_one(input):
    res = 0
    for i, i_val in enumerate(input):
        for j, j_val in enumerate(i_val):
            smallest = find_smallest_one(j_val, i,j)
            if smallest != None:
                # print(smallest)
                res += (smallest+1)
    return(res)

print(first_one(input))


# for i in input:
#     print(i)
