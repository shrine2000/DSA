class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])

        direction_map = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0)
        }

        visited = set()
        r, c = 0, 0

        while True:
            visited.add((r, c))
            dr, dc = direction_map[grid[r][c]]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < m and 0 <= nc < n):
                return [r, c]
            if (nr, nc) in visited:
                return [r, c]

            r, c = nr, nc