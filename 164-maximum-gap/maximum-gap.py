class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        diff = 0
        for i in range(n - 1):
            diff = max(diff, nums[i + 1] - nums[i])

        return diff
