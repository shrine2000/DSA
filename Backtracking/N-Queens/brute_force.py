from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if there's a queen in the same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check if there's a queen in the upper left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check if there's a queen in the upper right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == "Q":
                    return False

            return True

        def generate_board(placement):
            board = [["." for _ in range(n)] for _ in range(n)]
            for row, col in enumerate(placement):
                board[row][col] = "Q"
            return ["".join(row) for row in board]

        solutions = []
        for i in range(n**n):
            placement = []
            num = i
            for _ in range(n):
                placement.append(num % n)
                num //= n
            if len(set(placement)) == n and all(
                is_safe(generate_board(placement), r, c)
                for r, c in enumerate(placement)
            ):
                solutions.append(generate_board(placement))
        return solutions


if __name__ == "__main__":
    n = 4
    solution = Solution()
    print(solution.solveNQueens(n))
