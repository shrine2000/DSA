class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak = 0
        valley = 0

        N = len(nums)

        for i in range(1, N - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak += nums[i]

            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                valley += nums[i]
        return peak - valley
