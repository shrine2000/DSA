class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        fresh = 0
        queue = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        max_time = 0
        visited = set()
        while queue:
            x, y, t = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < R
                    and 0 <= ny < C
                    and grid[nx][ny] == 1
                    and (nx, ny) not in visited
                ):
                    max_time = max(max_time, t + 1  )
                    queue.append((nx, ny, t + 1))
                    visited.add((nx, ny))
                    fresh -= 1
        return max_time if fresh == 0 else -1
