from collections import defaultdict, Counter

def fn():
    target = [1,2,3,4]
    arr = [2,4,1,3]

    # c1 = defaultdict(int)
    # c2 = defaultdict(int)
    # for n1,n2 in zip(target, arr):
    #     c1[n1]+=1
    #     c2[n2]+=1
    # if c1!=c2:
    #     return False
    # return True

    # c = defaultdict(int)
    # for n1,n2 in zip(target,arr):
    #     c[n1]+=1
    #     c[n2]-=1
    # for k,v in c.items():
    #     if v!=0:
    #         return False
    # return True

    # return sorted(target) == sorted(arr)

    return Counter(target) == Counter(arr)

print(fn())