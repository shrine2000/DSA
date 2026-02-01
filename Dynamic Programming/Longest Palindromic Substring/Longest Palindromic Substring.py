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
                    dp[i][j] = 1  # Single character is always a palindrome
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0  # Two characters
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    ans = s[i : j + 1]
        return ans

    def longestPalindromeExpandFromCenter(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0

        def expand(left: int, right: int) -> None:
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)  # odd-length palindromes
            expand(i, i + 1)  # even-length palindromes

        return s[start : end + 1]

    # TC = O(n²)
    # SC = O(1)


if __name__ == "__main__":
    print(Solution().longestPalindromeExpandFromCenter("babad"))  # "bab" or "aba"
    print(Solution().longestPalindromeExpandFromCenter("cbbd"))  # "bb"
    print(Solution().longestPalindromeExpandFromCenter("a"))  # "a"
    print(Solution().longestPalindromeExpandFromCenter(""))  # ""
