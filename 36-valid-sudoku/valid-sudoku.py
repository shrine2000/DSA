from collections import defaultdict
from typing import List

# https://www.youtube.com/watch?v=TjFXEUCMqI8&ab_channel=NeetCode


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                box_idx = (r // 3) * 3 + (c // 3)
                if num in cols[c] or num in rows[r] or num in boxes[box_idx]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)

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
