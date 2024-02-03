class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = float("inf")
        subarray_sum = 0

        while right < len(nums):
            subarray_sum += nums[right]

            while subarray_sum >= target:
                min_len = min(min_len, right - left + 1)
                subarray_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float("inf") else 0
