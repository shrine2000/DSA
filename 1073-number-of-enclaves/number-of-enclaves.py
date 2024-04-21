class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while queue:
            r, c = queue.popleft()

            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] == 1
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

        return count
