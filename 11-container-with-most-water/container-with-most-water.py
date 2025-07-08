class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float('-inf')
        N = len(height)

        left, right = 0, N - 1

        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area