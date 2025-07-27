class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        n = len(height)
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            if water_level > height[i]:
                total_water += water_level - height[i]
        return total_water
