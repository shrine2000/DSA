class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # area = height * width
        # width = right - left
        # height = min(height[left], height[right])
        # height = [1,8,6,2,5,4,8,3,7]
        # idx    =  0,1,2,3,4,5,6,7,8 
        while left < right:
            rec_height = min(height[left], height[right])
            width = right - left 
            area = width * rec_height
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
            






