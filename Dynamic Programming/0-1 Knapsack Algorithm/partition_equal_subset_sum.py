# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        @lru_cache(None)
        def helper(idx, current_sum):

            if current_sum == target_sum:
                return True

            if idx >= n or current_sum > target_sum:
                return False

            take = helper(idx + 1, current_sum + nums[idx])
            not_take = helper(idx + 1, current_sum)

            return take or not_take

        return helper(0, 0)
