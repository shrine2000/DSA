class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dfs(i, j, T, visited):
            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or grid[i][j] > T:
                return False
            if i == n - 1 and j == n - 1:
                return True

            visited[i][j] = True

            return (
                dfs(i - 1, j, T, visited)
                or dfs(i + 1, j, T, visited)
                or dfs(i, j - 1, T, visited)
                or dfs(i, j + 1, T, visited)
            )

        n = len(grid)
        l, r = 0, n * n - 1

        while l < r:
            m = l + ((r - l) >> 1)
            if dfs(0, 0, m, [[False] * n for _ in range(n)]):
                r = m
            else:
                l = m + 1

        return l
