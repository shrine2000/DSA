class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        max_count = float("-inf")

        def bfs(X, Y):
            queue = deque([(X, Y)])
            visited.add((X, Y))
            count = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and (nx, ny) not in visited
                        and grid[nx][ny] == "1"
                    ):
                        count += 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return count

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands
