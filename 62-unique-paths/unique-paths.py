class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i > m or j > n :
                return 0
            pick =  dfs(i + 1, j)
            not_pick = dfs(i, j + 1)
            return pick + not_pick
        return dfs(0, 0)
