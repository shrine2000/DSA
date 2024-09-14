from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1

        for num in nums:
            prefix_sum += num
            count += prefix_sum_count[prefix_sum - goal]
            prefix_sum_count[prefix_sum] += 1

        return count


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(Solution().numSubarraysWithSum(nums, goal))
