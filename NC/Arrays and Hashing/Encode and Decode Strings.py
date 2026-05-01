class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ""
        for i in range(len(strs)):
            op+=str(len(strs[i]))+"#"+strs[i]
        return op
    def decode(self, s: str) -> List[str]:
        op=[]
        i=0
        j=0
        while i<len(s):
            while s[j]!='#':
               j+=1
            length=int(s[i:j])
            i=j+1
            word = s[i:i+length]
            op.append(word)
            i+=length
            j=i
        return op
    
# R1
class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for word in strs:
            length=len(word)
            op+=f"{length}#{word}"
        return op
    def decode(self, s: str) -> List[str]:
        op=[]
        length=""
        i=0
        while i<len(s):
            if s[i]!="#":
                length+=s[i]
                i+=1
                continue
            length=int(length)
            op.append(s[i+1:i+length+1])
            i+=length+1
            length=""
        return op