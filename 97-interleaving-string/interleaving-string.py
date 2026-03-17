class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        @cache
        def dfs(i, j):
            k = i + j
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1):
                return True
            return False

        return dfs(0, 0)
