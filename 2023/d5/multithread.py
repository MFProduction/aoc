#!usr/bin/env python
from collections import defaultdict
import time
import math
from multiprocessing import Pool


def mmap():
    lines = open("input.txt").read().strip().split('\n\n')
    mmap = defaultdict(list)
    for i,line in enumerate(lines):
        if i == 0:
            continue
        map_name,vals = line.strip().split(':')
        ranges = vals.strip().split("\n")
        for r in ranges:
            fr,sr,r = r.split()
            mmap[map_name].append([int(fr),int(sr),int(r)])
    return mmap

def map_seed(seed):
    seed = int(seed)
    for _,map in mmap().items():
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

# for seed in seeds:
#     ans = min(ans, map_seed(seed))
# print(ans)

# for seed_r in range(0,len(seeds),2):
#     seed_start = int(seeds[seed_r])
#     seed_end = int(seeds[seed_r+1])
#     seed_range = seed_start+seed_end
#     print(seed_start,seed_end,seed_range)
    # for seed in range(seed_start, seed_range,1):
    #     ans1 = min(ans1, map_seed(seed))
    #     print(seed)


# MULTI THREAD
def process(range):
    aaa = 10000000000000000
    for seed in range:
        aaa = min(aaa, map_seed(seed))
        # print(aaa)
    print(aaa)


def main():
    lines = open("input.txt").read().strip().split('\n\n')

    ans = ans1 = 100000000000000000
    seeds = lines[0].split(':')[-1:][0].split()
    x = []
    for seed_r in range(0,len(seeds),2):
        seed_start = int(seeds[seed_r])
        seed_end = int(seeds[seed_r+1])
        seed_range = seed_start+seed_end
        x.append(range(seed_start,seed_range))


    print(x)
    out = ""
    # out = run_multiprocessing(process, x, n_processors)

    with Pool(12) as pool:
        start=time.time()
        result = pool.map(process, x)
        pool.terminate()
        pool.join()
        print("Time Taken: ",str(time.time()-start))

if __name__ == '__main__':
    main()



# def split_processing(seeds):
#     threads = []
#     for seed_r in range(0,len(seeds),2):
#     # for i in range(num_splits):
#         seed_start = int(seeds[seed_r])
#         seed_end = int(seeds[seed_r+1])
#         seed_range = seed_start+seed_end
#         threads.append(
#             threading.Thread(target=process, args=(seed_start, seed_range)))
#         threads[-1].start() # start the thread we just created

#     # wait for all threads to finish
#     for t in threads:
#         t.join()

# split_processing(seeds)
# Good stuff
# print("="*80)