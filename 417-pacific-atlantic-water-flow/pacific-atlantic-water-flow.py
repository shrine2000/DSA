class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        R, C = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if (
                        0 <= nx < R
                        and 0 <= ny < C
                        and (nx, ny) not in visited
                        and heights[nx][ny] >= heights[x][y]
                    ):
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited

        pacific = [(i, 0) for i in range(R)] + [(0, j) for j in range(C)]
        atlantic = [(i, C - 1) for i in range(R)] + [(R - 1, j) for j in range(C)]

        pacific_ocean = bfs(pacific)
        atlantic_ocean = bfs(atlantic)
        return list(pacific_ocean & atlantic_ocean)
