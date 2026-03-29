class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        visited=set()


        def dfs(i, j):
            if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1' or (i, j) in visited):
                return

            visited.add((i, j))
            
            dfs(i+1, j)
            dfs(i, j + 1)
            dfs(i-1, j)
            dfs(i, j - 1)


        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i, j)
                    islands += 1
        return islands