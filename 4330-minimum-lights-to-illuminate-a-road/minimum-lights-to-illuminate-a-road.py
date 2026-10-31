class Solution:
    def minLights(self, lights: list[int]) -> int:
        N = len(lights)
        diff = [0] * (N + 1)

        for i, v in enumerate(lights):
            if v > 0:
                diff[max(0, i - v)] += 1
                diff[min(N - 1, i + v) + 1] -= 1

        is_lit = [False] * N
        cover = 0
        for i in range(N):
            cover += diff[i]
            is_lit[i] = cover > 0

        count = 0
        for i in range(N):
            if not is_lit[i]:
                count += 1
                for j in range(i, min(N - 1, i + 2) + 1):
                    is_lit[j] = True
        return count