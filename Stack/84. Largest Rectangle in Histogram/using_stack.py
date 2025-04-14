class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        def nsr():
            stack = []
            res = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res

        def nsl():
            stack = []
            res = [-1] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res

        left = nsl()
        right = nsr()
        total_area = 0

        for i in range(n):
            height = heights[i]
            width = right[i] - left[i] - 1
            total_area = max(total_area, height * width)
        return total_area


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
