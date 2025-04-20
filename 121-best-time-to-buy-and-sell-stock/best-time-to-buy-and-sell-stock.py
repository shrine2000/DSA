class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        n = len(prices)
        min_price = prices[0]
        max_profit = 0

        for curr_price in prices[1:]:
            profit = curr_price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, curr_price)

        return max_profit

