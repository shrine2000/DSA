class Solution:
    def minLights(self, lights: list[int]) -> int:
        N = len(lights)
        is_illuminated = [False] * N
        diff = [0] * (N + 1)

        for i in range(N):
            if lights[i] > 0:
                v = lights[i]
                diff[max(0, i - v)] += 1
                diff[min(N - 1, i + v) + 1] -= 1

        cover = 0
        for i in range(N):
            cover += diff[i]
            if cover > 0:
                is_illuminated[i] = True

        count = 0
        for i in range(N):
            if not is_illuminated[i]:
                install = min(i + 1, N - 1)
                for j in range(max(0, install - 1), min(N - 1, install + 1) + 1):
                    is_illuminated[j] = True
                count += 1
        return count