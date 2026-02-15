class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][a] = number of ways to make amount a using coins from index i onward
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i + 1][a]
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]
