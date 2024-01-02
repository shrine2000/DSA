class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bottom = row - 1
        left = 0
        right = col - 1

        out = []

        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right + 1):
                out.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                out.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse bottom row
                for i in range(right, left - 1, -1):
                    out.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    out.append(matrix[i][left])
                left += 1

        return out
