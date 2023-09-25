class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c):
            if r == m - 1 or c == n - 1:
                return 1

            right_path = dfs(r, c + 1) if c + 1 < n else 0
            left_path = dfs(r + 1, c) if r + 1 < m else 0

            return right_path + left_path

        return dfs(0, 0)