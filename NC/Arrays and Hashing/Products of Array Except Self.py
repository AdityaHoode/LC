class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        lp=1
        rp=1
        for i in range(1,len(nums)):
            lp*=nums[i-1]
            left.append(lp)

        for i in range(len(nums)-2,-1,-1):
            rp*=nums[i+1]
            right.append(rp)
        right.reverse()

        op=[]
        for l,r in zip(left,right):
            op.append(l*r)

        return op

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]

        return res

# R1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        p=1
        for i in range(len(nums)-1):
            p*=nums[i]
            left.append(p)
        p=1
        for i in range(len(nums)-1,0,-1):
            p*=nums[i]
            right.append(p)
        op=[]
        for l,r in zip(left,reversed(right)):
            op.append(l*r)
        return(op)