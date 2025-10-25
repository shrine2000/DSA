class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0


        R, C = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:
                x, y = queue.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if (0 <= nx < R and 0 <= ny < C and 
                        grid[nx][ny] == "1" and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        island = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    bfs(i, j)
        return island








            