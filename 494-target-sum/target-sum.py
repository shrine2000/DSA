class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def backtrack(idx, curr_sum):
            if idx == len(nums):
                return 1 if curr_sum == target else 0

            return backtrack(idx + 1, curr_sum + nums[idx]) + backtrack(idx + 1, curr_sum - nums[idx])

        return backtrack(0, 0)
