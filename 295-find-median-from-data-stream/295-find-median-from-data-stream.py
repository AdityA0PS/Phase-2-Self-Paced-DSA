from bisect import bisect


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        index = bisect(self.nums, num)
        self.nums.insert(index, num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        
        if len(self.nums) % 2 == 0:
            return (self.nums[mid-1] + self.nums[mid]) / 2
        
        return self.nums[mid]