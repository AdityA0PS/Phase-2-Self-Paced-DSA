class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        res = []
        intervals.sort()
        last = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= last[0] and intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])
            else:
                res.append(last)
                last = intervals[i]
        res.append(last)
        return res
        