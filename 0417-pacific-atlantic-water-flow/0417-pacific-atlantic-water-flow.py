from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        def dfs(r, c, visited):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                if pacific_visited[x][y] and atlantic_visited[x][y]:
                    result.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        stack.append((nx, ny))
                        
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]  
        result = set()
        
        for i in range(m):
            dfs(i, 0, pacific_visited)
            dfs(i, n - 1, atlantic_visited)
        for j in range(n):
            dfs(0, j, pacific_visited)
            dfs(m - 1, j, atlantic_visited)

        return list(result)
