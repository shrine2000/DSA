class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def dfs(i, j, k):
            if len(s1) == i and len(s2) == j :
                return True
            a, b = False, False
            if i < len(s1) and s1[i] == s3[k]:
                a = dfs(i + 1, j, k + 1)
        
            if j < len(s2) and s2[j] == s3[k]:
                b = dfs(i, j + 1, k + 1)
            return a or b
        return dfs(0, 0, 0)