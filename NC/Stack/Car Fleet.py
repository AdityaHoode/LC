class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d=dict(sorted({p:s for p,s in zip(position,speed)}.items(), reverse=True))
        p=list(d.keys())
        s=list(d.values())
        stk=[]
        for i in range(len(p)):
            time=(target-p[i])/s[i]
            if stk and time<=stk[-1]:
                continue
            else:
                stk.append(time)
        return len(stk)
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk=[]
        for p,s in cars:
            time=(target-p)/s
            if stk and time<=stk[-1]:
                continue
            else:
                stk.append(time)
        return len(stk)

# R1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        res=0
        ps_list=sorted([(p,s) for p,s in zip(position,speed)], reverse=True)
        for p,s in ps_list:
            t=(target-p)/s
            if stk and stk[-1]<t:
                res+=1
                stk=[]
            elif stk and stk[-1]>t:
                continue
            stk.append(t)

        return res+1 if stk else res
    
# R1 - Optimized
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        fleet_time=0
        for p,s in sorted(zip(position, speed), reverse=True):
            t=(target-p)/s
            if t>fleet_time:
                res+=1
                fleet_time=t
        return res