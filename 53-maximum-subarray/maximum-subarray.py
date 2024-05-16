class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = max_current = nums[0]
        for num in nums[1:]:
            max_current = max(num, num + max_current)
            max_global = max(max_global, max_current)
        return max_global