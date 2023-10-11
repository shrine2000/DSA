from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_sum(idx, nums):
            if idx < 0:
                return 0
            pick = nums[idx] + max_sum(idx - 2, nums)
            not_pick = max_sum(idx - 1, nums)
            return max(pick, not_pick)

        n = len(nums)

        if n == 1:
            return nums[0]

        nums1, nums2 = [], []

        for i in range(n):
            if i != 0:
                nums1.append(nums[i])
            if i != n - 1:
                nums2.append(nums[i])
        return max(max_sum(n - 2, nums1), max_sum(n - 2, nums2))
