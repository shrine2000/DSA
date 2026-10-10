class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen.get(complement), idx]
            seen[value] = idx
        return [-1, -1]