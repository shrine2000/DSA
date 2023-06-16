import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        rows, cols = len(heightMap), len(heightMap[0])
        trappedWater = 0
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = []
        
        for r in range(rows):
            heapq.heappush(pq, (heightMap[r][0], r, 0))
            heapq.heappush(pq, (heightMap[r][cols - 1], r, cols - 1))
            visited[r][0] = True
            visited[r][cols - 1] = True
            
        for c in range(cols):
            heapq.heappush(pq, (heightMap[0][c], 0, c))
            heapq.heappush(pq, (heightMap[rows - 1][c], rows - 1, c))
            visited[0][c] = True
            visited[rows - 1][c] = True
            
        while pq:
            height, row, col = heapq.heappop(pq)
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    trappedWater += max(0, height - heightMap[new_row][new_col])
                    heapq.heappush(pq, (max(height, heightMap[new_row][new_col]), new_row, new_col))
                    visited[new_row][new_col] = True
        
        return trappedWater

heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]

solution = Solution()
print(solution.trapRainWater(heightMap))
