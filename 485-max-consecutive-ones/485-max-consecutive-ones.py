class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = max_consecutive = 0
        for num in range(len(nums)):
            if nums[num] == 1:
                consecutive += 1
                if max_consecutive < consecutive:
                    max_consecutive = consecutive
            else:
                consecutive = 0 
        return max_consecutive