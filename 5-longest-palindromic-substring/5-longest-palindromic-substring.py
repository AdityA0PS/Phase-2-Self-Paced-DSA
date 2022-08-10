class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        l = len(s)
        
        if s==s[::-1]:
            return s
        
        for i in range(l):
            for j in range(i+1,l+1):
                st = s[i:j]
                if (st==st[::-1]) and (len(st)>len(res)):
                    res = st
                    
        return res