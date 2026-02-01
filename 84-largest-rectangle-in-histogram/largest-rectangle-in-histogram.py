class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        stack = []
        left_res = [-1] * n
        right_res = [n] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_res[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_res[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            width = right_res[i] - left_res[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
