class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                price += prices[i] - prices[i - 1]
        return price
