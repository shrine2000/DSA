void dfs(int** grid, int gridSize, int* gridColSize, int i, int j, int dist) {
    if (i < 0 || j < 0 || i >= gridSize || j >= gridColSize[i] || (grid[i][j] != 0 && grid[i][j] <= dist))
        return;

    grid[i][j] = dist;

    dfs(grid, gridSize, gridColSize, i - 1, j, dist + 1);
    dfs(grid, gridSize, gridColSize, i + 1, j, dist + 1);
    dfs(grid, gridSize, gridColSize, i, j - 1, dist + 1);
    dfs(grid, gridSize, gridColSize, i, j + 1, dist + 1);
}

int maxDistance(int** grid, int gridSize, int* gridColSize) {
    int mx = -1;

    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            if (grid[i][j] == 1) {
                grid[i][j] = 0;
                dfs(grid, gridSize, gridColSize, i, j, 1);
            }
        }
    }

    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            if (grid[i][j] > 1) {
                mx = (mx < grid[i][j] - 1) ? grid[i][j] - 1 : mx;
            }
        }
    }

    return mx;
}
