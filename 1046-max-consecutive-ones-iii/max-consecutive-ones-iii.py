class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_window = 0
        left = 0
        N = len(nums)

        zeros = 0
        for right in range(N):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            max_window = max(max_window, right - left + 1)
        return max_window
