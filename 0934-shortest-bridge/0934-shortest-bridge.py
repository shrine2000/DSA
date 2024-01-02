class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = -1
                island.append((i, j))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(i + dx, j + dy)

        def bfs():
            distance = 0
            while island:
                size = len(island)
                for _ in range(size):
                    x, y = island.popleft()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            if grid[nx][ny] == 1:
                                return distance
                            elif grid[nx][ny] == 0:
                                grid[nx][ny] = -1
                                island.append((nx, ny))

                distance += 1
            return -1

        island = deque()
        found = False

        for i in range(len(grid)):
            if found:
                break

            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        return bfs()
