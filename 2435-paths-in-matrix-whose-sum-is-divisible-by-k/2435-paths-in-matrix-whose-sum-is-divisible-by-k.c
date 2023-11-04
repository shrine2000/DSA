int solve(int i, int j, int pathSum, int k, int** grid, int gridSize, int* gridColSize, int*** memo) {
    if (i == 0 && j == 0) {
        return (pathSum + grid[i][j]) % k == 0 ? 1 : 0;
    }

    if (i < 0 || j < 0) {
        return 0;
    }

    if (memo[i][j][pathSum] != -1) {
        return memo[i][j][pathSum];
    }

    int up = solve(i - 1, j, (pathSum + grid[i][j]) % k, k, grid, gridSize, gridColSize, memo);
    int left = solve(i, j - 1, (pathSum + grid[i][j]) % k, k, grid, gridSize, gridColSize, memo);
    int ans = (up + left) % 1000000007; 

    memo[i][j][pathSum] = ans;
    return ans;
}

int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize;
    int n = *gridColSize;

    int*** memo = (int***)malloc(m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        memo[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            memo[i][j] = (int*)malloc(k * sizeof(int));
            for (int l = 0; l < k; l++) {
                memo[i][j][l] = -1;
            }
        }
    }

    int result = solve(m - 1, n - 1, 0, k, grid, gridSize, gridColSize, memo);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            free(memo[i][j]);
        }
        free(memo[i]);
    }
    free(memo);

    return result;
}