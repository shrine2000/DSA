from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0

        def calculate_nsl():
            stack = []
            nsl = [-1] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                nsl[i] = stack[-1] if stack else -1
                stack.append(i)
            return nsl

        def calculate_nsr():
            stack = []
            nsr = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                nsr[i] = stack[-1] if stack else n
                stack.append(i)
            return nsr

        nsl = calculate_nsl()
        nsr = calculate_nsr()

        for i in range(n):
            temp_area = (nsr[i] - nsl[i] - 1) * heights[i]
            area = max(temp_area, area)

        return area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
