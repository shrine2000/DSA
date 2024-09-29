from functools import lru_cache


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


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)
