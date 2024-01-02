from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        start, end = -1, -1

        while left <= right and nums[left] <= target <= nums[right]:
            if left == right or nums[left] == nums[right]:
                if nums[left] == target:
                    start = left
                break

            pos = left + ((target - nums[left]) * (right - left)) // (
                nums[right] - nums[left]
            )
            if nums[pos] == target:
                start = pos
                right = pos - 1
            elif nums[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        left, right = 0, len(nums) - 1
        while left <= right and nums[left] <= target <= nums[right]:
            if left == right or nums[left] == nums[right]:
                if nums[left] == target:
                    end = right
                break

            pos = left + ((target - nums[left]) * (right - left)) // (
                nums[right] - nums[left]
            )
            if nums[pos] == target:
                end = pos
                left = pos + 1
            elif nums[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        return [start, end]
