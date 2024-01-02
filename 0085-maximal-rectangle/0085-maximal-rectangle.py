class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        n = len(heights)
        nsl = [-1] * n
        nsr = [n] * n
        area = []

        for i in range(n):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                nsl[i] = -1
            else:
                nsl[i] = stack[-1][1]
            stack.append((heights[i], i))

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                nsr[i] = n
            else:
                nsr[i] = stack[-1][1]
            stack.append((heights[i], i))

        ans = 0
        for i in range(n):
            width = nsr[i] - nsl[i] - 1
            area.append(heights[i] * width)
            ans = max(ans, area[i])

        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = max(area, self.largestRectangleArea(heights))

        return area
