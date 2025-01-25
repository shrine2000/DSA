class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if (i == m - 1) and (j == n - 1):
                return 1
            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            return right + down

        return dfs(0, 0)
