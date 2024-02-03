class Solution:
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()

        i = 0
        j = len(nums) // 2
        count = 0

        while i < len(nums) // 2 and j < len(nums):
            if nums[i] * 2 <= nums[j]:
                i += 1
                j += 1
                count += 2
            else:
                j += 1

        return count
