from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        left_sum = [0] * n
        right_sum = [0] * n
        left_sum = self.calculate_heights_sum(heights)
        right_sum = self.calculate_heights_sum(heights[::-1])[::-1]
        max_sum = max(
            left + right - height
            for left, right, height in zip(left_sum, right_sum, heights)
        )
        return max_sum

    def calculate_heights_sum(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = [-1]
        res = [0] * n
        for i in range(n):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                j = stack.pop()
            res[i] = res[stack[-1]] + (i - stack[-1]) * heights[i]
            stack.append(i)
        return res
