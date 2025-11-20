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

        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while rotten:

            r, c, count = rotten.popleft()

            time = max(time, count)

            for dr, dc in directions:
                dx, dy = dr + r, dc + c

                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    grid[dx][dy] = 2
                    fresh_count -= 1
                    rotten.append((dx, dy, time + 1))

        return time if fresh_count == 0 else -1
