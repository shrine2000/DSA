class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        @cache
        def recursion(i, j):
            if i == M or j == N:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + recursion(i + 1, j + 1)
            
            return max(recursion(i + 1, j), recursion(i, j+ 1))
        return recursion(0, 0)