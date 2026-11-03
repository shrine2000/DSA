class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        N = len(nums)
        used = [False] * N
        def backtrack(path):
            if len(path) == N:
                res.append(path[:])
                return
            for i in range(N):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res
