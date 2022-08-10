class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

		res = []

		def helper(x, path):
			if sum(path) == target:
				res.append(path[:])
				return

			if sum(path) > target:
				return

			for i in range(x, len(candidates)):
				path.append(candidates[i])
				helper(i, path)
				path.pop()

		helper(0, [])
		return res