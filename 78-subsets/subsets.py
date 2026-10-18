class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        path = []
        def backtrack(idx):
            result.append(path[:])
            for i in range(idx, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return result