from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_set = set()
        max_sum = 0
        cur_sum = 0
        l = 0

        for r in range(len(nums)):
            while nums[r] in num_set:
                num_set.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

            num_set.add(nums[r])
            cur_sum += nums[r]

            if r - l + 1 == k:
                max_sum = max(max_sum, cur_sum)
                num_set.remove(nums[l])
                cur_sum -= nums[l]
                l += 1

        return max_sum
