class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        total = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                total += nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                total -= nums[i]
        return total