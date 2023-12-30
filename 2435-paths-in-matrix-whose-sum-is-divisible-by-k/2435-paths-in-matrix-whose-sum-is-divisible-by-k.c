int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    int n = gridColSize[0];
    int mod = 1000000007;

    int dp[m][n][k];
    memset(dp, 0, sizeof(dp));

    dp[0][0][grid[0][0] % k] = 1;

    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            for (int z = 0; z < k; z++) {
                if (x > 0) {
                    dp[x][y][(z + grid[x][y]) % k] = (dp[x][y][(z + grid[x][y]) % k] + dp[x - 1][y][z]) % mod;
                }
                if (y > 0) {
                    dp[x][y][(z + grid[x][y]) % k] = (dp[x][y][(z + grid[x][y]) % k] + dp[x][y - 1][z]) % mod;
                }
            }
        }
    }

    int res = dp[m - 1][n - 1][0];

    return res;
}
