class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i,len(nums)-1):
        #         if nums[i]+nums[j+1]==target:
        #             return [i,j+1]
        # return []

        # for i in nums:
        #     if abs(i-target) in nums:
        #         return [nums.index(i), nums.index(abs(i-target))]
        # return []

        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [nums.index(nums[i]), nums[i+1:].index(target-nums[i])+i+1]
        return []
    
# R1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op=[]
        for i in range(len(nums)):
            if target-nums[i] in nums[:i] or target-nums[i] in nums[i+1:]:
                op.append(i)
        return op