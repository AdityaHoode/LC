class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and t>stk[-1][1]:
                lower_temp_index, lower_temp=stk.pop()
                res[lower_temp_index]=i-lower_temp_index
            stk.append((i,t))
        return res

# R1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stk and t>temperatures[stk[-1]]:
                prev_day=stk.pop()
                res[prev_day]=i-prev_day
            stk.append(i)
        return res