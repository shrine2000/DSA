class Solution:
    # Either rob houses from index 0 to n-2 (exclude last), OR from index 1 to n-1 (exclude first). Then take the max of both cases.
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        def helper(_nums):
            n = len(_nums)
            if n == 1:
                return _nums[0]
            dp = [0] * n
            dp[0] = _nums[0]
            dp[1] = max(_nums[0], _nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], _nums[i] + dp[i - 2])
            return dp[-1]

        return max(helper(nums[: - 1]), helper(nums[1:]))
