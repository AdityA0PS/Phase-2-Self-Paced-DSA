class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        f = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for key,val in count.items():
            f[val].append(key)
        
        ans = []
        for i in range(len(f)-1,0,-1):
            for val in f[i]:
                ans.append(val)
            if len(ans) == k:
                return ans