class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        
        def backtrack(index):
            if index==n:
                ans.append(nums.copy())
                return
            for i in range(index,n):
                nums[index],nums[i]=nums[i],nums[index]
                backtrack(index+1)
                nums[index],nums[i]=nums[i],nums[index]
            
        backtrack(0)
        return ans