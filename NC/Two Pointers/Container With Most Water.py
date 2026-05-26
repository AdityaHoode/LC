class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        temp=0
        i,j=0,len(heights)-1
        while i<j:
            temp=(j-i)*min(heights[i],heights[j])
            area=max(area,temp)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return area

# R1
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        area=0
        while i<j:
            area=max(area,min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return area