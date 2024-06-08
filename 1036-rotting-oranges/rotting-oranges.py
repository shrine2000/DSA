from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])
        mins = 0
        queue = deque()
        fresh_oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while queue:
            r, c, time = queue.popleft()
            mins = max(mins, time)

            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx, ny, time + 1))

        return mins if fresh_oranges == 0 else -1
