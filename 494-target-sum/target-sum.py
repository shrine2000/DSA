class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def helper(idx, remaining):
            if idx == len(nums):
                return 1 if remaining == 0 else 0
            take = helper(idx + 1, remaining + nums[idx])
            not_take = helper(idx + 1, remaining - nums[idx])
            return take + not_take

        return helper(0, target)
