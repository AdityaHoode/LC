class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break

            m=(l+r)//2
            res=min(res,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return res
    
# Easily Understandable
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return nums[r]