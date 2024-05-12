from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Helper function to check if placing a queen at board[row][col] is safe
        def is_safe(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == "Q":
                    return False

            return True

        # Backtracking function to explore all possible placements of queens
        def backtrack(board, row):
            # If all queens are placed successfully, add the solution to the solutions list
            if row == n:
                solutions.append(["".join(row) for row in board])
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if placing a queen at board[row][col] is safe
                if is_safe(board, row, col):
                    # Place the queen at board[row][col]
                    board[row][col] = "Q"
                    # Recur to place the next queen in the next row
                    backtrack(board, row + 1)
                    # Backtrack: Remove the queen from board[row][col] to explore other possibilities
                    board[row][col] = "."

        # List to store all solutions
        solutions = []
        # Initialize an empty board with '.' representing empty cells
        empty_board = [["."] * n for _ in range(n)]
        # Start backtracking from the first row (row 0)
        backtrack(empty_board, 0)
        # Return the list of solutions
        return solutions
