from typing import List


class Solution:
    def canPartition(nums: List[int]) -> bool:
        total_sum = sum(nums)
        target_sum = total_sum // 2

        def helper(k, n):

            if k < 0 or n < 0:
                return False

            if total_sum % 2 != 0:
                return False

            if k == 0:
                return True

            pick = helper(k - nums[n], n - 1)
            not_pick = helper(k, n - 1)

            return pick or not_pick

        return helper(target_sum, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(Solution.canPartition(nums))
