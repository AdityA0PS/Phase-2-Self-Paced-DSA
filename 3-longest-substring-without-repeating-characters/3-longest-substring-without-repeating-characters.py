class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        start = 0
        length, max_length = 0, 0
        
        for i in range(len(s)):
            val = s[i]
            if val not in data:
                length += 1
            else:
                if data[val] >= start:
                    start = data[val] + 1     
                length = i-start+1
                
            data[val] = i  
            if length > max_length: 
                max_length = length
                
        del data       
        return max_length
        