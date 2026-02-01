class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Example Run
            nums = [2, 7, 9, 3, 1]

            dp[0] = 2

            dp[1] = max(2, 7) = 7

            dp[2] = max(7, 9+2) = 11

            dp[3] = max(11, 3+7) = 11

            dp[4] = max(11, 1+11) = 12

            answer = dp[-1]
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
