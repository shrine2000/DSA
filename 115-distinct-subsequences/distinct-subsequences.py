class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def helper(i, j):
            if len(t) == j:
                return 1
            if len(s) == i:
                return 0
            if s[i] == t[j]:
                return helper(i + 1, j + 1) + helper(i + 1, j)
            else:
                return helper(i + 1, j)

        return helper(0, 0)
