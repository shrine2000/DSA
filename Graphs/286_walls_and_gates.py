from collections import deque


def walls_and_gates(rooms):
    if not rooms or not rooms[0]:
        return

    rows, cols = len(rooms), len(rooms[0])
    GATE = 0
    WALL = -1
    EMPTY = 2**31 - 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == GATE:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or rooms[nr][nc] != EMPTY:
                continue
            rooms[nr][nc] = rooms[r][c] + 1
            queue.append((nr, nc))
