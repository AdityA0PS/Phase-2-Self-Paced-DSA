class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ll=collections.deque()
        f=0
        l=0
        res=[]
        while l<len(nums):
            while len(ll)>=1 and ll[-1]<nums[l]:
                ll.pop()
            ll.append(nums[l])
            if l-f+1<k:
                l=l+1

            elif l-f+1==k:
                res.append(ll[0])
                if nums[f]==ll[0]:
                    ll.popleft()
                f=f+1
                l=l+1
        return res