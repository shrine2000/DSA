from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(x, y):
            queue = deque([(x, y)])
            area = 0
            grid[x][y] = 0

            while queue:
                cx, cy = queue.popleft()
                area += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))

            return area

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))

        return max_area
