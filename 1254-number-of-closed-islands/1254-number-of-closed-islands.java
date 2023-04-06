class Solution {
    public int closedIsland(int[][] grid) {
        
        // get the number of rows and columns in the grid
        int m = grid.length;
        int n = grid[0].length;

        // traverse the left and right edges of the grid and call dfs on each cell that is 0
        for (int i=0; i<m; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, n-1);
        }

        // traverse the top and bottom edges of the grid and call dfs on each cell that is 0
        for (int j=0; j<n; j++) {
            dfs(grid, 0, j);
            dfs(grid, m-1, j);
        }

        // count the number of closed islands
        int island = 0;
        for (int k=0; k<m; k++) {
            for (int l=0; l<n; l++) {
                if (grid[k][l] == 0) {
                    island++;
                    dfs(grid, k, l);
                }
            }
        }

        return island;
    }


    private void dfs (int[][] grid, int row, int col) {

        // if the current cell is out of bounds or has already been visited or is not 0, return
        if (row < 0 || row > grid.length-1 || col <0 || col>grid[0].length-1 || grid[row][col] != 0) {
            return;
        } 

        // mark the current cell as visited
        grid[row][col] = -1;

        // call dfs on each of the neighboring cells that are 0
        dfs(grid, row+1, col);
        dfs(grid, row-1, col);
        dfs(grid, row, col+1);
        dfs(grid, row, col-1);

    }
}
