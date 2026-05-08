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
