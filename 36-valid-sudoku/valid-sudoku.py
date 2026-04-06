class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(m):
            for j in range(m):
                if board[i][j] == ".":
                    continue

                value = board[i][j]
                box_id = (i // 3) * 3 + (j // 3)

                if value in rows[i] or value in cols[j] or value in boxes[box_id]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxes[box_id].add(value)

        return True
