from typing import List


class Solution:
    def is_square(self, matrix, top, left, size):
        for i in range(top, top + size):
            for j in range(left, left + size):
                if matrix[i][j] == 0:
                    return False

        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        count = 0
        for size in range(1, min(m, n) + 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if self.is_square(matrix, i, j, size):
                        count += 1

        return count
