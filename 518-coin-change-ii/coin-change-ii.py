class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(idx, remaining):
            if remaining == 0:
                return 1
            
            if remaining < 0 or idx == n:
                return 0

            ways = 0
            ways += dfs(idx, remaining - coins[idx])
            ways += dfs(idx + 1, remaining)
            return ways
        return dfs(0, amount)