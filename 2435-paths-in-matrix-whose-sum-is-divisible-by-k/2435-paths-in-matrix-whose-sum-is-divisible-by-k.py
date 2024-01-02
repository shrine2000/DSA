class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7

        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1

        for x in range(m):
            for y in range(n):
                for z in range(k):
                    if x > 0:
                        dp[x][y][(z + grid[x][y]) % k] = (
                            dp[x][y][(z + grid[x][y]) % k] + dp[x - 1][y][z]
                        ) % mod
                    if y > 0:
                        dp[x][y][(z + grid[x][y]) % k] = (
                            dp[x][y][(z + grid[x][y]) % k] + dp[x][y - 1][z]
                        ) % mod

        res = dp[m - 1][n - 1][0]

        return res
