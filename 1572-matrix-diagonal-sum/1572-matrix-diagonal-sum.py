class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
            sum += mat[i][n - i - 1]
        if n % 2 == 1:
            mid = n // 2
            sum -= mat[mid][mid]

        return sum
