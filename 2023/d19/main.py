#!usr/bin/env python
from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase

workflows , ratings = [i.split() for i in open(0).read().strip().split('\n\n')]
rules_map = defaultdict(list)
for w in workflows:
    name,rules = w.split('{')
    rules = rules[:-1]
    rules = rules.split(',')
    rules_map[name] = rules

def do_workflow(x,m,a,s,wf_name):
    rules = rules_map[wf_name].copy()
    default_rule = rules.pop()
    result = None
    for rule in rules:
        r,res=rule.split(':')
        if eval(r):
            result=res
            break

    if result == None:
        result = default_rule

    # print(result, rules, default_rule)
    if result in ["A","R"]:
        return result
    else:
        return do_workflow(x,m,a,s,result)


ans = ans1 = 0
for rating in ratings:
    rating = rating[1:-1]
    rating = rating.split(',')
    for r in rating:
        exec(r)
    result = do_workflow(x,m,a,s,'in')
    if result == "A":
        ans+=sum([x,m,a,s])
    print('='*88)

x = m = a = s = 0
for x in range(0,4000):
    for m in range(0,4000):
        for a in range(0,4000):
            for s in range(0,4000):
                result = do_workflow(x,m,a,s,'in')
                if result == "A":
                    ans1+=sum([x,m,a,s])
            print(a)
print(ans)
print(ans1)
# Good stuff
# print("="*80)