class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(idx):
            if idx == n:
                return 1
            if s[idx] == "0":
                return 0
            ways = dfs(idx + 1)
            if idx + 1 < n and 10 <= int(s[idx : idx + 2]) <= 26:
                ways += dfs(idx + 2)
            return ways
        return dfs(0)
