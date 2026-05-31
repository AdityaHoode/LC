# Prefix & Suffix Arrays
class Solution:
    def trap(self, height: List[int]) -> int:
        res1=[0]
        res2=[0]
        prefix=0
        for i in range(1,len(height)):
            prefix=max(prefix,height[i-1])
            res1.append(prefix)
        print(res1)
        suffix=0
        for i in range(len(height)-2,-1,-1):
            suffix=max(suffix,height[i+1])
            res2.append(suffix)
        res2.reverse()
        print(res2)
        res3=0
        for i in range(len(height)):
            temp=min(res1[i],res2[i])-height[i]
            if temp>0:
                res3+=temp
        return res3

class Solution:
    def trap(self, height: List[int]) -> int:
        res=[0]
        prefix=0
        for i in range(1,len(height)):
            prefix=max(prefix,height[i-1])
            res.append(prefix)
        suffix=0
        for i in range(len(height)-2,-1,-1):
            suffix=max(suffix,height[i+1])
            res[i+1]=min(res[i+1], suffix)-height[i+1]
        return sum(n for n in res if n>0)
    
# Two Pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        res=0
        lmax,rmax=height[i],height[j]
        while i<j:
            if lmax<=rmax:
                i+=1
                res+=max(lmax-height[i],0)
                lmax=max(lmax,height[i])
            else:
                j-=1
                res+=max(rmax-height[j],0)
                rmax=max(rmax,height[j])
        return res

# Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        s=[]
        for i,h in enumerate(height):
            while s and s[-1][1]<h:
                cbottom=s.pop()
                if len(s)!=0:
                    cwidth=(i-s[-1][0])-1
                    cheight=min(h,s[-1][1])-cbottom[1]
                    res+=max(cwidth*cheight,0)
            s.append((i,h))
        return res 

# R1 - Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stk=[]
        area=0
        for i,h in enumerate(height):
            while stk and stk[-1][1]<h:
                bottom=stk.pop()
                if len(stk)!=0:
                    width=i-stk[-1][0]-1
                    height=min(stk[-1][1], h)-bottom[1]
                    area+=height*width
            stk.append((i,h))    
        return area                                           
    
# R1 - Prefix & Suffix Arrays
class Solution:
    def trap(self, height: List[int]) -> int:
        res=[0]
        prefix_max=0
        for i in range(1,len(height)):
            prefix_max=max(prefix_max,height[i-1])
            res.append(prefix_max)
        suffix_max=0
        for j in range(len(height)-2,-1,-1):
            suffix_max=max(suffix_max,height[j+1])
            res[j+1]=max(min(res[j+1],suffix_max)-height[j+1],0)
        return sum(res)
    
# R1 - Two Pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        lmax,rmax=height[i],height[j]
        area=0
        while i<j:
            if lmax<=rmax:
                i+=1
                area+=max(0, lmax-height[i])
                lmax=max(lmax,height[i])
            else:
                j-=1            
                area+=max(0, rmax-height[j])
                rmax=max(rmax,height[j])
        return area