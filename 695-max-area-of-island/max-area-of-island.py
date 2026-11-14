class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        visited = set()

        def dfs(x, y):
            if (
                not (0 <= x < R and 0 <= y < C)
                or grid[x][y] != 1
                or (x, y) in visited
            ):
                return 0
            area = 1
            visited.add((x,y))
            for nx, ny in directions:
                dx, dy = nx + x, ny + y
                area += dfs(dx, dy)
            return area

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        return max_area
