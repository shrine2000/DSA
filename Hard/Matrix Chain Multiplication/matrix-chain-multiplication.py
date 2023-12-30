# User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[-1] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 0

        for i in range(N - 1, 0, -1):
            for j in range(i + 1, N):
                res = float('inf')

                for k in range(i, j):
                    ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    res = min(res, ans)

                dp[i][j] = res

        return dp[1][N - 1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
