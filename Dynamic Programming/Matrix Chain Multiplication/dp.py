class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[-1] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 0

        for i in range(N - 1, 0, -1):
            for j in range(i + 1, N):
                res = float("inf")

                for k in range(i, j):
                    ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    res = min(res, ans)

                dp[i][j] = res

        return dp[1][N - 1]
