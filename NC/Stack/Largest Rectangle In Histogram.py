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
