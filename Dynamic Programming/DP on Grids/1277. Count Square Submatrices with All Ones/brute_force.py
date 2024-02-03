from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])


if __name__ == "__main__":
    matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
    sol = Solution
    print(sol.countSquares(matrix=matrix))
