class Solution:
    MOD = 10**9 + 7
    
    def countPaths(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            count = 1  # Path itself
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    count = (count + dfs(ni, nj)) % self.MOD
            
            dp[i][j] = count
            return count
        
        total_paths = 0
        for i in range(m):
            for j in range(n):
                total_paths = (total_paths + dfs(i, j)) % self.MOD
        
        return total_paths

 
