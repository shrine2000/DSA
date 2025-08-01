class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        left, right = 0, N - 1
        max_area = 0

        while left < right:
            width = right - left 
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1


        return max_area
