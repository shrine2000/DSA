class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(end, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            if end >= len(candidates) or remaining < 0:
                return

            for i in range(end, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res
