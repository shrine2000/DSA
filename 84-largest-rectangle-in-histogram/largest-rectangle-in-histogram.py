class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        Rleft, Rright = [-1] * n, [n] * n
        Sleft, Sright = [], []

        for i in range(n):
            while Sleft and heights[Sleft[-1]] >= heights[i]:
                Sleft.pop()

            if Sleft:
                Rleft[i] = Sleft[-1]
            Sleft.append(i)

        for i in range(n - 1, -1, -1):
            while Sright and heights[Sright[-1]] >= heights[i]:
                Sright.pop()

            if Sright:
                Rright[i] = Sright[-1]
            Sright.append(i)

        area = 0

        for i in range(n):
            width = Rright[i] - Rleft[i] - 1
            area = max(area, width * heights[i])

        return area
