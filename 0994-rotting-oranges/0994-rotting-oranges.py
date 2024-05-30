# https://www.youtube.com/watch?v=yf3oUhkvqA0

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        if not grid or not grid[0]:
            return -1

        r, c = len(grid), len(grid[0])
        o = 0
        rtn = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    o += 1
                elif grid[i][j] == 2:
                    rtn.append((i, j))

        if o == 0:
            return 0

        dtn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minutes = 0

        while rtn and o > 0:
            s = len(rtn)

            for _ in range(s):
                x, y = rtn.popleft()

                for dx, dy in dtn:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        o -= 1
                        rtn.append((nx, ny))

            minutes += 1

        return minutes if o == 0 else -1
