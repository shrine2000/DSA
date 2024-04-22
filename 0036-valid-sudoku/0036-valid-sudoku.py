class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            seen = set()
            for cell in unit:
                if cell != ".":
                    if cell in seen:
                        return False
                    seen.add(cell)
            return True

        for row in board:
            if not is_valid_unit(row):
                return False

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not is_valid_unit(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [
                    board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)
                ]
                if not is_valid_unit(sub_box):
                    return False

        return True
