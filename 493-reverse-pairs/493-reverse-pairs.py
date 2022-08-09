from sortedcontainers import SortedList
class Solution:
     def reversePairs(self, nums: List[int]) -> int:
        res = 0
        bst = SortedList()
        for e in nums:
            res += len(bst) - bst.bisect_left(2 * e + 1) # the count is the N - index
            bst.add(e) # add the the bst
        return res
        