class Solution {
  public static int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == 0) {
                    if (dfs(grid, visited, i, j, m, n)) {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    private static boolean dfs(int[][] grid, boolean[][] visited, int i, int j, int m, int n) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return false;
        }
        if (visited[i][j] || grid[i][j] == 1) {
            return true;
        }
        visited[i][j] = true;

        boolean top = dfs(grid, visited, i - 1, j, m, n);
        boolean bottom = dfs(grid, visited, i + 1, j, m, n);
        boolean left = dfs(grid, visited, i, j - 1, m, n);
        boolean right = dfs(grid, visited, i, j + 1, m, n);

        boolean isClosed = top && bottom && left && right;
        if (isClosed) {
            markVisited(grid, visited, i, j, m, n);
        }
        return isClosed;
    }

    private static void markVisited(int[][] grid, boolean[][] visited, int i, int j, int m, int n) {
        if (i < 0 || j < 0 || i >= m || j >= n || visited[i][j] || grid[i][j] == 1) {
            return;
        }
        visited[i][j] = true;

        markVisited(grid, visited, i - 1, j, m, n);
        markVisited(grid, visited, i + 1, j, m, n);
        markVisited(grid, visited, i, j - 1, m, n);
        markVisited(grid, visited, i, j + 1, m, n);
    }
}
