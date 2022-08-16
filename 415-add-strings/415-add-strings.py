class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = 0
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            n=int(num1[i])
            s += n*(10**i)
            
        for i in range(len(num2)):
            n=int(num2[i])
            s += n*(10**i)
            
        s = str(s)  
        
        return s
        