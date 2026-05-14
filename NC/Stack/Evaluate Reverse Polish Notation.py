class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for t in tokens:
            if t not in "+-*/":
                stk.append(int(t))
            else:
                op=t
                op2=stk.pop()
                op1=stk.pop()
                if op=='+':
                    stk.append(op1+op2)
                elif op=='-':
                    stk.append(op1-op2)
                elif op=='*':
                    stk.append(op1*op2)
                else:
                    stk.append(int(op1/op2))
        return int(stk[-1])