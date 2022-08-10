class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1        
        curr = a
        
        while b not in curr:            
            curr += a
            count += 1                         
            if count > 3 and len(curr) > 3 * len(b): return -1
                
        return count