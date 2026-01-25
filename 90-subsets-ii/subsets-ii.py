class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[idx])
            dfs(idx + 1)

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return res