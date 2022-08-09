class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        n  = floor(len(nums)/3)
        print(n)
        mp = {}
        s = set()
        for num in nums:
            if num in mp.keys():
                mp[num]+=1
            else:
                mp[num] = 1
            if mp[num]>n:
                s.add(num)
        return list(s)
        