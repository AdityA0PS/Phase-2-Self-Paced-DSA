class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}
        for position, number in enumerate(nums):

            if target - number in lookup:
                return lookup[target-number],position
            else: lookup[number]=position
            