class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float("inf")

        @lru_cache(None)
        def dfs(i, rem):
            if rem == 0:
                return 0
            if rem < 0 or i == n:
                return INF
            pick = 1 + dfs(i, rem - coins[i])
            not_pick = dfs(i + 1, rem)
            return min(pick, not_pick)
        ans = dfs(0, amount)
        return -1 if ans == INF else ans
