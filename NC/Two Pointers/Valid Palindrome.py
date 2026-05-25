import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            if c.isalnum():
                s1+=c
        return s1.lower()==s1[::-1].lower()

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=re.sub(r'\s+|[^a-zA-Z0-9]','',s)
        return s1.lower()==s1[::-1].lower()
    
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=re.sub(r'\s+|[^a-zA-Z0-9]','',s).lower()
        i,j=0,len(s1)-1
        while i<j:
            if s1[i]==s1[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=list(re.sub(r'\s+|[^a-zA-Z0-9]','',s).lower())
        i,j=0,len(s1)-1
        while i<j:
            if s1[i]==s1[j]:
                i+=1
                j-=1
            else:
                return False
        return True

# R1 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if not s[i].isalnum() or not s[j].isalnum():
                if not s[i].isalnum():
                    i+=1
                if not s[j].isalnum():
                    j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True