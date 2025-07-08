class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        queue = deque()

        for i in range(rows):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][cols - 1] == "O":
                queue.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[rows - 1][j] == "O":
                queue.append((rows - 1, j))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "S"
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.append((r + dr, c + dc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
