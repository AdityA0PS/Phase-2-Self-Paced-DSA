class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li=[]
        for i in range(len(indices)):
            li.append(0)
            
        for i in range(len(indices)):
            c=indices[i]
            li[c]=s[i]
         
        s=''
        for i in li:
            s += i
        
        return s
            
            