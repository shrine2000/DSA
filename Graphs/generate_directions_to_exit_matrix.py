# https://leetcode.com/discuss/interview-question/5898854/L5-Google-or-Interview-Exp.-or-Rejected
# https://leetcode.com/playground/A6Qh6zFr

from collections import deque


def get_direction_matrix(path):
    rows, cols = len(path), len(path[0])
    directions_matrix = [["?" for _ in range(cols)] for _ in range(rows)]

    q = deque()

    dir_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    reverse_dir = {"U": "D", "D": "U", "L": "R", "R": "L"}

    for r in range(rows):
        for c in range(cols):
            if path[r][c] == 1:
                directions_matrix[r][c] = "#"
            elif path[r][c] == 2:
                directions_matrix[r][c] = "E"
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dir_char, (dr, dc) in dir_map.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and directions_matrix[nr][nc] == "?":
                directions_matrix[nr][nc] = reverse_dir[dir_char]
                q.append((nr, nc))

    return directions_matrix


def optimized_get_direction_matrix(path):
    rows, cols = len(path), len(path[0])
    directions_matrix = [["?" for _ in range(cols)] for _ in range(rows)]

    q = deque()
    dir_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    reverse_dir = {"U": "D", "D": "U", "L": "R", "R": "L"}

    unexplored_cells = 0
    for r in range(rows):
        for c in range(cols):
            if path[r][c] == 1:
                directions_matrix[r][c] = "#"
            elif path[r][c] == 2:
                directions_matrix[r][c] = "E"
                q.append((r, c))
            else:
                unexplored_cells += 1
    while q and unexplored_cells > 0:
        r, c = q.popleft()
        for dir_char, (dr, dc) in dir_map.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and directions_matrix[nr][nc] == "?":
                directions_matrix[nr][nc] = reverse_dir[dir_char]
                q.append((nr, nc))
                unexplored_cells -= 1
    return directions_matrix


if __name__ == "__main__":
    matrix = [[1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 2]]

    directions = get_direction_matrix(matrix)
    for row in directions:
        print(" ".join(row))

    matrix = [[1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 2]]

    directions = optimized_get_direction_matrix(matrix)
    for row in directions:
        print(" ".join(row))
