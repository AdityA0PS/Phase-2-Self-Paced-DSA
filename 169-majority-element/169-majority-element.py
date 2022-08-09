class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            rep = len(nums) //2
            m = {}
            for x in nums:
                if x not in m:
                    m[x] = 1
                else:
                    m[x] +=1
            print(m)
            for x in m:
                if m[x] > rep:
                    return x