class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left ) //  2
            row = mid // n
            col = mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left += 1
            else:
                right -= 1
        return False