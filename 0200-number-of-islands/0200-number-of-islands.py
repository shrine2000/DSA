from typing import List

class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        count = 0
        
  
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        visited = set()

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def dfs(x, y):
            if not is_valid(x, y) or (x, y) in visited or matrix[x][y] == '0':
                return
            visited.add((x, y))  
        
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                dfs(new_x, new_y)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1' and (i, j) not in visited:
                    count += 1 
                    dfs(i, j)   

        return count
