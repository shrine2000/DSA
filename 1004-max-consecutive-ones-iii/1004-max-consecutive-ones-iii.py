class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        max_length = 0
        zero_count = 0

        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            count = right - left + 1
            max_length = max(max_length, count)

        return max_length
