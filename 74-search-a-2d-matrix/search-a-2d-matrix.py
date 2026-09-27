class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        # l = 0, r = 15
        # mid = 7
        # r, c = 2, 1
        # l, r = 0, 6
        # mid = 3
        # r, c = 1, 0
        #  
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1

            else :
                r = mid - 1

        return False
