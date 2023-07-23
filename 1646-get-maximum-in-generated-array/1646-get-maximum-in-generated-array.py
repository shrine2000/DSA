class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        num = [0] * (n + 1)
        num[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                num[i] = num[i // 2]
            else:
                num[i] = num[i // 2] + num[i // 2 + 1]

        return max(num)
