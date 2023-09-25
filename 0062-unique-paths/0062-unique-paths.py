class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(r, c):
            if r == m - 1 or c == n -1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            
            right_path = dfs(r, c + 1) if c + 1 < n else 0
            left_path = dfs(r + 1, c) if r + 1 < m  else 0
            
            memo[r][c] = right_path + left_path
            
            return memo[r][c]
        
        return dfs(0, 0)