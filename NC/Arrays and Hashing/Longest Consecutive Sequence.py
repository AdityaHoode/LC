class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result=1
        if nums==[]:
            return 0
        for n in nums:
            if n-1 not in s:
                length=1
                while n+1 in s:
                    length+=1
                    n+=1
                result=max(result, length)
        return result

# R1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        res=1
        temp=1
        l=sorted(set(nums))
        for i in range(len(l)):
            if l[i]-1 in l:
                temp+=1
            else:
                temp=1
            res=max(res,temp)
        return res
    
# Recommended TSC
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        res=0
        i=0
        while i<len(nums):
            if nums[i]-1 not in set_nums:
                length=1
                n=nums[i]
                while n+1 in set_nums:
                    length+=1
                    n+=1
                res=max(res,length)
            i+=1
        return res