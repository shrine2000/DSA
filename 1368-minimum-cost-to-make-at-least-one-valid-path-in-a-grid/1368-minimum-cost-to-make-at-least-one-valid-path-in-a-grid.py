from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = deque([(0, 0, 0)])  # tuple - cell position, path cost
        result = 0

        while queue:
            current = queue.popleft()
            cr, cc = current[0] // cols, current[0] % cols

            if current[0] not in visited:
                visited.add(current[0])
                result = current[1]

            if (cr, cc) == (rows - 1, cols - 1):
                return result

            for direction in directions:
                nr, nc = cr + direction[0], cc + direction[1]
                position = nr * cols + nc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or position in visited:
                    continue

                cost = 0  # Assume initial cost is 0

                # Determine the cost based on the grid and direction
                if grid[cr][cc] == 1 and direction == (0, 1):
                    cost = 0
                elif grid[cr][cc] == 2 and direction == (0, -1):
                    cost = 0
                elif grid[cr][cc] == 3 and direction == (1, 0):
                    cost = 0
                elif grid[cr][cc] == 4 and direction == (-1, 0):
                    cost = 0
                else:
                    cost = 1

                if cost == 1:
                    queue.append((position, current[1] + cost))
                else:
                    queue.appendleft(
                        (position, current[1] + cost)
                    )  # append at beginning

        return result
