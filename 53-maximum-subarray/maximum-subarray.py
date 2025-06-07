class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(idx, picked):
            if idx >= len(nums):
                return 0 if picked else float("-inf")
            if picked:
                return max(0, nums[idx] + dp(idx + 1, True))
            else:
                return max(nums[idx] + dp(idx + 1, True), dp(idx + 1, False))

        return dp(0, False)
