from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island_count += 1
                    queue = deque([(i, j)])
                    visited.add((i, j))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and (nr, nc) not in visited
                                and grid[nr][nc] == "1"
                            ):
                                visited.add((nr, nc))
                                queue.append((nr, nc))

        return island_count


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands(grid1) == 3, "Test case 1 failed"

    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert solution.numIslands(grid2) == 1, "Test case 2 failed"

    grid3 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands(grid3) == 2, "Test case 3 failed"

    print("All test cases passed!")
