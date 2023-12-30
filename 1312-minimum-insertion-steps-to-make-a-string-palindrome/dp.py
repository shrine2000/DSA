class Solution:
    def minInsertions(self, s: str) -> int:
        # Check if the string is already a palindrome
        if s == s[::-1]:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]  # Initialize a 2D DP matrix

        # Fill the DP matrix
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1  # Base case: a single character is a palindrome by itself
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2  # Characters match, extend the palindrome
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # Characters don't match, take the max of left or below cell

        # Minimum number of insertions needed to make the string a palindrome
        return n - dp[0][n - 1]
