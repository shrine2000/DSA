from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [
            [float("inf") if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)
        ]
        visited = set()
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            r, c = queue.popleft()
            for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = r + nr, c + nc
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                    res[dx][dy] = min(res[dx][dy], res[r][c] + 1)
                    queue.append((dx, dy))
                    visited.add((dx, dy))

        return res
