class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return

            if curr_sum > target or idx >= len(candidates):
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, curr_sum + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res
