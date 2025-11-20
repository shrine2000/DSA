class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
 
         

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs():
            nonlocal fresh_count
            minutes = 0

            while rotten:
                r, c, time = rotten.popleft()
                minutes = max(minutes, time)

                for dx, dy in directions:
                    nx, ny = r + dx, c + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        rotten.append((nx, ny, time + 1))

            return minutes if fresh_count == 0 else -1

        minutes_passed = bfs()
        return minutes_passed