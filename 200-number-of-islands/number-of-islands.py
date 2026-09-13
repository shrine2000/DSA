class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        self.max_count = 0
        visited = set()


        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols


        def bfs_matrix(i, j):
            queue = deque([(i, j)])  
            visited.add((i, j))
            count = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        visited.add((nx, ny))
    

            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs_matrix(i, j)
                    self.max_count += 1

        return self.max_count



        
