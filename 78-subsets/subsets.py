class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(idx, path):
            res.append(path[:])
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return res

