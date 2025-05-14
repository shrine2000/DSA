class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 2):
            first, middle, third = nums[i], nums[i + 1], nums[i + 2]
            if middle == 2 * (first + third):
                count += 1

        return count
