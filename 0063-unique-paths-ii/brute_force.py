from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n or grid[r][c] == 1:
                return 0

            if r == m - 1 or c == n - 1:
                return 1

            down = dfs(r + 1, c)
            right = dfs(r, c + 1)

            return down + right

        return dfs(0, 0)
