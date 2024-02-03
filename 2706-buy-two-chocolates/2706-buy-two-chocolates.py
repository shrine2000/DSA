class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        amt = prices[0] + prices[1]
        if amt > money:
            return money
        else:
            return money - amt
