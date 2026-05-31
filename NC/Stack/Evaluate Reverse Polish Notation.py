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
    
# R1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for op in tokens:
            if op in '+-*/':
                operator=op
                operand2=int(stk.pop())
                operand1=int(stk.pop())
                if operator=='+':
                    stk.append(operand1+operand2)
                elif operator=='-':
                    stk.append(operand1-operand2)
                elif operator=='*':
                    stk.append(operand1*operand2)
                else:
                    stk.append(int(operand1/operand2))
            else:
                stk.append(op)
        return int(stk[-1])