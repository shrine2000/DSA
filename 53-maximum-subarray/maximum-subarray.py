class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def solve(nums, pick, idx):
            if idx >= len(nums):
                return 0 if pick else float("-inf")
            if (pick, idx) in memo:
                return memo[(pick, idx)]
            if pick:
                result = max(0, nums[idx] + solve(nums, True, idx + 1))
            else:
                result = max(
                    nums[idx] + solve(nums, True, idx + 1), solve(nums, False, idx + 1)
                )
            memo[(pick, idx)] = result
            return result

        return solve(nums, False, 0)
