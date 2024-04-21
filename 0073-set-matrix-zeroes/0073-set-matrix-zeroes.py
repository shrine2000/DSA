from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        zero_sets = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_sets[0].add(i)
                    zero_sets[1].add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_sets[0] or j in zero_sets[1]:
                    matrix[i][j] = 0
