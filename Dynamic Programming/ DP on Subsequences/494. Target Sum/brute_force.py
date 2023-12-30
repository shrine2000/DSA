from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(idx, current_sum):
            if idx == len(nums):
                return 1 if current_sum == target else 0

            positive_ways = backtrack(idx + 1, current_sum=current_sum + nums[idx])
            negative_ways = backtrack(idx + 1, current_sum=current_sum - nums[idx])

            return positive_ways + negative_ways

        return backtrack(0, 0)
