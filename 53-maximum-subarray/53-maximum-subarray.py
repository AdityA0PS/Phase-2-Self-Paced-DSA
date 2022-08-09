class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -float('infinity')
        runningMax = -float('infinity')
        
        for num in nums:
            if num> runningMax and runningMax < 0: runningMax = num
            
            else: runningMax+=num
            if runningMax > maximum: maximum = runningMax
                
        return maximum
        