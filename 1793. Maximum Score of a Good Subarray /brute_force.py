from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        max_score: int = 0

        for i in range(n):
            for j in range(i, n):
                if i <= k <= j:
                    # Calculate the minimum value in the subarray
                    min_val: int = min(nums[i:j + 1])
                    # Calculate the score for this subarray
                    score: int = min_val * (j - i + 1)
                    max_score: int = max(max_score, score)

        return max_score


if __name__ == "__main__":
    sol: Solution = Solution()

    nums: List[int]
    k: int

    nums, k = [1, 4, 3, 7, 4, 5], 3
    print(sol.maximumScore(nums=nums, k=k))  # Output: 15

    nums, k = [5, 5, 4, 5, 4, 1, 1, 1], 0
    print(sol.maximumScore(nums=nums, k=k))  # Output: 20
