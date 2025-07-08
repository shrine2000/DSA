class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        vis = set()
        count = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            vis.add((r, c))

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < R
                        and 0 <= ny < C
                        and grid[nx][ny] == "1"
                        and (nx, ny) not in vis
                    ):
                        q.append((nx, ny))
                        vis.add((nx, ny))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in vis:
                    bfs(r, c)
                    count += 1

        return count
