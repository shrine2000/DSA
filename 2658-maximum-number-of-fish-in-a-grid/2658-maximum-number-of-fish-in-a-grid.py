from collections import deque
from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_fish = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    queue = deque([(i, j)])
                    fish_count = grid[i][j]
                    grid[i][j] = 0

                    while queue:
                        current_cell = queue.popleft()
                        x, y = current_cell

                        for dx, dy in directions:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] > 0:
                                fish_count += grid[new_x][new_y]
                                grid[new_x][new_y] = 0
                                queue.append((new_x, new_y))

                    max_fish = max(max_fish, fish_count)

        return max_fish