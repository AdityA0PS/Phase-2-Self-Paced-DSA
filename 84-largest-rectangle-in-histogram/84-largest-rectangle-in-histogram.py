class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        heights.append(0) #dummy for the ending
        
        for i, h in enumerate(heights):
            start = i
            while stack and h<stack[-1][1]: #[0]
                j, h2 = stack.pop()
                maxArea = max(maxArea, h2*(i-j))
                start = j
            stack.append((start, h)) #[1]
        
        return maxArea