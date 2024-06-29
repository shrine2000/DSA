from collections import deque


def bfs_matrix(matrix):
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    queue = deque([(0, 0)])  # Starting from the top-left corner (0,0)
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        print(f"Visiting node ({x}, {y}) with value {matrix[x][y]}")

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
bfs_matrix(matrix)


def dfs_matrix(matrix):
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited = set()

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y):
        if not is_valid(x, y) or (x, y) in visited:
            return
        visited.add((x, y))
        print(f"Visiting node ({x, y}) with value {matrix[x][y]}")
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    dfs(0, 0)  # Start from the top-left corner (0, 0)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dfs_matrix(matrix)


# BFS
#   Time Complexity: O(N * M), where N is the number of rows and M is the number of columns. This is because each node in the matrix is processed once.
#   Space Complexity: O(N * M) for the visited set and the queue in the worst case.
# DFS
#   Time Complexity: O(N * M), where N is the number of rows and M is the number of columns. Each node is visited once.
#   Space Complexity:
#       Recursive: O(N * M) in the worst case due to the recursion stack.
#       Iterative: O(N * M) for the visited set and the stack in the worst case.
