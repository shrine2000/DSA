class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (
                r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or board[r][c] != word[idx]
            ):
                return False

            t, board[r][c] = board[r][c], "#"

            for x, y in directions:
                if dfs(r + x, c + y, idx + 1):
                    return True

            board[r][c] = t
            return False

        rs, cs = len(board), len(board[0])

        for r in range(rs):
            for c in range(cs):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
