import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        pq = [(grid[0][0], 0, 0)]  # elevation, row, column
        
        while pq:
            e, r, c = heapq.heappop(pq)
            visited.add((r, c))
            
            if r == n - 1 and c == n - 1:
                return e
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(pq, (max(e, grid[nr][nc]), nr, nc))
                    visited.add((nr, nc))
                    
        return -1
