class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(i, j, count):
            if i >= m or j >= n:
                return 0
            if (i == m - 1) and (j == n - 1):
                return 1
            left = dfs(i + 1, j, count + 1) 
            down = dfs(i, j + 1, count + 1)
            return left + down
        return dfs(0, 0, 0)
            