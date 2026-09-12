class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            
            pick = nums[idx] + dfs(idx + 2)
            skip = dfs(idx + 1)
            return max(pick, skip)
        return dfs(0)
