class Solution {
     public static int closedIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int count = 0;

        // Traverse the cells on the boundary and mark the connected cells as visited
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if ((i == 0 || i == rows - 1 || j == 0 || j == cols - 1) && grid[i][j] == 0 && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                }
            }
        }

        // Traverse the remaining cells and count the number of closed islands
        for (int i = 1; i < rows - 1; i++) {
            for (int j = 1; j < cols - 1; j++) {
                if (!visited[i][j] && grid[i][j] == 0) {
                    count++;
                    dfs(grid, visited, i, j);
                }
            }
        }

        return count;
    }

    private static void dfs(int[][] grid, boolean[][] visited, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;

        if (i < 0 || j < 0 || i >= rows || j >= cols || visited[i][j] || grid[i][j] == 1) {
            return;
        }

        visited[i][j] = true;

        dfs(grid, visited, i + 1, j);
        dfs(grid, visited, i, j + 1);
        dfs(grid, visited, i - 1, j);
        dfs(grid, visited, i, j - 1);
    }
}