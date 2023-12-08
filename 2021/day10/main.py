def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
OPEN  = ["{", "(", "[", "<"]
CLOSE  = ["}", ")", "]", ">"]
REVERSE_PAIR = {
    "{": "}"
    "}": "}"
}

def is_valid(line, position):
    if line[position] in OPEN:
        is_valid(line, position+1)
    elif line[position] in CLOSE:
        if line[position-1] in OPEN:



input = [line.strip("\n") for line in open("input-test.txt", 'r') if line != "\n"]
for i in input:
    is_valid(i)
