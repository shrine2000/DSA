class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0 or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]
        visited = set()
        visited.add((0, 0))

        queue = deque([(0, 0)])
        path = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                if (r, c) == (n - 1, n - 1):
                    return path

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and grid[nr][nc] == 0
                        and (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            path += 1

        return -1
