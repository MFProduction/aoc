# AOC - 2022 day7
from ast import literal_eval

file = open(0).read().strip()
queries = file.split("\n\n")

def compare(x,y):
    if x <= y:
        print(True)
    else:
        print(False)


for q in queries:
    left,right = q.split("\n")
    lleft = literal_eval(left)
    lright = literal_eval(right)
    print(lleft,lright)
    print()
    while len(lleft) > 0:
        x = lleft.pop(0)
        y = lright.pop(0)
        print(x, y)
        if isinstance(x, list):
            x.pop(0)
        if x <= y:
          print(True)
        else:
            print(False)


    #     else:
    #         print(True)
    # except IndexError:
    #     print(False)
    break