class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r] 
        res = 0
        
        while l < r:
            if maxL < maxR:
                l += 1
                if maxL < height[l]: maxL = height[l]         
                else: res += maxL - height[l]      
            else:
                r -= 1  
                if maxR < height[r]: maxR = height[r]
                else: res += maxR - height[r]
                            
        return res
        