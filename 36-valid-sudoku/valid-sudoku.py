class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes=defaultdict(set)
        cols=defaultdict(set)
        rows=defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                box_idx = ( r // 3) *3 + (c // 3)

                if num in cols[c] or num in rows[r] or num in boxes[box_idx]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)
        return True
