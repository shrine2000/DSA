class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        nd = set()
        pd = set()
        res = []

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in pd or (r - c) in nd:
                    continue

                cols.add(c)
                pd.add(r + c)
                nd.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                cols.remove(c)
                pd.remove(r + c)
                nd.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
