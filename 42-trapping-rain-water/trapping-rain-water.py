class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_min, right_min = [0] * N, [0] * N

        left_min[0] = height[0]
        for i in range(1, N):
            left_min[i] = max(left_min[i - 1], height[i])

        right_min[-1] = height[-1]
        for i in range(N - 2, -1, -1):
            right_min[i] = max(right_min[i + 1], height[i])

        water = 0
        for i in range(N):
            water += min(left_min[i], right_min[i]) - height[i]
        return water
