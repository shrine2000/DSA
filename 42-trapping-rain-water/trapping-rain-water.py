class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N == 0:
            return 0

        left_max = [0] * N
        right_max = [0] * N

        left_max[0] = height[0]
        for i in range(N):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[-1] = height[-1]
        for i in range(N - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        
        total_water = 0

        for i in range(N):
            total_water += min(right_max[i], left_max[i]) - height[i]
        return total_water