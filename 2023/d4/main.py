#!usr/bin/env python
from collections import defaultdict

lines = [line.rstrip() for line in open(0).readlines()]

ans = ans1 = 0
noo = defaultdict(int)
for i,line in enumerate(lines):
    card_number = i+1
    noo[card_number] += 1
    _,cards = line.strip().split(':')
    win,you= cards.split('|')
    win = win.split()
    you = you.split()
    num = 0
    for _ in range(noo[card_number]):
        n = 0
        for y in you:
            if y in win:
                n += 1
                noo[card_number+n] += 1

    if n == 0:
        next
    elif n == 1:
        num += 1
    else:
        for x in range(n-1):
          if num == 0:
              num += 1
          num += num
    ans += num

for keys, value in noo.items():
   print(keys, value)
   ans1 += value

print(ans)
print(ans1)
# Good stuff
# print("="*80)