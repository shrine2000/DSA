from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[l] + nums[r] < target:
                l += 1
                if nums[l] + nums[r] == target:
                    return [l + 1, r + 1]
            while l < r and nums[l] + nums[r] > target:
                r -= 1
                if nums[l] + nums[r] == target:
                    return [l + 1, r + 1]
            l += 1
            r -= 1

            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
        return []


if __name__ == "__main__":
    numbers = [3, 24, 50, 79, 88, 150, 345]
    target = 200

    print(Solution.twoSum(numbers, target))
