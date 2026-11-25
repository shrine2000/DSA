class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_so_far = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            if curr_max > max_so_far:
                max_so_far = curr_max
        return max_so_far
