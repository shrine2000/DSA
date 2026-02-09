class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    i = x + dx
                    j = y + dy
                    if (
                        0 <= i < R
                        and 0 <= j < C
                        and grid[i][j] == "1"
                        and (i, j) not in visited
                    ):
                        visited.add((i, j))
                        queue.append((i, j))

        count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
        return count
