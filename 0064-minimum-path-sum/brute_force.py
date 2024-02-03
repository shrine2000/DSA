from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        memo = [[-1] * (m + n) for _ in range(m)]

        def helper(x, y):
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            if x == m - 1:
                return grid[x][y] + helper(x, y + 1)
            if y == n - 1:
                return grid[x][y] + helper(x + 1, y)

            if memo[x][y] != -1:
                return memo[x][y]

            down = helper(x + 1, y)
            right = helper(x, y + 1)

            memo[x][y] = min(down, right) + grid[x][y]
            return memo[x][y]

        return helper(0, 0)


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    solution = Solution()
    min_path_sum = solution.minPathSum(grid)
    print("Minimum Path Sum:", min_path_sum)
