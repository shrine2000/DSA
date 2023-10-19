from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = [[-1] * (len(nums) + 1) for _ in range(len(nums))]
        return self.lis(0, -1, nums)

    def lis(self, current_index, previous_index, nums):
        if current_index == len(nums):
            return 0

        if self.memo[current_index][previous_index + 1] != -1:
            return self.memo[current_index][previous_index + 1]

        not_pick = self.lis(current_index + 1, previous_index, nums)

        pick = 0

        if previous_index == -1 or nums[current_index] > nums[previous_index]:
            pick = 1 + self.lis(current_index + 1, current_index, nums)

        self.memo[current_index][previous_index + 1] = max(pick, not_pick)

        return max(pick, not_pick)

