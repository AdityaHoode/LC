class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        area=0
        min_i=0
        for i,h in enumerate(heights):
            pop=False
            while stk and h<stk[-1][0]:
                pop=True
                prev_h,prev_i=stk.pop()
                area=max(area, prev_h*(i-prev_i))
                min_i=prev_i
            if not pop:
                stk.append((h,i))
            else:
                stk.append((h,min_i))

        for h,i in stk:
            area=max(area,h*(len(heights)-i))

        return area

# R1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        area=0
        for i,h in enumerate(heights):
            prev_i=i
            while stk and h<stk[-1][1]:
                prev_i,prev_h=stk.pop()
                area=max(area,prev_h*(i-prev_i))
            stk.append((prev_i,h))
        h_len=len(heights)
        for i,h in stk:
            area=max(area,h*(h_len-i))
        return area