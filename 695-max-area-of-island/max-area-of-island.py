class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            area = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows
                        and 0 <= ny < cols
                        and grid[nx][ny] == 1
                        and not (nx, ny) in visited
                    ):
                        area += 1
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not (i, j) in visited:
                    max_area = max(max_area, bfs(i, j))

        return max_area
