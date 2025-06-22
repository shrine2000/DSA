from typing import List


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    )

        return dp[0][n - 1]

    @staticmethod
    def maxCoinsBruteForce(nums: List[int]) -> int:
        padded_nums = [1] + nums + [1]

        def dfs(current_list):
            MAX_COINS = float("-inf")
            N = len(current_list)
            if N <= 2:
                return 0
            for idx in range(1, N - 1):
                left = current_list[idx - 1]
                right = current_list[idx + 1]
                middle = current_list[idx]
                ans = left * middle * right
                new_list = current_list[:idx] + current_list[idx + 1 :]
                total = ans + dfs(new_list)
                MAX_COINS = max(MAX_COINS, total)
            return MAX_COINS

        return dfs(padded_nums)


if __name__ == "__main__":
    print(Solution.maxCoinsBruteForce([3, 1, 5, 8]))
