class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0

        for row in matrix:
            for col in range(cols):
                heights[col] = heights[col] + 1 if row[col] == "1" else 0

            stack = [-1]
            for col in range(cols + 1):
                while heights[col] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = col - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(col)

        return max_area
