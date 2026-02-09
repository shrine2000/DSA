class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if (
                0 <= i < R
                and 0 <= j < C
                and (i, j) not in visited
                and grid[i][j] == "1"
            ):
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count
