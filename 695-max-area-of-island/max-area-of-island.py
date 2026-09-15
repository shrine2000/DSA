class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        max_area = float('-inf')

        def dfs(i, j):
            if (0 <= i < rows) and ( 0 <= j < cols) and grid[i][j] != 0:
                grid[i][j] = 0
                return 1 + (
                    dfs(i + 1, j) +
                    dfs(i, j + 1) +
                    dfs(i - 1, j) +
                    dfs(i, j - 1) 
                )
            return 0

        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    max_area = max(max_area, dfs(x, y))
        return max_area if max_area != float('-inf') else 0


