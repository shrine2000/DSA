class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        window_sum = 0
        N = len(nums)
        min_len = float('inf')
        for r in range(N):
            window_sum += nums[r]
            while window_sum >= target:
                min_len = min(min_len, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0

