class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)

        def dfs(idx, path, remaining):
            if idx == n or remaining < 0:
                return

            if remaining == 0:
                res.append(path[:])
                return

            for end in range(idx, n):
                path.append(candidates[end])
                dfs(end, path,remaining - candidates[end])
                path.pop()

        dfs(0, [], target)
        return res
