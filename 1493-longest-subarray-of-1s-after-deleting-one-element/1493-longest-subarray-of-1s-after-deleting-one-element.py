class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        zero_count = 0
        max_length = 0

        while j < n:
            if nums[j] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1

            max_length = max(max_length, j - i)
            j += 1

        return max_length
