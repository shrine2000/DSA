from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        size = 3
        rows, cols = [0] * size, [0] * size
        diag1 = diag2 = 0

        for index, move in enumerate(moves):
            i, j = move
            player_sign = 1 if index % 2 == 0 else -1

            rows[i] += player_sign
            cols[j] += player_sign

            if i == j:
                diag1 += player_sign
            if i + j == size - 1:
                diag2 += player_sign

            if (
                abs(rows[i]) == size
                or abs(cols[j]) == size
                or abs(diag1) == size
                or abs(diag2) == size
            ):
                return "A" if player_sign == 1 else "B"

        return "Draw" if len(moves) == (size * size) else "Pending"
