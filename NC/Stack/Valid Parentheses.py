class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in "({[":
                stk.append(c)
            else:
                if stk and d.get(c, None)==stk[-1]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0   