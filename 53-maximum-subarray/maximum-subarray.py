from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_crossing_subarray(arr, low, mid, high):
            left_sum = float('-inf')
            right_sum = float('-inf')
            max_left_sum = 0
            max_right_sum = 0

            for i in range(mid, low - 1, -1):
                max_left_sum += arr[i]
                if max_left_sum > left_sum:
                    left_sum = max_left_sum

            for i in range(mid + 1, high + 1):
                max_right_sum += arr[i]
                if max_right_sum > right_sum:
                    right_sum = max_right_sum

            return left_sum + right_sum

        def max_subarray_iterative(arr):
            max_sum = float('-inf')
            curr_sum = 0

            for num in arr:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)

            return max_sum

        def max_subarray_recursive(arr, low, high):
            if low == high:
                return arr[low]

            mid = (low + high) // 2

            left_sum = max_subarray_recursive(arr, low, mid)
            right_sum = max_subarray_recursive(arr, mid + 1, high)
            crossing_sum = max_crossing_subarray(arr, low, mid, high)

            return max(left_sum, right_sum, crossing_sum)

        # Check if the input list is not empty
        if not nums:
            return 0

        # Call the recursive implementation of Tamaki and Tokuyama's Algorithm
        return max_subarray_recursive(nums, 0, len(nums) - 1)

 