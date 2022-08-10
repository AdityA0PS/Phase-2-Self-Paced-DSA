class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        bigger = [x for x in nums if x > pivot]
        eq = [x for x in nums if x == pivot]
        less = [x for x in nums if x < pivot]        
        
        if len(bigger) >= k: 
            return self.findKthLargest(bigger,k)
        elif len(bigger) + len(eq) < k:
            return self.findKthLargest(less,k - len(bigger) - len(eq)) 
        else:
            return eq[0] 