class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		ans = []
		self.Helper(0,nums, [], ans)
		ans.sort()
		return ans

	def Helper(self, idx, nums, temp, ans):
		if idx >= len(nums):
			res = []
			[res.append(i) for i in temp]
			res.sort()
			if res not in ans:ans.append(res)
			return
		else:
			temp.append(nums[idx])
			self.Helper(idx+1, nums, temp, ans)
			temp.pop()
			self.Helper(idx+1, nums, temp, ans)