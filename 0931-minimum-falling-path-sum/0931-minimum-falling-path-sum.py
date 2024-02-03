from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])

        dp = [[0] * c for _ in range(r)]
        dp[0] = matrix[0]

        for i in range(1, r):
            for j in range(c):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == c - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(
                        dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]
                    )

        return min(dp[-1])


if __name__ == "__main__":
    solution = Solution()
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(solution.minFallingPathSum(matrix))
