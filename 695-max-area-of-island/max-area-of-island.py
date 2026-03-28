class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        def bfs(x, y):
            queue = deque([(x, y)])
            visited.add((x, y))
            area = 1
            while queue:
                i, j = queue.popleft()
                for dx, dy in directions:
                    nx = dx + i
                    ny = dy + j
                    if (
                        (0 <= nx < m)
                        and (0 <= ny < n)
                        and (nx, ny) not in visited
                        and grid[nx][ny] == 1
                    ):
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        area += 1
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
        return max_area
