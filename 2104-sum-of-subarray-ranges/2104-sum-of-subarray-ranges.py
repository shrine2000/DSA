from typing import List

class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        total_range_sum = 0
        array_size = len(nums)

        for i in range(array_size):
            min_value = nums[i]
            max_value = nums[i]

            for j in range(i + 1, array_size):
                min_value = min(min_value, nums[j])
                max_value = max(max_value, nums[j])

                total_range_sum += max_value - min_value

        return total_range_sum

