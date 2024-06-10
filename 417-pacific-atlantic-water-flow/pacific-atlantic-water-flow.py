class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        dtn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def bfs(starting_points):
            visited = set(starting_points)
            queue = deque(starting_points)
            while queue:
                x, y = queue.popleft()
                for dx, dy in dtn:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited
        
        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic_starts = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        
        return list(pacific_reachable & atlantic_reachable)
