class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
            count += 1

        for length in range(2, N + 1):
            for i in range(N - length +1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    count += 1
        return count
