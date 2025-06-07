from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result: List[List[int]] = []
        total_subsets = 1 << N
        for bitmask in range(total_subsets):
            subset = []
            for j in range(N):
                if bitmask & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        return result


if __name__ == "__main__":
    pass
