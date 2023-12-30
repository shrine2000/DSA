from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if total_sum < target or (total_sum - target) % 2 != 0:
            return 0

        target_subset_sum = (total_sum - target) // 2

        dp = [0] * (target_subset_sum + 1)
        dp[0] = 1

        for n in nums:
            for i in range(target_subset_sum, n - 1, -1):
                dp[i] += dp[i - n]

        return dp[target_subset_sum]
