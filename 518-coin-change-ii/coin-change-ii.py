class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]  # idx, remaining

        for i in range(n + 1):
            dp[i][0] = 1

        for idx in range(n - 1, -1, -1):
            for rem in range(1, amount + 1):
                dp[idx][rem] = dp[idx + 1][rem]

                if rem >= coins[idx]:
                    dp[idx][rem] += dp[idx][rem - coins[idx]]
        return dp[0][amount]

        # @cache
        # def recursive(idx, remaining):
        #     if remaining == 0:
        #         return 1
        #     if idx >= len(coins) or remaining < 0:
        #         return 0
        #     pick = recursive(idx, remaining - coins[idx])
        #     not_pick = recursive(idx + 1, remaining)
        #     return pick + not_pick
        # count = recursive(0, amount)
        # return count
