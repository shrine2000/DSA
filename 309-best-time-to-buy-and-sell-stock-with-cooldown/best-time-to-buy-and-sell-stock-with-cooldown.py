class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")

        @cache
        def dfs(i, holding) -> int:
            if i >= len(prices):
                return 0

            if holding == 1:  # sell, skip
                pick = prices[i] + dfs(i + 2, 0)
                not_pick = dfs(i + 1, 1)
                return max(pick, not_pick)

            else:  # buy, skip
                not_pick = dfs(i + 1, 0)
                pick = -prices[i] + dfs(i + 1, 1)
                return max(pick, not_pick)

        return dfs(0, 0)
