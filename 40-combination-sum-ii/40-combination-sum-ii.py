class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(cur, cur_sum, idx):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                backtracking(cur + [candidates[i]], cur_sum + candidates[i], i+1)

        backtracking([], 0, 0)
        return res
        