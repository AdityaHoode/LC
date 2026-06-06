import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1,10**18):
            hours_taken=sum([math.ceil(p/i) for p in piles])
            if hours_taken<=h:
                return i

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        k=max(piles)
        while l<=r:
            m=(l+r)//2
            hours_taken=sum([math.ceil(p/m) for p in piles])
            if hours_taken>h:
                l=m+1
            elif hours_taken<=h:
                r=m-1
                k=min(k,m)
        return k

# Optimized
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            m=(l+r)//2
            hours_taken=sum([math.ceil(p/m) for p in piles])
            if hours_taken>h:
                l=m+1
            elif hours_taken<=h:
                r=m-1
        return l
