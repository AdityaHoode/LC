from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in range(len(strs)):
            d.setdefault(''.join(sorted(strs[i])),[]).append(strs[i])
        return list(d.values())

# R1
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in range(len(strs)):
            if d["".join(sorted(strs[i]))] is None:
                d["".join(sorted(strs[i]))]=[]
            d["".join(sorted(strs[i]))].append(strs[i])
        # op=[]
        # for k,v in d.items():
        #     op.append(v)
        # return op
        return list(d.values())

# Recommended TS complexity
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-97]+=1
            key=tuple(count)
            d[key].append(word)
        return list(d.values())