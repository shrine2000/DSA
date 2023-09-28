class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        dp[1][1][1] = grid[0][0]

        for x1 in range(1, n + 1):
            for y1 in range(1, n + 1):
                for x2 in range(1, n + 1):
                    y2 = x1 + y1 - x2
                    if y2 < 1 or y2 > n:
                        continue
                    if grid[x1 - 1][y1 - 1] == -1 or grid[x2 - 1][y2 - 1] == -1:
                        continue
                    ans = max(dp[x1 - 1][y1][x2], dp[x1 - 1][y1][x2 - 1],
                              dp[x1][y1 - 1][x2], dp[x1][y1 - 1][x2 - 1])
                    if ans < 0:
                        continue
                    dp[x1][y1][x2] = ans + grid[x1 - 1][y1 - 1]
                    if x1 != x2:
                        dp[x1][y1][x2] += grid[x2 - 1][y2 - 1]

        return max(0, dp[n][n][n])
