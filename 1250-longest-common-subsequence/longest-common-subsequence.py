class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recursive(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + recursive(i + 1, j + 1)
            else:
                return max(recursive(i + 1, j), recursive(i, j + 1))

        return recursive(0, 0)
