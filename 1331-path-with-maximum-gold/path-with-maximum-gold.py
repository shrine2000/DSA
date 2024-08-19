class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        max_gold = 0
        def dfs(i, j, visited):
            if not 0 <= i < m or not 0 <= j < n or not (i, j) not in visited or grid[i][j] == 0:
                return 0
            max_temp = 0
            visited.add((i, j))
            for dx, dy in directions:
                max_temp = max(max_temp, dfs(i + dx, j + dy, visited))
            visited.remove((i, j))
            return max_temp  + grid[i][j]
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = set()
                    max_gold = max(max_gold, dfs(i, j, visited))
        return max_gold
                    