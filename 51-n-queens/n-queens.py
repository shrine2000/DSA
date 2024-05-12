class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            for i, j in zip(range(row-1, -1 , -1), range(col-1, -1, -1)):
                if board[i][j] == "Q":
                    return False
                    
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == "Q":
                    return False
                           
            return True
                           
        def backtrack(board, row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    board[row][col] = "."
                           
        solutions = []
        empty_board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(empty_board, 0)
        return solutions
