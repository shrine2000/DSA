class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
 
        visited = set()
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            count = 1
            while queue:
                x, y = queue.popleft()
                for dy, dx in dir:
                    nx, ny = x +dx, y + dy
                    if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        count += 1
            return count
        
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area =max(max_area, bfs(i, j))
        return max_area



            