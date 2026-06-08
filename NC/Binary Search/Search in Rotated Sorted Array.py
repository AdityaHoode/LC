class Solution:
    def binary_search(self, nums: List[tuple[int]], target: int, deflection_index: int):
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m][1]:
                l=m+1
            elif target<nums[m][1]:
                r=m-1
            else:
                return nums[m][0]
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        deflection_index=r        
        snums=[(i,val) for i,val in enumerate(nums)]
        res1=self.binary_search(snums[:r], target, deflection_index)
        res2=self.binary_search(snums[r:], target, deflection_index)
        return res2 if res1==-1 else res1

class Solution:
    def findDeflectionIndex(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return r
    
    def binary_search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        deflection_index=self.findDeflectionIndex(nums)
        if target>=nums[deflection_index] and target<=nums[-1]:
            index=self.binary_search(nums[deflection_index:], target)
            return deflection_index+index if index!=-1 else index
        else:
            return self.binary_search(nums[:deflection_index], target)

# Recommended TS Complexity
class Solution:
    def findDeflectionIndex(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return r
    
    def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if nums[0]<=nums[-1]:
            return self.binary_search(nums, target, 0, len(nums)-1)
        deflection_index=self.findDeflectionIndex(nums)
        if target>=nums[deflection_index] and target<=nums[-1]:
            return self.binary_search(nums, target, deflection_index, len(nums)-1)
        else:
            return self.binary_search(nums, target, 0, deflection_index-1)
