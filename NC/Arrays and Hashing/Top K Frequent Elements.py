from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        
        return [i[0] for i in c.most_common(k)]
    
# R1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.setdefault(num,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in d.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            if buckets[i]==[]:
                continue
            res.extend(buckets[i]) # extend() can add multiple elements at once. So len(res) can overshoot k
            if len(res)==k:
                return res
            
# Recommended TS Complexity
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.setdefault(num,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in d.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k:
                    return res