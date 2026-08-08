class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return  0

            pick  = nums[i] +  dfs(i - 2)
            not_pick = dfs(i - 1)
            return max(pick, not_pick)

        return dfs(n - 1)
