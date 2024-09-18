class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recursion(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0

            if text1[idx1] == text2[idx2]:
                return 1 + recursion(idx1 - 1, idx2 - 1)

            return max(recursion(idx1 - 1, idx2), recursion(idx1, idx2 - 1))

        return recursion(len(text1) - 1, len(text2) - 1)
