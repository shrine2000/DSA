class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        max_time = 0
        while queue:
            x, y, t = queue.popleft()
            max_time = max(max_time, t)
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, t + 1))
                    fresh -= 1

        return max_time if fresh == 0 else -1
