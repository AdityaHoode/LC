class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sn = sorted(nums)
        for i in range(len(sn)-1):
            if sn[i] == sn[i+1]:
                return True
        return False
    
# R1
from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        if c == {}:
            return False
        elif c.most_common(1)[0][1] > 1:
            return True
        return False
    
# R1
from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
