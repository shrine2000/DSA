class Solution:
    def trap(self, height: list[int]) -> int:
        N = len(height)
        left, right = [0] * N, [0] * N

        left[0] = height[0]
        for i in range(1, N):
            left[i] = max(left[i - 1], height[i])
        right[N - 1] = height[N - 1]
        for i in range(N - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        water = 0
        for i in range(N):
            water += min(left[i], right[i]) - height[i]
        return water
