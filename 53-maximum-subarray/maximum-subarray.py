class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + curr_max)
            max_sum = max(max_sum, curr_max)
        return max_sum
