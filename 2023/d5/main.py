#!usr/bin/env python
from collections import defaultdict
import time

lines = open(0).read().strip().split('\n\n')
seeds = [int(s) for s in lines[0].split(':')[-1:][0].split()]
lines.pop(0)

mmap = defaultdict(list)
for i,line in enumerate(lines):
    map_name,vals = line.strip().split(':')
    ranges = vals.strip().split("\n")
    for r in ranges:
        mmap[map_name].append([int(i) for i in r.split()])

def map_seed(seed):
    for _,map in mmap.items():
        done = False
        for range in map:
                if not done:
                    diff = 0
                    sr=range[0]
                    fr=range[1]
                    r=range[2]
                    if fr <= seed <= fr+r:
                        done = True
                        if fr == 0 or sr == 0:
                            diff = max(fr,sr)
                        else:
                            diff = abs(fr - sr)
                        if fr < sr:
                            seed += diff
                        else:
                            seed -= diff
    return seed

ans = ans1 = 0
for seed in seeds:
    if ans == 0:
        ans = map_seed(seed)
    else:
        ans = min(ans, map_seed(seed))
print(ans)

# for seed_r in range(0,len(seeds),2):
#     seed_start = int(seeds[seed_r])
#     seed_end = int(seeds[seed_r+1])
#     seed_range = seed_start+seed_end
#     print(seed_start,seed_end,seed_range)
#     for seed in range(seed_start, seed_range,1):
#         ans1 = min(ans1, map_seed(seed))
#         print(seed)


# Good stuff
# print("="*80)