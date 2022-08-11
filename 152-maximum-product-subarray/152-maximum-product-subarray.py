class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		curMax, curMin = 1, 1
		res = max(nums)

		for i in nums:
			if i == 0:
				curMax = curMin = 1
				continue

			temp = curMax*i
			curMax = max(temp, curMin*i, i)
			curMin = min(temp, curMin*i, i)
			res = max(res, curMax)

		return res