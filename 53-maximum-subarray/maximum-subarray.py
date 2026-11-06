class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float("-inf")
        # Kadane's algo - a negative prefix can never help a future subarray max sum.
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum if max_sum != float("-inf") else -1
