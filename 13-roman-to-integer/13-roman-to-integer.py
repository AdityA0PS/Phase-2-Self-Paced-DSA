class Solution(object):
    def romanToInt(slef, s):

        romanos = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sums = 0
        subs = 0
        num = 0

        i = 0
        j = 0
        

        while i < len(s):

            if s[i] == "I": 
                sums = sums + 1
            
            elif s[i] == "V": 
                sums = sums + 5
            
            elif s[i] == "X": 
                sums = sums + 10
            
            elif s[i] == "L": 
                sums = sums + 50
            
            elif s[i] == "C": 
                sums = sums + 100
            
            elif s[i] == "D": 
                sums = sums + 500
            
            elif s[i] == "M": 
                sums = sums + 1000
            
            i += 1
            
        while j < len(s):

            if s[j:j+2] == "IV" or s[j:j+2] == "IX":
                subs = subs -2

            elif s[j:j+2] == "XL" or s[j:j+2] == "XC":
                subs = subs -20
            
            elif s[j:j+2] == "CD" or s[j:j+2] == "CM":
                subs = subs -200
            
            else:
                subs = subs

            j += 1

        num = sums + subs
        return (num)