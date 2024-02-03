from typing import List, Tuple


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def is_valid_pyramid(apex: Tuple[int, int], height: int) -> bool:
            r, c = apex

            if (r, c, height) in ph:
                return ph[(r, c, height)]

            for i in range(r, r + height):
                for j in range(c - (i - r), c + (i - r) + 1):
                    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                        return False
            ph[(r, c, height)] = True
            return True

        def is_valid_inverse_pyramid(apex: Tuple[int, int], height: int) -> bool:
            r, c = apex

            if (r, c, height) in iph:
                return iph[(r, c, height)]

            for i in range(r - height + 1, r + 1):
                for j in range(c - (r - i), c + (r - i) + 1):
                    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                        return False
            iph[(r, c, height)] = True
            return True

        m, n = len(grid), len(grid[0])
        total_plots = 0
        ph, iph = {}, {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for height in range(2, m - i + 1):
                        if is_valid_pyramid((i, j), height):
                            total_plots += 1

                    for height in range(2, i + 2):
                        if is_valid_inverse_pyramid((i, j), height):
                            total_plots += 1

        return total_plots
