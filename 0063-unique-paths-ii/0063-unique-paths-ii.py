from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        if grid[0][0] == 0:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    # Test cases
    solution = Solution()
    grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(solution.uniquePathsWithObstacles(grid1))  # Output: 2

    grid2 = [[0, 1], [0, 0]]
    print(solution.uniquePathsWithObstacles(grid2))  # Output: 1

    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.uniquePathsWithObstacles(grid3))  # Output: 0
