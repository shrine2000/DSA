class Solution(object):
    def numEnclaves(self, grid: list[list[int]]) -> int:
        if len(grid) <=2 or len(grid[0]) <= 2:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        border_cells = [(0, j) for j in range(cols)] + \
                       [(rows-1, j) for j in range(cols)] + \
                       [(i, 0) for i in range(1, rows-1)] + \
                       [(i, cols-1) for i in range(1, rows-1)]
        queue = deque(border_cells)
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited or grid[i][j] == 0:
                continue
            visited.add((i, j))
            if i != 0:
                queue.append((i-1, j))
            if j != 0:
                queue.append((i, j-1))
            if i < rows-1:
                queue.append((i+1, j))
            if j < cols-1:
                queue.append((i, j+1))
        return sum(1 for i in range(rows) for j in range(cols) if grid[i][j] == 1 and (i, j) not in visited)