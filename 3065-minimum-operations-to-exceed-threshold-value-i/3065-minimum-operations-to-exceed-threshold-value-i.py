from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        while nums and nums[0] < k:
            nums.pop(0)
            count += 1
        return count
