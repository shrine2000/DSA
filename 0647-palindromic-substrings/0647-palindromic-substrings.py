class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] *n for _ in range(n)]
        count = 0
        for diff in range(n):
            for i in range(n-diff):
                j = i + diff
                if i == j:
                    dp[i][j] = 1
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > 0:
                    count += 1
        return count
                