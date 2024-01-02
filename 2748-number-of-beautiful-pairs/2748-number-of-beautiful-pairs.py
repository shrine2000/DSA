import math
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if self.isCoprime(int(str(nums[i])[0]), int(str(nums[j])[-1])):
                    count += 1

        return count

    def isCoprime(self, x, y) -> bool:
        return math.gcd(x, y) == 1
