from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0

        while queue:
            x, y, mins = queue.popleft()
            minutes = max(minutes, mins)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if is_valid(nx, ny) and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny, mins + 1))

        return minutes if fresh == 0 else -1