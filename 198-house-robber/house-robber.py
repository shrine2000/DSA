class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # dp = [0] * (n  +  2)

        # for i in range(n-1, -1, -1):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        # return dp[0]

        @cache
        def dfs(idx):
            if idx >= N:
                return 0
            pick = dfs(idx + 2) + nums[idx]
            not_pick = dfs(idx + 1)
            return max(pick, not_pick)
        return dfs(0)
