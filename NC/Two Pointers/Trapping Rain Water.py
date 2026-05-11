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