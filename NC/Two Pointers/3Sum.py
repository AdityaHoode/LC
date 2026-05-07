class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        i,j=0,1
        while i<len(nums) - 2:
            j,k=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                i+=1    
                continue
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]]) 
                    j+=1
                    k-=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
            i+=1    
        return res