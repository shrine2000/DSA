class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i, j, s, t):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] == -1
            ):
                return 0

            if grid[i][j] == 2:
                return 1 if s == t else 0

            grid[i][j] = -1

            path = (
                dfs(i + 1, j, s + 1, t)
                + dfs(i, j + 1, s + 1, t)
                + dfs(i - 1, j, s + 1, t)
                + dfs(i, j - 1, s + 1, t)
            )

            grid[i][j] = 0

            return path

        sr, sc, t = 0, 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sr, sc = i, j
                if grid[i][j] != -1:
                    t += 1

        return dfs(sr, sc, 1, t)
