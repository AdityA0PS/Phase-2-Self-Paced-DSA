class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        last_index = -1
        
        for index, item in enumerate(nums):
            if item in unique:
                continue
            else:
                unique.add(item)
                nums[last_index + 1] = item
                last_index = last_index + 1
        return len(unique)