class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s
        s = s[::-1]

        return self.lcs(s, t)

    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[-1] * (m + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(m + 1):
            dp[0][i] = 0

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if s1[x - 1] == s2[y - 1]:
                    dp[x][y] = 1 + dp[x - 1][y - 1]
                else:
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

        return dp[n][m]
