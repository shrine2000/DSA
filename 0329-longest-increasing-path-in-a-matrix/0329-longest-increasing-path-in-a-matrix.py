class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_length = 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(x, y))

            dp[i][j] = max_length
            return max_length

        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))

        return max_path
