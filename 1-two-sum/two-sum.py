from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], key]
            seen[value] = key
        return [-1, -1]
