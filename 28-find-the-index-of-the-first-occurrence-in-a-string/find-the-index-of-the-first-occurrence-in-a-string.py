class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n > m:
            return -1

        for i in range(m - n + 1):
            j = 0

            while j < n and haystack[i + j] == needle[j]:
                j += 1

            if j == n:
                return i

        return -1
