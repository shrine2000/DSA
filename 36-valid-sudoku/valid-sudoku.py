from collections import defaultdict
from typing import List

# https://www.youtube.com/watch?v=TjFXEUCMqI8&ab_channel=NeetCode


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i // 3, j // 3)]
                ):
                    return False

                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        return True


if __name__ == "__main__":
    sol = Solution()

    # Test Case: Valid Sudoku
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    # Test Case: Invalid Sudoku (two 8s in top-left box)
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print("Valid Board:", sol.isValidSudoku(valid_board))  # Expected: True
    print("Invalid Board:", sol.isValidSudoku(invalid_board))  # Expected: False
