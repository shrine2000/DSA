class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 2)

        for i in range(N - 1, -1, -1):
            pick = nums[i] + dp[i + 2]
            not_pick = dp[i + 1]
            dp[i] = max(pick, not_pick)
        return dp[0]
