class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0

        def expand(left, right):
            nonlocal start, end

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start : end + 1]
