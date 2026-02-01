class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")

        left, right = 0, len(height) - 1

        # area = min(height[left], height[right]) * width

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = min_height * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return 0 if max_area == float("-inf") else max_area
