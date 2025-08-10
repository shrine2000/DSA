class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return

            if curr_sum > target or idx >= len(candidates):
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, curr_sum + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return res
