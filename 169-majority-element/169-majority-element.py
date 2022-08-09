class Solution(object):
    def __init__(self):
        self.chapter_count = {}

    def majorityElement(self, nums):
        half_len = (len(nums) + 1) // 2
        for num in nums:
            chapter_count = self.chapter_count.get(num)
            if chapter_count is None:
                chapter_count = nums.count(num)
            if chapter_count >= half_len:
                return num
            self.chapter_count[num] = chapter_count

        