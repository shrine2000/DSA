class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        global_max = 0
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j, prev):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev:
                return 0
            current_val = matrix[i][j]
            a = dfs(i + 1, j, current_val) + 1
            b = dfs(i - 1, j, current_val) + 1
            c = dfs(i, j + 1, current_val) + 1
            d = dfs(i, j - 1, current_val) + 1
            return max(a, b, c, d)

        for i in range(m):
            for j in range(n):
                val = dfs(i, j, -1)
                global_max = max(global_max, val)

        return global_max
