class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] *( amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0


        for i in range(1, n + 1):
            coin = coins[i -1]
            for a in range(1, amount + 1):
                dp[i][a] = dp[i -1][a]
                if a >= coin:
                    dp[i][a] = min(dp[i][a], 1 + dp[i][a-coin])
        ans = dp[n][amount]
        return -1 if ans == float('inf') else ans

