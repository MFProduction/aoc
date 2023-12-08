#!usr/bin/env python
import re
import itertools


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


lines = [line.rstrip() for line in open(0).readlines()]
inst = lines[0]
nodes = lines[2:]

node_map = {}
start_nodes = []
for node in nodes:
    data = node.strip().split("=")[0].strip()
    n = Node(data)
    node_map[data] = n
    if data[-1] == "A":
        start_nodes.append(n)

root = node_map["AAA"]
for node in nodes:
    data, children = node.strip().split("=")
    left,right=re.sub("[()]","",children).split(',')
    data = data.strip()
    right = right.strip()
    left = left.strip()
    node_map[data].left = node_map[left]
    node_map[data].right = node_map[right]

tmp_node = root
steps = 0

for i in itertools.cycle(inst):
    if tmp_node.data == "ZZZ":
        break
    steps +=1
    if i == "L":
        tmp_node = tmp_node.left
    elif i == "R":
        tmp_node = tmp_node.right

print(steps)


#  PART 2

# greatest common devisor
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b,a%b)


# least common multiple
def lcm(a,b):
    return int(a * b / gcd(a,b))


steps = 0
step_counts = []
end_nodes = []
for i in itertools.cycle(inst):
    for j, nodes in enumerate(start_nodes):
        if nodes.data[-1] == "Z":
            end_nodes.append(nodes.data)
            step_counts.append(steps)
        if i == "L":
            start_nodes[j] = nodes.left
        elif i == "R":
            start_nodes[j] = nodes.right
    if len(end_nodes) == len(start_nodes):
        break
    steps +=1

ans = step_counts.pop()
for count in step_counts:
    ans = lcm(ans,count)
print(ans)

