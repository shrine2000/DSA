from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        n = len(prices)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                prev_price = prices[j]
                curr_price = prices[i]
                if prev_price > curr_price:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
                j += 1
        return max_profit


if __name__ == "__main__":
    print(Solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
