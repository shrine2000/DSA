class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            elif price < min_price:
                min_price = price
        return max_profit  

