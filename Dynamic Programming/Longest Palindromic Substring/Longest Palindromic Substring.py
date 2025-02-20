# https://www.youtube.com/watch?v=0CKUjDcUYYA&t=563s

# https://github.com/Errichto/youtube/blob/master/leetcode/5-palindromic-substring.cpp

# https://www.scaler.com/topics/longest-palindromic-substring/

# https://www.youtube.com/watch?v=fxwvVnBMN6I

# https://www.youtube.com/watch?v=fxwvVnBMN6I
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len, ans = 0, ""

        for diff in range(n):
            for i in range(n - diff):
                j = i + diff
                if i == j:
                    dp[i][j] = 1 # Single character is always a palindrome
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0 # Two characters
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    ans = s[i:j + 1]
        return ans
